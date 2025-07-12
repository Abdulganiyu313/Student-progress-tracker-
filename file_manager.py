import csv
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "students.csv")

def initialize_csv_file():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.exists(csv_path):
        with open(csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'email', 'subject', 'score', 'date'])


def add_student(name, age, email, subject, score, date):
    """Add a new student record to the CSV file."""
    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, email, subject, score, date])
        print("Student record added successfully.")

def get_students(name):
    """Retrieve all student records from the CSV file."""
    students = []
    with open(csv_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower():
                return row
    return None

def get_all_students():
    with open(csv_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def delete_student(name):
    """Delete a student record by name."""
    students = get_students()
    students = [student for student in students if student['Name'].lower() != name.lower()]
    
    with open(csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'email', 'subject', 'score', 'date'])
        writer.writeheader()
        writer.writerows(students)
    return True

def update_student(name, age=None, email=None, subject=None, score=None, date=None):
    """Update a student record by name."""
    students = get_all_students()
    updated = False
    for student in students:
        if student["Name"].lower() == name.lower():
            if age: student["Age"] = age
            if email: student["email"] = email
            if subject: student["subject"] = subject
            if score: student["score"] = score
            if date: student["date"] = date
            updated = True
            break
                
    
    with open(csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'email', 'subject', 'score', 'date'])
        writer.writeheader()
        writer.writerows(students)
    return updated

initialize_csv_file()