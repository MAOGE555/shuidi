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

# 设置启动UI的固定
if getattr(sys, 'frozen', False):
    pyqt_path = os.path.dirname(sys.modules['PyQt6'].__file__)
    os.environ['QT_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt6", "plugins")



# 获取当前绝对路径
tools_path = os.getcwd()
if platform.system() == "Windows":
    java8_path = (tools_path + "\\tools\\0_path\\java-8\\bin\\java.exe").replace("\\", "\\\\")
    java21_path = (tools_path + "\\tools\\0_path\\jdk-21\\bin\\java.exe").replace("\\", "\\\\")
    python3 = (tools_path + "\\tools\\0_path\\Python39\\python.exe").replace("\\", "\\\\")


class button(new.Ui_MainWindow):
    def messageDialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(
            '本工具所有蓝色的地方，都是需要输入URL启动的。\n黄色的地方点开是打开在线网站。\n无颜色或灰白色的地方会自行打开软件或打开目录。')
        msg_box.setWindowTitle('功能介绍')
        msg_box.exec()

    def messagetwo(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        th = threading.Thread(target=self.messagetwo_start, )  # 启动子类
        th.start()
        msg_box.setText('https://github.com/MAOGE555/shuidi  \n')
        msg_box.setWindowTitle('项目地址:')
        msg_box.exec()
    def messagetwo_start(self):
        command = 'explorer https://github.com/MAOGE555/shuidi'
        subprocess.Popen(command, shell=True)

    def messagethree(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText('欢迎反馈问题\nQ群：261086583')
        msg_box.setWindowTitle('反馈群:')
        msg_box.exec()




    # ======================================================================
    #                            分页栏
    # ======================================================================
    def burpsuite(self):#文档未改
        th = threading.Thread(target=self.burpsuite_start, )  #启动子类
        th.start()
    def burpsuite_start(self):
        #os.system('start ''cmd \"/K cd tools\\1_常用\\BurpSuiteV2024.3.1.2\\ && CNBurp.VBS\"')
        command = 'cd tools\\1_常用\\BurpSuite\\ && BurpSuitePro.exe'
        subprocess.Popen(command, shell=True)

    def yaki(self):#文档未改
        th = threading.Thread(target=self.yaki_start, )  #启动子类
        th.start()
    def yaki_start(self):
        #os.system('start ''cmd \"/K cd tools\\1_常用\\BurpSuiteV2024.3.1.2\\ && CNBurp.VBS\"')
        command = 'cd tools\\1_常用\\Yaki\\Yakit\\ && Yakit.exe'
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
        command = '%SystemRoot%/explorer.exe tools\\5_内网渗透工具\\'   #取当前目录
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
        command = 'cd tools\\1_常用\\mobaxterm\\ && MobaXterm_Personal.exe'
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

    def openvpn(self):  # 文档未改
        th = threading.Thread(target=self.openvpn_start, )  # 启动子类
        th.start()
    def openvpn_start(self):
        command = 'cd tools\\1_常用\\openvpn\\ && OpenVPNConnect.exe'
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

    # ======================================================================
    #                            分页栏1
    # ======================================================================


    def e0e1_wx(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_微信小程序\\e0e1-wx\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def KillWxapkg(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_微信小程序\\KillWxapkg\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def wxapkg(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_微信小程序\\wxapkg\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def wxapkgconvertor(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_微信小程序\\wxapkg-convertor\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def app_fby(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\2_微信小程序\\app反编译\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动



    def app_ke(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\3_杂项栏\\APP查壳反编译\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def ingram(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\3_杂项栏\\摄像头检测\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def awvs(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\3_杂项栏\\AWVS安装包\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def awvs_scan(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\3_杂项栏\\Awvs14批量\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def ipguishu(self):  # 文档未改
        #command = '%SystemRoot%/explorer.exe {} \\tools\\3_杂项栏\\IP归属批量查询\\'.format(tools_path)
        #subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.ipguishu_start, )  # 启动子类
        th.start()
    def ipguishu_start(self):
        command = 'cd tools\\3_杂项栏\\IP归属批量查询\\ && {} -jar SelfIPManager-1.4.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def shuapin(self):
        th = threading.Thread(target=self.shuapin_start, )
        th.start()
    def shuapin_start(self):
        command = 'cd tools\\3_杂项栏\\ && QQ轰炸.exe'
        subprocess.Popen(command, shell=True)

    def tuba(self):
        th = threading.Thread(target=self.tuba_start, )
        th.start()
    def tuba_start(self):
        command = 'cd tools\\3_杂项栏\\图吧工具箱\\ && 图吧工具箱2025.exe'
        subprocess.Popen(command, shell=True)

    def vpsssss(self):
        self.textEdit_5.setFontPointSize(12)
        self.textEdit_5.setPlainText('')
        self.textEdit_5.append('命令为：bash <(wget -qO- bash.spiritlhl.net/ecs)')
        self.textEdit_5.append('或者：curl -L https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh -o ecs.sh && chmod +x ecs.sh && bash ecs.sh')


    def nimingvps(self):
        self.textEdit_5.setFontPointSize(12)
        self.textEdit_5.setPlainText('')
        self.textEdit_5.append('网址：https://www.vultr.com')

        th = threading.Thread(target=self.nimingvps_start, )  # 启动子类
        th.start()
    def nimingvps_start(self):
        time.sleep(2)
        command = 'explorer https://www.vultr.com'
        subprocess.Popen(command, shell=True)


    def wireshark(self):
        th = threading.Thread(target=self.wireshark_start, )
        th.start()
    def wireshark_start(self):
        command = 'cd tools\\3_杂项栏\\Wireshark\\ && Wireshark.exe'
        subprocess.Popen(command, shell=True)

    # ======================================================================
    #                            分页栏2
    # ======================================================================
    def No_filtering(self):#1.无过滤
        url =self.textEdit.toPlainText()#获取文本内容
        return url

    def fscan(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\fscan\\fscan.exe"
        target = self.No_filtering()
        user_args = target.split()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-h"]  + user_args
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\fscan\\ && fscan.exe -h {}\"'.format(self.No_filtering()))



    def dddd(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\dddd-main\\dddd64.exe"
        target = self.No_filtering()
        user_args = target.split()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-t"]  + user_args +  ["-gpt", "800", "-wt", "1000"]
            final_command = ['cmd', '/K'] + scan_command
            print(f"即将执行的命令: {final_command}")
            tool_directory = os.path.dirname(path)

            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)

    def rustscan(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\rustscan\\rustscan.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-a", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)

        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\rustscan\\ && rustscan.exe -a {}\"'.format(self.No_filtering()))

    def vscan(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\vscan\\vscan.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-host", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)


        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\vscan\\ && vscan.exe -host {}\"'.format(self.No_filtering()))
    def soda(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\soda\\soda64.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-t", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        #
        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\soda\\ && soda64.exe -t {}\"'.format(self.No_filtering()))

    def gogo(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\gogo\\gogo.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-i", target,"-p", "win,db,top2,http"]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)

        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\gogo\\ && gogo.exe -i {} -p win,db,top2,http \"'.format(self.No_filtering()))

    def tscan(self):
        th = threading.Thread(target=self.tscan_start, )
        th.start()
    def tscan_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\Tscanplus\\ && TscanPlus_Win_Amd64.exe'
        subprocess.Popen(command, shell=True)

    def tscan_cient(self):
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\TscanCient\\TscanClient.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-h',target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\TscanCient\\ && TscanClient.exe -h {} \"'.format(self.No_filtering()))

    def nmap(self):  # 文档未改
        path = tools_path+"\\tools\\4_redteam\\1_扫描器\\nmap\\nmap.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-sn","-PS80", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # if self.No_filtering() ==None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system ('start ''cmd \"/K cd tools\\4_redteam\\1_扫描器\\nmap\\ && nmap.exe -sn -PS80 {}\"'.format(self.No_filtering()))


    def masscan(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\1_扫描器\\masscan\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def railgun(self):
        th = threading.Thread(target=self.railgun_start, )
        th.start()
    def railgun_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\Railgun\\ && Railgun.exe'
        subprocess.Popen(command, shell=True)


    def tanggo(self):
        th = threading.Thread(target=self.tanggo_start, )
        th.start()
    def tanggo_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\tanggo\\ && tanggo.exe'
        subprocess.Popen(command, shell=True)

    def mitan(self):
        th = threading.Thread(target=self.mitan_start, )
        th.start()
    def mitan_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\mitan\\ && {} -jar mitan-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def Slack(self):
        th = threading.Thread(target=self.Slack_start, )
        th.start()
    def Slack_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\slack\\ && Slack-windows-amd64.exe'
        subprocess.Popen(command, shell=True)

    def ez(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\1_扫描器\\EZ\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def xray(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\1_扫描器\\Xray\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def goby(self):
        th = threading.Thread(target=self.goby_start, )
        th.start()
    def goby_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\goby\\ && Goby.exe'
        subprocess.Popen(command, shell=True)

    def chaojiruokoulin(self):  # 文档未改
        th = threading.Thread(target=self.chaojiruokoulin_start, )  # 启动子类
        th.start()

    def chaojiruokoulin_start(self):
        command = 'cd tools\\4_redteam\\1_扫描器\\超级弱口令检查工具V1.0 Beta28 20190715\\ && SNETCracker.exe'
        subprocess.Popen(command, shell=True)


    def dirsearch(self):  # 文档未改
        th = threading.Thread(target=self.dirsearch_start, )  # 启动子类
        th.start()
    def dirsearch_start(self):
        # path = tools_path + "\\tools\\4_redteam\\1_扫描器\\nmap\\nmap.exe"
        # target = self.No_filtering()
        # if os.path.exists(path):
        #     # 将要执行的完整命令（程序+参数）构建成一个列表
        #     scan_command = [path, "-sn", "-PS80", target]
        #     final_command = ['cmd', '/K'] + scan_command
        #     tool_directory = os.path.dirname(path)
        #     subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        # else:
        #     program_dir = os.path.dirname(path)
        #     if os.path.exists(program_dir):
        #         os.startfile(program_dir)
        #     elif 'tools_path' in locals() and os.path.exists(tools_path):
        #         os.startfile(tools_path)
        os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\dirsearch\\ && {} dirsearch.py -u {}\"'.format(python3,self.No_filtering()))


    def spray(self):  # 文档未改
        path = tools_path+"\\tools\\4_redteam\\2_目录扫描\\spray\\spray.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-d", "top1000.txt", "-u",target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)

    #
    #     th = threading.Thread(target=self.spray_start, )  # 启动子类
    #     th.start()
    # def spray_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\spray\\ && spray.exe -d top1000.txt -u {}\"'.format(self.No_filtering()))

    def kbscan(self):
        th=threading.Thread(target=self.kbscan_start,)#启动子类
        th.start()
    def kbscan_start(self):
        command = 'cd tools\\4_redteam\\2_目录扫描\\7kbscan\\ && 7kbscan-WebPathBrute.exe'
        subprocess.Popen(command, shell=True)

    def yujian(self):
        th=threading.Thread(target=self.yujian_start,)#启动子类
        th.start()
    def yujian_start(self):
        command = 'cd tools\\4_redteam\\2_目录扫描\\御剑\\ && 御剑后台扫描工具.exe'
        subprocess.Popen(command, shell=True)

    def feroxbuster(self):  # 文档未改
        path = tools_path+"\\tools\\4_redteam\\2_目录扫描\\feroxbuster\\feroxbuster.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-u',target,'-w', 'top1000.txt']
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.feroxbuster_start, )  # 启动子类
    #     th.start()
    # def feroxbuster_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\feroxbuster\\ && feroxbuster.exe -u {} -w top1000.txt\"'.format(self.No_filtering()))

    def nomore403(self):  # 文档未改
        path = tools_path + "\\tools\\4_redteam\\2_目录扫描\\403绕过\\nomore403.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-u", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.nomore403_start, )  # 启动子类
    #     th.start()
    # def nomore403_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\403绕过\\ && nomore403.exe -u {}\"'.format(self.No_filtering()))


    def ffuf(self):  # 文档未改
        th = threading.Thread(target=self.ffuf_start, )  # 启动子类
        th.start()
    def ffuf_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\ffuf\\ && ffuf.exe -u {}/FUZZ -w parameter.txt\"'.format(self.No_filtering()))

    def Arjun(self):  # 文档未改
        th = threading.Thread(target=self.Arjun_start, )  # 启动子类
        th.start()

    def Arjun_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\Arjun\\ && arjun -u {}\"'.format(self.No_filtering()))

    def katana(self):  # 文档未改
        path = tools_path + "\\tools\\4_redteam\\2_目录扫描\\katana\\katana.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-u", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.katana_start, )  # 启动子类
    #     th.start()
    # def katana_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\katana\\ && katana.exe -u {}\"'.format(self.No_filtering()))

    def rad(self):  # 文档未改
        path = tools_path + "\\tools\\4_redteam\\2_目录扫描\\rad\\rad.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-t", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.rad_start, )  # 启动子类
    #     th.start()
    # def rad_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\2_目录扫描\\rad\\ && rad.exe -t {}\"'.format(self.No_filtering()))

    # ======================================================================
    #                            分页栏3
    # ======================================================================


    def subfinder(self):  # 文档未改
        path = tools_path + "\\tools\\4_redteam\\3_子域名and指纹识别\\subfinder\\subfinder.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-d", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # os.system(
        #     'start ''cmd \"/K cd tools\\4_redteam\\3_子域名and指纹识别\\subfinder\\ && subfinder.exe -d {}\"'.format(self.No_filtering()))

    def oneforall(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\3_子域名and指纹识别\\OneForAll-0.4.5\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def ksubdomain(self):  # 文档未改
        path = tools_path + "\\tools\\4_redteam\\3_子域名and指纹识别\\ksubdomain\\ksubdomain.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "e",'-d', target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.ksubdomain_start, )  # 启动子类
    #     th.start()
    # def ksubdomain_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\3_子域名and指纹识别\\ksubdomain\\ && ksubdomain.exe e -d {}\"'.format(self.No_filtering()))



    def ziyumingwajueji(self):  # 文档未改
        th = threading.Thread(target=self.ziyumingwajueji_start, )  # 启动子类
        th.start()
    def ziyumingwajueji_start(self):
        command = 'cd tools\\4_redteam\\3_子域名and指纹识别\\子域名挖掘机5.0最新版\\ && Layer.exe'
        subprocess.Popen(command, shell=True)

    def chunsou(self):  # 文档未改
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\3_子域名and指纹识别\\chunsou\\ && {} chunsou.py -u {}\"'.format(python3, self.No_filtering()))



    def P1finger(self):
        path = tools_path + "\\tools\\4_redteam\\3_子域名and指纹识别\\P1finger\\P1finger.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "rule", '-u', target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # if self.No_filtering() == None:
        #     msg_box = QMessageBox(QMessageBox.Warning, '你这扑街仔', '不许啥都不输入')
        #     msg_box.exec_()
        # else:
        #     os.system('start ''cmd \"/K cd tools\\4_redteam\\3_子域名and指纹识别\\P1finger\\ && P1finger.exe rule -u {}\"'.format(
        #         self.No_filtering()))

    def observer_ward(self):  # 文档未改
        path = tools_path+"\\tools\\4_redteam\\3_子域名and指纹识别\\observer_ward\\observer_ward.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, "-t", target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)

    #     th = threading.Thread(target=self.observer_ward_start, )  # 启动子类
    #     th.start()
    # def observer_ward_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\3_子域名and指纹识别\\observer_ward\\ && observer_ward.exe -t {}\"'.format(self.No_filtering()))



    def lengtong(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\3_子域名and指纹识别\\Ehole棱桐资产扫描梳理\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def chaoxi(self):
        th = threading.Thread(target=self.chaoxi_start, )  # 启动子类
        th.start()
    def chaoxi_start(self):
        command = 'explorer http://finger.tidesec.com/'
        subprocess.Popen(command, shell=True)

    def P1fingeronline(self):
        th = threading.Thread(target=self.P1fingeronline_start, )  # 启动子类
        th.start()

    def P1fingeronline_start(self):
        command = 'explorer http://p1finger.securapath.org/'
        subprocess.Popen(command, shell=True)



    def URLFinder(self):
        path = tools_path + "\\tools\\4_redteam\\4_JS探测\\URLFinder\\URLFinder.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-u', target,"-s", 'all','-m','3']
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            # 尝试打开程序所在的文件夹
            program_dir = os.path.dirname(path)
            # 如果程序所在的文件夹存在，就打开它
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            # 如果它不存在，就尝试打开更上层的 tools_path 目录 (如果它存在的话)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # os.system(
        #     'start ''cmd \"/K cd tools\\4_redteam\\4_JS探测\\URLFinder\\ && URLFinder.exe -u {} -s all -m 3\"'.format(
        #         self.No_filtering()))



    def jjjjjjjjjjjjs(self):
        path = tools_path+"\\tools\\4_redteam\\4_JS探测\\jjjjjjjs\\jjjjjjjjjjjjjs.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, target,'fuzz nobody']
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # os.system(
        #     'start ''cmd \"/K cd tools\\4_redteam\\4_JS探测\\jjjjjjjs\\ && jjjjjjjjjjjjjs.exe {} fuzz nobody\"'.format(
        #         self.No_filtering()))

    def swagger_hack(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\4_JS探测\\swagger-hack-main\\ && {} swagger-hack2.0.py -u {}\"'.format(
                python3, self.No_filtering()))

    def SwaggerHound(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\4_JS探测\\SwaggerHound-main\\ && {} swagger-hound.py -u {}\"'.format(
                python3, self.No_filtering()))


    def packjs(self):  # 文档未改
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\4_JS探测\\packjs\\ && {} PackerFuzzer.py -u {}\"'.format(
                python3, self.No_filtering()))


    def packjsjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\4_JS探测\\packjs\\reports\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动




    def fofa(self):  # 文档未改
        th = threading.Thread(target=self.fofa_start, )  # 启动子类
        th.start()
    def fofa_start(self):
        command = 'cd tools\\4_redteam\\5_信息收集and漏扫\\fofa\\ && {} -jar fofaviewer.jar'.format(java8_path)
        print(command)
        subprocess.Popen(command, shell=True)

    def enscan(self):#棱桐c段获取
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\enscan\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def httpxjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\httpx\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def webfinder(self):  # 文档未改
        th = threading.Thread(target=self.webfinderstart, )  # 启动子类
        th.start()
    def webfinderstart(self):
        command = 'cd tools\\4_redteam\\5_信息收集and漏扫\\web批量请求器\\ && {} -jar WebBatchRequest.jar'.format(java8_path)
        print(command)
        subprocess.Popen(command, shell=True)

    def nuclei(self):
        path = tools_path+"\\tools\\4_redteam\\5_信息收集and漏扫\\B_nuclei\\nuclei.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-u',target,'-stats']
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
        # th = threading.Thread(target=self.nuclei_start, )  # 启动子类
        # th.start()
    # def nuclei_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\5_信息收集and漏扫\\B_nuclei\\ && nuclei.exe -u {} -rl 1000 -bs 200 -c 200 -stats\"'.format(
    #                                                                                                          self.No_filtering()))

    def afrog(self):
        path = tools_path+"\\tools\\4_redteam\\5_信息收集and漏扫\\afrog\\afrog.exe"
        target = self.No_filtering()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-t',target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.afrog_start, )  # 启动子类
    #     th.start()
    # def afrog_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\5_信息收集and漏扫\\afrog\\ && afrog.exe -t {}\"'.format(
    #                                                                                                          self.No_filtering()))


    def pocsuite3(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\5_信息收集and漏扫\\pocsuite3-2.1.0\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def sqlmap(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\sqlmap\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动


    def ghauri(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\ghauri\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def sqlmap_plus(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\SqlmapXPlus\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def venom(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\5_信息收集and漏扫\\venom\\'  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    # ============================================================================================================================================
    #                            分页栏3
    # ============================================================================================================================================


    def No_filtering2(self):#1.无过滤
        url =self.textEdit_2.toPlainText()#获取文本内容
        return url


    def OAzonghe1(self):
        th = threading.Thread(target=self.OAzonghe1_start, )  # 启动子类
        th.start()
    def OAzonghe1_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\1_MYExploit\\ && {} -jar MYExploit.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe2(self):
        th = threading.Thread(target=self.OAzonghe2_start, )  # 启动子类
        th.start()
    def OAzonghe2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\2_exp-tools\\ && {}'.format(
            java8_path + ' -javaagent:Exp-Tools-1.3.1-encrypted.jar -jar Exp-Tools-1.3.1-encrypted.jar')  # 取当前目录
        subprocess.Popen(command, shell=True)  # 启动

    def OAzonghe3(self):
        th = threading.Thread(target=self.OAzonghe3_start, )  # 启动子类
        th.start()
    def OAzonghe3_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\3_IWannaGetAll\\ && {} -jar IWannaGetAll-v1.4.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)  # 启动

    def OAzonghe4(self):
        th = threading.Thread(target=self.OAzonghe4_start, )  # 启动子类
        th.start()
    def OAzonghe4_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\4_daydayexp\\ && {} -jar daydayExp-1.1-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe5(self):
        th = threading.Thread(target=self.OAzonghe5_start, )  # 启动子类
        th.start()
    def OAzonghe5_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\7_hyacinth\\ && {} -jar hyacinth.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe6(self):
        th = threading.Thread(target=self.OAzonghe6_start, )  # 启动子类
        th.start()
    def OAzonghe6_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\5_LiqunKit\\ && {} -jar LiqunKit_1.6.2.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe7(self):
        th = threading.Thread(target=self.OAzonghe7_start, )  # 启动子类
        th.start()
    def OAzonghe7_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\6_apt_tools\\ && {} -jar apt.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe8(self):
        th = threading.Thread(target=self.OAzonghe8_start, )  # 启动子类
        th.start()
    def OAzonghe8_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\8_大华\\ && {} -jar DahuaExploitGUI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def OAzonghe9(self):
        th = threading.Thread(target=self.OAzonghe9_start, )  # 启动子类
        th.start()
    def OAzonghe9_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\9_海康威视\\ && hikvision漏洞利用工具.exe'
        subprocess.Popen(command, shell=True)

    def OAzonghe10(self):
        th = threading.Thread(target=self.OAzonghe10_start, )  # 启动子类
        th.start()
    def OAzonghe10_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\ruoyi\\ruoyiVuln\\ && {} -jar ruoyiVuln.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe11(self):
        th = threading.Thread(target=self.OAzonghe11_start, )  # 启动子类
        th.start()
    def OAzonghe11_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\ruoyi\\Ruoyi-All\\ && {} -jar Ruoyi-All-1.0-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe12(self):
        th = threading.Thread(target=self.OAzonghe12_start, )  # 启动子类
        th.start()
    def OAzonghe12_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\ruoyi\\RuoYiExploitGUI\\ && {} -jar RuoYiExploitGUI_v1.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def OAzonghe13(self):
        th = threading.Thread(target=self.OAzonghe13_start, )  # 启动子类
        th.start()
    def OAzonghe13_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\1_综合利用\\8号_海康与亿赛通通杀\\ && {} -jar Rookie.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def nacosgui(self):
        th = threading.Thread(target=self.nacosgui_start, )  # 启动子类
        th.start()
    def nacosgui_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\nacos\\one_nacos_gui\\ && {} -jar NacosExploitGUI_v4.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def nacosexploit(self):
        th = threading.Thread(target=self.nacosexploit_start, )  # 启动子类
        th.start()
    def nacosexploit_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\nacos\\nacosexploit\\ && {} -jar NacosExploit.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def nacos_one(self):
        th = threading.Thread(target=self.nacos_one_start, )  # 启动子类
        th.start()
    def nacos_one_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\6_框架and组件\\nacos\\nacos_adduser\\ && {} NacosAddUser.py -u {}\"'.format(python3,self.No_filtering2()))


    def nacos_two(self):
        th = threading.Thread(target=self.nacos_two_start, )  # 启动子类
        th.start()
    def nacos_two_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\nacos\\Nacos内存马gui\\ && {} -jar NacosExploit_v1.1.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def nacosneicunma(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\6_框架and组件\\nacos\\nacos_内存马\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动



    def struts2_one(self):
        th = threading.Thread(target=self.struts2_one_start, )  # 启动子类
        th.start()

    def struts2_one_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\struts2\\ABC123\\ && {} -jar Struts2.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def struts2zonghe(self):  # 待增加
        th = threading.Thread(target=self.struts2zonghe_scan, )  # 启动子类
        th.start()

    def struts2zonghe_scan(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\struts2\\ &&  Struts2漏洞检查工具2018版.exe'
        subprocess.Popen(command, shell=True)



    def shiro1(self):
        th = threading.Thread(target=self.shiro1_start, )  # 启动子类
        th.start()

    def shiro1_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\shiro\\shiro增强\\ && {} -jar shiro_attack-4.7.0-SNAPSHOT-all.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def shiro2(self):
        th = threading.Thread(target=self.shiro2_start, )  # 启动子类
        th.start()

    def shiro2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\shiro\\ShiroExploit-飞鸿\\ && {} -jar ShiroExploit.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def shiro_key(self):
        th = threading.Thread(target=self.shiro_key_start, )  # 启动子类
        th.start()

    def shiro_key_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\6_框架and组件\\shiro\\有key无链\\ && {} -jar shiro_tool.jar\"'.format(
            java8_path))





    def thinkphp(self):
        th = threading.Thread(target=self.thinkphp_start, )  # 启动子类
        th.start()

    def thinkphp_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\thinkphp\\thinkphp_gui_tools\\ && {} -jar ThinkPHP.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def thinkphp2(self):
        th = threading.Thread(target=self.thinkphp2_start, )  # 启动子类
        th.start()
    def thinkphp2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\thinkphp\\ThinkphpGUI-莲花\\ && {} -jar ThinkphpGUI-1.3-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def thinkphp3(self):
        th = threading.Thread(target=self.thinkphp3_start, )  # 启动子类
        th.start()
    def thinkphp3_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\thinkphp\\Aazhen-RexHa\\ && {} -javaagent:rexha.jar -jar rexha.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def thinkphp4(self):
        th = threading.Thread(target=self.thinkphp4_start, )  # 启动子类
        th.start()
    def thinkphp4_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\thinkphp\\TP_Attack_GUI\\ && {} -jar TP_Attack_GUI.jar'.format(java21_path)
        subprocess.Popen(command, shell=True)

    def thinkphp5(self):
        th = threading.Thread(target=self.thinkphp5_start, )  # 启动子类
        th.start()
    def thinkphp5_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\thinkphp\\ThinkPHPLogScan\\ && {} -jar ThinkPHPLogScan.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def springboot(self):
        th = threading.Thread(target=self.springboot_start, )  # 启动子类
        th.start()

    def springboot_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\springboot\\springboot综合利用\\ && {} -jar SpringBootExploit-1.3-SNAPSHOT-all.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)


    def springboot2(self):
        th = threading.Thread(target=self.springboot2_start, )  # 启动子类
        th.start()

    def springboot2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\springboot\\springboot2\\ && {} -jar Spring_All_Reachable-2.1.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)


    def springexploit(self):
        th = threading.Thread(target=self.springexploit_start, )  # 启动子类
        th.start()

    def springexploit_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\springboot\\springboot综合2\\ && {} -jar XM-SpringExploitGUI-v2.3.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def springbootjiaoben(self):
        th = threading.Thread(target=self.springbootjiaoben_start(), )  # 启动子类
        th.start()

    def springbootjiaoben_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\6_框架and组件\\springboot\\SpringBoot-Scan\\ && {} SpringBoot-Scan.py -u {}\"'.format(
                python3, self.No_filtering2()))

    def SBjioaben(self):
        th = threading.Thread(target=self.SBjioaben_start(), )  # 启动子类
        th.start()

    def SBjioaben_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\6_框架and组件\\springboot\\SBSCAN\\ && {} sbscan.py -u {}\"'.format(
                python3, self.No_filtering2()))





    def weblogic1(self):
        th = threading.Thread(target=self.weblogic1_start, )  # 启动子类
        th.start()
    def weblogic1_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\weblogic\\weblogic_old_superman\\ && {} -jar WebLogic全版本.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def weblogic2(self):
        th = threading.Thread(target=self.weblogic2_start, )  # 启动子类
        th.start()
    def weblogic2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\weblogic\\WeblogicTool_kimjun\\ && {} -jar WeblogicTool_1.3.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def weblogic3(self):
        th = threading.Thread(target=self.weblogic3_start, )  # 启动子类
        th.start()
    def weblogic3_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\weblogic\\WeblogicExploit-内存马\\ && {} -jar Weblogic-GUI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)
    def weblogic4(self):
        th = threading.Thread(target=self.weblogic4_start, )  # 启动子类
        th.start()
    def weblogic4_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\weblogic\\weblogic_old_雷石\\ && {} -jar WeblogicVuln.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def oajiemi(self):  # 文档未改
        th = threading.Thread(target=self.oajiemi_start, )  # 启动子类
        th.start()
    def oajiemi_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\OA解密\\ && {} -jar DecryptTools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def tongda1(self):  # 文档未改
        th = threading.Thread(target=self.tongda1_start, )  # 启动子类
        th.start()
    def tongda1_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\通达skyxuan\\ && {} -jar TongDaOATools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def tongda2(self):  # 文档未改
        th = threading.Thread(target=self.tongda2_start, )  # 启动子类
        th.start()
    def tongda2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\通达xiaokp7\\ && {} -jar TongdaTools.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def yongyou1(self):  # 文档未改
        th = threading.Thread(target=self.yongyou1_start, )  # 启动子类
        th.start()
    def yongyou1_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\用友wgpsec\\ && {} -jar YongYouNcTool-1.0.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def yongyou2(self):  # 文档未改
        th = threading.Thread(target=self.yongyou2_start, )  # 启动子类
        th.start()
    def yongyou2_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\用友Chave0v0\\ && {} -jar YONYOU-TOOL-2.0.9.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def zhiyuan(self):  # 文档未改 ***
        th = threading.Thread(target=self.zhiyuan_start, )  # 启动子类
        th.start()
    def zhiyuan_start(self):
        command = 'cd tools\\4_redteam\\6_框架and组件\\OA\\致远oA\\ && {} -jar 致远OA漏洞全版本扫描工具v1.0.1.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    # ================================================================================================================
    #                            分页栏4
    # ================================================================================================================

    def No_filtering_three(self):#1.无过滤
        url =self.textEdit_6.toPlainText()#获取文本内容
        return url

    def zidian(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\1、渗透常用放这\\A--字典大全\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def wannengbm(self):
        th = threading.Thread(target=self.wannengbm_start, )  # 启动子类
        th.start()

    def wannengbm_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\shegong\\ToolsFx-1.18.0-withjre-win-x64\\ && ToolsFx.exe'
        subprocess.Popen(command, shell=True)

    def onlonebianma(self):
        th = threading.Thread(target=self.onlonebianma_start, )  # 启动子类
        th.start()
    def onlonebianma_start(self):
        command = 'explorer http://www.hiencode.com/'
        subprocess.Popen(command, shell=True)

    def shegong1(self):  # 文档未改
        th = threading.Thread(target=self.shegong1_start, )  # 启动子类
        th.start()
    def shegong1_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\shegong\\dicttools\\ && {} -jar dicttools-1.0-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)
    def shegong2(self):
        th = threading.Thread(target=self.shegong2_start, )  # 启动子类
        th.start()
    def shegong2_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\shegong\\社工字典生成\\ && index.html'
        subprocess.Popen(command, shell=True)


    def heapdumpjieguo(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\7_zonghe\\文件利用类\\heapdump_tool\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动


    def JDumpSpider(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\7_zonghe\\文件利用类\\JDumpSpider\\'   #取当前目录
        subprocess.Popen(command, shell=True)#启动

    def druid_sessions(self):
        th = threading.Thread(target=self.druid_sessions_start, )
        th.start()
    def druid_sessions_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\文件利用类\\druid_sessions\\ && {} -jar druid_sessions.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def dumpall(self):  # 文档未改
        th = threading.Thread(target=self.dumpall_start, )  # 启动子类
        th.start()
    def dumpall_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\7_zonghe\\文件利用类\\dumpall\\ && dumpall\"'.format(self.No_filtering_three()))


    def svn(self):  # 文档未改
        th = threading.Thread(target=self.svn_start, )  # 启动子类
        th.start()
    def svn_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\文件利用类\\svn\\ && Seay-Svn.exe'
        subprocess.Popen(command, shell=True)



    def ossjieguo(self):
        th = threading.Thread(target=self.ossjieguo_start, )  # 启动子类
        th.start()
    def ossjieguo_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\7_zonghe\\OSS\\1号_最好接管工具\\ && cf.exe\"')


    def ossjieguo_lc(self):
        th = threading.Thread(target=self.ossjieguo_lc_start, )  # 启动子类
        th.start()
    def ossjieguo_lc_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\7_zonghe\\OSS\\3号_最新云接管好工具\\ && lc.exe -h\"')


    def oss_gui(self):
        th = threading.Thread(target=self.oss_gui_start, )  # 启动子类
        th.start()
    def oss_gui_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\OSS\\2号_oss接管图形化工具\\ && 云资产管理工具.exe'
        subprocess.Popen(command, shell=True)


    def aksk_tool(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\OSS\\aksk_tool\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def alykeyone(self):
        th = threading.Thread(target=self.alykeyone_start, )  # 启动子类
        th.start()
    def alykeyone_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\OSS\\AliyunAccessKeyTools\\ && AliyunAkTools.exe'
        subprocess.Popen(command, shell=True)

    def alykeytwo(self):
        th = threading.Thread(target=self.alykeytwo_start, )  # 启动子类
        th.start()
    def alykeytwo_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\OSS\\ && 阿里Key命令执行Tools.exe'
        subprocess.Popen(command, shell=True)

    def API_explorer(self):
        th = threading.Thread(target=self.API_explorer_start, )  # 启动子类
        th.start()
    def API_explorer_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\OSS\\API-explorer\\ && API-Explorer_v2.1.0.exe'
        subprocess.Popen(command, shell=True)

    def API_T00L(self):
        th = threading.Thread(target=self.API_T00L_start, )
        th.start()
    def API_T00L_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\OSS\\API-T00L\\ && {} -jar API-T00L_v1.3.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def mapkey(self):  # 文档未改
        th = threading.Thread(target=self.mapkey_start, )  # 启动子类
        th.start()
    def mapkey_start(self):
        os.system(
            'start ''cmd \"/K cd tools\\4_redteam\\7_zonghe\\OSS\\map_key_check-main\\ && {} check.py\"'.format(
                python3))

    def old_JNDII(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\内存马\\老JNDI\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def JNDIInject(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\内存马\\JNDIInject-1.2\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def RMI_Inj_MemShell(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\内存马\\RMI_Inj_MemShell\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def jndi_tool(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\内存马\\jndi_tool\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def jMG_gui(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\内存马\\jMG-gui\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.jMG_gui_start, )
        th.start()
    def jMG_gui_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\内存马\\jMG-gui\\ && {} -jar jMG-gui-1.0.8.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def shai_IP(self):
        #self.label_9.setText("Take my hand now, Stay close to me")
        th = threading.Thread(target=self.shai_IP_start, )  # 启动子类
        th.start()
    def shai_IP_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\内存马\\URL-IP-main\\ && index.html'
        subprocess.Popen(command, shell=True)

    def seay(self):
        #self.label_9.setText("Take my hand now, Stay close to me")
        th = threading.Thread(target=self.seay_start, )  # 启动子类
        th.start()
    def seay_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\内存马\\Seay源代码审计系统\\ && Seay源代码审计系统.exe'
        subprocess.Popen(command, shell=True)

    def siqianzhangmi(self):
        #self.label_9.setText("Take my hand now, Stay close to me")
        th = threading.Thread(target=self.siqianzhangmi_start, )  # 启动子类
        th.start()
    def siqianzhangmi_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\内存马\\四千账密\\ && 四千多个厂商默认帐号、默认密码.mhtml'
        subprocess.Popen(command, shell=True)






    def fanruan(self):
        th = threading.Thread(target=self.fanruan_start, )
        th.start()
    def fanruan_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\帆软\\帆软1\\ && {} -jar FrChannelPlus.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def fanruanyecp(self):
        th = threading.Thread(target=self.fanruanyecp_start, )
        th.start()
    def fanruanyecp_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\帆软\\帆软2\\ && {} -jar FrChannel-v3.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def xxl_job(self):
        th = threading.Thread(target=self.xxl_job_start, )
        th.start()
    def xxl_job_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\XXL-JOB\\XXL-JOB\\ && {} -jar XXL-JOB.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def xxl_job_attack(self):
        th = threading.Thread(target=self.xxl_job_attack_start, )
        th.start()
    def xxl_job_attack_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\XXL-JOB\\xxl-job-attack\\ && {} -jar xxl-job-attack.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def Jeecg_Tools(self):
        th = threading.Thread(target=self.Jeecg_Tools_start, )
        th.start()
    def Jeecg_Tools_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\jeecg\\Jeecg_Tools\\ && {} -jar Jeecg_Tools-1.0-java8.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def jeecgExploitss(self):
        th = threading.Thread(target=self.jeecgExploitss_start, )
        th.start()
    def jeecgExploitss_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\jeecg\\jeecgExploitss\\ && {} -jar jeecgExploitss.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def jeecgBootAttack(self):
        th = threading.Thread(target=self.jeecgBootAttack_start, )
        th.start()
    def jeecgBootAttack_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\jeecg\\jeecgBootAttack\\ && {} -jar jeecgBootAttack-1.0-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def JenkinsExploit(self):
        th = threading.Thread(target=self.JenkinsExploit_start, )
        th.start()
    def JenkinsExploit_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\JenkinsExploit-GUI\\ && {} -jar JenkinsExploit-GUI-1.3-SNAPSHOT.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)






    def tomcat(self):  # 文档未改
        th = threading.Thread(target=self.tomcat_start, )  # 启动子类
        th.start()
    def tomcat_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\7_zonghe\\za_xiang\\Tomcat\\TomcatScanPro\\ && {} TomcatScanPro.py -u {}\"'.format(python3,self.No_filtering_three()))


    def tomcat2(self):
        th = threading.Thread(target=self.tomcat2_start, )
        th.start()
    def tomcat2_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\Tomcat\\TomcatVuln\\ && {} -jar TomcatVuln-1.0-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def UEditorGetShell(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\editor\\UEditorGetShell-master\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def fck(self):
        th = threading.Thread(target=self.fck_start, )  # 启动子类
        th.start()
    def fck_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\editor\\FCK\\ && FCK编辑器漏洞综合利用工具.exe'
        subprocess.Popen(command, shell=True)



    def Apache_Solr(self):
        th = threading.Thread(target=self.Apache_Solr_start, )
        th.start()
    def Apache_Solr_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\Apache\\Apache_Solr\\ && solr_scan.exe'
        subprocess.Popen(command, shell=True)


    def ActiveMQ_RCE(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\Apache\\ActiveMQ_RCE\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def Confluence(self):
        th = threading.Thread(target=self.Confluence_start, )
        th.start()
    def Confluence_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\Confluence利用\\ && {} -jar confluence_memshell-1.1-SNAPSHOT.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def fcs_tools(self):
        th = threading.Thread(target=self.fcs_tools_start, )
        th.start()
    def fcs_tools_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\other\\方程式工具包图形界面版\\ && {} -jar 方程式工具包图形界面版V0.42.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)


    def wpscan(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\other\\wpscan\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def IIS(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\other\\IIS\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def PRET(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\other\\打印机PRET\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def XSS_PDF(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\other\\xss_pdf\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def snmp(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\7_zonghe\\za_xiang\\other\\snmp默认团体字\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.snmp_start, )
        th.start()
    def snmp_start(self):
        command = 'cd tools\\4_redteam\\7_zonghe\\za_xiang\\other\\snmp默认团体字\\ && Snmputilg.exe'
        subprocess.Popen(command, shell=True)

    # ================================================================================================================
    #                            分页栏5
    # ================================================================================================================


    def No_filtering_four(self):#1.无过滤
        url =self.textEdit_3.toPlainText()#获取文本内容
        return url



    def Multiple(self):
        th = threading.Thread(target=self.Multiple_start, )  # 启动子类
        th.start()
    def Multiple_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\1号_Multiple\\ && {} -jar Multiple.Database.Utilization.Tools-2.1.1-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def Multiple_plus(self):
        th = threading.Thread(target=self.Multiple_plus_start, )  # 启动子类
        th.start()
    def Multiple_plus_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\2号_MDUT修改版\\ && {} -jar Multiple.Database.Utilization.Tools-2.1.1-Extend-1.2.0-T00ls-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def Sylas(self):  # 文档未改
        th = threading.Thread(target=self.Sylas_start, )  # 启动子类
        th.start()
    def Sylas_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\5号_Sylas\\ && Sylas-T.exe'
        subprocess.Popen(command, shell=True)

    def mssql_rce(self):
        th = threading.Thread(target=self.mssql_rce_start, )  # 启动子类
        th.start()
    def mssql_rce_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\3号_mssql命令执行\\ && 121.exe'
        subprocess.Popen(command, shell=True)


    def oracle_rce(self):
        th = threading.Thread(target=self.oracle_rce_start, )  # 启动子类
        th.start()
    def oracle_rce_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\2号_只针对oracle\\ && {} -jar oracleShell.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def postgre_rce(self):
        th = threading.Thread(target=self.postgre_rce_start, )  # 启动子类
        th.start()
    def postgre_rce_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\4号_针对postgresql\\ && {} -jar postgreUtil-1.0-SNAPSHOT-jar-with-dependencies.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def redis(self):
        path = tools_path+"\\tools\\4_redteam\\8_后渗透\\1_database\\redis-cli.exe"
        target = self.No_filtering_four()
        if os.path.exists(path):
            # 将要执行的完整命令（程序+参数）构建成一个列表
            scan_command = [path, '-h',target]
            final_command = ['cmd', '/K'] + scan_command
            tool_directory = os.path.dirname(path)
            subprocess.Popen(final_command, creationflags=0x10, cwd=tool_directory)
        else:
            program_dir = os.path.dirname(path)
            if os.path.exists(program_dir):
                os.startfile(program_dir)
            elif 'tools_path' in locals() and os.path.exists(tools_path):
                os.startfile(tools_path)
    #     th = threading.Thread(target=self.redis_start(), )  # 启动子类
    #     th.start()
    # def redis_start(self):
    #     os.system('start ''cmd \"/K cd tools\\4_redteam\\8_后渗透\\1_database\\ && redis-cli.exe -h {}\"'.format(self.No_filtering_four()))

    def redis_desptop(self):
        th = threading.Thread(target=self.redis_desptop_start, )  # 启动子类
        th.start()
    def redis_desptop_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\1_database\\RedisDesktopManager\\ && RedisDesktop.exe'
        subprocess.Popen(command, shell=True)

    def redis_plus(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\1_database\\RedisEXP\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动








    def bingxie(self):
        th = threading.Thread(target=self.bingxie_start, )  # 启动子类
        th.start()
    def bingxie_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\冰蝎\\ && {} -jar Behinder.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def gesila(self):
        th = threading.Thread(target=self.gesila_start, )  # 启动子类
        th.start()
    def gesila_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\Godzilla\\ && {} -jar godzilla.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def gesila_erkai(self):
        th = threading.Thread(target=self.gesila_erkai_start, )  # 启动子类
        th.start()
    def gesila_erkai_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\哥斯拉二开\\ && {} -jar Godzilla_null.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)


    def gesila_plus(self):
        th = threading.Thread(target=self.gesila_plus_start, )  # 启动子类
        th.start()
    def gesila_plus_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\Godzilla-plus\\ && {} -jar Godzilla_ekp1.1.jar'.format(
            java8_path)
        subprocess.Popen(command, shell=True)

    def tianxie(self):
        th = threading.Thread(target=self.tianxie_start, )  # 启动子类
        th.start()
    def tianxie_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\天蝎\\ && {} -jar 天蝎权限管理工具.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def antsword(self):
        th = threading.Thread(target=self.antsword_start, )  # 启动子类
        th.start()
    def antsword_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\AntSword\\AntSword-Loader-v4.0.3-win32-x64\\ && AntSword.exe'
        subprocess.Popen(command, shell=True)

    def caidao(self):
        th = threading.Thread(target=self.caidao_start, )  # 启动子类
        th.start()
    def caidao_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\caidao-20160622\\ && caidao.exe'
        subprocess.Popen(command, shell=True)

    def webshell(self):
        th = threading.Thread(target=self.webshell_start, )  # 启动子类
        th.start()
    def webshell_start(self):
        command = '%SystemRoot%/explorer.exe tools\\4_redteam\\8_后渗透\\2_webshell\\1_马子大全\\'
        subprocess.Popen(command, shell=True)

    def onlinechasha(self):
        th = threading.Thread(target=self.onlinechasha_start, )  # 启动子类
        th.start()
    def onlinechasha_start(self):
        command = 'explorer https://forum.ywhack.com/bountytips.php?process'
        subprocess.Popen(command, shell=True)

    def chasha(self):
        th = threading.Thread(target=self.chasha_start, )  # 启动子类
        th.start()
    def chasha_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\2_webshell\\Anti-Virus\\ && 杀软测试.html'
        subprocess.Popen(command, shell=True)






    def mianshawebshell(self):
        th = threading.Thread(target=self.mianshawebshell_start, )  # 启动子类
        th.start()
    def mianshawebshell_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\1号免杀_全部\\ && {} -jar Webshell_Generate-1.2.4.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def xgnitai(self):
        th = threading.Thread(target=self.xgnitai_start, )  # 启动子类
        th.start()
    def xgnitai_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\4号_小刚拟态\\ && {} -jar XG_NTAI.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def webshellbp(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\3_miansha\\5号_webshell_bypass\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.webshellbp_start, )  # 启动子类
        th.start()
    def webshellbp_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\5号_webshell_bypass\\ && webshell.exe'
        subprocess.Popen(command, shell=True)


    def bingxie_miansha(self):
        th = threading.Thread(target=self.bingxie_miansha_start, )  # 启动子类
        th.start()
    def bingxie_miansha_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\8_后渗透\\3_miansha\\2号_冰蝎\\ && ByPassBehinder.exe\"')



    def gesila_miansha(self):
        th = threading.Thread(target=self.gesila_miansha_start, )  # 启动子类
        th.start()
    def gesila_miansha_start(self):
        os.system('start ''cmd \"/K cd tools\\4_redteam\\8_后渗透\\3_miansha\\3号_哥斯拉\\ && ByPassGodzilla.exe\"')



    def Sign_Sacker(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\3_miansha\\Sign-Sacker\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.Sign_Sacker_start, )  # 启动子类
        th.start()
    def Sign_Sacker_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\Sign-Sacker\\ && Sign-Sacker.exe'
        subprocess.Popen(command, shell=True)


    def SharpThief(self):
        th = threading.Thread(target=self.SharpThief_start, )  # 启动子类
        th.start()
    def SharpThief_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\SharpThief\\ && SharpThief.exe'
        subprocess.Popen(command, shell=True)
        
    def RingQ(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\3_miansha\\RingQ\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def NimShellCodeLoader(self):
        th = threading.Thread(target=self.NimShellCodeLoader_start, )  # 启动子类
        th.start()
    def NimShellCodeLoader_start(self):
        command = 'cd tools\\4_redteam\\8_后渗透\\3_miansha\\NimShellCodeLoader\\ && codeLoader.exe'
        subprocess.Popen(command, shell=True)




    def cs45(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\coablt_strike_4.5_jx\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def cs48(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\cs4.8\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def cs49(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\cs4.9\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def vshell(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\vshell\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def XiebroC2(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\XiebroC2\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    def sliver(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\sliver\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def c2chajian(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\4_redteam\\8_后渗透\\4_C2\\000000___CS插件____000000\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    # ================================================================================================================
    #                            分页栏6
    # ================================================================================================================


    def wangduantc(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\1_探测\\探测\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def duowangka(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\1_探测\\多网卡\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def chuantou(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\2_穿透\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def zhuamima(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\4_抓密码\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def hengxiang(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\5_横向、域控\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def tiquan(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\3_提权\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def vcenter(self):
        th = threading.Thread(target=self.vcenter_start, )  # 启动子类
        th.start()
    def vcenter_start(self):
        command = 'cd tools\\5_内网渗透工具\\6_其他工具\\Vcenter\\ && VcenterKit.exe'
        subprocess.Popen(command, shell=True)

    def exchange(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\6_其他工具\\Exchange邮服'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
    def cdk(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\5_内网渗透工具\\6_其他工具\\CDK\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动

    # ================================================================================================================
    #                            分页栏7
    # ================================================================================================================

    def weibu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('微步社区网址： https://x.threatbook.com')
        th = threading.Thread(target=self.weibu_start, )  # 启动子类
        th.start()
    def weibu_start(self):
        command = 'explorer https://x.threatbook.com'
        subprocess.Popen(command, shell=True)


    def weixie360(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('360威胁情报： https://ti.360.net/#/homepage')
        th = threading.Thread(target=self.weixie360_start, )  # 启动子类
        th.start()
    def weixie360_start(self):
        command = 'explorer https://ti.360.net/#/homepage'
        subprocess.Popen(command, shell=True)

    def qianxin(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('奇安信威胁情报： https://ti.qianxin.com/')
        th = threading.Thread(target=self.qianxin_start, )  # 启动子类
        th.start()
    def qianxin_start(self):
        command = 'explorer https://ti.qianxin.com/'
        subprocess.Popen(command, shell=True)


    def shaxiangwb(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('微步沙箱： https://s.threatbook.com')
        th = threading.Thread(target=self.shaxiangwb_start, )  # 启动子类
        th.start()
    def shaxiangwb_start(self):
        command = 'explorer https://s.threatbook.com'
        subprocess.Popen(command, shell=True)

    def VT(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('VT沙箱： https://www.virustotal.com/gui/home/upload')
        th = threading.Thread(target=self.VT_start, )  # 启动子类
        th.start()
    def VT_start(self):
        command = 'explorer https://www.virustotal.com/gui/home/upload'
        subprocess.Popen(command, shell=True)


    def shaxiang360(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('360沙箱： https://ata.360.net/')
        th = threading.Thread(target=self.shaxiang360_start, )  # 启动子类
        th.start()
    def shaxiang360_start(self):
        command = 'explorer https://ata.360.net/'
        subprocess.Popen(command, shell=True)


    def suyuantoolbox(self):
        th = threading.Thread(target=self.suyuantoolbox_start, )  # 启动子类
        th.start()
    def suyuantoolbox_start(self):
        command = 'cd tools\\6_溯源\\1_蓝队工具箱\\ && {} -jar BlueTeamToolsV2.18.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)

    def d_eyes(self):
        th = threading.Thread(target=self.d_eyes_start, )  # 启动子类
        th.start()
    def d_eyes_start(self):
        os.system('start ''cmd \"/K cd tools\\6_溯源\\2_D-Eyes_1.1.0\\ && d-eyes_windows_amd64.exe -h\"')


    def QDoctor(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\3_QDoctor\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.QDoctor_start, )  # 启动子类
        th.start()
    def QDoctor_start(self):
        command = 'cd tools\\6_溯源\\3_QDoctor\\ && QDoctor.exe'
        subprocess.Popen(command, shell=True)


    def Hawkeye(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\4_Hawkeye\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.Hawkeye_start, )  # 启动子类
        th.start()
    def Hawkeye_start(self):
        command = 'cd tools\\6_溯源\\4_Hawkeye\\ && HawkEye.exe'
        subprocess.Popen(command, shell=True)


    def whoamifuck(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\5_whoamifuck\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def LinuxCheck(self):  # 文档未改
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\6_LinuxCheck\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def shell_analyzer(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\7_shell-analyzer\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动
        th = threading.Thread(target=self.shell_analyzer_start, )  # 启动子类
        th.start()
    def shell_analyzer_start(self):
        command = 'cd tools\\6_溯源\\7_shell-analyzer\\ && {} -jar gui-0.1.jar'.format(java8_path)
        subprocess.Popen(command, shell=True)



    def neicunmacs(self):
        command = '%SystemRoot%/explorer.exe {} \\tools\\6_溯源\\10_内存马2\\'.format(tools_path)
        subprocess.Popen(command, shell=True)  # 启动


    def hema(self):  # 文档未改
        th = threading.Thread(target=self.hema_start, )  # 启动子类
        th.start()
    def hema_start(self):
        command = 'cd tools\\6_溯源\\8_hema\\ && qhm.exe'
        subprocess.Popen(command, shell=True)


    def Ddun(self):  # 文档未改
        th = threading.Thread(target=self.Ddun_start, )  # 启动子类
        th.start()
    def Ddun_start(self):
        command = 'cd tools\\6_溯源\\9_Ddun\\ && D_Safe_Manage.exe'
        subprocess.Popen(command, shell=True)


    def lesuojiemi(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('勒索解密项目： https://github.com/jiansiting/Decryption-Tools')
        th = threading.Thread(target=self.lesuojiemi_start, )  # 启动子类
        th.start()
    def lesuojiemi_start(self):
        command = 'explorer https://github.com/jiansiting/Decryption-Tools'
        subprocess.Popen(command, shell=True)



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
        self.textEdit_4.setPlainText('查看登录信息：last')

    def Linux_duankou(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('查看端口信息：netstat -tnlp')

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



    def Linux_fanghuoqiang(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.append('永久关闭防火墙：sudo ufw disable')
        self.textEdit_4.append('查看防火墙状态：sudo ufw status')

    def Linux_cpu_number(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看CPU个数：cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l')

    def Linux_cpu_xiancheng(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看CPU逻辑线程数：nproc')


    def Linux_cipanzhanyong(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看磁盘占用情况：df -hl')


    def Linux_neicun(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看内存：grep MemTotal /proc/meminfo')


    def Linux_dhcp(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('')
        self.textEdit_4.setPlainText('查看是否是dhcp： nmcli device show')






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


    def duankou(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('全部端口命令为：netstat -ano')
        self.textEdit_4.append('更为详细的检查：netstat -ano | findstr "8080"')

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


    def xitongfuwu(self):
        self.textEdit_4.setFontPointSize(12)
        self.textEdit_4.setPlainText('命令为：win+r services.msc')
        th = threading.Thread(target=self.xitongfuwu_start, )  # 启动子类
        th.start()
    def xitongfuwu_start(self):
        command = 'services.msc'
        subprocess.Popen(command, shell=True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    w = QMainWindow()
    ui = button()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec())  # 注意 PyQt6 用 exec()
