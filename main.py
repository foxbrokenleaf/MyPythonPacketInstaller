# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import time

###########################################################################
## Class MyWindowsApp
###########################################################################

class MyWindowsApp ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"python第三方库一键安装小程序", pos = wx.DefaultPosition, size = wx.Size( 500,330 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		GlobarLayout = wx.BoxSizer( wx.VERTICAL )
		
		StaticText = wx.GridSizer( 0, 2, 0, 0 )
		
		StaticText_Right = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"网络爬虫", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		StaticText_Right.Add( self.m_staticText2, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"实用功能", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		StaticText_Right.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		StaticText.Add( StaticText_Right, 1, wx.EXPAND, 5 )
		
		StaticText_Left = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"游戏开发", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		StaticText_Left.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"GUI开发", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		StaticText_Left.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		StaticText.Add( StaticText_Left, 1, wx.EXPAND, 5 )
		
		
		GlobarLayout.Add( StaticText, 1, wx.EXPAND, 5 )
		
		CheckBox = wx.GridSizer( 0, 2, 0, 0 )
		
		CheckBox_Right = wx.GridSizer( 0, 2, 0, 0 )
		
		Network = wx.BoxSizer( wx.VERTICAL )
		
		self._1 = wx.CheckBox( self, wx.ID_ANY, u"bs4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._1.SetValue(False) 
		self._1.SetToolTip( u"解析html" )
		
		Network.Add( self._1, 0, wx.ALL, 5 )
		
		self._2 = wx.CheckBox( self, wx.ID_ANY, u"lxml", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._2.SetToolTip( u"lxml解释器" )
		
		Network.Add( self._2, 0, wx.ALL, 5 )
		
		self._3 = wx.CheckBox( self, wx.ID_ANY, u"pyhttpx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._3.SetToolTip( u"https请求？" )
		
		Network.Add( self._3, 0, wx.ALL, 5 )
		
		self._4 = wx.CheckBox( self, wx.ID_ANY, u"requests", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._4.SetToolTip( u"请求库" )
		
		Network.Add( self._4, 0, wx.ALL, 5 )
		
		self._5 = wx.CheckBox( self, wx.ID_ANY, u"selenium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._5.SetToolTip( u"模拟浏览器" )
		
		Network.Add( self._5, 0, wx.ALL, 5 )
		
		self._6 = wx.CheckBox( self, wx.ID_ANY, u"urllib3==1.23", wx.DefaultPosition, wx.DefaultSize, 0 )
		Network.Add( self._6, 0, wx.ALL, 5 )
		
		
		CheckBox_Right.Add( Network, 1, wx.EXPAND, 5 )
		
		GoodForJob = wx.BoxSizer( wx.VERTICAL )
		
		self._7 = wx.CheckBox( self, wx.ID_ANY, u"keyboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._7.SetToolTip( u"模拟键盘" )
		
		GoodForJob.Add( self._7, 0, wx.ALL, 5 )
		
		self._8 = wx.CheckBox( self, wx.ID_ANY, u"numpy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._8.SetToolTip( u"数学运算" )
		
		GoodForJob.Add( self._8, 0, wx.ALL, 5 )
		
		self._9 = wx.CheckBox( self, wx.ID_ANY, u"pillow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._9.SetToolTip( u"图像处理" )
		
		GoodForJob.Add( self._9, 0, wx.ALL, 5 )
		
		self._10 = wx.CheckBox( self, wx.ID_ANY, u"pyinstaller", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._10.SetToolTip( u"程序打包" )
		
		GoodForJob.Add( self._10, 0, wx.ALL, 5 )
		
		self._11 = wx.CheckBox( self, wx.ID_ANY, u"click", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._11.SetToolTip( u"模拟鼠标" )
		
		GoodForJob.Add( self._11, 0, wx.ALL, 5 )
		
		self._12 = wx.CheckBox( self, wx.ID_ANY, u"zipp", wx.DefaultPosition, wx.DefaultSize, 0 )
		GoodForJob.Add( self._12, 0, wx.ALL, 5 )
		
		
		CheckBox_Right.Add( GoodForJob, 1, wx.EXPAND, 5 )
		
		
		CheckBox.Add( CheckBox_Right, 1, wx.EXPAND, 5 )
		
		CheckBox_Left = wx.GridSizer( 0, 2, 0, 0 )
		
		GameDevelop = wx.BoxSizer( wx.VERTICAL )
		
		self._13 = wx.CheckBox( self, wx.ID_ANY, u"pygame", wx.DefaultPosition, wx.DefaultSize, 0 )
		GameDevelop.Add( self._13, 0, wx.ALL, 5 )
		
		
		CheckBox_Left.Add( GameDevelop, 1, wx.EXPAND, 5 )
		
		GuiDevelop = wx.BoxSizer( wx.VERTICAL )
		
		self._14 = wx.CheckBox( self, wx.ID_ANY, u"wxPython", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._14.SetToolTip( u"wxWiget库" )
		
		GuiDevelop.Add( self._14, 0, wx.ALL, 5 )
		
		
		CheckBox_Left.Add( GuiDevelop, 1, wx.EXPAND, 5 )
		
		
		CheckBox.Add( CheckBox_Left, 1, wx.EXPAND, 5 )
		
		
		GlobarLayout.Add( CheckBox, 1, wx.EXPAND, 5 )
		
		self.Install = wx.Button( self, wx.ID_ANY, u"一键安装", wx.DefaultPosition, wx.DefaultSize, 0 )
		GlobarLayout.Add( self.Install, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.logs = wx.TextCtrl( self, wx.ID_ANY, u'', wx.DefaultPosition, wx.DefaultSize, 0 )
		GlobarLayout.Add( self.logs, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.gauge_total = wx.Gauge( self, wx.ID_ANY, 14, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_total.SetValue( 0 ) 
		GlobarLayout.Add( self.gauge_total, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( GlobarLayout )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Install.Bind( wx.EVT_BUTTON, self.IS_CLICK )
	
	def __del__( self ):
		pass
	
	# str(eval("self._" + str(1) + ".GetValue()"))
	# Virtual event handlers, overide them in your derived class
	def IS_CLICK( self, event ):
            True_For_Check_Box = '' #保存当前遍历到的包名专用变量
            output_logs = ''    #输出日志专用变量
            Get_time = str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + str(time.localtime().tm_hour) + str(time.localtime().tm_min) + str(time.localtime().tm_sec)
            for i in os.listdir():
                if i == "Logs":
                    break
                else:
                    os.mkdir("Logs")
            Logs_file = open("./Logs/" + Get_time,'w',encoding="UTF-8")  #输出日志至文件专用变量
            Get_time = '[' + str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + "] -> "
            for i in range(1,15):
                if eval("self._" + i.__str__() + ".GetValue()") == True:
                    True_For_Check_Box = eval("self._" + i.__str__() + ".GetLabel()")
                    Get_time = '[' + str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + "] -> "
                    output_logs = Get_time + u"正在安装" + True_For_Check_Box
                    Logs_file.writelines(output_logs + '\n')
                    self.logs.SetValue(output_logs)
                    Get_time = '[' + str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + "] -> "
                    if os.system("pip install " + True_For_Check_Box) == 0:
                        output_logs = u'' + Get_time + True_For_Check_Box + " 安装成功"
                        Logs_file.writelines(output_logs + '\n')
                        self.logs.SetValue(output_logs)
                    else:
                        output_logs = u'' + Get_time + True_For_Check_Box + " 安装失败"
                        Logs_file.writelines(output_logs + '\n')
                        self.logs.SetValue(output_logs)
                self.gauge_total.Value += 1
            Get_time = '[' + str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + "] -> "
            output_logs = Get_time + u"安装完成"
            Logs_file.writelines(output_logs + '\n')
            self.logs.SetValue(output_logs)

app = wx.App()
Frame = MyWindowsApp(None)
Frame.Show()
app.MainLoop()