"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Suggest a library for building a user interface that showcases the different distance learning careers available at ISIV, including Seguridad e Higiene Laboral.
Generated: DETERMINISTIC_fc96b54e189421f1
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of clean, production-ready Python code using the `tkinter` library for building a simple user interface to showcase distance learning careers available at ISIV, including "Seguridad e Higiene Laboral":

```python
import tkinter as tk
from tkinter import messagebox

# Data: List of distance learning careers at ISIV
CAREERS = [
    "Seguridad e Higiene Laboral",
    "Gestión Ambiental",
    "Administración de Empresas",
    "Diseño Gráfico",
    "Programación",
    "Marketing Digital",
    "Turismo y Hotelería"
]

def show_career_details(career):
    """
    Display a message box with details of the selected career.
    :param career: The name of the selected career.
    """
    # Simulated details for each career (in production, fetch from a database or API)
    career_details = {
        "Seguridad e Higiene Laboral": "Focuses on workplace safety and hygiene standards.",
        "Gestión Ambiental": "Specializes in environmental management and sustainability.",
        "Administración de Empresas": "Covers business administration and leadership skills.",
        "Diseño Gráfico": "Learn creative design techniques and software tools.",
        "Programación": "Develop software applications using various programming languages.",
        "Marketing Digital": "Study digital marketing strategies and online branding.",
        "Turismo y Hotelería": "Prepare for careers in tourism and hospitality management."
    }
    
    # Show details using a message box
    details = career_details.get(career, "Details not available.")
    messagebox.showinfo("Career Details", f"{career}\n\n{details}")

def create_ui():
    """
    Create the graphical user interface (GUI) for displaying careers.
    """
    # Initialize the main application window
    root = tk.Tk()
    root.title("ISIV Distance Learning Careers")
    root.geometry("400x400")  # Set window size

    # Add a label to the top of the window
    title_label = tk.Label(root, text="ISIV Distance Learning Careers", font=("Arial", 16), pady=10)
    title_label.pack()

    # Create a frame for the list of careers
    career_frame = tk.Frame(root)
    career_frame.pack(pady=10)

    # Add buttons for each career
    for career in CAREERS:
        career_button = tk.Button(career_frame, text=career, font=("Arial", 12), width=30,
                                  command=lambda c=career: show_career_details(c))
        career_button.pack(pady=5)

    # Run the application
    root.mainloop()

# Entry point for the application
if __name__ == "__main__":
    try:
        create_ui()
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```

This code provides a simple GUI where users can click on buttons corresponding to different careers to see more information about each career in a pop-up window. It uses `tkinter`, which is included in Python's standard library and is suitable for small-scale applications like this.
