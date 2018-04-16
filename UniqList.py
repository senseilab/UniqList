# -*- coding: utf8 -*-
import tkinter as tk
import tkinter.filedialog as tkdialog
import datetime
import csv

root = tk.Tk()
filePath =tkdialog.askopenfilename(filetypes=[('data files','*.csv;*.txt')])
root.withdraw()

targetFile = open(filePath,'r')

reader = csv.reader(targetFile)

li_uniq = []

for x in reader:
    if x not in li_uniq:
        li_uniq.append(x)
        
now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

fileName = 'UniqList_' + now  + '.txt'

newFile = open(fileName,'w')
writer = csv.writer(newFile,lineterminator='\n')
writer.writerows(li_uniq)

newFile.close()
    
targetFile.close()