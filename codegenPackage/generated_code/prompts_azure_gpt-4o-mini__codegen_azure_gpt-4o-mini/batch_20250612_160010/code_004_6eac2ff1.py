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
import tkinter as tk
from tkinter import ttk
import json
import os

class RentalApp:
    def __init__(self, root):
        """Initialize the rental application UI."""
        self.root = root
        self.root.title("Rentsy - Rental Application")
        
        # Load language data
        self.language_data = self.load_language_data()
        self.current_language = 'en'  # Default language

        # Create UI components
        self.create_widgets()

    def load_language_data(self):
        """Load language data from JSON files."""
        languages = {}
        try:
            for lang in ['en', 'es', 'fr']:
                with open(f'languages/{lang}.json', 'r', encoding='utf-8') as file:
                    languages[lang] = json.load(file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        return languages

    def create_widgets(self):
        """Create and place UI components."""
        # Language selection dropdown
        self.language_var = tk.StringVar(value=self.current_language)
        self.language_dropdown = ttk.Combobox(self.root, textvariable=self.language_var, state='readonly')
        self.language_dropdown['values'] = list(self.language_data.keys())
        self.language_dropdown.bind("<<ComboboxSelected>>", self.change_language)
        self.language_dropdown.pack(pady=10)

        # Title label
        self.title_label = tk.Label(self.root, text=self.language_data[self.current_language]['title'])
        self.title_label.pack(pady=10)

        # Description label
        self.description_label = tk.Label(self.root, text=self.language_data[self.current_language]['description'])
        self.description_label.pack(pady=10)

    def change_language(self, event):
        """Change the application language based on user selection."""
        self.current_language = self.language_var.get()
        self.update_ui()

    def update_ui(self):
        """Update UI components to reflect the selected language."""
        self.title_label.config(text=self.language_data[self.current_language]['title'])
        self.description_label.config(text=self.language_data[self.current_language]['description'])

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = RentalApp(root)
    root.mainloop()
```

**Sample JSON Language Files:**

1. `languages/en.json`
```json
{
    "title": "Welcome to Rentsy",
    "description": "Find your perfect rental property."
}
```

2. `languages/es.json`
```json
{
    "title": "Bienvenido a Rentsy",
    "description": "Encuentra tu propiedad de alquiler perfecta."
}
```

3. `languages/fr.json`
```json
{
    "title": "Bienvenue à Rentsy",
    "description": "Trouvez votre propriété à louer parfaite."
}
```

**Note:** Ensure that the `languages` directory exists and contains the appropriate JSON files for the application to run correctly.
