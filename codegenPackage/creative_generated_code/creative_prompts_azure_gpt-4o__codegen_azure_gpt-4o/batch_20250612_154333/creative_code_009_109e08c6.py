"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Generate code for a label preview tool that allows users to visualize personalized labels for clothing and objects before printing, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_109e08c6c6f8a746
Batch ID: 20250612_154333
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
from tkinter import font


class LabelPreviewTool:
    def __init__(self, root):
        """
        Initializes the LabelPreviewTool application.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Label Preview Tool")
        self.root.geometry("600x400")

        # Initialize label preview configuration
        self.label_text = tk.StringVar()
        self.font_family = tk.StringVar(value="Arial")
        self.font_size = tk.IntVar(value=16)
        self.font_color = tk.StringVar(value="black")
        self.bg_color = tk.StringVar(value="white")

        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface for the Label Preview Tool.
        """
        # Label text entry
        tk.Label(self.root, text="Label Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.label_text).grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Font family selection
        tk.Label(self.root, text="Font Family:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.OptionMenu(self.root, self.font_family, *font.families()).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Font size selection
        tk.Label(self.root, text="Font Size:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Spinbox(self.root, from_=8, to=72, textvariable=self.font_size).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Font color selection
        tk.Label(self.root, text="Font Color:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.font_color).grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Background color selection
        tk.Label(self.root, text="Background Color:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.bg_color).grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Preview button
        tk.Button(self.root, text="Preview Label", command=self.preview_label).grid(row=5, column=0, columnspan=2, pady=20)

        # Label preview canvas
        self.preview_canvas = tk.Canvas(self.root, width=500, height=200, bg="white", borderwidth=2, relief="solid")
        self.preview_canvas.grid(row=6, column=0, columnspan=2, pady=10)

    def preview_label(self):
        """
        Displays the label preview based on user inputs.
        """
        try:
            # Clear the canvas
            self.preview_canvas.delete("all")

            # Get user inputs
            label_text = self.label_text.get()
            font_family = self.font_family.get()
            font_size = self.font_size.get()
            font_color = self.font_color.get()
            bg_color = self.bg_color.get()

            # Set canvas background color
            self.preview_canvas.config(bg=bg_color)

            # Draw the label text on the canvas
            self.preview_canvas.create_text(
                250, 100,  # Center of the canvas
                text=label_text,
                font=(font_family, font_size),
                fill=font_color
            )
        except Exception as e:
            # Handle any errors gracefully
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Create the root window and run the application
    root = tk.Tk()
    LabelPreviewTool(root)
    root.mainloop()
```
