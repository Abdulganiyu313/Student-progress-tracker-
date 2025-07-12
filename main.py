from tkinter import Tk, Label, Button, Entry, messagebox
from file_manager import add_student, get_students, delete_student, update_student

window = Tk()
window.title("Student Record Management System")
window.config(padx=50, pady=50)

#labels and entries
Label(text="Name").grid(row=0, column=0)
name_entry = Entry(width=35)
name_entry.grid(row=0, column=1)
name_entry.focus()

Label(text="Age").grid(row=1, column=0)
age_entry = Entry(width=35)
age_entry.grid(row=1, column=1)

Label(text="Email").grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)

Label(text="Subject").grid(row=3, column=0)
subject_entry = Entry(width=35)
subject_entry.grid(row=3, column=1)

Label(text="Score").grid(row=4, column=0)
score_entry = Entry(width=35)
score_entry.grid(row=4, column=1)

Label(text="Date").grid(row=5, column=0)
date_entry = Entry(width=35)
date_entry.grid(row=5, column=1)

# Button commands
def save_student():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    subject = subject_entry.get()
    score = score_entry.get()
    date = date_entry.get()

    add_student(name, age, email, subject, score, date)
    messagebox.showinfo("Success", "Student record added successfully.")
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    subject_entry.delete(0, 'end')
    score_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    
def search_record():
    name = name_entry.get()
    student = get_students(name)
    if student:
        age_entry.delete(0, 'end')
        age_entry.insert(0, student['age'])
        email_entry.delete(0, 'end')
        email_entry.insert(0, student['email'])
        subject_entry.delete(0, 'end')
        subject_entry.insert(0, student['subject'])
        score_entry.delete(0, 'end')
        score_entry.insert(0, student['score'])
        date_entry.delete(0, 'end')
        date_entry.insert(0, student['date'])
    else:
        messagebox.showerror("Error", "Student not found.")

def update_record():
    update_student(
        name= name_entry.get(),
        age=age_entry.get(),
        email=email_entry.get(),
        subject=subject_entry.get(),
        score=score_entry.get(),
        date=date_entry.get()
    )
    messagebox.showinfo("Success", "Student record updated successfully.")

def delete_record():
    name = name_entry.get()
    if delete_student(name):
        messagebox.showinfo("Success", "Student record deleted successfully.")
    else:
        messagebox.showerror("Error", "Student not found.")

#Buttons
save_button = Button(text="Save Record", width=15, command=save_student)
save_button.grid(row=6, column=1, columnspan=2)

delete_button = Button(text="Delete Record", width=20, command=delete_record)
delete_button.grid(row=7, column=1, columnspan=2)

search_button = Button(text="Search Record", width=20, command=search_record)
search_button.grid(row=8, column=1, columnspan=2)

update_button = Button(text="Update Record", width=20, command=update_record)
update_button.grid(row=9, column=1, columnspan=2)

window.mainloop()