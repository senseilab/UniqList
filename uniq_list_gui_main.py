# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UniqueListTool_v1.0.0", pos = wx.DefaultPosition, size = wx.Size( 672,146 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnExcu = wx.Button( self.m_panel1, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnExcu, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnExit = wx.Button( self.m_panel1, wx.ID_ANY, u"終了", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnExit, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtFilePath = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		bSizer3.Add( self.txtFilePath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnGetFilePath = wx.Button( self.m_panel2, wx.ID_ANY, u"ファイル選択", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnGetFilePath, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnExcu.Bind( wx.EVT_BUTTON, self.btnExcuClick )
		self.btnExit.Bind( wx.EVT_BUTTON, self.btnExitClick )
		self.btnGetFilePath.Bind( wx.EVT_BUTTON, self.btnGetFilePathClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnExcuClick( self, event ):
		event.Skip()
	
	def btnExitClick( self, event ):
		event.Skip()
	
	def btnGetFilePathClick( self, event ):
		event.Skip()
	

