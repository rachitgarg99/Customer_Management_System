from tkinter import *
from tkinter import messagebox

# import CMS_OOPS_Project
from CMSBLL_SQL import *


def btnAdd_Click():
    cus = Customer()
    cus.id = varId.get()
    cus.name = varName.get()
    cus.age = varAge.get()
    ans = cus.addCustomer()
    varId.set("")
    varAge.set("")
    varName.set("")
    if ans == "done":
        messagebox.showinfo("CMS", "Customer Added Successfully")
    else:
        messagebox.showinfo("CMS", ans)


def btnSearch_Click():
    cus = Customer()
    cus.id = varId.get()
    ans = cus.searchCustomer()
    # varAge.set(cus.age)
    # varName.set(cus.name)
    if ans != "Not Found":
        messagebox.showinfo("CMS", ans)
    else:
        messagebox.showinfo("CMS", ans)


def btnDelete_Click():
    cus = Customer()
    cus.id = varId.get()
    ans=cus.deleteCustomer()
    varId.set("")
    if ans == "done":
        messagebox.showinfo("CMS", "Customer Deleted Successfully")
    else:
        messagebox.showinfo("CMS", ans)
    # messagebox.showinfo("CMS", "Customer Deleted Successfully")


def btnModify_Click():
    cus = Customer()
    cus.id = varId.get()
    cus.name = varName.get()
    cus.age = varAge.get()
    ans = cus.modifyCustomer()
    varId.set("")
    varAge.set("")
    varName.set("")
    if ans == "done":
        messagebox.showinfo("CMS", "Customer Modified Successfully")
    else:
        messagebox.showinfo("CMS", ans)


def btnAll_Click():
    cus=Customer()
    root1 = Tk()
    lblId1 = Label(root1, text="CUST ID", bg="orange", font=1, width=20)
    lblId1.grid(row=0, column=0)
    lblName1 = Label(root1, text="CUST AGE", bg="orange", font=1, width=20)
    lblName1.grid(row=0, column=1)
    lblAge1 = Label(root1, text="CUST NAME", bg="orange", font=1, width=20)
    lblAge1.grid(row=0, column=2)
    i = 1
    for e in cus.displayCustomer():
        lblId2 = Label(root1, text=f"{e[0]}", bg="yellow", font=1, width=20)
        lblId2.grid(row=i, column=0)
        lblName2 = Label(root1, text=f"{e[1]}", bg="yellow", font=1, width=20)
        lblName2.grid(row=i, column=1)
        lblAge2 = Label(root1, text=f"{e[2]}", bg="yellow", font=1, width=20)
        lblAge2.grid(row=i, column=2)
        i += 1




root = Tk()
root.geometry("380x200")
#root.config(height=500, width=500)
# can = Canvas(root, bg = 'red', height=100, width=100)
# can.place(x=200, y=200, anchor=NW)

lblId = Label(root, text="Enter Cust ID:", font=1)
lblId.grid(row=0, column=0, sticky=NSEW)
lblAge = Label(root, text="Enter Cust Age:", font=1)
lblAge.grid(row=1, column=0, sticky=NSEW)
lblName = Label(root, text="Enter Cust Name:", font=1)
lblName.grid(row=2, column=0,sticky=NSEW)

varId = StringVar()
entId = Entry(root, textvariable=varId, font=1)
entId.grid(row=0, column=1, sticky=NSEW)
varAge = StringVar()
entAge = Entry(root, textvariable=varAge, font=1)
entAge.grid(row=1, column=1, sticky=NSEW)
varName = StringVar()
entName = Entry(root, textvariable=varName, font=1)
entName.grid(row=2, column=1, sticky=NSEW)

btnAdd = Button(root, text="Add Cust", font=1, command=btnAdd_Click, width=20)
btnAdd.grid(row=3, column=0, sticky=NSEW)
btnSearch = Button(root, text="Search Cust", font=1, command=btnSearch_Click, width=20)
btnSearch.grid(row=3, column=1, sticky=NSEW)
btnDelete = Button(root, text="Delete Cust", font=1, command=btnDelete_Click, width=20)
btnDelete.grid(row=4, column=0, sticky=NSEW)
btnModify = Button(root, text="Modify Cust", font=1, command=btnModify_Click, width=20)
btnModify.grid(row=4, column=1, sticky=NSEW)
btnAll = Button(root, text="Display All", font=1, command=btnAll_Click, width=20)
btnAll.grid(row=5, column=1, sticky=NSEW)

root.mainloop()
