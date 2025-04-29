import tkinter as tk
from tkinter import ttk


class Entry:
    def __init__(self, name, surname, telephone, city, street):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.city = city
        self.street = street

    def getStr(self):
        return self.name+"  |  "+self.surname+"  |  "+self.telephone+"  |  "+self.city+"  |  "+self.street


def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)



entries = [
    Entry("A", "B", "1", "C", "D"),
    Entry("Andrew", "Bohan", "141351234", "Detroit", "Piquette avenue")
]


# Window initialization
root = create_widget(None, tk.Tk)
root.geometry('600x400')
root.title("")

#Window objects
## Search block
frame = create_widget(root, tk.Frame, width = 580)


search_var = tk.StringVar()

def search(*args):
    print(search_var.get())

e_search = create_widget(frame, tk.Entry, textvariable=search_var, width = 40)
e_search.pack(side = tk.LEFT)

b_search = create_widget(frame, tk.Button, text = "Search", command = search)
b_search.pack(side = tk.LEFT)

l_by = create_widget(frame, tk.Label, text = "by:", font = "20")
l_by.pack(side = tk.LEFT)

combo_var = tk.StringVar()
cb_search = create_widget(frame, ttk.Combobox, textvariable = combo_var, width = 40)
cb_search['values'] = ("name", "surname", "telephone", "city", "street")
cb_search.current(0)
cb_search.pack(side = tk.LEFT, expand = True)

frame.pack()
## Search block end

b_add = create_widget(root, tk.Button, text = "Add", width = 580)
b_add.pack()

scroll_bar = create_widget(root, tk.Scrollbar)
scroll_bar.pack(side=tk.RIGHT, fill = tk.Y)

#mylist = create_widget(root, tk.Listbox, yscrollcommand=scroll_bar.set, width = 580, bg="lightgrey", font = "20")

#one = Entry("A", "B", "1", "C", "D")
#mylist.insert(tk.END, one.getStr()) 

mylist = create_widget(root, tk.Frame, width = 580)
 
l_na= create_widget(mylist, tk.Label, text = "Name", font = "20")
l_su= create_widget(mylist, tk.Label, text = "Surname", font = "20")
l_nu= create_widget(mylist, tk.Label, text = "Number", font = "20")
l_ci= create_widget(mylist, tk.Label, text = "City", font = "20")
l_st= create_widget(mylist, tk.Label, text = "Street", font = "20")
l_na.grid(row = 0, column = 0) 
l_su.grid(row = 0, column = 1)
l_nu.grid(row = 0, column = 2)
l_ci.grid(row = 0, column = 3)
l_st.grid(row = 0, column = 4)


iteration = 1
for e in entries:
    l_name = create_widget(mylist, tk.Label, text = e.name, font = "20")
    l_surname = create_widget(mylist, tk.Label, text = e.surname, font = "20")
    l_number = create_widget(mylist, tk.Label, text = e.telephone, font = "20")
    l_city= create_widget(mylist, tk.Label, text = e.city, font = "20")
    l_street= create_widget(mylist, tk.Label, text = e.street, font = "20")
    l_name.grid(row = iteration, column = 0) 
    l_surname.grid(row = iteration, column = 1)
    l_number.grid(row = iteration, column = 2)
    l_city.grid(row = iteration, column = 3)
    l_street.grid(row = iteration, column = 4)
    iteration+=1

#mylist.pack(side = tk.LEFT, fill = tk.BOTH)
mylist.pack()

#scroll_bar.config(command = mylist.yview)

root.mainloop()
