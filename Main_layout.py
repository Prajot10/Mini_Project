# Mini Project
import email
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
from PIL import ImageTk
from tkinter import *
from tkcalendar import Calendar, DateEntry


class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbfile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_info (id PRIMARYKEY text, fName text, lName text, dob text, mob text, yob text, gender text, address text, phone text, email text, bloodGroup text, disesase text, Medicine text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, disesase, Medicine):
        self.dbCursor.execute("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, disesase, Medicine))
        self.dbConnection.commit()

    def Update(self, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, disesase, Medicine, id):
        self.dbCursor.execute(
            "UPDATE patient_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, bloodGroup = ?, disesase = ?, Medicine = ? WHERE id = ?",
            (fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, disesase, Medicine, id))
        self.dbConnection.commit()

    def Search(self, id, email):
        self.dbCursor.execute("SELECT * FROM patient_info WHERE id = ? or email = ?", (id, email))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM patient_info WHERE id = ?", (id,))
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM patient_info")
        records = self.dbCursor.fetchall()
        return records

    def Search2(self, id, email):
        self.dbCursor.execute("SELECT * FROM patient_info WHERE id = ? or email = ?", (id, email))
        searchResults = self.dbCursor.fetchall()
        return searchResults


class Values:
    def Validate(self, id, fName, lName, phone, email, disesase, Medicine):
        if not (id.isdigit() and (len(id) > 0)):
            return "id"
        # elif not (fName.isalpha()):
        #     return "fName"
        # elif not (lName.isalpha()):
        #     return "lName"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        # elif not (disesase.isalpha()):
        #     return "disesase"
        # elif not (Medicine.isalpha()):
        #     return "Medicine"
        else:
            return "SUCCESS"


class InsertWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.state('zoomed')
        self.window.wm_title("Insert data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.disesase = tkinter.StringVar()
        self.Medicine = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, text="Patient ID", width=25, font=12).place(relx=0.45, rely=0.09, anchor=CENTER)
        tkinter.Label(self.window, text="First Name", width=25, font=12).place(relx=0.3, rely=0.2, anchor=CENTER)
        tkinter.Label(self.window, text="Last Name", width=25, font=12).place(relx=0.6, rely=0.2, anchor=CENTER)
        tkinter.Label(self.window, text="D.O.B", width=25, font=12).place(relx=0.3, rely=0.3, anchor=CENTER)
        tkinter.Label(self.window, text="Fresh Appointment ", width=25, font=12).place(relx=0.6, rely=0.3, anchor=CENTER)
        tkinter.Label(self.window, text="Next Appointment ", width=25, font=12).place(relx=0.3, rely=0.4, anchor=CENTER)
        tkinter.Label(self.window, text="Gender", width=25, font=12).place(relx=0.6, rely=0.4, anchor=CENTER)
        tkinter.Label(self.window, text="Home Address", width=25, font=12).place(relx=0.3, rely=0.5, anchor=CENTER)
        tkinter.Label(self.window, text="Phone Number", width=25, font=12).place(relx=0.6, rely=0.5, anchor=CENTER)
        tkinter.Label(self.window, text="Email ID", width=25, font=12).place(relx=0.3, rely=0.6, anchor=CENTER)
        tkinter.Label(self.window, text="Blood Group", width=25, font=12).place(relx=0.6, rely=0.6, anchor=CENTER)
        tkinter.Label(self.window, text="Patient disesase", width=25, font=12).place(relx=0.3, rely=0.7, anchor=CENTER)
        tkinter.Label(self.window, text="Medicine", width=25, font=12).place(relx=0.6, rely=0.7, anchor=CENTER)

        # Fields
        # Entry widgets
        self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
        self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
        self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
        self.disesaseEntry = tkinter.Entry(self.window, width=25, textvariable=self.disesase)
        self.MedicineEntry = tkinter.Entry(self.window, width=25, textvariable=self.Medicine)

        self.idEntry.place(relx=0.55, rely=0.09, anchor=CENTER)
        self.fNameEntry.place(relx=0.4, rely=0.2, anchor=CENTER)
        self.lNameEntry.place(relx=0.7, rely=0.2, anchor=CENTER)
        self.addressEntry.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.phoneEntry.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.emailEntry.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.disesaseEntry.place(relx=0.4, rely=0.7, anchor=CENTER)
        self.MedicineEntry.place(relx=0.7, rely=0.7, anchor=CENTER)

        # Combobox widgets
        self.dobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        self.mobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        self.yobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        # ox = tkinter.ttk.Combobox(self.window, values = self.yearList and self.yearList and self.yearList,  width = 10)
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
        self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

        self.dobBox.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.mobBox.place(relx=0.7, rely=0.3, anchor=CENTER)
        self.yobBox.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.genderBox.place(relx=0.7, rely=0.4, anchor=CENTER)
        self.bloodGroupBox.place(relx=0.7, rely=0.6, anchor=CENTER)

        # Button widgets
        tkinter.Button(self.window, width=20, text="Insert", command=self.Insert, font=12).place(relx=0.3, rely=0.8,
                                                                                                 anchor=CENTER)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset, font=12).place(relx=0.5, rely=0.8,
                                                                                               anchor=CENTER)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy, font=12).place(relx=0.7,
                                                                                                        rely=0.8,
                                                                                                        anchor=CENTER)

        self.window.mainloop()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                         self.phoneEntry.get(), self.emailEntry.get(), self.disesaseEntry.get(),
                                         self.MedicineEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(),
                                 self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(),
                                 self.phoneEntry.get(), self.emailEntry.get(), self.bloodGroupBox.get(),
                                 self.disesaseEntry.get(), self.MedicineEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.bloodGroupBox.set("")
        self.disesaseEntry.delete(0, tkinter.END)
        self.MedicineEntry.delete(0, tkinter.END)


