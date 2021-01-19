#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:22:58 2020

@author: vikrant
"""
import numpy as np

import joblib
cllg_prediction = joblib.load('college_prediction_linear_reg.pkl')

import tkinter as tk
from tkinter import *
from tkinter.ttk import *


window = tk.Tk()
window.title('College Acceptance Rate')
window.geometry('500x500')

lbl1 = tk.Label(window, text = 'Enter GRE Score')
lbl1.grid(row = 1, column = 0)

gre = tk.Entry(window, width = 10)
gre.grid(row = 1, column = 1 )
gre.focus()

lbl2 = tk.Label(window, text = 'Enter TOEFL Score')
lbl2.grid(row = 2, column = 0)
         
toefl = tk.Entry(window, width = 10)
toefl.grid(row = 2, column = 1 )

lbl3 = tk.Label(window, text = 'Your University Rating')
lbl3.grid(row = 3, column = 0)

combo = Combobox(window, width = 10)
combo['values']= (1, 2, 3, 4, 5)
combo.grid(row = 3, column=1)

lbl4 = tk.Label(window, text = 'SOP')
lbl4.grid(row = 4, column = 0)

combo1 = Combobox(window, width = 10)
combo1['values']= (0, 0,5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
combo1.grid(row = 4, column=1)

lbl5 = tk.Label(window, text = 'LOR')
lbl5.grid(row = 5, column = 0)

combo2 = Combobox(window, width = 10)
combo2['values']= (0, 0,5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
combo2.grid(row = 5, column=1)

lbl6 = tk.Label(window, text = 'Enter CGPA')
lbl6 .grid(row = 6, column = 0)
         
cgpa = tk.Entry(window, width = 10)
cgpa.grid(row = 6, column = 1 )

lbl7 = tk.Label(window, text = 'Research Paper Published')
lbl7 .grid(row = 7, column = 0)

chk_state = IntVar()
chk1 = Radiobutton(window, text='Yes', value = 1, variable = chk_state)
chk1.grid(row=7, column = 1)

chk2 = Radiobutton(window, text='No', value = 0, variable = chk_state)
chk2.grid(row=7, column = 2)

# C = tk.Canvas(window, bg="blue", height=250, width=300)
# filename = tk.PhotoImage(file = "/home/vikrant/Downloads/Photos/UCLA_logo.png")
# background_label = tk.Label(window, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# #C.pack()

def clicked():
    input_arr = np.empty(7, dtype = np.float32)
    # i_gre = gre.get()
    # i_toefl = toefl.get()
    # i_uni_rating = combo.get()
    # i_sop = combo1.get()
    # i_lor = combo2.get()
    # i_cgpa = cgpa.get()
    # i_research = chk_state
    input_arr[0] = gre.get() 
    input_arr[1] = toefl.get()
    input_arr[2] = combo.get()
    input_arr[3] = combo1.get() 
    input_arr[4] = combo2.get()
    input_arr[5] = cgpa.get()
    input_arr[6] = chk_state.get()
    
    #inp = np.asarray(input_arr, dtype = np.float32)
    inp = input_arr.reshape(1, -1)
    ans = cllg_prediction.predict(inp)
    result(ans)

def result(ans):
   tk.messagebox.showinfo("Predicted college acceptance rate:", ans)

submit = tk.Button(window, text = 'Get your prediction!',  command = clicked)
submit.grid(row = 8, column = 1)#,)


window.mainloop()
