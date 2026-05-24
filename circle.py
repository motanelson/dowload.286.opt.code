import tkinter as tk





class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("oval")
        self.root.geometry("480x480")
        self.root.configure(background="black")
        self.colors=["white","black"]
        self.canvas=tk.Canvas(background="black",width=480,height=480)
        self.canvas.pack(padx=0,pady=0)
        canv=self.canvas
        for a in range(10):
            aa=a*20
            aaa=480-aa
            b=a & 1
            canv.create_oval(aa,aa,aaa,aaa,fill=self.colors[b])





root=tk.Tk()
apps=myapps(root)
root.mainloop()