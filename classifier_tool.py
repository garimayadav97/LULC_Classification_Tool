
# coding: utf-8

# In[10]:


from tkinter import *
from tkinter import filedialog
from tkinter import ttk,StringVar,IntVar
from PIL import ImageTk, Image
from osgeo import gdal
from tkinter import messagebox
from keras.layers import *
import matplotlib.pyplot as plt
import os
import numpy as np
import tkinter.messagebox
import keras 
from keras import Sequential
from keras.utils import np_utils
from PIL import Image
import string
import matplotlib
import test_filetype
import array
import sys
import time
from threading import Thread
import io
from contextlib import redirect_stdout


tell=0

class NEURAL:
    def __init__(self, master):
        
        self.textfile=StringVar()
        self.texthdr=StringVar()
        self.textfile2=StringVar()
        self.texthdr2=StringVar()
        self.textweight=StringVar()
        self.red=IntVar()
        self.green=IntVar()
        self.blue=IntVar()
        self.col=IntVar()
        self.row=IntVar()
        self.pixels=IntVar()
        self.bands=IntVar()
        self.image=[]
        self.data=[]
        self.layer=[]
        self.my_var=IntVar()
        #self. my_var.set(5)
        self.my_var2=IntVar()
        self.my_var3=IntVar()
        self.my_var4=IntVar()
        self.my_var7=IntVar()
       
        
        self.loadimagewindow=0
        self.data2={}
 
        
        
        self.master = master
        self.master.configure(background='dark grey')
        self.master.geometry('800x600')  
        self.master.resizable(0, 0)
        
        tkinter.ttk.Style().configure('s.TCheckbutton', font=('times new roman', 10, 'bold'),foreground='black', background='lavender')
 
        
        separator1 = Frame(self.master,height=7,background='cornflowerblue')
        separator1.pack(fill=X)
        separator2 = Frame(self.master,width=7,background='cornflowerblue')
        separator2.pack(fill=Y,side=LEFT)
        separator3 = Frame(self.master,height=7,background='cornflowerblue')
        separator3.pack(fill=X,side=BOTTOM)
        separator4 = Frame(self.master,width=7, bd=10,background='cornflowerblue')
        separator4.pack(fill=Y,side=RIGHT)
        self.tab_control = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='   Create Training Data   ')
        self.tab_control.add(self.tab2, text='  Training and Testing  ')
        self.tab_control.add(self.tab3, text='  Load Training Data  ')
        self.tab_control.add(self.tab4, text='  History  ')
        
        
        separator7 = Frame(self.tab2,height=4)#background='cornflowerblue')
        separator7.pack(fill=X)
        self.tab_control2 = ttk.Notebook(self.tab2)
        self.tab11 = ttk.Frame(self.tab_control2)
        self.tab22 = ttk.Frame(self.tab_control2)
        self.tab_control2.add(self.tab11, text='   Artificial Neural Network   ')
        self.tab_control2.add(self.tab22, text='  Convolutional Neural Network  ')
        self.tab_control2.pack(expand=1, fill='both')

        
        self.tab_control.pack(expand=1, fill='both')     
        
        self.puttab1()
        self.putloaddata()
        self.putann()
        self.putcnn()
        self.puthistory()
                
        self.c=0
 
    def clicked(self):
        filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Binary files","*.*")))
        self.textfile.set(filename)
        
    def clickedhdr(self):
        self.loadimagewindow=1
        filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Binary files","*.*")))
        self.texthdr.set(filename)
        if (self.ifuint16()==True):
           #print('done')
            self.D_type=np.uint16
            self.mul=(float(2**16-1))
        else:
            self.D_type=np.uint8
            self.mul=float(255)
    
    def clicked2(self):
        
        filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Binary files","*.*")))
        self.img=filename
        self.textfile2.set(filename)
        
    def clickedhdr2(self):
        self.loadimagewindow=2
        filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Binary files","*.*")))
        self.texthdr2.set(filename)
        if (self.ifuint16()==True):
            #print('done')
            self.D_type=np.uint16
            self.mul=2**16-1
        else:
            self.D_type=np.uint8
            self.mul=255
            
    
    def puttab1(self):
        
        self.back1= Frame(self.tab1,height=800)
        self.back1.pack(fill=BOTH)
        
        self.gap1= Frame(self.back1,height=40)
        self.gap1.pack(fill=X)
        
        btn = Button(self.back1, text="Choose Image",foreground='white',background='grey',command=self.clicked)
        btn.pack(fill=X,side=TOP,padx=300,pady=20)
        
        self.textFile=Label(self.back1,textvariable=self.textfile,relief="sunken")
        self.textFile.pack(fill=X,padx=150,pady=20)
        
        btnhdr = Button(self.back1, text="Choose hdr file",foreground='white',background='grey',command=self.clickedhdr)
        btnhdr.pack(fill=X,padx=300,pady=20)
        
        self.textHdr=Label(self.back1,textvariable=self.texthdr,relief="sunken")
        self.textHdr.pack(fill=X,padx=150,pady=20)
        
        def RGB2():
            self.my_var7=2
        
            self.FCC()
            
            
            

            
        def RGB():
            self.my_var7=1
            self.FCC()
        
        
        btnok = Button(self.tab1, text="Load",foreground='black',background='cornflowerblue',command=RGB)
        btnok.pack(fill=X,padx=300,pady=20)
        btnSAVE = Button(self.tab1, text="Save",foreground='black',background='cornflowerblue',command=RGB2)
        btnSAVE.pack(fill=X,padx=300,pady=20)
        
    def putann(self):
        
        button2= Button(self.tab11, text='*Choose Image',foreground='white',background='grey',command=self.clicked2)
        button2.grid(row=0,column=20,padx=50,pady=50)
        self.textFile2=Label(self.tab11,textvariable=self.textfile2,relief="sunken",width=50)
        self.textFile2.grid(row=0,column=60,padx=5,pady=10)
        
        button3= Button(self.tab11, text='*Choose Header',foreground='white',background='grey',command=self.clickedhdr2)
        button3.grid(row=1,column=20)
        self.textFile3=Label(self.tab11,textvariable=self.texthdr2,relief="sunken",width=50)
        self.textFile3.grid(row=1,column=60,padx=5,pady=5,columnspan=100)
        
        """back = Frame(self.tab11)
        back.grid(row=0,column=0,sticky=W,padx=100,pady=5,columnspan=50)"""
        back2 = Frame(self.tab11,background='white')
        back2.grid(row=2,column=0,sticky=W,padx=20,pady=5)
        self.rb1 = tkinter.ttk.Checkbutton(back2, text='Training',variable=self.my_var,style='s.TCheckbutton')
        self.rb1.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        
        separator5 = Frame(self.tab11,height=2,width=600,background='lavender')
        separator5.grid(row=2,column=20,columnspan=50)
        
        lbl2 = Label(self.tab11, text='*Choose Training Data')
        lbl2.grid(row=4,column=20,sticky=W,padx=50)
        
        self.variable=StringVar(self.tab11)
        self.listt=[]

        self.w1= ttk.Combobox(self.tab11)
        self.w1['values']=("NULL")
        self.w1.current(0)
        self.w1.config(state=DISABLED)
        self.w1.grid(row=4,column=60,sticky=W)
        
        #self.combored['values']= (y)
        
        """self.w=ttk.OptionMenu(self.tab11,self.variable,*self.listt)
        self.w.config(state=DISABLED)
        self.w.grid(row=2,column=50,sticky=W)"""
        
        
        lbl3 = Label(self.tab11, text='*Learning Rate')
        lbl3.grid(row=6,column=20,sticky=W,pady=5,padx=50)
        self.entry2=Entry(self.tab11)
        self.entry2.grid(row=6,column=60,sticky=W,pady=5)
        
        lbl4 = Label(self.tab11, text='*Epochs')
        lbl4.grid(row=7,column=20,sticky=W,pady=5,padx=50)
        self.entry3=Entry(self.tab11)
        self.entry3.grid(row=7,column=60,sticky=W,pady=5)
        
        lbl5= Label(self.tab11, text='*Hidden Neurons')
        lbl5.grid(row=8,column=20,sticky=W,pady=5,padx=50)
        self.entry4=Entry(self.tab11)
        self.entry4.grid(row=8,column=60,sticky=W,pady=5)
        
        
        
        
        back3 = Frame(self.tab11,background='white')
        back3.grid(row=10,column=0,sticky=W,padx=20,pady=5,columnspan=50)
        self.rb2 = tkinter.ttk.Checkbutton(back3, text='Testing',variable=self.my_var2,style='s.TCheckbutton')
        self.rb2.grid(row=10,column=60,sticky=W,padx=5,pady=5)
        separator6 = Frame(self.tab11,height=2,width=600,background='lavender')
        separator6.grid(row=10,column=20,columnspan=50)
        
        def clicked3():
            filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",defaultextension='.txt')
            self.textweight.set(filename)
        
        button4= Button(self.tab11, text='Load Model',foreground='white',background='grey',command=clicked3)
        button4.grid(row=13,column=20)
        self.textFile4=Label(self.tab11,textvariable=self.textweight,relief="sunken",width=50)
        self.textFile4.grid(row=13,column=60,sticky=W,padx=5,pady=5)
        
        
        button5= Button(self.tab11, text='Classify',foreground='black',background='cornflowerblue',command=self.classifyANN)
        button5.grid(row=30,column=60,sticky=W,pady=30)
        
        
            
    
        
    def putcnn(self):
        self.textweight.set("")
        
        button22= Button(self.tab22, text='*Choose Image',foreground='white',background='grey',command=self.clicked2)
        button22.grid(row=0,column=20,padx=50,pady=50)
        self.textFile2=Label(self.tab22,textvariable=self.textfile2,relief="sunken",width=50)
        self.textFile2.grid(row=0,column=60,padx=5,pady=10)
        
        button33= Button(self.tab22, text='*Choose Header',foreground='white',background='grey',command=self.clickedhdr2)
        button33.grid(row=1,column=20)
        self.textFile3=Label(self.tab22,textvariable=self.texthdr2,relief="sunken",width=50)
        self.textFile3.grid(row=1,column=60,padx=5,pady=5,columnspan=100)
        
        """back = Frame(self.tab11)
        back.grid(row=0,column=0,sticky=W,padx=100,pady=5,columnspan=50)"""
        back2 = Frame(self.tab22,background='white')
        back2.grid(row=2,column=0,sticky=W,padx=20,pady=5)
        self.rb11 = tkinter.ttk.Checkbutton(back2, text='Training',variable=self.my_var3,style='s.TCheckbutton')
        self.rb11.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        separator5 = Frame(self.tab22,height=2,width=600,background='lavender')
        separator5.grid(row=2,column=20,columnspan=50)
        
        lbl22 = Label(self.tab22, text='*Choose Training Data')
        lbl22.grid(row=4,column=20,sticky=W,padx=50)
        
        self.variable=StringVar(self.tab11)
        self.listt=[]

        self.w= ttk.Combobox(self.tab22)
        self.w['values']=("NULL")
        self.w.current(0)
        self.w.config(state=DISABLED)
        self.w.grid(row=4,column=60,sticky=W)
        
        
        lbl33= Label(self.tab22, text='*Threshold Value')
        lbl33.grid(row=6,column=20,sticky=W,pady=5,padx=50)
        self.entry22=Entry(self.tab22)
        self.entry22.grid(row=6,column=60,sticky=W,pady=5)
        
        lbl4 = Label(self.tab22, text='*Epochs')
        lbl4.grid(row=7,column=20,sticky=W,pady=5,padx=50)
        self.entry33=Entry(self.tab22)
        self.entry33.grid(row=7,column=60,sticky=W,pady=5)

        
        separator53 = Frame(self.tab22,height=5,background='grey')
        separator53.grid(row=9,column=1,columnspan=50)
        
        back3 = Frame(self.tab22,background='white')
        back3.grid(row=10,column=0,sticky=W,padx=20,pady=5,columnspan=50)
        self.rb22 = tkinter.ttk.Checkbutton(back3, text='Testing',variable=self.my_var4,style='s.TCheckbutton')
        self.rb22.grid(row=10,column=60,sticky=W,padx=5,pady=5)
        separator6 = Frame(self.tab22,height=2,width=600,background='lavender')
        separator6.grid(row=10,column=20,columnspan=50)
        
        def clicked3():
            filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",defaultextension='.txt')
            self.textweight.set(filename)
        
        button44= Button(self.tab22, text='Load Model',foreground='white',background='grey',command=clicked3)
        button44.grid(row=13,column=20)
        self.textFile4=Label(self.tab22,textvariable=self.textweight,relief="sunken",width=50)
        self.textFile4.grid(row=13,column=60,sticky=W,padx=5,pady=5)
        
        
        button5= Button(self.tab22, text='Classify',foreground='black',background='cornflowerblue',command=self.classifyCNN)
        button5.grid(row=30,column=60,sticky=W,pady=30)
        
    def putloaddata(self):
  
        def addDATASET():
            self.window3=tkinter.Toplevel()
            self.window3.geometry('200x200')
            label=Label(self.window3,text="Name the Dataset")
            label.pack()
            self.entry1=Entry(self.window3)
            self.entry1.pack()
            button1=Button(self.window3,text="OK",command=savedataset)
            button1.pack()

        def delDATASET():
            try:
                item=self.listbox1.get(self.listbox1.curselection()[0])
                item2=self.listbox1.curselection()[0]
                print(item,item2)
                self.listbox1.delete(item2)
                del self.listt[item2]
                self.w['values']=self.listt
                self.w1['values']=self.listt
                if item2!=0:
                    self.w.current(0)
                    self.w1.current(0)
                else:
                    self.w['values']=("NULL")
                    self.w1['values']=("NULL")
                    self.c=0
                    self.w.config(state=DISABLED)
                    self.w1.config(state=DISABLED)
                    
                if item in self.data2:
                    del self.data2[item]
            except IndexError:
                    messagebox.showerror("Error","Select Dataset First")
        
        def addfiles():
            
            try:
                items = int(self.listbox1.curselection()[0])
                add =  filedialog.askopenfilename(initialdir = "/",title = "Select file",parent=self.master)
                var=self.listbox1.get(items)
                print(var)
                self.data2[var].append(add)
                print(self.data2)
            except IndexError:
                    messagebox.showerror("Error","Select Dataset to Add Files")
 
        
        def savedataset():

                    
                    self.data2[self.entry1.get()]=[]
                    print(self.data2)
                    if self.entry1.get() in self.listt:
                        messagebox.showerror("Error","Name already exist")
                    else:
                        self.listbox1.insert(END,self.entry1.get())
                        self.listt.append(self.entry1.get())
                        self.w['values']=self.listt
                        self.w1['values']=self.listt
                        print(self.listt)
                    
                    if self.c==0:
                        self.btnremove.config(state='normal')
                        self.btnadd2.config(state='normal')
                        self.btnadd3.config(state='normal') 
                        self.w.config(state='readonly')
                        self.w.current(0)
                        self.w1.config(state='readonly')
                        self.w1.current(0)
                        self.c=1
                    
                    self.window3.destroy()
                    
            
            
        def viewfiles():
            
                try:
                    item=self.listbox1.get(self.listbox1.curselection()[0])
                    self.window=tkinter.Toplevel()
                    self.window.geometry('500x200')
                    
                    back5=Frame(self.window,width=400)
                    back5 .grid(column=0, row=0, sticky=(N,W,E,S))
                    listbox2 = Listbox(back5, height=10,font=("Helvetica", 10),width=65)
                    listbox2 .grid(column=0, row=0, sticky=(N,W,E,S))
                    s = ttk.Scrollbar(back5, orient=VERTICAL, command=listbox2.yview)
                    s.grid(column=1, row=0, sticky=(N,S))
                    listbox2 ['yscrollcommand'] = s.set

                    
                    

                    for i in self.data2[item]:
                            listbox2.insert(END,i)
                except IndexError:
                    messagebox.showerror("Error","Select Dataset to View Files")
                
           

        back4=Frame(self.tab3,width=100)
        back4.pack(fill=X,padx=100,pady=20)
        

        btnadd = Button(self.tab3, text="Add Data set",foreground='white',background='grey',command=addDATASET)
        btnadd.pack(fill=X,padx=300,pady=10)
        
        separator5 = Frame(self.tab3,height=1,background='grey')
        separator5.pack(fill=X,padx=100)
        
        self.btnremove = Button(self.tab3, text=" Remove Data set",state=DISABLED,foreground='black',background='sky blue',command=delDATASET)
        self.btnremove.pack(fill=X,padx=300,pady=10)
  
        
        
        self.btnadd2 = Button(self.tab3, text="Add Files",state=DISABLED,foreground='black',background='sky blue',command=addfiles)
        self.btnadd2.pack(fill=X,padx=300,pady=10)
        
        self.btnadd3 = Button(self.tab3, text="View Files",state=DISABLED,foreground='black',background='sky blue',command=viewfiles)
        self.btnadd3.pack(fill=X,padx=300,pady=10)
            
            
        frm=Frame(self.tab3,width=100)
        frm.pack(fill=X,padx=100,pady=10)
        self.listbox1 = Listbox(frm, height=5,font=("Times new roman", 14))
        self.listbox1 .grid(column=0, row=0, sticky=(N,W,E,S))
        s = ttk.Scrollbar(frm, orient=VERTICAL, command=self.listbox1 .yview)
        s.grid(column=1, row=0, sticky=(N,S))
        self.listbox1 ['yscrollcommand'] = s.set

        frm.grid_columnconfigure(0, weight=1)
        frm.grid_rowconfigure(0, weight=1)
        
    def puthistory(self):
        
        def clear():
            self.T1.config(state="normal")
            self.T1.delete('1.0', END)
    
            self.puthistorytext("Run Model to view Hisotry!\n")
        
        frm=Frame(self.tab4)
        frm.pack(fill='both',expand=1)
        
        self.T1 =Text(frm)
        self.count2=0
        self.puthistorytext("Run Model to view Hisotry!\n")
        self.T1.place(x=5,y=5,width=750,height=450)
        s = ttk.Scrollbar(self.T1,orient=VERTICAL, command=self.T1.yview)
        s.pack(fill=Y,side=RIGHT)
        self.T1 ['yscrollcommand'] = s.set
        button6=Button(frm,text="Clear",background="cornflowerblue",width=50,command=clear)
        button6.place(x=350,y=500,width=100)
       
        
        
       
        
    def puthistorytext(self,strr):
        

        self.T1.config(state="normal")
        #self.T1.delete('0', END)
        self.T1.insert(END, strr+'\n')
        self.T1.config(state="disabled")
        
    def putimage(self,result):
            
                self.window3=tkinter.Toplevel()
                frame = Frame(self.window3, bd=2, relief=SUNKEN)
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
                
                #imae=Image.open('C:/Users/Acer/Documents/222.tiff')
                img = ImageTk.PhotoImage(result)
                
                label = Label(frame, bd=0,image=img)
                label.grid(row=0, column=0, sticky=N+S+E+W)
  
                label.image=img
     
                frame.pack(fill=BOTH,expand=1)
                
            
        

            
    def FCC(self):
        val1=self.textfile.get().split("/")
        val2=self.texthdr.get().split("/")
        
        if((self.textfile.get()=="") or (self.texthdr.get()=="")):
            messagebox.showerror("Error","Kindly choose both the files")
        elif((val1[-1]+".hdr")!=(val2[-1])):
            messagebox.showerror("Error","Kindly choose correct hdr file for the image")
        else:
            self.window2=tkinter.Toplevel()
            self.window2.geometry('500x500')
            self.lbl=Label(self.window2,text="Choose the bands values for RGB")
            if self.my_var7==1:
                self.btnOk = Button(self.window2, text="OK",command=self.showFCC)
            elif self.my_var7==2:
                self.btnOk = Button(self.window2, text="OK",command=self.train)
            self.lred=Label(self.window2,text="Red")
            self.lbl.place(x=150,y=30,width=200)
            self.btnOk.place(x=200,y=300,width=100)
            img = gdal.Open(self.textfile.get())
            #b = img.RasterCount
            self.col.set(img.RasterXSize)
            self.row.set(img.RasterYSize)
            self.bands.set(img.RasterCount)
            #print(self.bands.get())
            self.pixels.set(self.row.get()*self.col.get())
            y=[]
            #image=extract(fname,bands,pixels)
            for i in range(1,self.bands.get()+1):
                y.append(i) 
            self.lred.place(x=130,y=160,width=30)
            self.combored = ttk.Combobox(self.window2,state="readonly")
            self.combored['values']= (y)
            self.combored.current(y[-2]) 
            self.combored.place(x=160,y=160,width=50)
            self.lgreen=Label(self.window2,text="Green")
            self.lgreen.place(x=220,y=160,width=30)
            self.combogreen = ttk.Combobox(self.window2,state="readonly")
            self.combogreen['values']= (y)
            self.combogreen.current(y[-2]) 
            self.combogreen.place(x=260,y=160,width=50)
            self.lblue=Label(self.window2,text="Blue")
            self.lblue.place(x=320,y=160,width=30)
            self.comboblue = ttk.Combobox(self.window2,state="readonly")
            self.comboblue['values']= (y)
            self.comboblue.current(y[-2]) 
            self.comboblue.place(x=350,y=160,width=50)
            self.lgreen=Label(self.window2,text="Green")
            self.lgreen.place(x=220,y=160,width=30)
            
            
            
            
    def showFCC(self):
                
                self.whichNN="image"
                self.whichRoot="root"
                self.count=0
                self.red.set(int(self.combored.get()))
                self.green.set(int(self.combogreen.get()))
                #print(D_type)
                self.blue.set(int(self.comboblue.get()))
                self.window2.destroy()
                
                self.window3=tkinter.Toplevel()
                self.window3.geometry("600x600")
                self.window3.protocol("WM_DELETE_WINDOW",self.delete)
                #self.window3.grab_set()
                frame = Frame(self.window3, bd=2, relief=SUNKEN)
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
                xscroll = Scrollbar(frame, orient=HORIZONTAL)
                xscroll.grid(row=1, column=0, sticky=E+W)
                yscroll = Scrollbar(frame)
                yscroll.grid(row=0, column=1, sticky=N+S)
                self.canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
                self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
                xscroll.config(command=self.canvas.xview)
                yscroll.config(command=self.canvas.yview)
                frame.pack(fill=BOTH,expand=1)
                
                def printcoords(event):
                    
                    def startClick():
                                self.window11.grab_release()
                                self.window3.grab_set()
                                def turn():
                                                self.window12.grab_release()
                                                self.window3.grab_set()
                                                height=int(self.xx2.get())
                                                length=int(self.xx1.get())
                                                print(height,length)
                                                self.a = array.array("H")
                                                self.window3.grab_release()
                                                self.window4=tkinter.Toplevel()
                                                self.window4.geometry('500x500')
                                                self.window4.protocol("WM_DELETE_WINDOW",self.callback)
                                                self.window4.configure(background='white')
                                                self.bsave=Button(self.window4,text="Save",command=self.savefile)
                                                self.bsave.place(relx=0.5, rely=0.5, anchor=CENTER,width=200)
                                                self.scrollbar = Scrollbar(self.window4)
                                                self.scrollbar.pack( side = RIGHT, fill=Y )
                                                self.t =Listbox(self.window4,yscrollcommand = self.scrollbar.set)
                                                j=1
                                        
                                                for k in range(0,height*2+1):
                                                    for l in range(0,length*2+1):
                                                        self.t.insert(END,"\n"+ "Click " + str(j)+'\n')
                                                        for i in range(0,self.bands.get()):
                                                            self.t.insert(END, str(self.newimage[event.y-2-height+k][event.x-2-length+l][i])+ '\n')
                                                            #print(self.newimage[event.y-2-height+k][event.x-2-length+l][i],event.y-2-height+k,event.x-2-length+l)
                                                            self.a.append(self.newimage[event.y-2-height+k][event.x-2-length+l][i])
                                            #t.place(x=0,y=0,height=17*self.bands.get()+17)
                                                        self.t.insert(END,'\n')
                                                        j=j+1
                                                self.t.pack( side = LEFT, fill = BOTH )
                                                self.scrollbar.config( command = self.t.yview )
                                                self.count=1
                                        
                                       

                                self.window11.destroy()
                                if self.my_var2.get()==20:    
                                        self.window3.grab_release()
                                        self.a = array.array("H")
                                        self.window4=tkinter.Toplevel()
                                        self.window4.geometry('500x500')
                                        self.window4.protocol("WM_DELETE_WINDOW",self.callback)
                                        self.window4.configure(background='white')
                                        self.bsave=Button(self.window4,text="Save",command=self.savefile)
                                        self.bsave.place(relx=0.5, rely=0.5, anchor=CENTER,width=200)
                                        self.scrollbar = Scrollbar(self.window4)
                                        self.scrollbar.pack( side = RIGHT, fill=Y )
                                        self.t =Listbox(self.window4,yscrollcommand = self.scrollbar.set)
                                        self.t.insert(END,"\n"+ "Click " + str(self.count)+'\n')
                                        for i in range(0,self.bands.get()):
                                            self.t.insert(END, str(self.newimage[event.y-2][event.x-2][i] )+ '\n')
                                            #print(self.newimage[event.y-2][event.x-2][i],event.x-2,event.y-2)
                                            self.a.append(self.newimage[event.y-2][event.x-2][i])
                                        #t.place(x=0,y=0,height=17*self.bands.get()+17)
                                        self.t.insert(END,'\n')
                                        self.t.pack( side = LEFT, fill = BOTH )
                                        self.scrollbar.config( command = self.t.yview )
                                        self.count=1
                                    
                                        #print (event.x-2,event.y-2) 
                                
                                elif self.my_var2.get()==15:
                                    self.window12=tkinter.Toplevel()
                                    self.window12.geometry("300x200")
                                    self.window3.grab_release()
                                    self.window12.grab_set()
                                    self.lbb1 = Label(self.window12, text= 'Length').place(x=20,y=20,width=100)
                                    self.lbb2 = Label(self.window12, text= 'Height').place(x=20,y=50,width=100)
                                    self.xx1=Entry(self.window12)
                                    self.xx1.place(x=120, y=20, width=80)
                                    self.xx2=Entry(self.window12)
                                    self.xx2.place(x=120, y=50, width=80)
                                    self.btnOk3 = Button(self.window12, text="OK",command=turn) 
                                    self.btnOk3.place(x=75,y=80,width=50)
                    
                    print(event.x,event.y)
                    if ((event.y>(self.row.get()+1))or (event.x>(self.col.get()+1))or(event.x<2)or (event.y<2)):
                                messagebox.showerror("Error","Kindly click inside the image",parent=self.window3)
                    
                    elif self.count==0:
                        MsgBox = messagebox.askquestion ('Select an option','Do you want to save the clicks',icon = 'warning',parent=self.window3)
                        if MsgBox=='yes':
                            
                            self.window11=tkinter.Toplevel()
                            self.window11.geometry("200x100")
                            self.window3.grab_release()
                            self.window11.grab_set()
                            #self.window11.protocol("WM_DELETE_WINDOW",self.delete)    
                            self.rb3 = tkinter.ttk.Radiobutton(self.window11, text='Automatic',style='s.TRadiobutton',variable=self.my_var2, value=15)
                            self.rb3.place(x=20,y=20,width=200)
                            self.rb4 = tkinter.ttk.Radiobutton(self.window11, text='Manual',style='s.TRadiobutton',variable=self.my_var2, value=20)
                            self.rb4.place(x=20,y=50,width=200)
                            self.btnOk2 = Button(self.window11, text="OK",command=startClick) 
                            self.btnOk2.place(x=20,y=80)
                            
                        else:
                            self.count=0
                    else:
                            self.t.insert(END, "\n"+"Click " + str(self.count)+'\n')
                            for i in range(0,self.bands.get()):
                                self.t.insert(END, str(self.newimage[event.y-2][event.x-2][i]) + '\n')
                                self.a.append(self.newimage[event.y-2][event.x-2][i])
  
                            self.t.insert(END,'\n')
                            self.t.pack( side = LEFT, fill = BOTH )
                            self.scrollbar.config( command = self.t.yview)
                            
                            self.count=self.count+1
                            

                self.image=self.train()
                #print(image[1][1])
                self.newimage=np.zeros((self.row.get(),self.col.get(),self.bands.get()),dtype=self.D_type)
                self.newimage=self.image.reshape((self.row.get(),self.col.get(),self.bands.get()))
                #File = filedialog.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
                self.window3.grab_set()
                img = ImageTk.PhotoImage(self.result)
                self.window3.img=img
                self.canvas.create_image(0,0,image=img,anchor="nw")
                self.canvas.config(scrollregion=self.canvas.bbox(ALL))
                self.canvas.bind("<Button 1>",printcoords)
    
    def train(self):
                    def ReadBilFile(bil,bands,pixels):
                        flag=0
                        extract_band = 1
                        image = np.zeros([pixels, bands], dtype=self.D_type)
                        gdal.GetDriverByName('EHdr').Register()
                        img = gdal.Open(bil)
                        while bands >= extract_band:
                            bandx = img.GetRasterBand(extract_band)
                            datax = bandx.ReadAsArray()
                            temp = datax
                            store = temp.reshape(pixels) # reshape(pixels,1)
                            for i in range(pixels):
                                image[i][extract_band - 1] = store[i]
                            extract_band = extract_band + 1
                        
                        
                        pic = np.zeros([pixels, 3],dtype=self.D_type)
                        pic[:,0]= image[:,self.red.get()-1]
                        pic[:,1] = image[:,self.green.get()-1]
                        pic[:,2]=image[:,self.blue.get()-1]
                        mini=np.zeros(3,dtype=self.D_type)
                        maxi=np.zeros(3,dtype=self.D_type)
                        for i in range(0,3):
                            mini[i]=(min(pic[:,i]))
                            maxi[i]=(max(pic[:,i]))
                        pic2 = np.zeros([pixels, 3],dtype='uint8')
                        if (self.ifuint16()==True):
                            flag=1
                            #print("hello")
                            for i in range(0,3):
                                for j in range(0,pixels):
                                    pic2[j][i]=((pic[j][i]-mini[i])/(maxi[i]-mini[i]))*255
                                    #print(pic[j][i])

                        if flag==1:
                            return pic2,image
                        else:
                            return pic,image
                    self.x_test,image= ReadBilFile(self.textfile.get(),self.bands.get(), self.pixels.get())
                    x_new=np.zeros((self.row.get(),self.col.get(),3),dtype='uint8')
                    x_new=self.x_test.reshape((self.row.get(),self.col.get(),3))
                    
                    self.result = Image.fromarray((x_new),'RGB')
                     
                    if self.my_var7==2:
                        fname2=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",defaultextension='.png')
                        if fname2:
                            self.result.save(fname2)
                        self.window2.destroy()
                    else:
                        return image
                
    def callback(self):
        self.count=0
        self.t.delete(0,'end')
        self.window4.destroy()
                
    def ifuint16(self):
        if self.loadimagewindow==1:
            self.D_type,self.width,self.height,self.unit=test_filetype.main(self.texthdr.get())
        elif self.loadimagewindow==2:
            self.D_type,self.width,self.height,self.unit=test_filetype.main(self.texthdr2.get())
        #print("yesssss",self.D_type)
        if self.D_type==np.uint16:
            print("here16")
            return True
        else:
            print("here8")
            return False
        
    
    def savefile(self):
            self.count=0
            self.t.delete(0,'end')
            self.window4.destroy()
            #self.btest.place(x=5, y=self.row.get()+5, width=100)
            self.fname2=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Binary files","*.*"),("all files","*.*")))
            print(self.a)
            if sys.byteorder == "little":
                self.a.byteswap()
            with open(self.fname2,"wb") as f:
                self.a.tofile(f)
                
    def delete(self):
        
        if self.whichNN=="ann":
            self.annroot.destroy()
        elif self.whichNN=="cnn":
            self.cnnroot.destroy()
        elif self.whichNN=="image":
            self.window3.grab_release()
            self.window3.destroy()
            
        elif self.whichNN=="addLayer":
            pass
        """if self.whichRoot=="root":
            root.deiconify()"""
            
    def trainann(self):  
                #try:
                nn=ANN(self.D_type,self.c_c,self.bands.get(),self.eta,self.epochs,self.neuron)
                D_type=self.D_type
                values=[]
                labels=[]
                flag='true'
                for address in self.data:
                    with open(address,"rb") as f:
                        click=0
                        block = f.read()
                        for ch in block:
                            if flag=='true':
                                flag='false'
                            elif flag=='false':
                                values.append(ch)
                                click=click+1
                                flag='true'
                        labels.append(click)


                print(len(values))            
                print(len(labels))
                ll=len(values)
                rex=int(ll/self.bands.get())
                arr=np.zeros([ll], dtype=D_type)
                for i in range(ll):
                    arr[i]=values[i]
                x_train=arr.reshape(rex,self.bands.get())  

                y_train = np.zeros([rex], dtype=D_type)
                lab=1
                i=0
                for index in labels:
                    ind=index/self.bands.get()
                    while (ind)>0:
                        y_train[i]=lab
                        ind=ind-1
                        i=i+1
                    lab=lab+1
                
                self.w11,self.w22=nn.fit(x_train, y_train, print_progress=True)
                
                #print(self.w11,self.w22)
                MsgBox = messagebox.askquestion ('Select an option','Do you want to save the new weights',icon = 'question')
                if MsgBox=="yes":
                    self.fileweightsave=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
                    
                    file = open(self.fileweightsave+".txt",'w') 
                    for i in range(0,self.w11.shape[0]):
                        for j in range(0,self.w11.shape[1]):
                            file.write(str(self.w11[i][j])+",")
                        file.write("\n")
                        
                    file.write("x\n")
                    
                    for i in range(0,self.w22.shape[0]):
                        for j in range(0,self.w22.shape[1]):
                            file.write(str(self.w22[i][j])+",")
                        file.write("\n")
                    
                if self.x==1:
                        pixels=self.row.get()*self.col.get()
                        x_test = nn.ReadBilFile(self.img,self.bands.get(),pixels)
                        y_pred1=nn.predict(x_test,self.w11,self.w22)
                        img=y_pred1.reshape(self.row.get(),self.col.get())
                        
                        print(self.mul,self.D_type)
                        if self.D_type==np.uint16: 
                            typ='uint16'
                        else:
                            print('8')
                            typ='uint8'
                        a,b=np.unique(img,return_counts=True)
                        print(a,b)
                        b=self.height*self.width*b
                        print(b)
                        self.showarea(a,b)
                        result = Image.fromarray(((img*((self.mul)/(self.c_c+1)))).astype(typ))
                        #result.save('C:/Users/Acer/Documents/2223.tiff')
                        self.putimage(result)
                        plt.imshow(img)
                        plt.colorbar()
                        plt.show()
            

                        
    def classifyANN(self):
        
        try:
            l=0
            val1=self.textfile2.get().split("/")
            val2=self.texthdr2.get().split("/")
        
            if((self.textfile2.get()=="") or (self.texthdr2.get()=="")):
                messagebox.showerror("Error","Kindly choose both the files")
            elif((val1[-1]+".hdr")!=(val2[-1])):
                messagebox.showerror("Error","Kindly choose correct hdr file for the image")
            else:
                self.img = gdal.Open(self.textfile2.get())
                self.col.set(self.img.RasterXSize)
                self.row.set(self.img.RasterYSize)
                self.bands.set(self.img.RasterCount)
                print(self.bands.get())

                if (self.my_var.get()==1 and self.my_var2.get()==1):
                    self.data=self.data2[(self.w.get())]
                    if len(self.data)==0:
                        raise KeyError
                    self.epochs=int(self.entry3.get())
                    self.neuron=int(self.entry4.get())
                    self.eta=float(self.entry2.get())
                    
                    if self.neuron<=0: 
                        l=1
                        raise ValueError
                    elif self.epochs<=0:
                        l=2
                        raise ValueError
                    elif self.eta<=0:
                        l=3
                        raise ValueError
                    if (not self.textweight.get().endswith(".txt")) and  (self.textweight.get()!=""):
                            messagebox.showerror("Error","Text File Expected for saved model")
                    else:
                        self.c_c=len(self.data)+1
                        print(self.my_var.get(),self.my_var2.get())
                        print("yes")
                        self.x=1

                        th=Thread(target=self.trainann)
                        th.run()  

                        if (self.textweight.get()!=""):
                            print("yes1")
                            isweight="yes"
                            print(self.textweight.get())
                            f=open(self.textweight.get(),'r')
                            lines=f.read()
                            warrays=lines.split("x")
                            w1array=warrays[0].split("\n")
                            w2array=warrays[1].split("\n")

                            w1=np.zeros([len(w1array)-1,len(w1array[0].split(","))-1])
                            k=len(w1array)-2
                            for i in range(0,k):
                                x=w1array[i].split(",")
                                #print(x)
                                for j in range(len(x)-1):
                                    w1[i][j]=x[j]

                            w2=np.zeros([len(w2array)-2,len(w2array[1].split(","))-1])
                            k=len(w2array)-2
                            for i in range(0,k):
                                x=w2array[i+1].split(",")
                                #print(x)
                                for j in range(len(x)-1):
                                        w2[i][j]=x[j]

                            nn=ANN(self.D_type,0,self.bands.get(),0,0,0)
                            pixels=self.row.get()*self.col.get()
                            x_test = nn.ReadBilFile(self.img,self.bands.get(),pixels)
                            y_pred=nn.predict(x_test,w1,w2)

                            img=y_pred.reshape(self.row.get(),self.col.get())
                            plt.imshow(img)
                            plt.colorbar()
                            plt.show()
                            a,b=np.unique(img,return_counts=True)
                            print(a,b)
                            b=self.height*self.width*b
                            print(b)
                            self.showarea(a,b)
                            if self.D_type==np.uint16: 
                                        typ='uint16'
                            else:
                                        print('8')
                                        typ='uint8'
                            result = Image.fromarray(((img*((self.mul)))).astype(typ))
                            #result.save('C:/Users/Acer/Documents/2223.tiff')
                            self.putimage(result)


                elif(self.my_var.get()==1):
                    self.data=self.data2[(self.w.get())]
                    if len(self.data)==0:
                        raise KeyError
                    self.epochs=int(self.entry3.get())
                    self.neuron=int(self.entry4.get())
                    self.eta=float(self.entry2.get())
                    
                    if self.neuron<=0: 
                        l=1
                        raise ValueError
                    elif self.epochs<=0:
                        l=2
                        raise ValueError
                    elif self.eta<=0:
                        l=3
                        raise ValueError
                        

                    print(self.data)
                    self.c_c=len(self.data)+1
                    print(self.my_var.get(),self.my_var2.get())
                    self.x=0
                    th=Thread(target=self.trainann)
                    th.start()

                elif(self.my_var2.get()==1):
                        print("oh no")
                        print(self.textweight.get())
                        if not self.textweight.get().endswith(".txt"):
                            messagebox.showerror("Error","Text File Expected for saved model")
                        else:
                            f=open(self.textweight.get(),'r')
                            lines=f.read()
                            warrays=lines.split("x")
                            w1array=warrays[0].split("\n")
                            w2array=warrays[1].split("\n")

                            w1=np.zeros([len(w1array)-1,len(w1array[0].split(","))-1])
                            k=len(w1array)-2
                            for i in range(0,k):
                                x=w1array[i].split(",")
                                #print(x)
                                for j in range(len(x)-1):
                                    w1[i][j]=x[j]

                            w2=np.zeros([len(w2array)-2,len(w2array[1].split(","))-1])
                            k=len(w2array)-2
                            for i in range(0,k):
                                x=w2array[i+1].split(",")
                                #print(x)
                                for j in range(len(x)-1):
                                        w2[i][j]=x[j]

                            nn=ANN(self.D_type,0,self.bands.get(),0,0,0)
                            pixels=self.row.get()*self.col.get()
                            x_test = nn.ReadBilFile(self.img,self.bands.get(),pixels)
                            y_pred=nn.predict(x_test,w1,w2)

                            img=y_pred.reshape(self.row.get(),self.col.get())
                            #self.putimage(img)
                            """plt.imshow(img)
                            plt.colorbar()
                            plt.show()"""

                            print(self.mul,self.D_type)
                            if self.D_type==np.uint16: 
                                typ='uint16'
                            else:
                                print('8')
                                typ='uint8'
                            result = Image.fromarray(((img*((self.mul)/2))).astype(typ))
                            print(result)
                            a,b=np.unique(im,return_counts=True)
                            print(a,b)
                            b=self.height*self.width*b
                            print(b)
                            self.showarea(a,b)
                            self.putimage(result)
        except KeyError:
            messagebox.showerror("Error","Add dataset first")
        except ValueError:
            if l==0:
                messagebox.showerror("Error","Incorrect Entry ")
            if l==1:
                messagebox.showerror("Error","Neurons must be a positive integer ")
            if l==2:
                messagebox.showerror("Error","Epochs must be a positive integer ")
            if l==3:
                messagebox.showerror("Error","Learning Rate must be a positive")
        
        
        
            
                
    def printimage(self,y_pred):
                y_test_old1=y_pred
                pixels=self.row.get()*self.col.get()
                y_testold1 = np.zeros([pixels], dtype=self.D_type)  

                mini=0
                for i in range(0,pixels):
                                y_1=y_pred[i].tolist()
                                if ((max(y_1))<=0.1):
                                    y_testold1[i]=0
                                else:
                                    y_testold1[i]=y_1.index(max(y_1))
                             
                k= np.zeros([self.row.get(),self.col.get()], dtype=self.D_type) 
                k = y_testold1.reshape(self.row.get(),self.col.get()) 
                k.tolist()
                a,b=np.unique(k,return_counts=True)
                print(a,b)
                b=self.height*self.width*b
                print(b)
                self.showarea(a,b)
                
                plt.imshow(k)
                plt.colorbar()
                plt.show()
                if self.D_type==np.uint16: 
                            typ='uint16'
                else:
                            print('8')
                            typ='uint8'
                result = Image.fromarray((k*((self.mul)/(self.c_c+1))).astype(typ))
                self.putimage(result)
                
    def showarea(self,a,b):
        
        windowlast1=tkinter.Toplevel()
        windowlast1.geometry("500x200")
        i=0
        frm=Frame(windowlast1)
        frm.pack(fill='both',expand=1)
        t2 =Text(frm)
        
        t2.place(x=0,y=0,width=490,height=195)
        s = ttk.Scrollbar(t2,orient=VERTICAL, command=t2.yview)
        s.pack(fill=Y,side=RIGHT)
        t2 ['yscrollcommand'] = s.set
        
        for v in a:
            if v!=0:
                newadd=self.data[v-1].split("/")
                t2.config(state="normal")
                t2.insert(END, str(newadd[-1])+"=====>"+str(b[i])+" "+str(self.unit)+" square"+'\n')
                t2.config(state="disabled")
            i=i+1
            
        
                
    def traincnn(self):
                    print("in train cnn")
                    
                    print(self.bands.get(),self.epochs,self.c_c,self.thresh,self.D_type,self.row.get(),self.col.get())
                    values = []
                    c_l = {}
                    i=1
                    for add in self.data:
                        print("{} class {} ".format(add,i))
                        c_l[add] = i
                        i=i+1
                    clicks={}
                    print(self.data)
                    for address in self.data:
                        with open(address, "rb") as f:
                            k = len(f.read())
                            clicks[address] = (k // 2 // self.bands.get()) 
                            print('{} ==> {}'.format(address, clicks[address]))

                    for address in self.data:
                        with open(address, "rb") as f:
                            b = array.array("H")
                            b.fromfile(f, clicks[address]*self.bands.get())
                            if sys.byteorder == "little":
                                b.byteswap()
                            for v in b:
                                values.append(v)

                    ll = (len(values))
                    rex = ll // self.bands.get()
                    print(ll, rex)
                    y_train = np.zeros([rex], dtype=self.D_type)
                    y_test = np.zeros([self.row.get() *self.col.get()], dtype=self.D_type) 

                    f_in = np.zeros([ll], dtype=self.D_type)
                    x = 0
                    for i in range(ll):
                        f_in[x] = values[i]
                        x += 1


                    mark = 0
                    for add in self.data:
                        for i in range(clicks[add]):
                            y_train[mark+i] = c_l[add]
                        mark = mark + clicks[add]
                    x_train = f_in.reshape(rex, self.bands.get())

                    seed = 7
                    np.random.seed(seed)#save value 
                    x_train = x_train / self.mul

                    #print(y_train)
                    y_train = np_utils.to_categorical(y_train) #converts to binary
                    print(y_train,y_train.shape)
                    #y_test = np_utils.to_categorical(y_test)



                    X = x_train.reshape(x_train.shape[0], self.bands.get(), 1) # new shape 1720x7x1
                    print(X.shape)
                    self.y=np.zeros([self.row.get()*self.col.get(), ], dtype=self.D_type)
                    def Loadcnn():
                        self.window7.destroy()
                        #self.putcnn()
                        def thredd():
                            nn=CNN(self.bands.get(),self.epochs,self.c_c,self.thresh,self.D_type,self.row.get(),self.col.get())
                            print(X.shape,y_train.shape)
                            self.model=nn.cnnfit(self.layer,X,y_train)                           

                            if self.x==1:
                                pixels=self.row.get()*self.col.get()
                                x_test = nn.ReadBilFile(self.img)
                                x_test = x_test.reshape(pixels, self.bands.get(), 1)
                                x_test = x_test / self.mul
                                y_pred = np.zeros([pixels, ], dtype=self.D_type)
                                y_pred=nn.predict2(x_test,self.model)
                                self.y=y_pred
                                y_test_old1=y_pred
                                y_testold1 = np.zeros([pixels], dtype=self.D_type)  

                                mini=0
                                for i in range(0,pixels):
                                    y_1=y_pred[i].tolist()
                                    if ((max(y_1))<=self.thresh):
                                        y_testold1[i]=0
                                    else:
                                        y_testold1[i]=y_1.index(max(y_1))

                                k= np.zeros([self.row.get(),self.col.get()], dtype=self.D_type) 
                                k = y_testold1.reshape(self.row.get(),self.col.get())
                                k.tolist()
                                a,b=np.unique(k,return_counts=True)
                                print(a,b)
                                b=self.height*self.width*b
                                print(b)
                                self.showarea(a,b)
                                plt.imshow(k)
                                plt.colorbar()
                                plt.show()
                                if self.D_type==np.uint16: 
                                            typ='uint16'
                                else:
                                            print('8')
                                            typ='uint8'
                                result = Image.fromarray((k*((self.mul)/(self.c_c+1))).astype(typ))
                                self.putimage(result)
                                
                            
                                    
                            if (self.textweight.get()!=""):
                                print("yes11")
                                isweight="yes"

                                model2 = Sequential() 
                                loc=self.textweight.get().split(".hdf5")
                                file = open(loc[0]+".txt",'r')
                                lines = file.readlines()
                                lines = [x.strip() for x in lines] 
                                print(lines[0])
                                num_classes=int(lines[0])
                                num=num_classes
                                for i in range(1,num_classes):
                                    w4=lines[i].split(",")
                                    print(w4[1])

                                activation_fn="relu"   
                                lenth=len(lines)-num_classes
                                j=3

                                for i in range(num_classes,len(lines)):
                                    print(lines[i])
                                    if(lines[i]=='Conv'):
                                        if i==num_classes:
                                            model2.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same', input_shape=[self.bands.get(), 1]))
                                        else:
                                            model2.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same'))
                                        j=j+1

                                    elif(lines[i]=="Maxpooling"):
                                        model2.add(MaxPooling1D(2))

                                    elif(lines[i]=="LSTM"):
                                        if i==num_classes:
                                            model2.add(LSTM(2**(j),return_sequences=False, input_shape=(self.bands.get() ,1)))
                                        else:
                                            model2.add(LSTM(2**(j),return_sequences=True))
                                        j=j+1



                                model2.add(Flatten())
                                model2.add(Dropout(0.1))
                                model2.add(Dense(256, activation='relu'))
                                model2.add(Dense(128, activation='relu'))
                                model2.add(Dense(num_classes, activation='sigmoid'))
                                #model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
                                #fname='weightsnew_cnn.hdf5'


                                pixels=self.row.get()*self.col.get()
                                model2.load_weights(self.textweight.get())
                                nn=CNN(self.bands.get(),self.epochs,self.c_c,self.thresh,self.D_type,self.row.get(),self.col.get())            
                                x_test = nn.ReadBilFile(self.img)
                                x_test = x_test.reshape(self.row.get()*self.col.get(), self.bands.get(), 1)
                                x_test = x_test / self.mul

                                y_pred2 = np.zeros([self.row.get()*self.col.get(), ], dtype=self.D_type)
                                y_pred2=nn.predict2(x_test,model2)  


                                y_test_old1=y_pred2
                                pixels=self.row.get()*self.col.get()
                                y_testold1 = np.zeros([pixels], dtype=self.D_type)  

                                mini=0
                                for i in range(0,pixels):
                                                y_1=y_pred2[i].tolist()
                                                if ((max(y_1))<=0.1):
                                                    y_testold1[i]=0
                                                else:
                                                    y_testold1[i]=y_1.index(max(y_1))
                                for i in range(0,pixels):
                                                y_1=y_pred[i].tolist()
                                                if y_testold1[i]==0:
                                                    if ((max(y_1))<=0.1):
                                                        y_testold1[i]=0
                                                    else:
                                                        y_testold1[i]=y_1.index(max(y_1))+self.c_c-1

                                k= np.zeros([self.row.get(),self.col.get()], dtype=self.D_type) 
                                k = y_testold1.reshape(self.row.get(),self.col.get()) 
                                k.tolist()
                                a,b=np.unique(k,return_counts=True)
                                print(a,b)
                                b=self.height*self.width*b
                                print(b)
                                self.showarea(a,b)
                                plt.imshow(k)
                                plt.colorbar()
                                plt.show()
                                if self.D_type==np.uint16: 
                                            typ='uint16'
                                else:
                                            print('8')
                                            typ='uint8'
                                result = Image.fromarray(((k*((self.mul)/(self.c_c+1)))).astype(typ))
                                self.putimage(result)  
                                MODEL
                                
                            MsgBox = messagebox.askquestion ('Select an option','Do you want to save the new weights',icon = 'question')
                            if MsgBox=="yes":
                                    self.fileweightsave=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",defaultextension=".hdf5")

                                    print(self.fileweightsave)
                                    loc=self.fileweightsave.split(".hdf5")
                                    file = open(loc[0]+'.txt','w') 
                                    file.write(str(self.c_c)+"\n")
                                    i=1
                                    for address in self.data:
                                        loc=address.split("/")
                                        namee=loc[-1]
                                        file.write(str(i)+","+namee+"\n")
                                        i=i+1

                                    for i in range(len(self.layer)):
                                        file.write(self.layer[i]+"\n")

                                    self.model.save_weights(self.fileweightsave,overwrite=True)
                                    
 
                        thredd()
                    
                    
                    
                    self.window7=tkinter.Toplevel()
                    """whichNN="addLayer"
                    self.window7.protocol("WM_DELETE_WINDOW",self.delete)"""
                    self.window7.geometry("300x500")
                    self.scrollbar1 = Scrollbar(self.window7)
                    self.scrollbar1.pack( side = RIGHT, fill=Y )

                    self.T2 =Listbox(self.window7,yscrollcommand = self.scrollbar1.set)
                    self.l11=Label(self.window7,text="Add Layers sequentially in the Neural Network")
                    self.l11.place(x=5,y=50,width=350)
                    self.l22=Label(self.window7,text="Convolution Layer")
                    self.l22.place(x=20,y=100,width=100)
                    self.l33=Label(self.window7,text="MaxPooling Layer")
                    self.l33.place(x=20,y=150,width=100)
                    self.l34=Label(self.window7,text="LSTM Layer")
                    self.l34.place(x=20,y=200,width=100)

                    self.b22 = ttk.Button(self.window7, text='+', cursor="plus", style='add.TButton' , command=self.addConv)
                    self.b22.place(x=200, y=100, width=25)
                    self.b44 = ttk.Button(self.window7, text='+', cursor="plus", style='add.TButton' , command=self.addPool)
                    self.b44.place(x=200, y=150, width=25)
                    self.b55 = ttk.Button(self.window7, text='+', cursor="plus", style='add.TButton' , command=self.addLSTM)
                    self.b55.place(x=200, y=200, width=25)
                    self.b33 = ttk.Button(self.window7, text='-', cursor="plus", style='remove.TButton' , command=self.delConv)
                    self.b33.place(x=200, y=250, width=25)

                    self.T2.place(x=75,y=350,width=100)
                    self.b66= ttk.Button(self.window7, text='Load', cursor="plus", command=Loadcnn)
                    self.b66.place(x=75, y=300, width=100)
                    self.scrollbar1.config(command = self.T2.yview)

                    
                    

    def addConv(self):
        
                self.layer.append("Conv")
                self.T2.config(state="normal")
                self.T2.delete('0', END)
                for ent in self.layer:
                    self.T2.insert(END, ent+'\n')
                self.T2.config(state="disabled")
                
    def delConv(self):
                
                self.layer=self.layer[:-1]
                self.T2.config(state="normal")
                self.T2.delete('0', END)
                for ent in self.layer:
                    self.T2.insert(END, ent+'\n')
                self.T2.config(state="disabled")
            
    def addPool(self):
                self.layer.append("Maxpooling")
                self.T2.config(state="normal")
                self.T2.delete('0', END)
                for ent in self.layer:
                    self.T2.insert(END, ent+'\n')
                self.T2.config(state="disabled")
                
    def addLSTM(self):
                self.layer.append("LSTM")
                self.T2.config(state="normal")
                self.T2.delete('0', END)
                for ent in self.layer:
                    self.T2.insert(END, ent+'\n')
                self.T2.config(state="disabled")
                

                    
                    
    def classifyCNN(self):
        try:
                l=0
                val1=self.textfile2.get().split("/")
                val2=self.texthdr2.get().split("/")

                if((self.textfile2.get()=="") or (self.texthdr2.get()=="")):
                    messagebox.showerror("Error","Kindly choose both the files")
                elif((val1[-1]+".hdr")!=(val2[-1])):
                    messagebox.showerror("Error","Kindly choose correct hdr file for the image")
                else:
                #print("yes1")
                    self.img = gdal.Open(self.textfile2.get())
                    self.col.set(self.img.RasterXSize)
                    self.row.set(self.img.RasterYSize)
                    self.bands.set(self.img.RasterCount)
                    print(self.bands.get())
                    self.x=0

                    if (self.my_var3.get()==1 and self.my_var4.get()==1):

                        self.data=self.data2[(self.w.get())]
                        self.epochs=int(self.entry33.get())
                        self.thresh=float(self.entry22.get())
                        if (not self.textweight.get().endswith(".hdf5")) and  (self.textweight.get()!=""):
                                messagebox.showerror("Error"," HDF5 File Expected for saved model")
                        else:

                            if len(self.data)==0:
                                        raise KeyError

                            if self.thresh<0: 
                                        l=1
                                        raise ValueError
                            elif self.epochs<=0:
                                        l=2
                                        raise ValueError


                            print(self.data)
                            self.c_c=len(self.data)+1
                            print(self.my_var3.get(),self.my_var4.get())
                            print("yes")
                            self.x=1

                            self.traincnn()
                            
                    elif(self.my_var3.get()==1):
                            self.x=0
                            self.data=self.data2[(self.w.get())]
                            if len(self.data)==0:
                                raise KeyError
                            self.epochs=int(self.entry33.get())
                            self.thresh=float(self.entry22.get())

                            print(self.data)
                            if len(self.data)==0:
                                        raise KeyError

                            if self.thresh<0: 
                                        l=1
                                        raise ValueError
                            elif self.epochs<=0:
                                        l=2
                                        raise ValueError

                            self.c_c=len(self.data)+1
                            print(self.my_var3.get(),self.my_var3.get())
                            self.x=0
                            self.traincnn()

                    elif(self.my_var4.get()==1):
                                print("oh no")
                                model2 = Sequential() 
                                if not self.textweight.get().endswith(".hdf5"):
                                    messagebox.showerror("Error"," HDF5 File Expected for saved model")
                                else:
                                    loc=self.textweight.get().split(".hdf5")
                                    file = open(loc[0]+".txt",'r')
                                    lines = file.readlines()
                                    lines = [x.strip() for x in lines] 
                                    print(lines[0])
                                    num_classes=int(lines[0])
                                    num=num_classes
                                    for i in range(1,num_classes):
                                        w4=lines[i].split(",")
                                        print(w4[1])
                                    pixels=self.row.get()*self.col.get()   
                                    activation_fn="relu"   
                                    lenth=len(lines)-num_classes
                                    j=3
                                    for i in range(num_classes,len(lines)):
                                        if(lines[i]=='Conv'):
                                            if i==num_classes:
                                                model2.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same', input_shape=[self.bands.get(), 1]))
                                            else:
                                                model2.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same'))
                                            j=j+1

                                        elif(lines[i]=="Maxpooling"):
                                            model2.add(MaxPooling1D(2))

                                        elif(lines[i]=="LSTM"):
                                            if i==num_classes:
                                                model2.add(LSTM(2**(j),return_sequences=False, input_shape=(bands ,1)))
                                            else:
                                                model2.add(LSTM(2**(j),return_sequences=True))
                                            j=j+1



                                    model2.add(Flatten())
                                    model2.add(Dropout(0.1))
                                    model2.add(Dense(256, activation='relu'))
                                    model2.add(Dense(128, activation='relu'))
                                    model2.add(Dense(num_classes, activation='sigmoid'))
                                    #model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
                                    #fname='weightsnew_cnn.hdf5'

                                    model2.load_weights(self.textweight.get())
                                    nn=CNN(self.bands.get(),0,0,0,self.D_type,self.row.get(),self.col.get())            
                                    x_test = nn.ReadBilFile(self.img)
                                    x_test = x_test.reshape(self.row.get()*self.col.get(), self.bands.get(), 1)
                                    x_test = x_test / self.mul
                                    y_pred = np.zeros([self.row.get()*self.col.get(), ], dtype=self.D_type)
                                    y_pred=nn.predict2(x_test,model2)

                                    self.printimage(y_pred)
        except KeyError:
            messagebox.showerror("Error","Add dataset/Files first")
        except ValueError:
            if l==0:
                messagebox.showerror("Error","Incorrect Entry ")
            if l==1:
                messagebox.showerror("Error","Threshold must be a positive integer ")
            if l==2:
                messagebox.showerror("Error","Epochs must be a positive integer ")
            

            
            
    
    #----------------------------------------ANN--------------------------------->>>>>>>>>>>>>>

    
class ANN:
    
    def __init__(self, D_type,n_output, n_features,eta,epochs,n_hidden=30,
                 l1=0.0, l2=0.0,alpha=0.0, decrease_const=0.0, shuffle=True,
                 minibatches=1, random_state=None):
        
        print(self, D_type,n_output, n_features,eta,epochs,n_hidden,l1, l2,alpha, decrease_const,shuffle,minibatches, random_state)

        np.random.seed(random_state)
        self.n_output = n_output
        self.n_features = n_features
        self.n_hidden = n_hidden
        self.w1, self.w2 = self._initialize_weights()
        self.l1 = l1
        self.l2 = l2
        self.epochs = epochs
        self.eta = eta
        self.alpha = alpha
        self.decrease_const = decrease_const
        self.shuffle = shuffle
        self.minibatches = minibatches
        self.D_type=D_type
        
    
    def ReadBilFile(self,bil,bands,pixels):
        extract_band=1
        image=np.zeros([pixels,bands], dtype=self.D_type)
        gdal.GetDriverByName('EHdr').Register()
        img = bil
        while bands>=extract_band:
            bandx = img.GetRasterBand(extract_band)
            datax = bandx.ReadAsArray()
            temp=datax
            store=temp.reshape(pixels)
            for i in range(pixels):
                image[i][extract_band-1]=store[i]
            extract_band=extract_band+1
        return image


    
    def _encode_labels(self, y, k):

        onehot = np.zeros((k, y.shape[0]))
        for idx, val in enumerate(y):
            onehot[val, idx] = 1.0

        return onehot

    def _initialize_weights(self):
        """Initialize weights with small random numbers."""
        w1 = np.random.uniform(-1, 1.0,
                               size=self.n_hidden*(self.n_features + 1))
        w1 = w1.reshape(self.n_hidden, self.n_features + 1)
        w2 = np.random.uniform(-1, 1.0,
                               size=self.n_output*(self.n_hidden + 1))
        w2 = w2.reshape(self.n_output, self.n_hidden + 1)
        return w1, w2

    def _sigmoid(self, z):

        return (1.0 / (1.0 + np.exp(-z)))
        #return np.tanh(z)

    def _sigmoid_gradient(self, z):
        sg = self._sigmoid(z)
        return sg * (1.0 - sg)

    def _add_bias_unit(self, X, how='column'):

        if how == 'column':
            X_new = np.ones((X.shape[0], X.shape[1] + 1))
            X_new[:, 1:] = X
        elif how == 'row':
            X_new = np.ones((X.shape[0] + 1, X.shape[1]))
            X_new[1:, :] = X
        else:
            raise AttributeError('`how` must be `column` or `row`')
        return X_new

    def _feedforward(self, X, w1, w2):


        a1 = self._add_bias_unit(X, how='column')
        z2 = w1.dot(a1.T)
        a2 = self._sigmoid(z2)
        a2 = self._add_bias_unit(a2, how='row')
        z3 = w2.dot(a2)
        a3 = self._sigmoid(z3)
        return a1, z2, a2, z3, a3


    def _L2_reg(self, lambda_, w1, w2):
        return (lambda_/2.0) * (np.sum(w1[:, 1:] ** 2) +
                                np.sum(w2[:, 1:] ** 2))

    def _L1_reg(self, lambda_, w1, w2):

        return (lambda_/2.0) * (np.abs(w1[:, 1:]).sum() +
                                np.abs(w2[:, 1:]).sum())

    def _get_cost(self, y_enc, output, w1, w2):
        term1 = -y_enc * (np.log(output))
        term2 = (1.0 - y_enc) * np.log(1.0 - output)
        cost=np.sum(term1-term2)
        self.error=cost/len(output)
        L1_term = self._L1_reg(self.l1, w1, w2)
        L2_term = self._L2_reg(self.l2, w1, w2)
        cost = cost + L1_term + L2_term
        return cost

    def _get_gradient(self, a1, a2, a3, z2, y_enc, w1, w2):    
        # backpropagation
        sigma3 = a3 - y_enc
        z2 = self._add_bias_unit(z2, how='row')
        sigma2 = w2.T.dot(sigma3) * self._sigmoid_gradient(z2)
        sigma2 = sigma2[1:, :]
        grad1 = sigma2.dot(a1)
        grad2 = sigma3.dot(a2.T)
        grad1[:, 1:] += self.l2 * w1[:, 1:]
        grad1[:, 1:] += self.l1 * np.sign(w1[:, 1:])
        grad2[:, 1:] += self.l2 * w2[:, 1:]
        grad2[:, 1:] += self.l1 * np.sign(w2[:, 1:])

        return grad1, grad2

    def predict(self, X,w1,w2):
    
        if len(X.shape) != 2:
            raise AttributeError('X must be a [n_samples, n_features] array.\n'
                                 'Use X[:,None] for 1-feature classification,'
                                 '\nor X[[i]] for 1-sample classification')

        a1, z2, a2, z3, a3 = self._feedforward(X, w1, w2)

        z3=(1.0 / (1.0 + np.exp(-z3)))
        y_pred = np.zeros([z3.shape[1]], dtype=self.D_type) 
        
        for i in range(0,z3.shape[1]):
            y_1=z3[:,i].tolist()
            y_pred[i]=y_1.index(max(y_1))

        return y_pred
    
    def predict2(self, X):
    
        if len(X.shape) != 2:
            raise AttributeError('X must be a [n_samples, n_features] array.\n'
                                 'Use X[:,None] for 1-feature classification,'
                                 '\nor X[[i]] for 1-sample classification')

        a1, z2, a2, z3, a3 = self._feedforward(X, self.w1, self.
                                               w2)

        z3=(1.0 / (1.0 + np.exp(-z3)))
        y_pred = np.zeros([z3.shape[1]], dtype=self.D_type) 
        
        for i in range(0,z3.shape[1]):
            y_1=z3[:,i].tolist()
            y_pred[i]=y_1.index(max(y_1))

        return y_pred

    def fit(self, X, y, print_progress=False):
        self.cost_ = []
        X_data, y_data = X.copy(), y.copy()
        """print("heyy")
        print(y_data)"""
        y_enc = self._encode_labels(y, self.n_output)
        #print 'test data'
        #print y_enc.shape
        delta_w1_prev = np.zeros(self.w1.shape)
        delta_w2_prev = np.zeros(self.w2.shape)

        #global tell
        self.error=0
        self.acc=0
        for i in range(self.epochs):

            self.eta /= (1 + self.decrease_const*i)
            #print(self.eta)

            

            if self.shuffle:
                #print(y_data.shape[0])
                idx = np.random.permutation(y_data.shape[0]) #make a copy and shuffle elements
                X_data, y_enc = X_data[idx], y_enc[:, idx]
   
            mini = np.array_split(range(y_data.shape[0]), self.minibatches)
            for idx in mini:
                # feedforward
                a1, z2, a2, z3, a3 = self._feedforward(X_data[idx],
                                                       self.w1,
                                                       self.w2)
                j=0
                z4=(1.0 / (1.0 + np.exp(-z3)))
                for k in range(0,z4.shape[1]):
                    y_1=z4[:,k].tolist()
                    if max(y_1)>0.8:
                        j=j+1
                self.acc=(j/z4.shape[1])*100
                #print(self.acc)
                cost = self._get_cost(y_enc=y_enc[:, idx],
                                      output=a3,
                                      w1=self.w1,
                                      w2=self.w2)
                self.cost_.append(cost)
                # compute gradient via backpropagation
                grad1, grad2 = self._get_gradient(a1=a1, a2=a2,
                                                  a3=a3, z2=z2,
                                                  y_enc=y_enc[:, idx],
                                                  w1=self.w1,
                                                  w2=self.w2)

                delta_w1, delta_w2 = self.eta * grad1, self.eta * grad2
                self.w1 -= (delta_w1 + (self.alpha * delta_w1_prev))
                self.w2 -= (delta_w2 + (self.alpha * delta_w2_prev))
                delta_w1_prev, delta_w2_prev = delta_w1, delta_w2 
                
            if print_progress:
                sys.stderr.write('\rEpoch: %d/%d' % (i+1, self.epochs))
                obj.puthistorytext("Epoch======================> "+str(i+1)+"/"+str(self.epochs)+"   "+"acc:"+str(self.acc)+"%    loss:"+str(self.error))
                sys.stderr.flush()

        return self.w1,self.w2


 
    
    #----------------------------------------CNN--------------------------------->>>>>>>>>>>>>>
    
    
    
class CNN:

    def __init__(self,bands,train_cycle,c_c,thresh,D_type,row,col):
            

            self.bands=bands
            self.row=row
            self.col=col
            self.pixels=row*col
            self.train_cycle=train_cycle
            self.c_c=c_c
            self.thresh=thresh
            self.D_type=D_type 
            print(self.pixels)
            
    def cnnfit(self,data,X,y_train):
                activation_fn='relu'
                print(self.c_c)
                model = Sequential()
                j=3
                for i in range(0,len(data)):
                    print(data[i])
                    if data[i]=="Conv":
                        if(i==0):
                            print("yes",self.bands)
                            model.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same', input_shape=[self.bands, 1]))
                        else:
                            model.add(Conv1D(2 ** j, 2, activation=activation_fn, padding='same'))
                        j=j+1
                    elif data[i]=="Maxpooling":
                        model.add(MaxPooling1D(2))
                        
                    elif data[i]=="LSTM":
                        if(i==0):
                            model.add(LSTM(2**j,return_sequences=False, input_shape=(bands ,1)))
                        else:
                            model.add(LSTM(2**j,return_sequences=True))
                        j=j+1
                          
                model.add(Flatten())
                model.add(Dropout(0.1))
                model.add(Dense(256, activation='relu'))
                model.add(Dense(128, activation='relu'))
                model.add(Dense(self.c_c, activation='sigmoid'))
                model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

                obj.puthistorytext("PLEASE WAIT...")
                print(y_train)
                history=model.fit(X, y_train, batch_size=50, epochs=self.train_cycle)
                
                #print(history.history['acc'])
                for i in range(0,len(history.history["acc"])):
                    obj.puthistorytext("Epoch======================> "+str(i+1)+"/"+str(self.train_cycle)+"   "+"acc:"+str(history.history["acc"][i])+"   loss:"+str(history.history["loss"][i]))
                    
                model.summary()
                
                return model
                                                                                                                                                    
    def ReadBilFile(self,bil):
                extract_band = 1
                image = np.zeros([self.pixels, self.bands], dtype=self.D_type)
                gdal.GetDriverByName('EHdr').Register()
                img=bil
                while self.bands>= extract_band:
                    bandx = img.GetRasterBand(extract_band)
                    datax = bandx.ReadAsArray()
                    temp = datax
                    store = temp.reshape(self.pixels) # reshape(pixels,1)
                    for i in range(self.pixels):
                        image[i][extract_band-1] = store[i]
                    extract_band = extract_band + 1
                return image
            
                                                                        
    def predict(self,x_test):
                
                y_test_old = np.zeros([self.pixels, ], dtype=self.D_type)
                y_test_old= model.predict(x_test, batch_size=50)
                return y_test_old
                                                                           
    def predict2(self,x_test,model1):
                
                y_test_old = np.zeros([self.pixels, ], dtype=self.D_type)
                y_test_old= model1.predict(x_test, batch_size=50)
                
                return y_test_old                                                                        

            
if __name__ == '__main__':
    root = Tk()
    obj = NEURAL(root)
    root.mainloop()


# In[6]:


th=threading.Thread(target=timeThread)
th.start()


# In[14]:


import numpy as np
import sys
import os

def main(file):
    if file.endswith('.hdr'):
        f= open(file,"r")
    else:
        return None
    i=1
    for line in f.readlines():
        line = str(line.lower())
        line = line.strip().lower()
        if i==11:
            loc=line.split(":")
            try:
                width=float(loc[1].strip())
            except:
                width=0
        if i==12:
            loc=line.split(":")
            try:
                height=float(loc[1].strip())
            except:
                height=0
        if i==13:
            loc=line.split(":")
            unit=loc[1].strip()
            break
        if str(line) == "datatype: u16" or (str(line) == "datatype: s16"):
            D_type=np.uint16
            
        if str(line) == "datatype: u8":
            D_type=np.uint8
        i=i+1
    return D_type,width,height,unit


main("C:\\Users\Acer\Desktop\major poject\\washdc30bands.hdr")