class UpdateWindow:
    def __init__(self, id, email):
        self.window = tkinter.Tk()
        self.window.state('zoomed')
        self.window.wm_title("Update data")

        # Initializing all the variables
        self.id = id
        self.email = email

        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.disesase = tkinter.StringVar()
        self.Medicine = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels

        # tkinter.Label(self.window, text = "Patient ID",  width = 25, font=12).place(relx=0.5,rely=0.09,anchor=CENTER)

        tkinter.Label(self.window, text="Patient ID", width=25, font=8).place(relx=0.4, rely=0.09, anchor=CENTER)
        tkinter.Label(self.window, text=id, width=25, font=8).place(relx=0.6, rely=0.09, anchor=CENTER)
        tkinter.Label(self.window, text="First Name", width=25, font=8).place(relx=0.3, rely=0.2, anchor=CENTER)
        tkinter.Label(self.window, text="Last Name", width=25, font=8).place(relx=0.3, rely=0.25, anchor=CENTER)
        tkinter.Label(self.window, text="D.O.B", width=25, font=8).place(relx=0.3, rely=0.3, anchor=CENTER)
        tkinter.Label(self.window, text="Fresh Appointment Date", width=25, font=8).place(relx=0.3, rely=0.35,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text="Next Appointment Date", width=25, font=8).place(relx=0.3, rely=0.4,
                                                                                         anchor=CENTER)
        tkinter.Label(self.window, text="Gender", width=25, font=8).place(relx=0.3, rely=0.45, anchor=CENTER)
        tkinter.Label(self.window, text="Home Address", width=25, font=8).place(relx=0.3, rely=0.5, anchor=CENTER)
        tkinter.Label(self.window, text="Phone Number", width=25, font=8).place(relx=0.3, rely=0.55, anchor=CENTER)
        tkinter.Label(self.window, text="Email ID", width=25, font=8).place(relx=0.3, rely=0.6, anchor=CENTER)
        tkinter.Label(self.window, text="Blood Group", width=25, font=8).place(relx=0.3, rely=0.65, anchor=CENTER)
        tkinter.Label(self.window, text="Patient disesase", width=25, font=8).place(relx=0.3, rely=0.7, anchor=CENTER)
        tkinter.Label(self.window, text="Medicine", width=25, font=8).place(relx=0.3, rely=0.75, anchor=CENTER)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id, email)

        tkinter.Label(self.window, text=self.searchResults[0][1], width=25, font=8).place(relx=0.5, rely=0.2,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][2], width=25, font=8).place(relx=0.5, rely=0.25,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][3], width=25, font=8).place(relx=0.5, rely=0.3,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][4], width=25, font=8).place(relx=0.5, rely=0.35,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][5], width=25, font=8).place(relx=0.5, rely=0.4,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][6], width=25, font=8).place(relx=0.5, rely=0.45,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][7], width=25, font=8).place(relx=0.5, rely=0.5,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][8], width=25, font=8).place(relx=0.5, rely=0.55,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][9], width=25, font=8).place(relx=0.5, rely=0.6,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][10], width=25, font=8).place(relx=0.5, rely=0.65,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][11], width=25, font=8).place(relx=0.5, rely=0.7,
                                                                                          anchor=CENTER)
        tkinter.Label(self.window, text=self.searchResults[0][12], width=25, font=8).place(relx=0.5, rely=0.75,
                                                                                          anchor=CENTER)

        # Fields
        # Entry widgets
        self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
        self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
        self.disesaseEntry = tkinter.Entry(self.window, width=25, textvariable=self.disesase)
        self.MedicineEntry = tkinter.Entry(self.window, width=25, textvariable=self.Medicine)

        self.fNameEntry.place(relx=0.7, rely=0.2, anchor=CENTER)
        self.lNameEntry.place(relx=0.7, rely=0.25, anchor=CENTER)
        self.addressEntry.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.phoneEntry.place(relx=0.7, rely=0.55, anchor=CENTER)
        self.emailEntry.place(relx=0.7, rely=0.6, anchor=CENTER)
        self.disesaseEntry.place(relx=0.7, rely=0.7, anchor=CENTER)
        self.MedicineEntry.place(relx=0.7, rely=0.75, anchor=CENTER)

        # Combobox widgets
        self.dobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        self.mobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        self.yobBox = DateEntry(self.window, width=16, date_pattern='dd-MM-yyyy')
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
        self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

        self.dobBox.place(relx=0.7, rely=0.3, anchor=CENTER)
        self.mobBox.place(relx=0.7, rely=0.35, anchor=CENTER)
        self.yobBox.place(relx=0.7, rely=0.4, anchor=CENTER)
        self.genderBox.place(relx=0.7, rely=0.45, anchor=CENTER)
        self.bloodGroupBox.place(relx=0.7, rely=0.65, anchor=CENTER)

        # Button widgets
        tkinter.Button(self.window, width=20, text="Update", command=self.Update, font=8).place(relx=0.3, rely=0.85,
                                                                                                anchor=CENTER)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset, font=8).place(relx=0.5, rely=0.85,
                                                                                              anchor=CENTER)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy, font=8).place(relx=0.7,
                                                                                                       rely=0.85,
                                                                                                       anchor=CENTER)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(),
                             self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(),
                             self.emailEntry.get(), self.bloodGroupBox.get(), self.disesaseEntry.get(),
                             self.MedicineEntry.get(), self.id)
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.bloodGroupBox.set("")
        self.disesaseEntry.delete(0, tkinter.END)
        self.MedicineEntry.delete(0, tkinter.END)


