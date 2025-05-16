import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import threading
import requests
import time
import re
import new
from subprocess import run
import subprocess
import platform
import pygame

# 获取当前绝对路径
tools_path = os.getcwd()
if platform.system() == "Windows":
    java8_path = (tools_path + "\\tools\\0_path\\java-8\\bin\\java.exe").replace("\\", "\\\\")
    java11_path = (tools_path + "\\tools\\0_path\\jdk-11\\bin\\java.exe").replace("\\", "\\\\")
    python3 = (tools_path + "\\tools\\0_path\\Python39\\python3").replace("\\", "\\\\")


class button(new.Ui_MainWindow):
    def messageDialog(self):
        #核心功能代码
        msg_box = QMessageBox(QMessageBox.Information, '功能介绍',
                                  '本工具所有蓝色的地方，都是需要输入URL才能启动的，\n可在上方URL栏直接输入，提高运行效率。'+"\n"+"\n"
                                  '无颜色的地方会自行打开软件或打开目录。'+"\n"
                              )
        msg_box.exec_()

    def messagetwo(self):
        #核心功能代码
        msg_box = QMessageBox(QMessageBox.Information, '提宝贵的建议:',
                              '如果你有任何使用问题或好的灵感，欢迎添加\n下方联系方式反馈问题，期待与你共进步。'+"\n"
                              'QQ：2401928412'+"\n"
                              'VX：xingjunyi248')
        msg_box.exec_()

    def messagethree(self):
        #核心功能代码
        msg_box = QMessageBox(QMessageBox.Information, '团队介绍:',
                              '本工具为前进四安全团队渗透测试工具箱。'+"\n"
                              '我们的官网：http://www.qjsteam.cn/')
        msg_box.exec_()

    def No_filtering(self):#1.无过滤
        url =self.textEdit.toPlainText()#获取文本内容
        return url

    # def Simple_filtering(self):  # 2.过滤url后面的内容，只留http+域名
    #     url = self.textEdit.toPlainText()#获取文本内容
    #     time.sleep(0.2)
    #     url.strip('\n')  # 去掉换行
    #     if "http" in url:  # 如果http的存在，就过滤掉，不留端口，只留http+域名
    #         list = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)# 如果http的存在，就过滤掉，不留端口，只留http+域名
    #         url_pro = ' '.join(list)
    #         return url_pro
    #     else:  #只留IP,过滤的是192.168.0.1:88
    #         if 'www' in url:  #如果存在www.baidu.com:80/asdga/gasd或者www.baidu.com/aaagsd  这样情况，滚去上面的，过滤端口
    #             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
    #             msg_box = QMessageBox(QMessageBox.Warning, '圣旨到', '小伙子，你真是哪壶不开提哪壶，加上http://去重试')
    #             msg_box.exec_()
    #             msg_box = QMessageBox(QMessageBox.Warning, 'Goodby', '我不会告诉你我解决不了闪退的，See you again. ')
    #             msg_box.exec_()
    #             exit()
    #         elif '.com' in url:
    #             msg_box = QMessageBox(QMessageBox.Warning, '圣旨到', '小伙子，你真是哪壶不开提哪壶，加上http://去重试')
    #             msg_box.exec_()
    #             msg_box = QMessageBox(QMessageBox.Warning, 'Goodby', '我不会告诉你我解决不了闪退的，See you again. ')
    #             msg_box.exec_()
    #             exit()
    #         elif '.cn' in url:
    #             msg_box = QMessageBox(QMessageBox.Warning, '圣旨到', '小伙子，你真是哪壶不开提哪壶，加上http://去重试')
    #             msg_box.exec_()
    #             msg_box = QMessageBox(QMessageBox.Warning, 'Goodby', '我不会告诉你我解决不了闪退的，See you again. ')
    #             msg_box.exec_()
    #             exit()
    #         elif '.net' in url:
    #             msg_box = QMessageBox(QMessageBox.Warning, '圣旨到', '小伙子，你真是哪壶不开提哪壶，加上http://去重试')
    #             msg_box.exec_()
    #             msg_box = QMessageBox(QMessageBox.Warning, 'Goodby', '我不会告诉你我解决不了闪退的，See you again. ')
    #             msg_box.exec_()
    #             exit()
    #         elif '.org' in url:
    #             msg_box = QMessageBox(QMessageBox.Warning, '圣旨到', '小伙子，你真是哪壶不开提哪壶，加上http://去重试')
    #             msg_box.exec_()
    #             msg_box = QMessageBox(QMessageBox.Warning, 'Goodby', '我不会告诉你我解决不了闪退的，See you again. ')
    #             msg_box.exec_()
    #             exit()
    #         else:
    #             list = re.findall("((?:[0-9]{1,3}\.){3}[0-9]{1,3})", url)  # 过滤ip专用，192.168.0.1:8888，秒变成192.168.0.1
    #             url_pro = ' '.join(list)
    #             return url_pro
    #
    #
    # def zhiliuip(self):#只留IP
    #     url = self.textEdit.toPlainText()#获取文本内容
    #     time.sleep(0.2)
    #     url.strip('\n')  # 去掉换行
    #     list = re.findall("((?:[0-9]{1,3}\.){3}[0-9]{1,3})", url)  # 过滤ip专用，192.168.0.1:8888，秒变成192.168.0.1
    #     url_pro = ' '.join(list)
    #     return url_pro


    # def check_ip(self,ipAddr):#检验IP真假
    #     compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    #     if compile_ip.match(ipAddr):
    #         return True
    #     else:
    #         return False
    #
    # def IP(self):  # 只留IP的和域名，留到ip和 baidu.com
    #     a = self.Simple_filtering()#http://www.baidu.com and 192.168.0.1
    #     time.sleep(0.1)
    #     b = self.check_ip(a)#检验IP真假
    #     if "https" in a:#过滤掉http头
    #         one = a[8:]
    #         return one
    #     elif "http" in a:
    #         two = a[7:]
    #         return two
    #     elif b:
    #         return a
    #     else:
    #         print("有问题啊扑街仔?")

    # def yuming(self):#过滤掉所有，只留域名，用于oneforall
    #     url = self.textEdit.toPlainText()  # 获取文本内容
    #     time.sleep(0.2)
    #     url.strip('\n')  # 去掉换行
    #     list = re.findall('(?:[a-zA-Z0-9](?:[a-zA-Z0-9\\-@]{,61}[a-zA-Z0-9])?\\.)+[a-zA-Z]{2,11}',
    #                       url)  # 如果http的存在，就过滤掉，不留端口，只留http+域名
    #     url_pro = ' '.join(list)
    #     return url_pro

    def burpsuite(self):#文档未改
        th = threading.Thread(target=self.burpsuite_start, )  #启动子类
        th.start()
    def burpsuite_start(self):
        #os.system('start ''cmd \"/K cd tools\\1_常用\\BurpSuiteV2024.3.1.2\\ && CNBurp.VBS\"')
        command = 'cd tools\\1_常用\\BurpSuite\\ && BurpSuitePro.exe'
        subprocess.Popen(command, shell=True)

    def goby(self):#文档未改
        th = threading.Thread(target=self.goby_start, )  #启动子类
        th.start()
    def goby_start(self):
        command = 'cd tools\\1_常用\\goby\\ && Goby.exe'
        subprocess.Popen(command, shell=True)


    def Xray(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\xray\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def Cobaltstrike49(self):  # 文档未改
        th = threading.Thread(target=self.Cobaltstrike49_start, )  # 启动子类
        th.start()
    def Cobaltstrike49_start(self):
        command = 'cd tools\\1_常用\\cs4.9\\Client\\ && {} -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -javaagent:uHook.jar -jar cobaltstrike-client.jar'.format(java11_path)
        subprocess.Popen(command, shell=True)


    def Cobaltstrike48(self):  # 文档未改
        th = threading.Thread(target=self.Cobaltstrike48_start, )  # 启动子类
        th.start()
    def Cobaltstrike48_start(self):
        command = 'cd tools\\1_常用\\cs4.8\\Client\\ && {} -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -javaagent:uHook.jar -Dfile.encoding=utf-8 -jar cobaltstrike-client.jar'.format(java11_path)
        subprocess.Popen(command, shell=True)


    def Cobaltstrike45(self):  # 文档未改
        th = threading.Thread(target=self.Cobaltstrike45_start, )  # 启动子类
        th.start()
    def Cobaltstrike45_start(self):
        command = 'cd tools\\1_常用\\coablt_strike_4.5_jx\\ && {} -Dfile.encoding=utf-8 -Xms1336M -Xmx1336M -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -javaagent:CSAgent.jar=f38eb3d1a335b252b58bc2acde81b542 -Duser.language=en -jar cobaltstrike.jar'.format(java11_path)
        subprocess.Popen(command, shell=True)

    def everything(self):
        th = threading.Thread(target=self.everything_start, )  # 启动子类
        th.start()
    def everything_start(self):
        command = 'cd tools\\1_常用\\Everything\\ && Everything.exe'
        subprocess.Popen(command, shell=True)

    def genmulu(self):
        command = '%SystemRoot%/explorer.exe {}'.format(tools_path)   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def neiwangmulu(self):
        command = '%SystemRoot%/explorer.exe 2、内网渗透工具\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动


    def finalshell(self):  # 文档未改
        th = threading.Thread(target=self.finalshell_start, )  # 启动子类
        th.start()
    def finalshell_start(self):
        command = 'cd tools\\1_常用\\finalshell\\ && finalshell.exe'
        subprocess.Popen(command, shell=True)


    def xshell(self):  # 文档未改
        th = threading.Thread(target=self.xshell_start, )  # 启动子类
        th.start()
    def xshell_start(self):
        command = 'cd tools\\1_常用\\Xshell\\ && Xshell.exe'
        subprocess.Popen(command, shell=True)

    def mobaxterm(self):  # 文档未改
        th = threading.Thread(target=self.mobaxterm_start, )  # 启动子类
        th.start()
    def mobaxterm_start(self):
        command = 'cd tools\\1_常用\\mobaxterm\\ && MobaXterm_Personal_24.1.exe'
        subprocess.Popen(command, shell=True)


    def putty(self):  # 文档未改
        th = threading.Thread(target=self.putty_start, )  # 启动子类
        th.start()
    def putty_start(self):
        command = 'cd tools\\1_常用\\ssh\\ && putty.exe'
        subprocess.Popen(command, shell=True)


    def FTP(self):  # 文档未改
        th = threading.Thread(target=self.FTP_start, )  # 启动子类
        th.start()
    def FTP_start(self):
        command = 'cd tools\\1_常用\\ftp\\ && 8uftp.exe'
        subprocess.Popen(command, shell=True)


    def SocksCap64(self):  # 文档未改
        th = threading.Thread(target=self.SocksCap64_start, )  # 启动子类
        th.start()
    def SocksCap64_start(self):
        command = 'cd tools\\1_常用\\SocksCap64\\ && SocksCap64.exe'
        subprocess.Popen(command, shell=True)

    def Proxifier(self):  # 文档未改
        th = threading.Thread(target=self.Proxifier_start, )  # 启动子类
        th.start()
    def Proxifier_start(self):
        command = 'cd tools\\1_常用\\Proxifier\\ && Proxifier.exe'
        subprocess.Popen(command, shell=True)


    def V2RayN(self):  # 文档未改
        th = threading.Thread(target=self.V2RayN_start, )  # 启动子类
        th.start()
    def V2RayN_start(self):
        command = 'cd tools\\1_常用\\v2rayN-Core\\ && v2rayN.exe'
        subprocess.Popen(command, shell=True)


    def clash(self):  # 文档未改
        th = threading.Thread(target=self.clash_start, )  # 启动子类
        th.start()
    def clash_start(self):
        command = 'cd tools\\1_常用\\clash-verge\\ && Clash-Verge.exe'
        subprocess.Popen(command, shell=True)




    def ihoneybakfilescan(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\ihoneyBakFileScan_Modify-main\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def fanruan(self):
        th = threading.Thread(target=self.fanruan_start, )
        th.start()
    def fanruan_start(self):
        command = 'cd tools\\1_常用\\ && {} -jar FrChannelPlus.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def UEditorGetShell(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\UEditorGetShell-master\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def DS_Store(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\Python-dsstore-master\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def acticemq(self):  # 文档未改
        th = threading.Thread(target=self.acticemq_start, )  # 启动子类
        th.start()
    def acticemq_start(self):
        command = 'cd tools\\1_常用\\ActiveMQ_RCE\\ && {} -jar ActiveMQ_RCE_GUI_v1.0.3.jar'.format(java11_path)
        subprocess.Popen(command, shell=True)

    def xxl_job(self):
        th = threading.Thread(target=self.xxl_job_start, )
        th.start()
    def xxl_job_start(self):
        command = 'cd tools\\1_常用\\ && {} -jar xxl-jobExploitGUI_v1.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def XSS_PDF(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\js_pdf_xss-main\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def google(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\google\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def DS_Store(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\Python-dsstore-master\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def shuapin(self):
        th = threading.Thread(target=self.shuapin_start, )
        th.start()
    def shuapin_start(self):
        command = 'cd tools\\1_常用\\ && QQ轰炸.exe'
        subprocess.Popen(command, shell=True)

    def ipcame(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\摄像头检测\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def ipguishu(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\1_常用\\整理IP\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.ipguishu_start, )  # 启动子类
        th.start()
    def ipguishu_start(self):
        command = 'cd tools\\1_常用\\整理IP\\ && {} -jar SelfIPAdressQuery-0.3-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def fscan(self):
        if self.No_filtering() ==None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system('start ''cmd \"/K cd tools\\2_redteam\\1_扫描器\\fscan\\ && fscan.exe -h {}\"'.format(self.No_filtering()))

    def dddd(self):
        if self.No_filtering() ==None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system ('start ''cmd \"/K cd tools\\2_redteam\\1_扫描器\\dddd-main\\ && dddd64.exe -t {} -gpt 800 -wt 1000 \"'.format(self.No_filtering()))

    def nacs(self):
        if self.No_filtering() ==None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system ('start ''cmd \"/K cd tools\\2_redteam\\1_扫描器\\nacs\\ && nacs.exe -h {}\"'.format(self.No_filtering()))

    def gogo(self):
        if self.No_filtering() ==None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system ('start ''cmd \"/K cd tools\\2_redteam\\1_扫描器\\gogo\\ && gogo.exe -i {} -p win,db,top2,http \"'.format(self.No_filtering()))

    def vscan(self):
        if self.No_filtering() ==None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system ('start ''cmd \"/K cd tools\\2_redteam\\1_扫描器\\vscan\\ && vscan.exe -host {}\"'.format(self.No_filtering()))

    def railgun(self):
        th = threading.Thread(target=self.railgun_start, )
        th.start()
    def railgun_start(self):
        command = 'cd tools\\2_redteam\\1_扫描器\\Railgun\\ && Railgun.exe'
        subprocess.Popen(command, shell=True)

    def tscan(self):
        th = threading.Thread(target=self.tscan_start, )
        th.start()
    def tscan_start(self):
        command = 'cd tools\\2_redteam\\1_扫描器\\tscan\\ && TscanPlus.exe'
        subprocess.Popen(command, shell=True)

    def xiaomifan(self):
        th = threading.Thread(target=self.xiaomifan_start, )
        th.start()
    def xiaomifan_start(self):
        command = 'cd tools\\2_redteam\\1_扫描器\\小米范\\ && {} -jar webfinder2.9.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def chaojiruokoulin(self):  # 文档未改
        th = threading.Thread(target=self.chaojiruokoulin_start, )  # 启动子类
        th.start()

    def chaojiruokoulin_start(self):
        command = 'cd tools\\2_redteam\\1_扫描器\\超级弱口令检查工具V1.0 Beta28 20190715\\ && SNETCracker.exe'
        subprocess.Popen(command, shell=True)


    def dirsearch(self):  # 文档未改
        th = threading.Thread(target=self.dirsearch_start, )  # 启动子类
        th.start()
    def dirsearch_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\2_目录扫描\\dirsearch\\ && {} dirsearch.py -u {}\"'.format(python3,self.No_filtering()))

    def kbscan(self):
        th=threading.Thread(target=self.kbscan_start,)#启动子类
        th.start()
    def kbscan_start(self):
        command = 'cd tools\\2_redteam\\2_目录扫描\\7kbscan\\ && 7kbscan-WebPathBrute.exe'
        subprocess.Popen(command, shell=True)


    def rad(self):  # 文档未改
        th = threading.Thread(target=self.rad_start, )  # 启动子类
        th.start()
    def rad_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\2_目录扫描\\ && rad.exe -t {}\"'.format(self.No_filtering()))


    def Arjun(self):  # 文档未改
        th = threading.Thread(target=self.Arjun_start, )  # 启动子类
        th.start()
    def Arjun_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\2_目录扫描\\Arjun\\ && arjun -u {}\"'.format(self.No_filtering()))


    def yujian(self):
        th=threading.Thread(target=self.yujian_start,)#启动子类
        th.start()
    def yujian_start(self):
        command = 'cd tools\\2_redteam\\2_目录扫描\\俩御剑\\ && 御剑后台扫描工具.exe'
        subprocess.Popen(command, shell=True)

    def yujian_pro(self):
        th = threading.Thread(target=self.yujian_pro_start, )  # 启动子类
        th.start()
    def yujian_pro_start(self):
        command = 'cd tools\\2_redteam\\2_目录扫描\\俩御剑\\ && 御剑目录扫描专业版v1.1.exe'
        subprocess.Popen(command, shell=True)



    def subfinder(self):  # 文档未改
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\3_子域名and指纹识别\\subfinder\\ && subfinder.exe -d {}\"'.format(self.No_filtering()))

    def ziyumingwajueji(self):  # 文档未改
        th = threading.Thread(target=self.ziyumingwajueji_start, )  # 启动子类
        th.start()
    def ziyumingwajueji_start(self):
        command = 'cd tools\\2_redteam\\3_子域名and指纹识别\\子域名挖掘机5.0最新版\\ && Layer.exe'
        subprocess.Popen(command, shell=True)

    def chunsou(self):  # 文档未改
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\3_子域名and指纹识别\\chunsou\\ && {} chunsou.py -u {}\"'.format(python3, self.No_filtering()))



    def tide(self):
        if self.No_filtering() == None:
            msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
            msg_box.exec_()
        else:
            os.system('start ''cmd \"/K cd tools\\2_redteam\\3_子域名and指纹识别\\Tide\\ && TideFinger.exe -u {} -pd\"'.format(
                self.No_filtering()))

    def dismap(self):  # 文档未改
        os.system('start ''cmd \"/K cd tools\\2_redteam\\3_子域名and指纹识别\\dismap\\ && dismap.exe -u {} \"'.format(
            self.No_filtering()))


    def lengtong(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\3_子域名and指纹识别\\Ehole棱桐资产扫描梳理\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def URLFinder(self):
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\4_JS探测\\URLFinder\\ && URLFinder.exe -u {} -s all -m 2\"'.format(
                self.No_filtering()))

    def jsfinder(self):
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\4_JS探测\\jsfinder\\ && {} JSFinder.py -u {}\"'.format(
                python3, self.No_filtering()))


    def packjs(self):  # 文档未改
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\4_JS探测\\Packer-Fuzzer-1.4\\ && {} PackerFuzzer.py -u {}\"'.format(
                python3, self.No_filtering()))


    def packjsjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\4_JS探测\\Packer-Fuzzer-1.4\\reports\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动


    def svn(self):  # 文档未改
        th = threading.Thread(target=self.svn_start, )  # 启动子类
        th.start()
    def svn_start(self):
        command = 'cd tools\\2_redteam\\4_JS探测\\svn\\ && Seay-Svn.exe'
        subprocess.Popen(command, shell=True)

    def webfinder(self):  # 文档未改
        th = threading.Thread(target=self.webfinderstart, )  # 启动子类
        th.start()
    def webfinderstart(self):
        command = 'cd tools\\2_redteam\\4_JS探测\\web批量请求器\\ && {} -jar WebBatchRequest.jar'.format(java8_path)
        print(command)
        subprocess.Popen(command, shell=True)

    def fofa(self):  # 文档未改
        th = threading.Thread(target=self.fofa_start, )  # 启动子类
        th.start()
    def fofa_start(self):
        command = 'cd tools\\2_redteam\\5_二页剩余其他\\fofa\\ && {} -jar fofaviewer.jar'.format(java11_path)
        print(command)
        subprocess.Popen(command, shell=True)


    def nuclei(self):
        th = threading.Thread(target=self.nuclei_start, )  # 启动子类
        th.start()
    def nuclei_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\5_二页剩余其他\\B_nuclei\\ && nuclei.exe -u {} -rl 1000 -bs 200 -c 200 -stats\"'.format(
                                                                                                             self.No_filtering()))

    def afrog(self):
        th = threading.Thread(target=self.afrog_start, )  # 启动子类
        th.start()
    def afrog_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\5_二页剩余其他\\afrog\\ && afrog.exe -t {} -rl 1000 -c 250 -rc 200\"'.format(
                                                                                                             self.No_filtering()))

    def httpxjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\httpx\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动


    def portscan(self):
        th = threading.Thread(target=self.portscan_start, )  # 启动子类
        th.start()
    def portscan_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\5_二页剩余其他\\portscan\\ && portscan.exe --ip {} --Pn --rate 1500\"'.format(
                                                                                                             self.No_filtering()))

    def heapdumpjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\headump\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动


    def sqlmap(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\sqlmap-1.8\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def sqlmap_plus(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\SqlmapXPlus-1.50\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def ghauri(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\ghauri\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动


    def yongheng(self):  # 文档未改
        th = threading.Thread(target=self.yongheng_start, )  # 启动子类
        th.start()
    def yongheng_start(self):
        command = 'cd tools\\2_redteam\\5_二页剩余其他\\方程式工具包图形界面版V0.3\\ && {} -jar 方程式工具包图形界面版V0.3.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def masscan(self):#棱桐c段获取
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\masscan\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动



    def enscan(self):#棱桐c段获取
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\5_二页剩余其他\\enscan\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def xiaokui(self):
        th = threading.Thread(target=self.xiaokui_start, )  # 启动子类
        th.start()
    def xiaokui_start(self):
        command = 'cd tools\\2_redteam\\5_二页剩余其他\\ && 小葵多功能转换工具.exe'
        subprocess.Popen(command, shell=True)


    def shegongzidian(self):
        th = threading.Thread(target=self.shegongzidian_start, )  # 启动子类
        th.start()

    def shegongzidian_start(self):
        command = 'cd tools\\2_redteam\\5_二页剩余其他\\shegong\\ && {} -jar bearSG.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def huohuazidian(self):
        self.label_9.setText("等闲识得东风面，万紫千红总是春。")
        th = threading.Thread(target=self.huohuazidian_start, )  # 启动子类
        th.start()

    def huohuazidian_start(self):
        command = 'cd tools\\2_redteam\\5_二页剩余其他\\shegong\\ && 火花字典生成器V1.2.exe'
        subprocess.Popen(command, shell=True)




    def No_filtering2(self):#1.无过滤
        url =self.textEdit_2.toPlainText()#获取文本内容
        return url


    def OAzonghe1(self):
        th = threading.Thread(target=self.OAzonghe1_start, )  # 启动子类
        th.start()
    def OAzonghe1_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\1号_MYExploit\\ && {} -jar MYExploit.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe2(self):
        th = threading.Thread(target=self.OAzonghe2_start, )  # 启动子类
        th.start()
    def OAzonghe2_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\2号_exp-tools\\ && {}'.format(
            java8_path + ' -javaagent:Exp-Tools-1.2.5-encrypted.jar -jar Exp-Tools-1.2.5-encrypted.jar')  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def OAzonghe3(self):
        th = threading.Thread(target=self.OAzonghe3_start, )  # 启动子类
        th.start()
    def OAzonghe3_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\3号_IWannaGetAll\\ && {} -jar IWannaGetAll.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)  # 启动

    def OAzonghe4(self):
        th = threading.Thread(target=self.OAzonghe4_start, )  # 启动子类
        th.start()
    def OAzonghe4_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\4号_最新Nday利用工具\\ && {} -jar 0Day_2023_by.V1.8.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe5(self):
        th = threading.Thread(target=self.OAzonghe5_start, )  # 启动子类
        th.start()
    def OAzonghe5_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\5号_LiqunKit\\ && {} -jar LiqunKit_1.6.2.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe6(self):
        th = threading.Thread(target=self.OAzonghe6_start, )  # 启动子类
        th.start()
    def OAzonghe6_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\6号_红蓝对抗重点OA系统漏洞利用工具新年贺岁版\\ && 红蓝对抗重点OA系统漏洞利用工具新年贺岁版V2.0.exe'
        subprocess.Popen(command, shell=True)

    def OAzonghe7(self):
        th = threading.Thread(target=self.OAzonghe7_start, )  # 启动子类
        th.start()
    def OAzonghe7_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\7号_最新的OA利用\\ && {} -jar apt_tools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe8(self):
        th = threading.Thread(target=self.OAzonghe8_start, )  # 启动子类
        th.start()
    def OAzonghe8_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\8号_海康与亿赛通通杀\\ && {} -jar Rookie.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe9(self):
        th = threading.Thread(target=self.OAzonghe9_start, )  # 启动子类
        th.start()
    def OAzonghe9_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\1_综合利用\\9_nanfeng\\ && POC工具箱.exe'
        subprocess.Popen(command, shell=True)


    def nacos_one(self):
        th = threading.Thread(target=self.nacos_one_start, )  # 启动子类
        th.start()
    def nacos_one_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\6_组件\\nacos\\ && {} nacosexp.py -u {}\"'.format(python3,self.No_filtering2()))

    def nacos_two(self):
        th = threading.Thread(target=self.nacos_two_start, )  # 启动子类
        th.start()
    def nacos_two_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\6_组件\\nacos\\ && {} NacosAddUser.py -u {}\"'.format(python3,self.No_filtering2()))


    def nacosgui(self):
        th = threading.Thread(target=self.nacosgui_start, )  # 启动子类
        th.start()
    def nacosgui_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\nacos\\one_nacos_gui\\ && {} -jar NacosExploitGUI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def nacosgui_two(self):
        th = threading.Thread(target=self.nacosgui_two_start, )  # 启动子类
        th.start()

    def nacosgui_two_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\nacos\\two_nacos_gui\\ && A-Nacos.exe'
        subprocess.Popen(command, shell=True)


    def nacos_rce(self):
        th = threading.Thread(target=self.nacos_rce_start, )  # 启动子类
        th.start()
    def nacos_rce_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\6_组件\\nacos\\three_nacos_rce\\ && {} -jar NacosRce.jar\"'.format(java8_path))

    def struts2_one(self):
        th = threading.Thread(target=self.struts2_one_start, )  # 启动子类
        th.start()

    def struts2_one_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\struts2\\ && {} -jar Struts2全版本过waf版.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def struts2zonghe(self):  # 待增加
        th = threading.Thread(target=self.struts2zonghe_scan, )  # 启动子类
        th.start()

    def struts2zonghe_scan(self):
        command = 'cd tools\\2_redteam\\6_组件\\struts2\\ &&  Struts2漏洞检查工具2018版.exe'
        subprocess.Popen(command, shell=True)

    def shiro2(self):
        th = threading.Thread(target=self.shiro2_start, )  # 启动子类
        th.start()

    def shiro2_start(self):
        command = 'cd tools\\2_redteam\\6_组件\shiro\\ && {} -jar shiro_attack-4.7.0-SNAPSHOT-all.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def shiro_key(self):
        th = threading.Thread(target=self.shiro_key_start, )  # 启动子类
        th.start()

    def shiro_key_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\6_组件\\shiro\有key无链\\ && {} -jar shiro_tool.jar\"'.format(
            java8_path))





    def thinkphp(self):
        th = threading.Thread(target=self.thinkphp_start, )  # 启动子类
        th.start()

    def thinkphp_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\thinkphp\\ && {} -jar ThinkPHP.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)


    def thinkphp2(self):
        th = threading.Thread(target=self.thinkphp2_start, )  # 启动子类
        th.start()
    def thinkphp2_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\thinkphp\\ && {} -jar ThinkphpGUI-1.3-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def thinkphp3(self):
        th = threading.Thread(target=self.thinkphp3_start, )  # 启动子类
        th.start()
    def thinkphp3_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\thinkphp\\ && {} -jar ThinkphpGUI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def springboot(self):
        th = threading.Thread(target=self.springboot_start, )  # 启动子类
        th.start()

    def springboot_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\springboot\\ && {} -jar SpringBootExploit-1.3-SNAPSHOT-all.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)


    def springexploit(self):
        th = threading.Thread(target=self.springexploit_start, )  # 启动子类
        th.start()

    def springexploit_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\springboot\\ && {} -jar SpringExploitGUI_v1.4.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def springbootjiaoben(self):
        th = threading.Thread(target=self.springbootjiaoben_start(), )  # 启动子类
        th.start()

    def springbootjiaoben_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\6_组件\\springboot\\SpringBoot-Scan-2.12\\ && {} SpringBoot-Scan.py -u {}\"'.format(
                python3, self.No_filtering2()))

    def SBjioaben(self):
        th = threading.Thread(target=self.SBjioaben_start(), )  # 启动子类
        th.start()

    def SBjioaben_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\2_redteam\\6_组件\\springboot\\SBSCAN-0.6\\ && {} sbscan.py -u {}\"'.format(
                python3, self.No_filtering2()))





    def weblogic1(self):
        th = threading.Thread(target=self.weblogic1_start, )  # 启动子类
        th.start()
    def weblogic1_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\weblogic\\ && {} -jar WebLogic全版本.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def weblogic2(self):
        th = threading.Thread(target=self.weblogic2_start, )  # 启动子类
        th.start()
    def weblogic2_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\weblogic\\ && {} -jar WeblogicVuln.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def weblogic3(self):
        th = threading.Thread(target=self.weblogic3_start, )  # 启动子类
        th.start()
    def weblogic3_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\weblogic\\ && {} -jar WeblogicTool_1.2.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def hyacinth(self):  # 文档未改
        th = threading.Thread(target=self.hyacinth_start, )  # 启动子类
        th.start()
    def hyacinth_start(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\6_组件\\OA\\hyacinth\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动
        command = 'cd tools\\2_redteam\\6_组件\\OA\\hyacinth\\ && {} -jar hyacinth.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def tongda1(self):  # 文档未改
        th = threading.Thread(target=self.tongda1_start, )  # 启动子类
        th.start()
    def tongda1_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\OA\\ && {} -jar TongdaOATool_V1.3.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def tongda2(self):  # 文档未改
        th = threading.Thread(target=self.tongda2_start, )  # 启动子类
        th.start()
    def tongda2_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\OA\\ && {} -jar TongDaOATools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def lanlin(self):  # 文档未改 ***
        th = threading.Thread(target=self.lanlin_start, )  # 启动子类
        th.start()
    def lanlin_start(self):
        command = 'cd tools\\2_redteam\\6_组件\\OA\\lanling\\ && {} -jar LandrayExploit-1.0-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)







    def No_filtering_red_two(self):#1.无过滤
        url =self.textEdit_3.toPlainText()#获取文本内容
        return url


    def shujukuzonghe(self):
        th = threading.Thread(target=self.shujukuzonghe_start, )  # 启动子类
        th.start()

    def shujukuzonghe_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\database\\1号_Multiple\\ && {} -jar Multiple.Database.Utilization.Tools-2.1.1-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def Sylas(self):  # 文档未改
        th = threading.Thread(target=self.Sylas_start, )  # 启动子类
        th.start()

    def Sylas_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\database\\Sylas\\ && Sylas-T.exe'
        subprocess.Popen(command, shell=True)

    def mssql_rce(self):
        th = threading.Thread(target=self.mssql_rce_start, )  # 启动子类
        th.start()
    def mssql_rce_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\database\\3号_mssql命令执行\\ && 121.exe'
        subprocess.Popen(command, shell=True)


    def oracle_rce(self):
        th = threading.Thread(target=self.oracle_rce_start, )  # 启动子类
        th.start()
    def oracle_rce_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\database\\2号_只针对oracle\\ && {} -jar oracleShell.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def postgre_rce(self):
        th = threading.Thread(target=self.postgre_rce_start, )  # 启动子类
        th.start()
    def postgre_rce_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\database\\4号_针对postgresql\\ && {} -jar postgreUtil-1.0-SNAPSHOT-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def redis(self):
        th = threading.Thread(target=self.redis_start(), )  # 启动子类
        th.start()
    def redis_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\7_第四页综合\\database\\ && redis-cli.exe -h {}\"'.format(self.No_filtering_red_two()))

    def redis_plus(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_redteam\\7_第四页综合\\database\\redis_plus\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def ossjieguo(self):
        th = threading.Thread(target=self.ossjieguo_start, )  # 启动子类
        th.start()
    def ossjieguo_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\7_第四页综合\\OSS\\1号_最吊接管工具\\ && cf.exe\"')

    def ossjieguo_new(self):
        th = threading.Thread(target=self.ossjieguo_new_start, )  # 启动子类
        th.start()
    def ossjieguo_new_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\7_第四页综合\\OSS\\3号_最新云接管好工具\\ && lc.exe -h\"')

    def oss_gui(self):
        th = threading.Thread(target=self.oss_gui_start, )  # 启动子类
        th.start()
    def oss_gui_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\OSS\\2号_oss接管图形化工具\\ && 云资产管理工具.exe'
        subprocess.Popen(command, shell=True)


    def alykeyone(self):
        th = threading.Thread(target=self.alykeyone_start, )  # 启动子类
        th.start()
    def alykeyone_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\OSS\\AliyunAccessKeyTools\\ && AliyunAkTools.exe'
        subprocess.Popen(command, shell=True)

    def alykeytwo(self):
        th = threading.Thread(target=self.alykeytwo_start, )  # 启动子类
        th.start()
    def alykeytwo_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\OSS\\ && 阿里Key命令执行Tools.exe'
        subprocess.Popen(command, shell=True)


    def fck(self):
        th = threading.Thread(target=self.fck_start, )  # 启动子类
        th.start()
    def fck_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\editor\\ && FCK编辑器漏洞综合利用工具.exe'
        subprocess.Popen(command, shell=True)


    def vcenter(self):
        th = threading.Thread(target=self.vcenter_start, )  # 启动子类
        th.start()

    def vcenter_start(self):
        # command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\Vcenter\\ && {} VcenterKit.py'.format(python3)
        # subprocess.Popen(command, shell=True)
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\Vcenter\\ && VcenterKit.exe'
        subprocess.Popen(command, shell=True)


    def ruoyigetshell(self):
        th = threading.Thread(target=self.ruoyigetshell_start, )  # 启动子类
        th.start()

    def ruoyigetshell_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\ruoyi\\1号 && {} -jar Ruoyi-All-1.0-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def ruoyi_two(self):
        th = threading.Thread(target=self.ruoyi_two_start, )  # 启动子类
        th.start()
    def ruoyi_two_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\ruoyi\\2号 && {} -jar ruoyiVuln.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def ruoyi_three(self):
        th = threading.Thread(target=self.ruoyi_three_start, )  # 启动子类
        th.start()
    def ruoyi_three_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\ruoyi\\3号 && {} -jar RuoYiExploitGUI_v1.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def tomcat(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_redteam\\7_第四页综合\\其他\\TomcatWeakScan-main\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def sharuan(self):
        th = threading.Thread(target=self.sharuan_start, )  # 启动子类
        th.start()
    def sharuan_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\Anti-Virus\\ && 杀软测试.html'
        subprocess.Popen(command, shell=True)

    def shai_IP(self):
        self.label_9.setText("Take my hand now, Stay close to me")
        th = threading.Thread(target=self.shai_IP_start, )  # 启动子类
        th.start()
    def shai_IP_start(self):
        command = 'cd tools\\2_redteam\\7_第四页综合\\其他\\URL-IP-main\\ && index.html'
        subprocess.Popen(command, shell=True)


    def bingxie(self):
        th = threading.Thread(target=self.bingxie_start, )  # 启动子类
        th.start()
    def bingxie_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\冰蝎\\ && javaw -jar Behinder.jar'.format(java11_path)
        subprocess.Popen(command, shell=True)


    def tianxie(self):
        th = threading.Thread(target=self.tianxie_start, )  # 启动子类
        th.start()
    def tianxie_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\天蝎\\ && {} -jar 天蝎权限管理工具.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def gesila(self):
        th = threading.Thread(target=self.gesila_start, )  # 启动子类
        th.start()
    def gesila_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\Godzilla\\ && {} -jar godzilla.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def gesila_plus(self):
        th = threading.Thread(target=self.gesila_plus_start, )  # 启动子类
        th.start()
    def gesila_plus_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\Godzilla-plus\\ && {} -jar Godzilla_ekp.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def antsword(self):
        th = threading.Thread(target=self.antsword_start, )  # 启动子类
        th.start()

    def antsword_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\AntSword\\AntSword-Loader-v4.0.3-win32-x64\\ && AntSword.exe'
        subprocess.Popen(command, shell=True)

    def caidao(self):
        th = threading.Thread(target=self.caidao_start, )  # 启动子类
        th.start()

    def caidao_start(self):
        command = 'cd tools\\2_redteam\\8_webshell\\caidao-20160622\\ && caidao.exe'
        subprocess.Popen(command, shell=True)

    def webshell(self):
        th = threading.Thread(target=self.webshell_start, )  # 启动子类
        th.start()
    def webshell_start(self):
        command = '%SystemRoot%/explorer.exe tools\\2_redteam\\8_webshell\\'
        subprocess.Popen(command, shell=True)

    def mianshawebshell(self):
        th = threading.Thread(target=self.mianshawebshell_start, )  # 启动子类
        th.start()
    def mianshawebshell_start(self):
        command = 'cd tools\\2_redteam\\9_miansha\\1号免杀_全部\\ && {} -jar Webshell_Generate-1.2.4.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def xgnitai(self):
        th = threading.Thread(target=self.xgnitai_start, )  # 启动子类
        th.start()
    def xgnitai_start(self):
        command = 'cd tools\\2_redteam\\9_miansha\\4号_小刚拟态\\ && {} -jar XG_NTAI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def bingxie_miansha(self):
        th = threading.Thread(target=self.bingxie_miansha_start, )  # 启动子类
        th.start()
    def bingxie_miansha_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\9_miansha\\2号_冰蝎\\ && ByPassBehinder.exe\"')


    def gesila_miansha(self):
        th = threading.Thread(target=self.gesila_miansha_start, )  # 启动子类
        th.start()
    def gesila_miansha_start(self):
        os.system('start ''cmd \"/K cd tools\\2_redteam\\9_miansha\\3号_哥斯拉\\ && ByPassGodzilla.exe\"')


    def weibu(self):
        th = threading.Thread(target=self.yweibu_start, )  # 启动子类
        th.start()

    def yweibu_start(self):
        command = 'explorer https://x.threatbook.com'
        subprocess.Popen(command, shell=True)
    def weixie360(self):
        th = threading.Thread(target=self.weixie360_start, )  # 启动子类
        th.start()

    def weixie360_start(self):
        command = 'explorer https://ti.360.net/#/homepage'
        subprocess.Popen(command, shell=True)

    def qianxin(self):
        th = threading.Thread(target=self.qianxin_start, )  # 启动子类
        th.start()

    def qianxin_start(self):
        command = 'explorer https://ti.qianxin.com/'
        subprocess.Popen(command, shell=True)


    def shaxiangwb(self):
        th = threading.Thread(target=self.shaxiangwb_start, )  # 启动子类
        th.start()

    def shaxiangwb_start(self):
        command = 'explorer https://s.threatbook.com'
        subprocess.Popen(command, shell=True)

    def VT(self):
        th = threading.Thread(target=self.VT_start, )  # 启动子类
        th.start()

    def VT_start(self):
        command = 'explorer https://www.virustotal.com/gui/home/upload'
        subprocess.Popen(command, shell=True)


    def shaxiang360(self):
        th = threading.Thread(target=self.shaxiang360_start, )  # 启动子类
        th.start()

    def shaxiang360_start(self):
        command = 'explorer https://ata.360.net/'
        subprocess.Popen(command, shell=True)

    def suyuantoolbox(self):
        th = threading.Thread(target=self.suyuantoolbox_start, )  # 启动子类
        th.start()
    def suyuantoolbox_start(self):
        command = 'cd tools\\3_溯源\\蓝队工具箱\\ && {} -jar BlueTeamTools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def d_eyes(self):
        th = threading.Thread(target=self.d_eyes_start, )  # 启动子类
        th.start()
    def d_eyes_start(self):
        os.system('start ''cmd \"/K cd tools\\3_溯源\\D-Eyes_1.1.0\\ && D-Eyes.exe -h\"')

    def whoamifuck(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\3_溯源\\linux应急响应\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def Ddun(self):  # 文档未改
        th = threading.Thread(target=self.Ddun_start, )  # 启动子类
        th.start()
    def Ddun_start(self):
        command = 'cd tools\\3_溯源\\Ddun\\ && D_Safe_Manage.exe'
        subprocess.Popen(command, shell=True)


    def linux_yingbi(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.append('输入命令再也不保存到history：set +o history')

    def Linux_qinglihj(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.append('Centos:')
        self.textEdit_4.append("""sudo sh -c 'files=("/var/log/wtmp" "/root/.bash_history" "/var/log/auth.log" "/var/log/secure" "/var/log/btmp" "/var/log/sudo.log" "/var/log/utmp" "/var/log/faillog" "/var/log/lastlog"); for file_path in "${files[@]}"; do if [ -w "$file_path" ]; then echo "Oh,Looks a bit of a problem,by maoge." > "$file_path"; echo "Successfully wrote to $file_path"; else echo "Failed to write to $file_path: Permission denied"; fi; done'""")
        self.textEdit_4.append('')
        self.textEdit_4.append('Ubuntu：')
        self.textEdit_4.append("""sudo bash -c 'files=("/var/log/wtmp" "/root/.bash_history" "/var/log/auth.log" "/var/log/syslog" "/var/log/btmp" "/var/log/sudo.log" "/var/log/utmp" "/var/log/faillog" "/var/log/lastlog"); for file_path in "${files[@]}"; do if [ -w "$file_path" ]; then echo "Oh, Looks a bit of a problem, by maoge." > "$file_path"; echo "Successfully wrote to $file_path"; else echo "Failed to write to $file_path: Permission denied"; fi; done'""")


    def Linux_cipanzhanyong(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看磁盘占用情况：df -hl')

    def Linux_cpu_number(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看CPU个数：cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l')

    def Linux_quanpanzhaoma(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('find / -name *.php')
        self.textEdit_4.append('php仅供参考，可以替换为jsp，asp，aspx等，或者目录，如：fscan，nmap')

    def Linux_history(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('export HISTTIMEFORMAT=\'%F %T\'')
        self.textEdit_4.append('history')

    def Linux_jincheng(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('查看当前系统上运行的所有进程：ps -ef')
        self.textEdit_4.append('查看运行中的进程：ps aux | grep pid')

    def Linux_denglu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('last')

    def Linux_duankou(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('netstat -tnlp')

    def Linux_duankoufuwu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('查看谁在使用某个端口：lsof -i :5001')

    def Linux_denglusuccess(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('grep "Accepted " /var/log/secure | awk \'{print $1,$2,$3,$9,$11}\' ')

    def Linux_xiangxiduankou(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('查看端口占用情况：netstat -apn|more')
        self.textEdit_4.append('进一步分析此进程：ps aux|grep \'pid\'')



    def rizhi(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：eventvwr')
        th = threading.Thread(target=self.rizhi_start, )  # 启动子类
        th.start()

    def rizhi_start(self):
        command = 'eventvwr'
        subprocess.Popen(command, shell=True)


    def renwu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：win+r schtasks.exe')
        th = threading.Thread(target=self.renwu_start, )  # 启动子类
        th.start()

    def renwu_start(self):
        os.system('start ''cmd \"/K schtasks.exe\"')

    def guanliqi(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('已启动任务管理器')
        th = threading.Thread(target=self.guanliqi_start, )  # 启动子类
        th.start()

    def guanliqi_start(self):
        command = 'C:\\Windows\\system32\\taskmgr.exe'
        subprocess.Popen(command, shell=True)

    def duankou(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：netstat -ano')
        th = threading.Thread(target=self.duankou_start, )  # 启动子类
        th.start()

    def duankou_start(self):
        os.system('start ''cmd \"/K netstat -ano\"')


    def yonghuzu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：win+r compmgmt.msc')
        th = threading.Thread(target=self.yonghuzu_start, )  # 启动子类
        th.start()

    def yonghuzu_start(self):
        command = 'compmgmt.msc'
        subprocess.Popen(command, shell=True)

    def qidongxiang(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：win+r msconfig')
        self.textEdit_4.append('启动目录：win+r shell:startup\n或者：%programdata%\Microsoft\Windows\Start Menu\Programs\Startup')
        th = threading.Thread(target=self.qidongxiang_start, )  # 启动子类
        th.start()

    def qidongxiang_start(self):
        command = 'msconfig'
        maoge_start = "explorer %programdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        subprocess.Popen(maoge_start, shell=True)
        #time.sleep(0.5)
        subprocess.Popen(command, shell=True)

    def keyi(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：netstat -b -n')
        th = threading.Thread(target=self.keyi_start, )  # 启动子类
        th.start()

    def keyi_start(self):
        os.system('start ''cmd \"/K netstat -b -n\"')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = button()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec())  # 注意 PyQt6 用 exec()
