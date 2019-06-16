#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani


import sys
from Bio import SeqIO
import csv
import gzip

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from tkinter import filedialog

from tkinter import *
from tkinter import messagebox

import FastaSearch_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    FastaSearch_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    FastaSearch_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def getFastaFile(self):
        self.fastafilename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.*"),("all files","*.*")))
        self.fastaFilePathLab.config(text=self.fastafilename)
        print(self.fastafilename)

    def getidFile(self):
        self.idfilename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.*"),("all files","*.*")))
        self.idFilePathLab.configure(text=self.idfilename)
        print(self.fastafilename)
    
    def searchReads(self):
        if len(self.fastafilename)<1:
            messagebox.showinfo("Alert", "Please Select a Fasta file")
            return
        id_list=[]
         
        if len(self.idfilename)>0:
            with open(self.idfilename, 'r') as f:
                reader=f.read()
                id_list = reader.split(',')

        #with open(self.idfilename, 'r') as f:
            #reader = csv.reader(f)
            #id_list = list(reader)
        text_ids=self.idText.get("1.0",END)
        if len(text_ids)<1 and len(self.idfilename)<1:
            messagebox.showinfo("Alert","Please enter sequence ids or select Id file")
            return
        print(text_ids)
        text_ids=text_ids.rstrip("\n")
        id_list1=text_ids.split(',')
        for ids in id_list1:
            id_list.append(ids)
        #id_list.append(id_list1)
        print(id_list)
        matched_reads=""
        
        if self.fastafilename.lower().endswith(('.fa', '.fasta', '.txt')):
            
            for id in id_list:
                for record in SeqIO.parse(self.fastafilename,"fasta"):
                    if id==record.id:
                        matched_reads=matched_reads+'>'+str(record.id)+'\n'+str(record.seq)+'\n'
                        print("i")
                        break
            print(matched_reads)
        else:
            
            for id in id_list:
                with gzip.open(self.fastafilename, "rt") as handle:
                    for record in SeqIO.parse(handle,"fasta"):
                        if id==record.id:
                            matched_reads=matched_reads+'>'+str(record.id)+'\n'+str(record.seq)+'\n'
                            print("i")
                            break
            print(matched_reads)
            
                
        
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save =str(matched_reads)
        fout.write(text2save)
        fout.close()




        



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.fastafilename=""
        self.idfilename=""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Semilight} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+295+130")
        top.resizable(False, False)
        top.title("Bulk Fasta Search by Suheel Yousuf Wani")
        top.configure(background="#33FFBD")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.233, rely=0.0, height=41, width=284)
        self.Label1.configure(background="#33FFBD")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Bulk Fasta Search''')
        self.Label1.configure(width=284)

        self.fastaFileBt = tk.Button(top)
        self.fastaFileBt.place(relx=0.35, rely=0.156, height=34, width=147)
        self.fastaFileBt.configure(activebackground="#ececec")
        self.fastaFileBt.configure(activeforeground="#000000")
        self.fastaFileBt.configure(background="#33FFBD")
        self.fastaFileBt.configure(borderwidth="6")
        self.fastaFileBt.configure(disabledforeground="#a3a3a3")
        self.fastaFileBt.configure(font=font11)
        self.fastaFileBt.configure(foreground="#000000")
        self.fastaFileBt.configure(highlightbackground="#d9d9d9")
        self.fastaFileBt.configure(highlightcolor="black")
        self.fastaFileBt.configure(pady="0")
        self.fastaFileBt.configure(text='''Browse Fastsa File.....''')
        self.fastaFileBt.configure(width=147)
        self.fastaFileBt.configure(command=self.getFastaFile)

        self.fastaFilePathLab = tk.Label(top)
        self.fastaFilePathLab.place(relx=0.617, rely=0.178, height=21, width=174)

        self.fastaFilePathLab.configure(background="#33FFBD")
        self.fastaFilePathLab.configure(disabledforeground="#a3a3a3")
        self.fastaFilePathLab.configure(foreground="#000000")
        self.fastaFilePathLab.configure(width=174)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.017, rely=0.4, height=39, width=226)
        self.TLabel1.configure(background="#33FFBD")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font12)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Enter the ID's seperated by commas(,)''')
        self.TLabel1.configure(width=226)

        self.idText = tk.Text(top)
        self.idText.place(relx=0.417, rely=0.289, relheight=0.342
                , relwidth=0.557)
        self.idText.configure(background="white")
        self.idText.configure(font="TkTextFont")
        self.idText.configure(foreground="black")
        self.idText.configure(highlightbackground="#d9d9d9")
        self.idText.configure(highlightcolor="black")
        self.idText.configure(insertbackground="black")
        self.idText.configure(selectbackground="#c4c4c4")
        self.idText.configure(selectforeground="black")
        self.idText.configure(width=334)
        self.idText.configure(wrap="word")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.283, rely=0.667, height=31, width=64)
        self.Label3.configure(background="#33FFBD")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(justify='right')
        self.Label3.configure(text='''Or''')
        self.Label3.configure(width=64)

        self.idFileBt = tk.Button(top)
        self.idFileBt.place(relx=0.417, rely=0.667, height=34, width=127)
        self.idFileBt.configure(activebackground="#ececec")
        self.idFileBt.configure(activeforeground="#000000")
        self.idFileBt.configure(background="#33FFBD")
        self.idFileBt.configure(disabledforeground="#a3a3a3")
        self.idFileBt.configure(font=font11)
        self.idFileBt.configure(foreground="#000000")
        self.idFileBt.configure(highlightbackground="#d9d9d9")
        self.idFileBt.configure(highlightcolor="black")
        self.idFileBt.configure(pady="0")
        self.idFileBt.configure(text='''Browse ID's File....''')
        self.idFileBt.configure(width=127)
        self.idFileBt.configure(command=self.getidFile)

        self.idFilePathLab = tk.Label(top)
        self.idFilePathLab.place(relx=0.65, rely=0.667, height=31, width=184)
        self.idFilePathLab.configure(background="#33FFBD")
        self.idFilePathLab.configure(disabledforeground="#a3a3a3")
        self.idFilePathLab.configure(foreground="#000000")
        self.idFilePathLab.configure(width=184)

        self.searchBt = tk.Button(top)
        self.searchBt.place(relx=0.383, rely=0.822, height=54, width=157)
        self.searchBt.configure(activebackground="#ececec")
        self.searchBt.configure(activeforeground="#000000")
        self.searchBt.configure(background="#33FFBD")
        self.searchBt.configure(borderwidth="8")
        self.searchBt.configure(disabledforeground="#a3a3a3")
        self.searchBt.configure(font=font14)
        self.searchBt.configure(foreground="#000000")
        self.searchBt.configure(highlightbackground="#d9d9d9")
        self.searchBt.configure(highlightcolor="black")
        self.searchBt.configure(highlightthickness="2")
        self.searchBt.configure(pady="0")
        self.searchBt.configure(text='''Search''')
        self.searchBt.configure(width=157)
        self.searchBt.configure(command=self.searchReads)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





