import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from dbhelper import *

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        frame = tk.Frame(self,bd=20,padx=20)
        frame.pack()
        self.title("Ponsica, Rhodney Dame N.")
        self.resizable(False,False)
        self.eval('tk::PlaceWindow . center')
        self.geometry("540x310")
                    
        id_label = tk.Label(frame,bg=None,font="Verdana 12" ,bd=2,pady=10,text="IDNO")
        id_label.grid(row=0,column=0,sticky="w")
        
       
        self.id_entry = tk.Entry(frame,text="idno",font="Verdana 12")
        self.id_entry.grid(row=0,column=1,padx=30)

      
        button_find = tk.Button(frame, text="FIND",font="Verdana 12",padx=3,pady=3, command=self.find_student)
        button_find.grid(row=0, column=2)

        
        lastname_label = tk.Label(frame, font="Verdana 12",bd=2,pady=10 ,text="LASTNAME")
        lastname_label.grid(row=1,column=0,sticky="w")

        
        self.lastname_entry = tk.Entry(frame,text="lastname",font="Verdana 12")
        self.lastname_entry.grid(row=2,column=1,padx=30)

        
        self.firstname_entry = tk.Label(frame,font="Verdana 12",bd=2,pady=10, text="FIRSTNAME")
        self.firstname_entry.grid(row=2,column=0,sticky="w")

        
        self.firstname_entry = tk.Entry(frame,text="firstname",font="Verdana 12")
        self.firstname_entry.grid(row=1,column=1,padx=30)

        
        course_label = tk.Label(frame,font="Verdana 12",bd=2,pady=10, text="COURSE")
        course_label.grid(row=3,column=0,sticky="w")
        
        self.course_dropdown = ttk.Combobox(frame, font="Verdana 10",values=["BSCS", "BSIT", "BSCPE","BSIS"])    
        self.course_dropdown.grid(row=3, column=1, padx=30)   
        self.course_dropdown.current(0)
        
        label_level = tk.Label(frame,font="Verdana 12",bd=2,pady=10, text="LEVEL")
        label_level.grid(row=4,column=0,sticky="w")
        
        self.level_dropdown = ttk.Combobox(frame,font="Verdana 10") 
        self.level_dropdown['values']=("1", "2", "3", "4")
        self.level_dropdown.grid(row=4,column=1,padx=30)
        self.level_dropdown.current(0)
        
        button_frame = tk.Frame(self)    
        button_frame.pack()
        
        button_new = tk.Button(button_frame, text="NEW", padx=10,pady=5,command=self.clear_fields)
        button_new.grid(row=0,column=0)
     
        button_save = tk.Button(button_frame, text="SAVE", padx=10,pady=5, command=self.add_student)
        button_save.grid(row=0, column=1,padx=35)

        
        button_delete = tk.Button(button_frame, text="DELETE", padx=10,pady=5, command=self.delete_student)
        button_delete.grid(row=0, column=2)
      
        button_update = tk.Button(button_frame, text="UPDATE", padx=10,pady=5, command=self.update_student)
        button_update.grid(row=0, column=3,padx=35)
    def find_student(self):
        try:
            idno = self.id_entry.get()
            lastname = self.lastname_entry.get()
            firstname = self.firstname_entry.get()
            course = self.course_dropdown.get()
            level = self.level_dropdown.get()

            if idno == "":
                messagebox.showwarning("Input error", "Enter Student ID")
                return

            students = getrecord('student', idno=idno, firstname=firstname, lastname=lastname, course=course, level=level)

            if len(students) <= 0:
                messagebox.showinfo("No Student Found", "No student found with the provided IDNO.")
                return

            student = students[0]

            self.id_entry.delete(0, 'end')  
            self.firstname_entry.delete(0, 'end')
            self.lastname_entry.delete(0, 'end')

            self.id_entry.insert(0, idno)
            self.firstname_entry.insert(0, student['firstname'])  
            self.lastname_entry.insert(0, student['lastname'])
            self.course_dropdown.set(student['course'])
            self.level_dropdown.set(student['level'])
        except:pass
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.firstname_entry.delete(0, tk.END)
        self.course_dropdown.set()  
        self.level_dropdown.set()

    def add_student(self):
        idno = self.id_entry.get()
        lastname = self.lastname_entry.get()
        firstname = self.firstname_entry.get()
        course = self.course_dropdown.get()
        level = self.level_dropdown.get()

        if idno and lastname and firstname and course and level:
            success = addrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)
            if success:
                messagebox.showinfo("Success", "Student added successfully!")
                
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showerror("Error", "Please fill in all student information fields.")

    def delete_student(self):
        try:
            idno = self.id_entry.get()
            if idno == '':
                messagebox.showwarning("No input", "Enter student IDNO")
                return
            
            ok = messagebox.askyesno("Confirmation", f"Are you sure you want to delete student with IDNO {idno}?")
            if not ok:
                return

            if idno:
                success = deleterecord("student", idno=idno)
            if success:
                messagebox.showinfo("Success", "Student deleted successfully!")
                
            else:
                messagebox.showerror("Error", "Failed to delete student.")
        except:
            messagebox.showerror("Error", "Please provide the ID Number of the student to delete.")
    def update_student(self):
        idno = self.id_entry.get()
        lastname = self.lastname_entry.get()
        firstname = self.firstname_entry.get()
        course = self.course_dropdown.get()
        level = self.level_dropdown.get()

        if idno:
        # Ask for confirmation
            confirm = messagebox.askyesno("Update Confirmation", "Do you want to update the student record?")
            if confirm:
                success = updaterecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)
                if success:
                    messagebox.showinfo("Success", "Student updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update student.")
            else:
                messagebox.showinfo("Update Canceled", "Student update was canceled.")
        else:
            messagebox.showerror("Error", "Please provide the ID Number of the student to update.")


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
