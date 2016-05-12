#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx

class ColorTextForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Colored text")

        panel = wx.Panel(self, wx.ID_ANY)
        self.log = wx.TextCtrl(panel, wx.ID_ANY, size=(100,100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_RICH)

        self.log.SetDefaultStyle(wx.TextAttr(wx.GREEN, wx.BLACK))
        #self.log.SetBackgroundColour(wx.BLACK)
        self.bgColor = wx.WHITE
        self.log.SetBackgroundColour(self.bgColor)

        btnRed = wx.Button(panel, wx.ID_ANY, 'Red')
        btnGreen = wx.Button(panel, wx.ID_ANY, 'Green')
        self.cbBG  = wx.CheckBox(panel, label='White')
        self.Bind(wx.EVT_BUTTON, self.onButtonRed, btnRed)
        self.Bind(wx.EVT_BUTTON, self.onButtonGreen, btnGreen)
        self.Bind(wx.EVT_CHECKBOX, self.onCheckChangeBG, self.cbBG)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.log, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btnRed, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btnGreen, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.cbBG, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    def onButtonGreen(self, event):
        self.log.SetDefaultStyle(wx.TextAttr(wx.GREEN,  self.bgColor))
        self.log.AppendText("Geen\n")

    def onButtonRed(self, event):
        self.log.SetDefaultStyle(wx.TextAttr(wx.RED,self.bgColor))
        self.log.AppendText("Red\n")

    def onCheckChangeBG(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        if isChecked:
            self.bgColor = wx.BLACK
            self.cbBG.SetLabel('Black')
        else:
            self.bgColor = wx.WHITE
            self.cbBG.SetLabel('White')

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ColorTextForm().Show()
    app.MainLoop()
