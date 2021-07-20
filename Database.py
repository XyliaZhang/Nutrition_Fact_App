# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:49:04 2021

@author: Xylia.Zhang
"""

#insert_new_data

import tkinter as tk
import pandas as pd
from tkinter import *
window = tk.Tk()

window.title('Insert Data')

window.geometry('500x380')

tk.Label(window, text='Good morning Lulu ^__^',  font=('Arial', 14), width=30, height=2).pack()

frame = tk.Frame(window)
frame.pack()

frame_l = tk.Frame(frame)
frame_m = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')


tk.Label(frame_l, text='料號',  font=('Arial', 12)).pack()
tk.Label(frame_l, text='名稱',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='碳水%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='糖%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='蛋白%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='脂質%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='飽和脂肪%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='反式脂肪%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='鈉%',  font=('Arial', 10)).pack()
tk.Label(frame_l, text='其他%',  font=('Arial', 10)).pack()
e1 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e2 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e3 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e4 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e5 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e6 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e7 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e8 = tk.Entry(frame_r, show=None, font=('Arial', 11))
e9 = tk.Entry(frame_r, show=None, font=('Arial', 11))
t = tk.Entry(frame_r, show=None, width=30)
e1.pack()
e2.pack()
e3.pack()
e4.pack()
e5.pack()
e6.pack()
e7.pack()
e8.pack()
e9.pack()
t.pack()
tk.Label(window, text='(ps.其他營養素請用>分隔,並以ex: vitA>0.001>vitB>30....寫法表示)',  font=('Arial', 10)).pack()

on_hit = False
def insert_done():
    global on_hit
#    if on_hit == False:
    on_hit = True
    data = (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),t.get())
    data_csv = ",".join(data)
    with open("./DATA_raw.csv","a",encoding="utf-8") as f:
        f.write(data_csv)
        f.write("\n")
              
    try:
        df = pd.read_csv("./DATA.csv",encoding="utf-8",index_col="id")
        df.drop(str(e1.get()),inplace=True) 
        df.to_csv("./DATA.csv",encoding="utf-8")
        with open("./DATA.csv","a",encoding="utf-8") as f:
            f.write(data_csv)
            f.write("\n")
        var.set('Reset [ ID={} ] is Done! '.format(e1.get()))
    except:
        with open("./DATA.csv","a",encoding="utf-8") as f:
            f.write(data_csv)
            f.write("\n")
        
        var.set('Insert [ ID={} ] is Done! '.format(e1.get()))
    e1.delete(0,END)  
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    t.delete(0,END)
#    else:
#        on_hit = False
#        var.set('Press one more time!')

b = tk.Button(window, text='insert', font=('Arial', 12), width=10, height=1, command=insert_done)
b.pack()

var = tk.StringVar() 
l = tk.Label(window, textvariable=var,   font=('Arial', 14), width=30, height=2)
l.pack()


window.mainloop()