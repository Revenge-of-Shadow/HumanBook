import tkinter as tk
from tkinter import ttk
import json


class Entry:
    def __init__(self, name, surname, telephone, city, street):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.city = city
        self.street = street



def obj_dict(obj):
    return obj.__dict__

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)


json_filename = "entries.json"
entries = []



def entries_contains(e):
    for i in entries:
        if(i.name == e.name and i.surname == e.surname):
           return True
    return False



def write_to_json():
    with open(json_filename, "w") as file:
            json.dump(entries, file, default=obj_dict)



# Following function initiates a window to add records.
def add_action():
    w_add = tk.Toplevel()
    w_add.geometry("800x100")
    sv_na = tk.StringVar()
    sv_su = tk.StringVar()
    sv_nu = tk.StringVar()
    sv_ci = tk.StringVar()
    sv_st = tk.StringVar()

    def addition():
        ## Checking for a duplicate
        person = Entry(sv_na.get(), sv_su.get(), sv_nu.get(), sv_ci.get(), sv_st.get())
        if(entries_contains(person)): 
            w_err = tk.Toplevel()
            l_err = create_widget(w_err, tk.Label, text = "A person with these name and surmane already exists.", font = "20")
            l_err.pack()
            w_err.title("Error.")
            w_err.mainloop()
        else:
            ## Updating the table
            entries.append(person) 
            ## Writing to a file.
            write_to_json() 
            ## Visual update
            search()
            ## Closing the dialog window
            w_add.destroy()

    ## Elements
    f_table = create_widget(w_add, tk.Frame, width = 500)

    l_na= create_widget(f_table, tk.Label, text = "Name", font = "20")
    l_su= create_widget(f_table, tk.Label, text = "Surname", font = "20")
    l_nu= create_widget(f_table, tk.Label, text = "Number", font = "20")
    l_ci= create_widget(f_table, tk.Label, text = "City", font = "20")
    l_st= create_widget(f_table, tk.Label, text = "Street", font = "20")
    l_na.grid(row = 0, column = 0) 
    l_su.grid(row = 0, column = 1)
    l_nu.grid(row = 0, column = 2)
    l_ci.grid(row = 0, column = 3)
    l_st.grid(row = 0, column = 4)
    e_na = create_widget(f_table, tk.Entry, textvariable = sv_na)
    e_su = create_widget(f_table, tk.Entry, textvariable = sv_su)
    e_nu = create_widget(f_table, tk.Entry, textvariable = sv_nu)
    e_ci = create_widget(f_table, tk.Entry, textvariable = sv_ci)
    e_st = create_widget(f_table, tk.Entry, textvariable = sv_st)
    e_na.grid(row = 1, column = 0) 
    e_su.grid(row = 1, column = 1)
    e_nu.grid(row = 1, column = 2)
    e_ci.grid(row = 1, column = 3)
    e_st.grid(row = 1, column = 4)
    b_ad = create_widget(f_table, tk.Button, text = "Add", font = "20", command = addition)
    b_ad.grid(row = 2, column = 0, columnspan = 5, sticky = tk.W+tk.E)

    f_table.pack(expand = True)
    ## Elements end

    w_add.title("")
    w_add.mainloop()



def del_entry(index):
    del entries[index]
    write_to_json()
    update_list()

def update_list(search_by="", search_word=""):
 
    for child in mylist.winfo_children():
        child.destroy()

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

    try:
        with open(json_filename, "r") as file:
            lst = json.load(file)

            del entries[:]
            for i in lst:
                e = Entry(i['name'], i['surname'], i['telephone'], i['city'], i['street'])
                entries.append(e)

    except FileNotFoundError:
        #  Does not matter, list can be empty.
        pass

    finally:

        iteration = 1
        for e in entries:
            #   Skip the entry if it does not contain the data.
            if(
                search_word == "" or
                (search_by == "name" and search_word in e.name) or
                (search_by == "surname" and search_word in e.surname) or
                (search_by == "telephone" and search_word in e.telephone) or
                (search_by == "city" and search_word in e.city) or
                (search_by == "street" and search_word in e.street)
                ):
               
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
                

                b_del = create_widget(mylist, tk.Button, text = "Delete", font = "20" )
                b_del.bind("<Button>", lambda event, iteration=iteration:del_entry(iteration-1))
                b_del.grid(row = iteration, column = 5)

                iteration+=1
        l_found = create_widget(mylist, tk.Label, text = f"Found: {iteration-1}", font = "20", bg = "white")
        l_found.grid(row = iteration, column = 0, columnspan = 5, sticky = tk.W+tk.E)



# Window initialization
root = create_widget(None, tk.Tk)
root.geometry('600x400')
root.title("")

#Window objects
## Search block
frame = create_widget(root, tk.Frame, width = 580)


search_var = tk.StringVar()

def search(*args):
    update_list(combo_var.get(), search_var.get())

e_search = create_widget(frame, tk.Entry, textvariable=search_var, width = 40)
e_search.pack(side = tk.LEFT)

b_search = create_widget(frame, tk.Button, text = "Search", font = "20", command = search)
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

b_add = create_widget(root, tk.Button, text = "Add", width = 580, command = add_action)
b_add.pack()

canvas = create_widget(root, tk.Canvas)

scroll_bar = create_widget(root, tk.Scrollbar, command = canvas.yview)
canvas.configure(yscrollcommand=scroll_bar.set)

scroll_bar.pack(side=tk.RIGHT, fill = tk.Y)

## Initiate the entry table
mylist = create_widget(canvas, tk.Frame, width = 580)
canvas.create_window((0,0), window = mylist, anchor = 'nw')
### Add entries to the table
search()
mylist.update_idletasks()   
canvas.configure(scrollregion=canvas.bbox('all'))
canvas.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)

## Entry table end

root.mainloop()