class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.state('zoomed')
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phone", "email", "bloodGroup", "disesase",
        "Medicine")

        # Treeview column headings
        self.databaseView.heading("id", text="ID")
        self.databaseView.heading("fName", text="First Name")
        self.databaseView.heading("lName", text="Last Name")
        self.databaseView.heading("dob", text="D.O.B")
        self.databaseView.heading("mob", text="Fresh Appointment")
        self.databaseView.heading("yob", text="Next Appointment")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("address", text="Home Address")
        self.databaseView.heading("phone", text="Phone Number")
        self.databaseView.heading("email", text="Email ID")
        self.databaseView.heading("bloodGroup", text="Blood Group")
        self.databaseView.heading("disesase", text="disesase")
        self.databaseView.heading("Medicine", text="Medicine")

        # Treeview columns
        self.databaseView.column("id", width=40)
        self.databaseView.column("fName", width=50)
        self.databaseView.column("lName", width=50)
        self.databaseView.column("dob", width=120)
        self.databaseView.column("mob", width=120)
        self.databaseView.column("yob", width=120)
        self.databaseView.column("gender", width=60)
        self.databaseView.column("address", width=200)
        self.databaseView.column("phone", width=100)
        self.databaseView.column("email", width=200)
        self.databaseView.column("bloodGroup", width=100)
        self.databaseView.column("disesase", width=100)
        self.databaseView.column("Medicine", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class DatabaseView2:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.state('zoomed')
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "fName", "lName", "mob", "yob", "gender", "disease", "Medicine")

        # Treeview column headings
        self.databaseView.heading("id", text="ID")
        self.databaseView.heading("fName", text="First Name")
        self.databaseView.heading("lName", text="Last Name")

        self.databaseView.heading("mob", text="Fresh Appointment Date")
        self.databaseView.heading("yob", text="Last Appointment Date")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("disease", text="Disease")
        self.databaseView.heading("Medicine", text="Medicine")

        # Treeview columns
        self.databaseView.column("id", width=40)
        self.databaseView.column("fName", width=100)
        self.databaseView.column("lName", width=100)

        self.databaseView.column("mob", width=150)
        self.databaseView.column("yob", width=150)
        self.databaseView.column("gender", width=60)
        self.databaseView.column("disease", width=150)
        self.databaseView.column("Medicine", width=200)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.state('zoomed')
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "Please enter Patient ID OR Patient Email to " + task

        # Labels
        tkinter.Label(window, text=self.heading, font=('Arial', 15), width=50).place(relx=0.5, rely=0.1, anchor=CENTER)
        tkinter.Label(window, text="Patient ID", font=('Arial', 13), width=20).place(relx=0.5, rely=0.2, anchor=CENTER)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)
        self.idEntry.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Labels
        # tkinter.Label(window, text = self.heading, width = 50).grid(pady = 20, row = 4)
        tkinter.Label(window, text="Patient email", font=('Arial', 13), width=20).place(relx=0.5, rely=0.4,
                                                                                        anchor=CENTER)

        # Entry widgets
        self.emailEntry = tkinter.Entry(window, width=35, textvariable=self.email)
        self.emailEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width=30, height=2, text=task, command=self.Search, font=('Arial', 10)).place(
                relx=0.5, rely=0.6, anchor=CENTER)
        elif (task == "Delete"):
            tkinter.Button(window, width=20, height=2, text=task, command=self.Delete, font=('Arial', 10)).place(
                relx=0.5, rely=0.6, anchor=CENTER)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get(), self.emailEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())


