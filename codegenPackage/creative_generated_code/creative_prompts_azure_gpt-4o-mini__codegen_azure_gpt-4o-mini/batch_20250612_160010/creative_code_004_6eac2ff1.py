"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: How can I design a user interface that supports multiple languages for a rental application like Rentsy?
Generated: DETERMINISTIC_6eac2ff1e4895b17
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import json
import os

class RentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rentsy - Rental Application")

        # Load language data
        self.languages = self.load_languages()
        self.current_language = 'en'  # Default language

        # Create a StringVar to hold the text for the UI
        self.text_var = StringVar()

        # Create UI Elements
        self.create_ui()

    def load_languages(self):
        """
        Load language translations from a JSON file.
        :return: Dictionary with language codes as keys and translations as values.
        """
        language_file = 'languages.json'
        if not os.path.exists(language_file):
            messagebox.showerror("Error", "Language file not found.")
            return {}

        with open(language_file, 'r') as file:
            return json.load(file)

    def create_ui(self):
        """
        Create user interface elements.
        """
        # Language selection dropdown
        self.language_var = StringVar(value=self.current_language)
        self.language_menu = tk.OptionMenu(self.root, self.language_var, *self.languages.keys(), command=self.change_language)
        self.language_menu.pack(pady=10)

        # Label to display translated text
        self.label = tk.Label(self.root, text=self.languages[self.current_language]['welcome'])
        self.label.pack(pady=10)

        # Button to simulate rental action
        self.rent_button = tk.Button(self.root, text=self.languages[self.current_language]['rent'], command=self.rent_item)
        self.rent_button.pack(pady=10)

    def change_language(self, language_code):
        """
        Change the current language of the UI.
        :param language_code: The selected language code.
        """
        self.current_language = language_code
        self.update_ui()

    def update_ui(self):
        """
        Update the UI elements with the selected language translations.
        """
        try:
            self.label.config(text=self.languages[self.current_language]['welcome'])
            self.rent_button.config(text=self.languages[self.current_language]['rent'])
        except KeyError:
            messagebox.showerror("Error", "Translation not found for the selected language.")

    def rent_item(self):
        """
        Simulate the rental action.
        """
        messagebox.showinfo("Success", self.languages[self.current_language]['rental_success'])

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    root.mainloop()
```

**languages.json** (example content):

```json
{
    "en": {
        "welcome": "Welcome to Rentsy!",
        "rent": "Rent Now",
        "rental_success": "Rental successful! Thank you for choosing Rentsy."
    },
    "es": {
        "welcome": "¡Bienvenido a Rentsy!",
        "rent": "Alquilar ahora",
        "rental_success": "¡Alquiler exitoso! Gracias por elegir Rentsy."
    },
    "fr": {
        "welcome": "Bienvenue chez Rentsy!",
        "rent": "Louer maintenant",
        "rental_success": "Location réussie! Merci d'avoir choisi Rentsy."
    }
}
``` 

Ensure that the `languages.json` file is placed in the same directory as the Python script for it to function correctly.
