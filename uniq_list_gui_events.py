"""Subclass of frmMain, which is generated by wxFormBuilder."""

import wx
import uniq_list_gui_main
import datetime
import csv
import os.path

# Implementing frmMain
class uniq_list_gui_events( uniq_list_gui_main.frmMain ):
    def __init__( self, parent ):
        uniq_list_gui_main.frmMain.__init__( self, parent )

    # Handlers for frmMain events.
    def btnExcuClick( self, event ):
        filePath = self.txtFilePath.Value
        
        if filePath == "":
            msgDialog = wx.MessageDialog(self,"ファイルを選択してください","情報",style=wx.OK)
            msgDialog.ShowModal()
            
        else:
            targetFolder = os.path.dirname(filePath)
            targetFile = open(filePath,'r')
            reader = csv.reader(targetFile)
            li_uniq = []
            for x in reader:
                if x not in li_uniq:
                    li_uniq.append(x)
            now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            fileName = targetFolder + '\\UniqList_' + now  + '.txt'
            newFile = open(fileName,'w')
            writer = csv.writer(newFile,lineterminator='\n')
            writer.writerows(li_uniq)
            newFile.close()
            targetFile.close()
            
            msgDialog = wx.MessageDialog(self,"重複削除が完了しました","情報",style=wx.OK)
            msgDialog.ShowModal()
        pass
    
    def btnExitClick( self, event ):
        self.Close()
        pass

    def btnGetFilePathClick( self, event ):
        getFileDialog = wx.FileDialog(None,"test",wildcard="*.txt*;*.csv*",style=wx.FD_OPEN)
        getFileDialog.ShowModal()
        self.txtFilePath.SetValue(getFileDialog.GetPath())
        pass