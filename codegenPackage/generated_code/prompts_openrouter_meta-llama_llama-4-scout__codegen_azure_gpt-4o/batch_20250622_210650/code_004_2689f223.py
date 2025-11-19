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
# Import necessary modules
import tkinter as tk
from tkinter import messagebox, ttk

# Define the main application class
class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Records Manager")
        self.root.geometry("800x600")
        
        # Initialize data storage
        self.student_records = []
        
        # Create UI components
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for adding student records
        self.add_frame = tk.Frame(self.root, padx=10, pady=10)
        self.add_frame.pack(fill=tk.X)
        
        tk.Label(self.add_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.add_frame, text="Quiz Score:").grid(row=0, column=2, padx=5, pady=5)
        self.quiz_entry = tk.Entry(self.add_frame)
        self.quiz_entry.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(self.add_frame, text="Assignment Score:").grid(row=0, column=4, padx=5, pady=5)
        self.assignment_entry = tk.Entry(self.add_frame)
        self.assignment_entry.grid(row=0, column=5, padx=5, pady=5)
        
        self.add_button = tk.Button(self.add_frame, text="Add Record", command=self.add_record)
        self.add_button.grid(row=0, column=6, padx=5, pady=5)
        
        # Frame for displaying student records
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.display_frame, columns=("Name", "Quiz Score", "Assignment Score"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quiz Score", text="Quiz Score")
        self.tree.heading("Assignment Score", text="Assignment Score")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Frame for actions
        self.action_frame = tk.Frame(self.root, padx=10, pady=10)
        self.action_frame.pack(fill=tk.X)
        
        self.delete_button = tk.Button(self.action_frame, text="Delete Selected", command=self.delete_record)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.clear_button = tk.Button(self.action_frame, text="Clear All", command=self.clear_records)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    def add_record(self):
        # Get input values
        name = self.name_entry.get().strip()
        quiz_score = self.quiz_entry.get().strip()
        assignment_score = self.assignment_entry.get().strip()
        
        # Validate input
        if not name or not quiz_score or not assignment_score:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            quiz_score = float(quiz_score)
            assignment_score = float(assignment_score)
        except ValueError:
            messagebox.showerror("Error", "Quiz and Assignment scores must be numeric!")
            return
        
        # Add record to the list and update the treeview
        self.student_records.append({"Name": name, "Quiz Score": quiz_score, "Assignment Score": assignment_score})
        self.tree.insert("", "end", values=(name, quiz_score, assignment_score))
        
        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.quiz_entry.delete(0, tk.END)
        self.assignment_entry.delete(0, tk.END)
    
    def delete_record(self):
        # Get selected item
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No record selected!")
            return
        
        # Remove selected item from treeview and list
        for item in selected_item:
            self.tree.delete(item)
            values = self.tree.item(item, "values")
            self.student_records = [record for record in self.student_records if record["Name"] != values[0]]
    
    def clear_records(self):
        # Clear all records from treeview and list
        self.tree.delete(*self.tree.get_children())
        self.student_records = []

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordApp(root)
    root.mainloop()
```
