#!/usr/bin/env python
#-*- coding:utf8 -*-

#
# Author: Chenxc
#
# Date: 2015-02-28
#

import os
import time
import psutil


def cat_file(path):
    """读取文件内容
    """
    try:
        with open(path) as f:
            return f.read()
    except IOError, e:
        print e            # 输出作为 zabbix 通知邮件中报警详情的内容
        exit()


class PUPPET_MONITOR(object):
    """ZABBIX 对 puppet agent 监控，可检测进程是否开启，以及 puppet 上一个同步
       周期是否出线同步超时情况。
    """

    process_name = "puppet"

    def __init__(self):
        """构造方法，PUPPET_MONITOR 类实例包含两个实例属性：

           last_sync_successful_date，puppet 同步成功后，生成的本次同步时间戳

           max_time，同步超时阈值，单位秒。
        """
        self.last_sync_successful_date = int(cat_file(path="/tmp/puppetmonitor")) # 注意：
                                                                                  #     path 为 puppet 生成的时间戳文件。
        self.max_time = 1800

    @classmethod
    def process_is_exist(cls):
        """监测 puppet agent 进程是否运行，运行则返回 PUPPET_MONITOR
           类实例，否则输出“进程未启动错误信息”。
        """
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'cmdline'])
            except psutil.NoSuchProcess:
                pass
            if cls.process_name in " ".join(pinfo.get('cmdline')):
                return cls()
        print "%(process_name)s process does not start." % {"process_name": cls.process_name}

    def sync_is_successful(self):
        """监测同步是否成功，本次监控动作时间戳大于预设同步超时阈值，
           输出“超时同步失败错误信息”，否则输出“0”代表上次同步成功。
        """
        current_date = int(time.time())
        time_diff = current_date - self.last_sync_successful_date
        if time_diff > self.max_time:
            print "Error,Synchronization failure."
        else:
            print "0"

if __name__ == "__main__":
    agent_pro = PUPPET_MONITOR.process_is_exist()
    if agent_pro:
        agent_pro.sync_is_successful()
