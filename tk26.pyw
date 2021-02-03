#p16 tk26.pyw

import tkinter as tk
def get_selpoint():
    sel_start = txt.index('sel.first')
    sel_end = txt.index('sel.last')
    print(txt.get(sel_start, sel_end))

root = tk.Tk()
txt = tk.Text(width=30, height=5)
bt = tk.Button(text='print selected area',command=get_selpoint)
[wiget.pack() for wiget in (txt,bt)]

root.mainloop()