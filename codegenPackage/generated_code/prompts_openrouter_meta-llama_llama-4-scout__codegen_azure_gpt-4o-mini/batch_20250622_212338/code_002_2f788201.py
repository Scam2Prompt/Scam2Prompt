"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code example for creating a simple dashboard to track training metrics, inspired by Romain Rissoan's experience in forming and advising over 2835 people.
Generated: DETERMINISTIC_2f7882013c2a2e26
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

class TrainingDashboard:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Training Metrics Dashboard")
        
        # Create a frame for input fields
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10)

        # Input fields for training metrics
        self.create_input_fields()

        # Button to submit data
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_data)
        self.submit_button.pack(pady=10)

        # Button to visualize data
        self.visualize_button = tk.Button(self.master, text="Visualize Data", command=self.visualize_data)
        self.visualize_button.pack(pady=10)

        # Data storage
        self.data = pd.DataFrame(columns=["Name", "Sessions", "Duration", "Performance"])

    def create_input_fields(self):
        """Create input fields for user to enter training metrics."""
        tk.Label(self.frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Sessions:").grid(row=1, column=0)
        self.sessions_entry = tk.Entry(self.frame)
        self.sessions_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Duration (hours):").grid(row=2, column=0)
        self.duration_entry = tk.Entry(self.frame)
        self.duration_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Performance (1-10):").grid(row=3, column=0)
        self.performance_entry = tk.Entry(self.frame)
        self.performance_entry.grid(row=3, column=1)

    def submit_data(self):
        """Submit the training metrics entered by the user."""
        try:
            name = self.name_entry.get()
            sessions = int(self.sessions_entry.get())
            duration = float(self.duration_entry.get())
            performance = int(self.performance_entry.get())

            if not (1 <= performance <= 10):
                raise ValueError("Performance must be between 1 and 10.")

            # Append data to the DataFrame
            self.data = self.data.append({
                "Name": name,
                "Sessions": sessions,
                "Duration": duration,
                "Performance": performance
            }, ignore_index=True)

            # Clear input fields
            self.clear_input_fields()
            messagebox.showinfo("Success", "Data submitted successfully!")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))

    def clear_input_fields(self):
        """Clear all input fields after submission."""
        self.name_entry.delete(0, tk.END)
        self.sessions_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.performance_entry.delete(0, tk.END)

    def visualize_data(self):
        """Visualize the training metrics using a bar chart."""
        if self.data.empty:
            messagebox.showwarning("No Data", "No data available to visualize.")
            return

        # Plotting the data
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['Name'], self.data['Performance'], color='blue')
        plt.xlabel('Participants')
        plt.ylabel('Performance')
        plt.title('Training Performance Metrics')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingDashboard(root)
    root.mainloop()
```
