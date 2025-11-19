"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Create a simple desktop application for managing student records and quiz/assignment tracking using a suitable programming language and framework."
Generated: DETERMINISTIC_2689f223dfd89dda
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student Record Manager Application**

```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class StudentRecordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Manager")
        self.root.geometry("800x600")

        # Create database connection
        self.conn = sqlite3.connect("student_records.db")
        self.cursor = self.conn.cursor()

        # Create tables if not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quizzes (
                id INTEGER PRIMARY KEY,
                student_id INTEGER NOT NULL,
                quiz_name TEXT NOT NULL,
                score REAL NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY,
                student_id INTEGER NOT NULL,
                assignment_name TEXT NOT NULL,
                score REAL NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        """)
        self.conn.commit()

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.student_tab = ttk.Frame(self.tab_control)
        self.quiz_tab = ttk.Frame(self.tab_control)
        self.assignment_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.student_tab, text="Students")
        self.tab_control.add(self.quiz_tab, text="Quizzes")
        self.tab_control.add(self.assignment_tab, text="Assignments")
        self.tab_control.pack(expand=1, fill="both")

        # Student tab
        self.student_name_label = tk.Label(self.student_tab, text="Name:")
        self.student_name_label.pack()
        self.student_name_entry = tk.Entry(self.student_tab)
        self.student_name_entry.pack()
        self.student_email_label = tk.Label(self.student_tab, text="Email:")
        self.student_email_label.pack()
        self.student_email_entry = tk.Entry(self.student_tab)
        self.student_email_entry.pack()
        self.add_student_button = tk.Button(self.student_tab, text="Add Student", command=self.add_student)
        self.add_student_button.pack()
        self.student_listbox = tk.Listbox(self.student_tab)
        self.student_listbox.pack()
        self.update_student_list()

        # Quiz tab
        self.quiz_name_label = tk.Label(self.quiz_tab, text="Quiz Name:")
        self.quiz_name_label.pack()
        self.quiz_name_entry = tk.Entry(self.quiz_tab)
        self.quiz_name_entry.pack()
        self.quiz_score_label = tk.Label(self.quiz_tab, text="Score:")
        self.quiz_score_label.pack()
        self.quiz_score_entry = tk.Entry(self.quiz_tab)
        self.quiz_score_entry.pack()
        self.student_id_label = tk.Label(self.quiz_tab, text="Student ID:")
        self.student_id_label.pack()
        self.student_id_entry = tk.Entry(self.quiz_tab)
        self.student_id_entry.pack()
        self.add_quiz_button = tk.Button(self.quiz_tab, text="Add Quiz", command=self.add_quiz)
        self.add_quiz_button.pack()
        self.quiz_listbox = tk.Listbox(self.quiz_tab)
        self.quiz_listbox.pack()
        self.update_quiz_list()

        # Assignment tab
        self.assignment_name_label = tk.Label(self.assignment_tab, text="Assignment Name:")
        self.assignment_name_label.pack()
        self.assignment_name_entry = tk.Entry(self.assignment_tab)
        self.assignment_name_entry.pack()
        self.assignment_score_label = tk.Label(self.assignment_tab, text="Score:")
        self.assignment_score_label.pack()
        self.assignment_score_entry = tk.Entry(self.assignment_tab)
        self.assignment_score_entry.pack()
        self.student_id_assignment_label = tk.Label(self.assignment_tab, text="Student ID:")
        self.student_id_assignment_label.pack()
        self.student_id_assignment_entry = tk.Entry(self.assignment_tab)
        self.student_id_assignment_entry.pack()
        self.add_assignment_button = tk.Button(self.assignment_tab, text="Add Assignment", command=self.add_assignment)
        self.add_assignment_button.pack()
        self.assignment_listbox = tk.Listbox(self.assignment_tab)
        self.assignment_listbox.pack()
        self.update_assignment_list()

    def add_student(self):
        try:
            name = self.student_name_entry.get()
            email = self.student_email_entry.get()
            self.cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
            self.conn.commit()
            self.update_student_list()
            self.student_name_entry.delete(0, tk.END)
            self.student_email_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

    def update_student_list(self):
        self.student_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()
        for student in students:
            self.student_listbox.insert(tk.END, f"{student[0]} - {student[1]} - {student[2]}")

    def add_quiz(self):
        try:
            quiz_name = self.quiz_name_entry.get()
            score = float(self.quiz_score_entry.get())
            student_id = int(self.student_id_entry.get())
            self.cursor.execute("INSERT INTO quizzes (student_id, quiz_name, score) VALUES (?, ?, ?)", (student_id, quiz_name, score))
            self.conn.commit()
            self.update_quiz_list()
            self.quiz_name_entry.delete(0, tk.END)
            self.quiz_score_entry.delete(0, tk.END)
            self.student_id_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Invalid score or student ID")

    def update_quiz_list(self):
        self.quiz_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM quizzes")
        quizzes = self.cursor.fetchall()
        for quiz in quizzes:
            self.quiz_listbox.insert(tk.END, f"{quiz[0]} - {quiz[1]} - {quiz[2]} - {quiz[3]}")

    def add_assignment(self):
        try:
            assignment_name = self.assignment_name_entry.get()
            score = float(self.assignment_score_entry.get())
            student_id = int(self.student_id_assignment_entry.get())
            self.cursor.execute("INSERT INTO assignments (student_id, assignment_name, score) VALUES (?, ?, ?)", (student_id, assignment_name, score))
            self.conn.commit()
            self.update_assignment_list()
            self.assignment_name_entry.delete(0, tk.END)
            self.assignment_score_entry.delete(0, tk.END)
            self.student_id_assignment_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Invalid score or student ID")

    def update_assignment_list(self):
        self.assignment_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM assignments")
        assignments = self.cursor.fetchall()
        for assignment in assignments:
            self.assignment_listbox.insert(tk.END, f"{assignment[0]} - {assignment[1]} - {assignment[2]} - {assignment[3]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordManager(root)
    root.mainloop()
```
