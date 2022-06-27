# -*- coding: utf-8 -*-

import logging
import json
from aliyun.log import LogClient


def logClient(endpoint, creds):
    # logger = logging.getLogger()
    # logger.info('creds info')
    # logger.info(creds.access_key_id)
    # logger.info(creds.access_key_secret)
    # logger.info(creds.security_token)
    client = LogClient(endpoint, creds.access_key_id,
                       creds.access_key_secret, creds.security_token)
    return client


def handler(event, context):
    logger = logging.getLogger()
    logger.info('start deal SLS data: {}'.format(event.decode().encode()))
    info_arr = json.loads(event.decode())
    return fetchdata(info_arr['source'], context)


def fetchdata(event, context):
    logger = logging.getLogger()
    endpoint = event['endpoint']
    creds = context.credentials
    client = logClient(endpoint, creds)
    if client == None:
        logger.info("client create failed")
        return False
    project = event['projectName']
    logstore = event['logstoreName']
    start_cursor = event['beginCursor']
    end_cursor = event['endCursor']
    loggroup_count = 10
    shard_id = event['shardId']
    while True:
        res = client.pull_logs(project, logstore, shard_id,
                               start_cursor, loggroup_count, end_cursor)

        # do your things, for example, print or import pymysql.cursors,  write etl data in mysql
        res.log_print()

        next_cursor = res.get_next_cursor()
        if next_cursor == start_cursor:
            break
        start_cursor = next_cursor

      # log_data =  res.get_loggroup_json_list()
    return True
