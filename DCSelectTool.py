#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2017年3月25日
@author: wuxiaobing
Mail:2683904575@qq.com
history: 
V1.0 采用wxpython类库实现DC选择对应要求出货的设备组合型号。（2017-03-25）。
'''
import wx
class RadioBoxFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, u'DCSelectTool V1.0 (GAG@wuxb)',size=(480, 320),style=wx.DEFAULT_FRAME_STYLE ^(wx.MAXIMIZE_BOX | wx.RESIZE_BORDER))  
        panel = wx.Panel(self, -1)
        self.Centre()
        sampleList = [u'硬件桥接', u'转发器']
        sampleList1 = [u'请选择',u'串口', u'并口', u'网口', u'U口']
        sampleList2 = [u'请选择',u'无线网',u'有线网']
        sampleList3 = [u'请选择',u'WIFI', u'联通3G', u'联通4G', u'移动4G']
        
        self.radio1=wx.RadioBox(panel, -1, u"设备类型", (30, 30), wx.DefaultSize, 
                        sampleList, 1, wx.RA_SPECIFY_COLS)
        self.radio2=wx.RadioBox(panel, -1, u"端口类型", (150, 30), wx.DefaultSize,  
                        sampleList1, 1, wx.RA_SPECIFY_COLS)  
        self.radio3=wx.RadioBox(panel, -1, u"网络类型", (270, 30), wx.DefaultSize,  
                        sampleList2, 1,wx.RA_SPECIFY_COLS)
        self.radio4=wx.RadioBox(panel, -1, u"连网方式", (390, 30), wx.DefaultSize,  
                        sampleList3, 1,wx.RA_SPECIFY_COLS)
        self.button=wx.Button(panel, -1, u"设备型号", pos=(180, 200),size=(100,60))
        self.button.SetForegroundColour("blue")
        self.button.Bind(wx.EVT_BUTTON, self.OnOpen)
        
                
#绑定事件          
        self.Bind(wx.EVT_RADIOBOX, self.OnRadio, self.radio1)
        self.Bind(wx.EVT_RADIOBOX, self.OnRadio3, self.radio3)
          
#事件处理器 &返回选中的Radio     
    def OnRadio(self, event):
        if self.radio1.GetSelection()== 1:
           self.radio2.Disable()|self.radio3.Disable()|self.radio4.Disable()
           self.radio2.SetSelection(0)
           self.radio3.SetSelection(0)
           self.radio4.SetSelection(0)
        else:
           self.radio2.Enable()|self.radio3.Enable()|self.radio4.Enable()
    
    def OnRadio3(self, event):
        if self.radio3.GetSelection()== 2:
           self.radio4.Disable()
           self.radio4.SetSelection(0)   
        else:
           self.radio4.Enable()  
           
#按钮调用方法
    def OnOpen(self,event):
       device_type = {u'硬件桥接': 'DC', u'转发器': 'DC531'}
       port_type = {u'请选择': '', u'串口': '1', u'并口': '2', u'网口': '3', u'U口': '4'}
       connect_type = {u'请选择': '',u'有线网': '01', u'无线网':'1'}
       service_provider_type = {u'请选择': '',u'WIFI': '5', u'联通3G': '3',  u'联通4G': '7', u'移动4G': '6'}
       type_list = [device_type, port_type,service_provider_type,connect_type]
       radio_list = [self.radio1, self.radio2,self.radio4,self.radio3]
       radio_choice = [type_list[i][radio_list[i].GetStringSelection()] for i in range(len(radio_list))]
       str = ''.join(radio_choice)
       wx.MessageBox(u">>>>>>>>>>>>"+"  "+str+"  "+"<<<<<<<<<<<<<", u"设备申请型号", wx.ICON_QUESTION)
 
if __name__ == '__main__':  
    app = wx.App()
    RadioBoxFrame().Show()
    app.MainLoop()