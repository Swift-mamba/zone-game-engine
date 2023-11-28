import tkinter as tk

class ZN_window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zone game engine")
        self.root.geometry("800x450")
        self.canvas = tk.Canvas(self.root, width=800, height=450)
        self.canvas.pack(fill = tk.BOTH)
        self.root.resizable(0,0)
        self.canvas.create_rectangle(0, 0, 800, 450, fill='#00003c')
    def Update(self):
        self.root.update()
    def Mainloop(self):
        self.root.mainloop()
    def Caption(self,title):
        self.root.title(title)
    def Setmode(self,x,y):
        REALX = str(x)
        REALY = str(y)
        STRING = REALX+"x"+REALY
        self.root.geometry(STRING)
    def Getcanvas(self):
        TORETURN = self.canvas
        return(TORETURN)
    def Fullscreen(self):
        self.root.attributes('-fullscreen',True)
    def Window(self):
        self.root.attributes('-fullscreen',False)
    def Clear(self):
        self.canvas.create_rectangle(0, 0, 800, 450, fill='#00003c')
