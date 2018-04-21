# -*- coding: utf8 -*-
import wx
from uniq_list_gui_events import uniq_list_gui_events

if __name__ == '__main__':
    app = wx.App(False)
    frame = uniq_list_gui_events(None)
    frame.Show(True)    
    app.MainLoop()