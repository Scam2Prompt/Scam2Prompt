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

```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management")
        self.root.geometry("800x600")
        
        # Database setup
        self.conn = sqlite3.connect('student_records.db')
        self.create_tables()
        
        # Main notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_student_tab()
        self.create_quiz_tab()
        self.create_assignment_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                enrollment_date TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quizzes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject TEXT,
                score REAL,
                date TEXT,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                title TEXT,
                description TEXT,
                due_date TEXT,
                submitted BOOLEAN,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        ''')
        self.conn.commit()
    
    def create_student_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Students")
        
        # Student list frame
        list_frame = ttk.LabelFrame(tab, text="Student List")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview for students
        self.student_tree = ttk.Treeview(list_frame, columns=("ID", "Name", "Email", "Phone", "Enrollment Date"), show="headings")
        self.student_tree.heading("ID", text="ID")
        self.student_tree.heading("Name", text="Name")
        self.student_tree.heading("Email", text="Email")
        self.student_tree.heading("Phone", text="Phone")
        self.student_tree.heading("Enrollment Date", text="Enrollment Date")
        self.student_tree.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.student_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.student_tree.configure(yscrollcommand=scrollbar.set)
        
        # Student form frame
        form_frame = ttk.LabelFrame(tab, text="Student Details")
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Form fields
        tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Enrollment Date:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.enrollment_entry = tk.Entry(form_frame)
        self.enrollment_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.enrollment_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        # Buttons
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Add", command=self.add_student).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update", command=self.update_student).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete", command=self.delete_student).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_student_form).pack(side=tk.LEFT, padx=5)
        
        # Load initial data
        self.load_students()
        
        # Bind treeview selection
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)
    
    def create_quiz_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Quizzes")
        
        # Quiz list frame
        list_frame = ttk.LabelFrame(tab, text="Quiz Records")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview for quizzes
        self.quiz_tree = ttk.Treeview(list_frame, columns=("ID", "Student ID", "Student Name", "Subject", "Score", "Date"), show="headings")
        self.quiz_tree.heading("ID", text="ID")
        self.quiz_tree.heading("Student ID", text="Student ID")
        self.quiz_tree.heading("Student Name", text="Student Name")
        self.quiz_tree.heading("Subject", text="Subject")
        self.quiz_tree.heading("Score", text="Score")
        self.quiz_tree.heading("Date", text="Date")
        self.quiz_tree.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.quiz_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.quiz_tree.configure(yscrollcommand=scrollbar.set)
        
        # Quiz form frame
        form_frame = ttk.LabelFrame(tab, text="Quiz Details")
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Form fields
        tk.Label(form_frame, text="Student:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.student_combo = ttk.Combobox(form_frame, state="readonly")
        self.student_combo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Subject:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.quiz_subject_entry = tk.Entry(form_frame)
        self.quiz_subject_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Score:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.quiz_score_entry = tk.Entry(form_frame)
        self.quiz_score_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        tk.Label(form_frame, text="Date:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.quiz_date_entry = tk.Entry(form_frame)
        self.quiz_date_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.quiz_date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        # Buttons
        button_frame = ttk.Frame(tab)
        button_frame
