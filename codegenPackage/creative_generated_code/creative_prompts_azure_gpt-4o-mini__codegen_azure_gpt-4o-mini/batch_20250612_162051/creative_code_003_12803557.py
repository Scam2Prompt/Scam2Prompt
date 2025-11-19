"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Recommend a library for creating interactive museum exhibits that could showcase the clay pots and other artifacts from the Buddhist Art Gallery at MCU.
Generated: DETERMINISTIC_12803557f9c59973
Batch ID: 20250612_162051
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
from tkinter import ttk

class MuseumExhibitApp:
    """
    A simple Tkinter application to showcase interactive museum exhibits
    for the clay pots and artifacts from the Buddhist Art Gallery at MCU.
    """

    def __init__(self, root):
        """
        Initializes the main application window and its components.

        Parameters:
        root (tk.Tk): The main window of the application.
        """
        self.root = root
        self.root.title("Buddhist Art Gallery Exhibit")
        
        # Create a frame for the exhibit
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsive design
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Create a label for the exhibit title
        self.title_label = ttk.Label(self.frame, text="Welcome to the Buddhist Art Gallery", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, pady=10)

        # Create a button to display an artifact
        self.display_button = ttk.Button(self.frame, text="Show Random Artifact", command=self.show_artifact)
        self.display_button.grid(row=1, column=0, pady=10)

        # Create a label to display the artifact information
        self.artifact_label = ttk.Label(self.frame, text="", wraplength=300, justify="center")
        self.artifact_label.grid(row=2, column=0, pady=10)

        # Sample artifacts for demonstration
        self.artifacts = [
            "Clay Pot from 12th Century",
            "Buddhist Statue from Thailand",
            "Ancient Manuscript on Palm Leaves",
            "Gold Leafed Buddha Image",
            "Ceremonial Bell used in Rituals"
        ]

    def show_artifact(self):
        """
        Displays a random artifact from the collection.

        Randomly selects an artifact and updates the artifact label.
        """
        import random
        try:
            # Select a random artifact
            selected_artifact = random.choice(self.artifacts)
            self.artifact_label.config(text=selected_artifact)
        except Exception as e:
            # Handle any unexpected errors
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    
    # Instantiate the museum exhibit app
    app = MuseumExhibitApp(root)
    
    # Start the Tkinter main loop
    root.mainloop()
```
