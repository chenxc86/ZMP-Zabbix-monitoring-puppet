# ZMP-Zabbix-monitoring-puppet

## 项目背景
  工作中要对服务器上的 Puppet agent 运行情况进行监控，监控服务使用 Zabbix。

## 监控需求
+ puppet agent进程是否开启。
+ Puppet Server 上一个同步周期是否同步成功。（实际应用中，由于网络问题可能导致同步因超时而失败的情况。）

## 监控思路
  Puppet Server 端同步时，待 Agent 端服务器同步成功则创建时间戳文件至指定目录，供 Zabbix 监控脚本计算超时时间。
  
## 使用方法
1. Python 已经安装了 psutil 模块，要求版本 2.X 以上。
2. Zabbix Item 设置 Type of information（接收值）类型为 Character。
