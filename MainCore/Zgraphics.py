import tkinter as tk

class ZN_GraphicsContext():
    def __init__(self):
        self.canvas = 0
    def Create(self,bindto):
        self.canvas = bindto
    def Drawtext(self,x,y,Text,color):
        c = self.canvas
        c.create_text(x, y, text=Text, fill=color,font=('Arial 15'))
    def DrawRect(xpo,ypo,xpt,ypt,color):
        self.canvas.create_rectangle(xpo, ypo, xpt, ypt, fill=color)
