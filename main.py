import tkinter as tk


class Entry:
    def __init__(self, name, surname, telephone, city, street):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.city = city
        self.street = street

    def getStr(self):
        return self.name+"  |  "+self.surname+"  |  "+self.telephone+"  |  "+self.city+"  |  "+self.street

search_var = ""
def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)


def search():
    print(search_var)


root = create_widget(None, tk.Tk)
root.geometry('600x400')
root.title("")

frame = create_widget(root, tk.Frame, width = 580)

e_search = create_widget(frame, tk.Entry,textvariable=search_var)
e_search.pack(side = tk.LEFT)

l_search = create_widget(frame, tk.Button, text = "Search", command = search)
l_search.pack(side = tk.LEFT)

frame.pack()

b_add = create_widget(root, tk.Button, text = "Add", width = 580)
b_add.pack()

scroll_bar = create_widget(root, tk.Scrollbar)
scroll_bar.pack(side=tk.RIGHT, fill = tk.Y)

mylist = create_widget(root, tk.Listbox, yscrollcommand=scroll_bar.set, width = 580, bg="lightgrey", font = "20")

one = Entry("A", "B", "1", "C", "D")
mylist.insert(tk.END, one.getStr()) 


mylist.pack(side = tk.LEFT, fill = tk.BOTH)

scroll_bar.config(command = mylist.yview)

root.mainloop()