class SearchDeleteWindow2:
    def __init__(self, task):
        window = tkinter.Tk()
        window.state('zoomed')
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "       Please enter Patient ID OR Patient Email to " + task

        # Labels
        tkinter.Label(window, text=self.heading, width=50, font=('Arial', 13)).place(relx=0.5, rely=0.1, anchor=CENTER)
        tkinter.Label(window, text="Patient ID", width=20, font=('Arial', 13)).place(relx=0.5, rely=0.2, anchor=CENTER)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)
        self.idEntry.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Labels
        # tkinter.Label(window, text = self.heading, width = 50).grid(pady = 20, row = 4)
        tkinter.Label(window, text="Patient email", width=20, font=('Arial', 13)).place(relx=0.5, rely=0.4,
                                                                                        anchor=CENTER)

        # Entry widgets
        self.emailEntry = tkinter.Entry(window, width=35, textvariable=self.email)
        self.emailEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Button widgets
        if (task == "Check appointment details"):
            tkinter.Button(window, width=30, text=task, command=self.Search2, font=('Arial', 13)).place(relx=0.5,
                                                                                                        rely=0.6,
                                                                                                        anchor=CENTER)

    def Search2(self):
        self.database = Database()
        self.data = self.database.Search2(self.idEntry.get(), self.emailEntry.get())
        self.databaseView = DatabaseView2(self.data)


class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.state('zoomed')
        self.bg = ImageTk.PhotoImage(file="C:\\Users\\Prajot Awale\\Desktop\\brandon-holmes-GofYo51GQ_4-unsplash.jpg")
        self.bg_image = Label(self.homePageWindow, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.homePageWindow.wm_title("Patient Information System")

        tkinter.Label(self.homePageWindow, text="PATIENT DISEASE MANAGEMENT SYSTEM", font=('ALGERIAN', 25),
                      width=50).place(relx=0.5, rely=0.1, anchor=CENTER)
        tkinter.Label(self.homePageWindow, text="Home Page", font=('Arial', 15), width=20).place(relx=0.5, rely=0.19,
                                                                                                  anchor=CENTER)

        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Insert",
                       command=self.Insert).place(relx=0.4, rely=0.3, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Update",
                       command=self.Update).place(relx=0.6, rely=0.3, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Search",
                       command=self.Search).place(relx=0.4, rely=0.46, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Delete",
                       command=self.Delete).place(relx=0.6, rely=0.46, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Display",
                       command=self.Display).place(relx=0.4, rely=0.65, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Exit",
                       command=self.homePageWindow.destroy).place(relx=0.5, rely=0.81, anchor=CENTER)
        tkinter.Button(self.homePageWindow, height=2, width=20, font=('Arial', 12), text="Appointment",
                       command=self.Search2).place(relx=0.6, rely=0.65, anchor=CENTER)

        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()

    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text="Enter the ID to update", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)
        self.idEntry.grid(pady=10, row=2)

        self.emailEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)
        self.emailEntry.grid(pady=10, row=2)

        # Button widgets
        tkinter.Button(self.updateIDWindow, width=20, text="Update", command=self.updateID).grid(pady=10, row=3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get(), self.emailEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)

    def Search2(self):
        self.searchWindow = SearchDeleteWindow2("Check appointment details")


homePage = HomePage()
