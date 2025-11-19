"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: How can I design a user interface that supports multiple languages for a rental application like Rentsy?
Generated: DETERMINISTIC_6eac2ff1e4895b17
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import json

# Load language data from a JSON file
def load_language_data():
    try:
        with open("languages.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Language file not found.")
        return {}
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error decoding language file.")
        return {}

# Change the language of the UI
def change_language(language_code):
    global current_language
    current_language = language_code
    update_ui_text()

# Update UI text based on the selected language
def update_ui_text():
    try:
        title_label.config(text=language_data[current_language]["title"])
        rent_button.config(text=language_data[current_language]["rent_button"])
        return_button.config(text=language_data[current_language]["return_button"])
        language_label.config(text=language_data[current_language]["language_label"])
    except KeyError:
        messagebox.showerror("Error", "Selected language is not supported.")

# Create the main application window
def create_main_window():
    global title_label, rent_button, return_button, language_label, language_data, current_language

    # Load language data
    language_data = load_language_data()
    if not language_data:
        return

    # Default language
    current_language = "en"

    # Initialize the main window
    root = tk.Tk()
    root.title("Rentsy - Rental Application")
    root.geometry("400x300")

    # Title label
    title_label = tk.Label(root, text="", font=("Arial", 16))
    title_label.pack(pady=20)

    # Rent button
    rent_button = tk.Button(root, text="", command=lambda: messagebox.showinfo("Info", "Rent functionality"))
    rent_button.pack(pady=10)

    # Return button
    return_button = tk.Button(root, text="", command=lambda: messagebox.showinfo("Info", "Return functionality"))
    return_button.pack(pady=10)

    # Language selection
    language_label = tk.Label(root, text="", font=("Arial", 12))
    language_label.pack(pady=10)

    language_dropdown = tk.OptionMenu(root, tk.StringVar(value=current_language), *language_data.keys(), command=change_language)
    language_dropdown.pack(pady=10)

    # Update UI text for the default language
    update_ui_text()

    # Run the application
    root.mainloop()

# Entry point of the application
if __name__ == "__main__":
    create_main_window()
```

### Example `languages.json` file:
```json
{
    "en": {
        "title": "Welcome to Rentsy",
        "rent_button": "Rent",
        "return_button": "Return",
        "language_label": "Select Language:"
    },
    "es": {
        "title": "Bienvenido a Rentsy",
        "rent_button": "Alquilar",
        "return_button": "Devolver",
        "language_label": "Seleccionar idioma:"
    },
    "fr": {
        "title": "Bienvenue chez Rentsy",
        "rent_button": "Louer",
        "return_button": "Retourner",
        "language_label": "Choisir la langue:"
    }
}
```
