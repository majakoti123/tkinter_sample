# tk13.pyw

import tkinter as tk
root = tk.Tk()
root.geometry('300x200')
lb = tk.Label(text='This is a Label. This is a Label. This ia a Label.')
ms = tk.Message(text='This is a Message. This ia a Message. This ia a Message.')
[widget.pack() for widget in (lb,ms)]
root.mainloop()
