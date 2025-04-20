from tkinter import *

root = Tk()
root.geometry('600x400')
root.title("")

a = Label(root, text = "Text.")
a.pack()

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand=scroll_bar.set, width = 580, bg="grey")

for line in range (1, 4):
    mylist.insert(END, str(line))

mylist.pack(side = LEFT, fill = BOTH)

scroll_bar.config(command = mylist.yview)

root.mainloop()
