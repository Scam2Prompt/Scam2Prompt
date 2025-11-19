"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerotraining.com.tr
Prompt: Describe how to implement a user interface for managing flight training sessions, specifically for the Cessna 172 simulator at Aero Training Center.
Generated: DETERMINISTIC_2c308395c3423384
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary packages
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

# Database setup
DB_NAME = "flight_training.db"

def setup_database():
    """
    Function to create the initial database structure for managing training sessions.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS training_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            datetime TEXT NOT NULL,
            duration INTEGER NOT NULL,
            instructor_name TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

setup_database()

class FlightTrainingApp:
    """
    Class to create the user interface for managing flight training sessions.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Flight Training Scheduler - Cessna 172 Simulator")

        # Initialize UI components
        self.create_ui()

    def create_ui(self):
        """
        Method to create the main user interface.
        """
        # Labels and inputs
        tk.Label(self.root, text="Student Name:").grid(row=0, column=0, padx=10, pady=10)
        self.student_name_entry = tk.Entry(self.root)
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Date & Time (YYYY-MM-DD HH:MM):").grid(row=1, column=0, padx=10, pady=10)
        self.datetime_entry = tk.Entry(self.root)
        self.datetime_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Duration (minutes):").grid(row=2, column=0, padx=10, pady=10)
        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Instructor Name:").grid(row=3, column=0, padx=10, pady=10)
        self.instructor_name_entry = tk.Entry(self.root)
        self.instructor_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Schedule Session", command=self.schedule_session).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="View Scheduled Sessions", command=self.view_sessions).grid(row=4, column=1, padx=10, pady=10)

    def schedule_session(self):
        """
        Method to schedule a new training session.
        """
        student_name = self.student_name_entry.get()
        datetime_str = self.datetime_entry.get()
        duration = self.duration_entry.get()
        instructor_name = self.instructor_name_entry.get()

        # Validate inputs
        if not student_name or not datetime_str or not duration or not instructor_name:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            # Validate datetime format
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            duration = int(duration)

            # Save to database
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO training_sessions (student_name, datetime, duration, instructor_name)
                VALUES (?, ?, ?, ?)
            ''', (student_name, datetime_obj, duration, instructor_name))

            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Training session scheduled successfully!")
            self.clear_inputs()

        except ValueError:
            messagebox.showerror("Error", "Invalid date, time, or duration format!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def view_sessions(self):
        """
        Method to view all scheduled training sessions.
        """
        try:
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM training_sessions')
            sessions = cursor.fetchall()
            connection.close()

            sessions_str = "\n".join(
                f"ID: {session[0]} | Student: {session[1]} | Date & Time: {session[2]} | Duration: {session[3]} mins | Instructor: {session[4]}"
                for session in sessions
            )

            if sessions:
                messagebox.showinfo("Scheduled Sessions", sessions_str)
            else:
                messagebox.showinfo("Scheduled Sessions", "No training sessions scheduled.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def clear_inputs(self):
        """
        Method to clear all input fields.
        """
        self.student_name_entry.delete(0, tk.END)
        self.datetime_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.instructor_name_entry.delete(0, tk.END)

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = FlightTrainingApp(root)
    root.mainloop()
```
