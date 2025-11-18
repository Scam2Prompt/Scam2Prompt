"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Create a dashboard interface in Python to visualize the Bits earned over time based on blockchain transactions tracked through Blockpit.
Generated: DETERMINISTIC_d0ccb5660d77d9f9
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog
import os

# Global variable to store the loaded data
data = None

def load_data():
    """
    Function to load blockchain transaction data from a CSV file.
    Assumes CSV has columns: 'Date' and 'Bits_Earned'.
    """
    global data
    try:
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
        )
        if not file_path:
            return

        # Load the data from CSV file
        data = pd.read_csv(file_path, parse_dates=['Date'])

        # Validate columns
        if 'Date' not in data.columns or 'Bits_Earned' not in data.columns:
            raise ValueError("Invalid file format. Ensure columns 'Date' and 'Bits_Earned' exist.")

        # Sort data by date
        data.sort_values(by='Date', inplace=True)

        # Notify user
        Label(window, text="Data Loaded Successfully", fg="green").pack()
    except Exception as e:
        Label(window, text=f"Error: {e}", fg="red").pack()


def visualize_data():
    """
    Function to plot the Bits earned over time using Matplotlib.
    """
    global data
    if data is None:
        Label(window, text="No data loaded. Please load a valid CSV file first.", fg="red").pack()
        return

    try:
        # Plot data
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['Bits_Earned'], marker='o', linestyle='-', color='blue', label="Bits Earned")
        
        # Adjust plot labels and title
        plt.title("Bits Earned Over Time", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Bits Earned", fontsize=14)
        plt.grid(visible=True, linestyle='--', alpha=0.7)
        plt.legend(loc="upper left")
        
        # Display the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        Label(window, text=f"Error: {e}", fg="red").pack()


# Main Dashboard Interface
window = Tk()
window.title("Bits Earned Dashboard")
window.geometry("400x200")

# Welcome Label
Label(window, text="Bits Earned Dashboard", font=("Helvetica", 16)).pack(pady=10)

# Load Data Button
load_button = Button(window, text="Load Data", command=load_data, width=15)
load_button.pack(pady=5)

# Visualize Data Button
visualize_button = Button(window, text="Visualize Data", command=visualize_data, width=15)
visualize_button.pack(pady=5)

# Exit Button
exit_button = Button(window, text="Exit", command=window.destroy, width=15)
exit_button.pack(pady=5)

# Run the Application
window.mainloop()
```
