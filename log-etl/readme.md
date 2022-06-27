# start-log-etl 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-log-etl&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-log-etl" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-log-etl&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-log-etl" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-log-etl&type=packageDownload">
  </a>
</p>

<description>

> ***日志自动触发函数计算进行ETL示例***

</description>

<table>



</table>

<codepre id="codepre">

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-log-etl) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-log-etl)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-log-etl -d start-log-etl`   
    - 进入项目，并进行项目部署：`cd start-log-etl && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

## 项目使用注意事项

项目Yaml中，声明了`actions`， 其对应的命令作用是 deploy 之前自动安装第三方依赖库， 同时 s deploy 部署的时候， 会自动增加相关的环境变量， 让您函数执行的时候能自动找到相关的依赖库。

## 应用详情

本应用是日志自动触发函数计算进行 ETL 示例, 通过 Serverless Devs 开发者工具，您只需要几步就能完成一个实习日志 ETL 的示例， 示例代码中留有`do your things` 区域。
>  更多示例代码请参看 [aliyun-log-fc-functions](https://github.com/aliyun/aliyun-log-fc-functions)

![](https://img.alicdn.com/imgextra/i1/O1CN01HPxM2G1ISa3WHMLIP_!!6000000000892-2-tps-1644-844.png)

**客户案例**

[115科技日志实时ETL](https://resources.functioncompute.com/115-tech.html)

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>