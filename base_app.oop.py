import tkinter
import tkinter.font
class Application(tkinter.Frame):
    def  __init__(self,master):
            tkinter.Frame. __init__(self, master)
            self.config(width=1000)
            self.config(height=200)
            self.config(bg="#00FFFF")
            self. pack()
            self.CreateWidgets()
    def CreateWidgets(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="Hello World\n I am BJ\n Nice to meet you")
        self.label1.config(bg="yellow")
        self.label1.config(fg="violet")
        self.myFont=tkinter.font.Font(family="Helvitica", size=18 ,weight=tkinter.font.BOLD,slant=tkinter.font.ITALIC,underline=True,overstrike=True)
        self.label1.config(font=self.myFont)
        self.label1.pack()
        
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()

        
        
        
