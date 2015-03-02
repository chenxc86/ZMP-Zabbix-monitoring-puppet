# ZMP-Zabbix-monitoring-puppet

## 项目背景
  工作中要对服务器上的 Puppet agent 运行情况进行监控，监控服务使用 Zabbix。

## 监控需求
+ puppet agent进程是否开启。
+ Puppet Server 上一个同步周期是否同步成功。（实际应用中，由于网络问题可能导致同步因超时而失败的情况。）
