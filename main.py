from tkinter import *


class Entry:
    def __init__(self, name, surname, telephone, city, street):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.city = city
        self.street = street

    def getStr(self):
        return self.name+" | "+self.surname+" | "+self.telephone+" | "+self.city+" | "+self.street



root = Tk()
root.geometry('600x400')
root.title("")


a = Label(root, text = "Text.")
a.pack()

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand=scroll_bar.set, width = 580, bg="lightgrey")

one = Entry("A", "B", "1", "C", "D")
mylist.insert(END, one.getStr()) 


mylist.pack(side = LEFT, fill = BOTH)

scroll_bar.config(command = mylist.yview)

root.mainloop()
