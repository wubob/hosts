#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年1月12日
@author: wuxiaobing
Mail:xbwu@dataman-inc.com;2683904575@qq.com
history: 
V1.0 采用wxpython类库实现Host配置文件追打。（2018-01-12）。
'''
import wx
import time

class RadioBoxFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, u'HostsConfig V1.0 (xbwu@DataMan)',size=(800, 400),style=wx.DEFAULT_FRAME_STYLE ^(wx.MAXIMIZE_BOX | wx.RESIZE_BORDER))  
        panel = wx.Panel(self, -1)
        self.Centre()
        self.button=wx.Button(panel, -1, u"写入hosts", pos=(290, 270),size=(100,50))
        self.button.SetForegroundColour("blue")
        self.Bind(wx.EVT_BUTTON,self.OnSave,self.button)
        
        self.button1=wx.Button(panel, -1, u"清除屏幕", pos=(490, 270),size=(100,50))
        self.button1.SetForegroundColour("red")
        self.Bind(wx.EVT_BUTTON,self.OnClear,self.button1)  
        self.icon = wx.Icon('D:\log\www.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  
        
        Label = wx.StaticText(panel, -1, "请输入hosts文件:",(210,30))  
        self.richText=wx.TextCtrl(panel,-1,
                            "",
                             (210,50),
                             size=(500,200),
                             style=wx.TE_MULTILINE|wx.TE_RICH2)
        self.richText.SetInsertionPoint(0)
        ee=self.richText.GetValue()
        
        self.rb1 = wx.RadioButton(panel,11, label = "Windows",pos = (80,80), style = wx.RB_GROUP) 
        self.rb2 = wx.RadioButton(panel,22, label = "Mac",pos = (80,110)) 
        self.rb3 = wx.RadioButton(panel,33, label = "linux",pos = (80,140))
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.hostsnew=""
        
    def OnRadiogroup(self, e): 
        rb = e.GetEventObject()
        if rb==self.rb1:
            self.hostsnew= 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        else:
            wx.MessageBox("功能开发中！")
            self.hostsnew= 'D:\\eeee'
            
    def OnSave(self, event):
        self.hostsnew= 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        f = open(self.hostsnew,'r')  
        origin = f.readlines()
        
        last = origin[-1]
        if "\n" not in last:
            f = open(self.hostsnew,'a')
            f.write("\n")
            f.close()
        savefile1=self.richText.GetValue()
        current = savefile1.split('\n')
        
        for line in current:
            if line+"\n" not in origin and len(line):
                origin.append(line)
                f = open(self.hostsnew,'a')
                f.write(line+"\n")
        f.close()
        wx.MessageBox("恭喜！hosts文件复制完成！") 
    
                  
    def OnClear(self, event):
        data=self.richText.Clear()       
        return data
    
if __name__ == '__main__':  
    app = wx.App()
    RadioBoxFrame().Show()
    app.MainLoop()