#!/usr/bin/env python3

import wx

class MainWindow(wx.Frame):
    def __init__(self):
        super(MainWindow, self).__init__(None, title='Test App')
        
        
app = wx.App()
app.SetAppName('Test App')
window = MainWindow()
window.Show()
app.MainLoop()
