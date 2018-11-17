
from tkinter import *
from tkinter import messagebox

class Note:

        def showDialog(self):
                dialog=Toplevel(root)
                dialog.geometry("300x300")

        def __init__(self):
                self.root=Tk()
                self.root.title("WrapTex")
                self.root.geometry("700x500")

                mb=Menu(self.root)
                fmenu=Menu(mb,tearoff=0)
                fmenu.add_command(label="New File          Ctrl+N",command=self.newFile)
                fmenu.add_command(label="Open...            Ctrl+O",command=self.openFile)
                fmenu.add_command(label="Save                 Ctrl+S",command=self.save)
                fmenu.add_command(label="Save As",command=self.saveas)
                fmenu.add_separator()
                fmenu.add_command(label="Page Setup...",command=self.showDialog)
                fmenu.add_command(label="Print...              Ctrl+P",command=self.showDialog)
                fmenu.add_separator()
                fmenu.add_command(label="Exit",command=self.root.destroy)
                mb.add_cascade(label="File",menu=fmenu)

                mc=Menu(self.root)
                emenu=Menu(mc,tearoff=0)
                emenu.add_command(label="Undo        Ctrl+Z",command=self.showmsg)
                emenu.add_command(label="Redo        Ctrl+Shift+Z",command=self.showmsg)
                emenu.add_separator()
                emenu.add_command(label="Cut           Ctrl+X",command=self.showmsg)
                emenu.add_command(label="Copy        Ctrl+C",command=self.showmsg)
                emenu.add_command(label="Paste        Ctrl+V",command=self.showmsg)
                emenu.add_command(label="Delete",command=self.showmsg)
                emenu.add_separator()
                emenu.add_command(label="Find",command=self.showmsg)
                emenu.add_command(label="Find Next",command=self.showmsg)
                emenu.add_command(label="Replace",command=self.showmsg)
                emenu.add_command(label="Select All",command=self.showmsg)
                mb.add_cascade(label="Edit",menu=emenu)

                md=Menu(self.root)
                gmenu=Menu(md,tearoff=0)
                gmenu.add_command(label="Word Wrap",command=self.showmsg)
                gmenu.add_command(label="Font...",command=self.setfont)
                mb.add_cascade(label="Format",menu=gmenu)

                me=Menu(self.root)
                hmenu=Menu(me,tearoff=0)
                hmenu.add_command(label="Status Bar",command=self.showmsg)
                mb.add_cascade(label="View",menu=self.hmenu)

                mf=Menu(self.root)
                imenu=Menu(mf,tearoff=0)
                imenu.add_command(label="View Help",command=self.viewhelp)
                imenu.add_separator()
                imenu.add_command(label="About WrapTex",command=self.about)
                mb.add_cascade(label="Help",menu=imenu)

                self.text = Text(self.root)
                self.text.pack(fill=BOTH,expand=1)
                self.text.config(font=("Times New Roman",12))
                self.root.config(menu=mb)
        
                self.root.mainloop()

        def newFile(self):
                newfile =Note()

        def save(self):
                self.m=open(self.name,"r")
                s=self.text.get(0.0,'end')
                self.m.close()
                self.m=open(self.name,"w")
                self.m.write(s)
                self.m.close()
                
        def saveas(self):
                top=Tk()
                top.geometry("480x180")
                top.title('open')
                l1 = Label(top,text="Enter File Name :",font=("Times New Roman",12))
                l1.place(x="0",y="40",height="25",width="150")

                e1 = Entry(top,font=("cambria",12))
                e1.place(x="140",y="40",height="25",width="300")
                
                b1=Button(top,text="Save As",font=("Times New Roman",14),command=self.save)
                b1.place(x="180",y="100",height="30",width="80")

                b2=Button(top,text="Cancel",font=("Times New Roman",14),command=top.destroy)
                b2.place(x="270",y="100",height="30",width="80")

                top.mainloop()

        def openre(self):
                n=self.e1.get()
                self.name=str(n)
                self.f=open(self.name,"r")
                d=file.read(self.f)
                self.text.insert(0.0,str(d),'end')
                self.root.title(self.name+" - Notepad")
                self.top.destroy()
                self.root.mainloop()                

        def openFile(self):
                self.top=Tk()
                self.top.geometry("480x180")
                self.top.title('open')
                l1 = Label(self.top,text="Enter File Name :",font=("Times New Roman",12))
                l1.place(x="0",y="40",height="25",width="150")

                self.e1 = Entry(self.top,font=("cambria",12))
                self.e1.place(x="140",y="40",height="25",width="300")
                       
                b1=Button(self.top,text="Open",font=("Times New Roman",14),command=self.openre)
                b1.place(x="180",y="100",height="30",width="80")

                b2=Button(self.top,text="Cancel",font=("Times New Roman",14),command=self.top.destroy)
                b2.place(x="270",y="100",height="30",width="80")
                self.top.mainloop()
                
        def setfont(self):
                self.top=Tk()
                self.top.geometry("450x350")
                self.top.title('Font...')
                
                l1 = Label(self.top,text="Font:",font=("Arial",10))
                l1.place(x="0",y="10",height="15",width="50")

                self.e1 = Entry(self.top,font=("cambria",12))
                self.e1.place(x="9",y="30",height="20",width="150")            

                self.lb1=Listbox(self.top,height=30)
                self.lb1.insert(0,"Arial")
                self.lb1.insert(1,"Bell MT")
                self.lb1.insert(2,"Book Antiqua")
                self.lb1.insert(3,"Cambria")
                self.lb1.insert(4,"Candara")
                self.lb1.insert(5,"Castellar")
                self.lb1.insert(6,"Century Gothic")
                self.lb1.insert(7,"Chiller")
                self.lb1.insert(8,"Comic Sans MS")
                self.lb1.insert(9,"Consolas")
                self.lb1.insert(10,"Constantia")
                self.lb1.insert(11,"Courier New")
                self.lb1.insert(12,"Forte")
                self.lb1.insert(13,"Georgia")
                self.lb1.insert(14,"Lucida Bright")
                self.lb1.insert(15,"Lucida Console")
                self.lb1.insert(16,"Lucida Sans Typewriter")
                self.lb1.insert(17,"Microsoft Sans Serif")
                self.lb1.insert(18,"MS Serif")
                self.lb1.insert(19,"Papyrus")
                self.lb1.insert(20,"Poor Richard")
                self.lb1.insert(21,"Rockwell")
                self.lb1.insert(22,"Script MT")
                self.lb1.insert(23,"Times New Roman")
                self.lb1.insert(24,"Verdana")
                self.lb1.place(x="9",y="55",height="100",width="150")
                scrollbar = Scrollbar(self.lb1, orient="vertical")
                scrollbar.config(command=self.lb1.yview)
                scrollbar.pack(side="right", fill="y")

                self.lb1.bind('<<ListboxSelect>>',self.CurSelet)
                
                l2 = Label(self.top,text="Font Style:",font=("Arial",10))
                l2.place(x="180",y="10",height="15",width="65")

                self.e2 = Entry(self.top,font=("cambria",12))
                self.e2.place(x="180",y="30",height="20",width="130")

                lb2=Listbox(self.top,height=30)
                lb2.insert(0,"Regular")
                lb2.insert(1,"Oblique")
                lb2.insert(2,"Bold")
                lb2.insert(3,"Bold Oblique")
                lb2.place(x="180",y="55",height="100",width="130")

                l3 = Label(self.top,text="Size:",font=("Arial",10))
                l3.place(x="340",y="10",height="15",width="30")
                
                self.e3 = Entry(self.top,font=("cambria",12))
                self.e3.place(x="340",y="30",height="20",width="80")

                lb3=Listbox(self.top,height=30)
                lb3.insert(0,"8")
                lb3.insert(1,"9")
                lb3.insert(2,"10")
                lb3.insert(3,"11")
                lb3.insert(4,"12")
                lb3.insert(5,"14")
                lb3.insert(6,"16")
                lb3.insert(7,"18")
                lb3.insert(8,"20")
                lb3.insert(9,"22")
                lb3.insert(10,"24")
                lb3.insert(11,"26")
                lb3.insert(12,"28")
                lb3.insert(13,"36")
                lb3.insert(14,"48")
                lb3.insert(15,"72")
                lb3.place(x="340",y="55",height="100",width="80")
                scrollbar = Scrollbar(lb3, orient="vertical")
                scrollbar.config(command=lb3.yview)
                scrollbar.pack(side="right", fill="y")

                lf=LabelFrame(self.top,text="Sample")
                lf.place(x="180",y="180",height="80",width="180")

                left=Label(lf, text="AaBbCc .... XxYyZz")
                lf.place(x="180",y="180",height="100",width="180")
                
                b1=Button(self.top,text="Done",font=("Times New Roman",14),command=self.ok)
                b1.place(x="180",y="300",height="30",width="80")

                b2=Button(self.top,text="Cancel",font=("Times New Roman",14),command=self.top.destroy)
                b2.place(x="270",y="300",height="30",width="80")
                self.top.mainloop()

        def CurSelet(self,evt):
                self.e1.delete(0,END)
                self.fs=str((self.lb1.get(self.lb1.curselection())))
                self.e1.insert(0,self.fs)
                
        def ok(self):
                self.text = Text(self.root)
                self.text.pack(fill=BOTH,expand=1)
                self.text.set(font=("Comic Sans MS",40))
                self.top.destroy()
                
        def hmenu(self):
                dialog=Toplevel(root)
                dialog.geometry("300x300")
                
        def showDialog(self):
                dialog=Toplevel(root)
                dialog.geometry("300x300")

        def showmsg():
                dialog=Toplevel(root)
                dialog.geometry("300x300")

        def viewhelp():
                dialog=Toplevel(root)
                dialog.geometry("500x500")
                dialog.showinfo("Help","This is Help")

        def about():
                dialog=Toplevel(root)
                dialog.geometry("500x500")
                messagebox.showinfo("About","This is notepad")

ob=Note()
