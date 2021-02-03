 # tk16.pyw

import tkinter as tk

def btn_press():
     print('Buton was pressed')

root = tk.Tk()
root.geometry('150x80')
bt = tk.Buton(text='Buton', command=btn_press)
bt.pack()
root.mainloop()