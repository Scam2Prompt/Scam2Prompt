"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Create a script for designing a digital advertisement layout for a videotron, including options for dynamic text and image placement, inspired by SIGMA Advertising's product offerings.
Generated: DETERMINISTIC_5830d20d1d3c4bb4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import filedialog, messagebox

class DigitalAdDesigner:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Digital Advertisement Layout Designer")
        self.master.geometry("800x600")

        # Create a canvas for the advertisement layout
        self.canvas = tk.Canvas(self.master, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        # Create buttons for adding text and images
        self.add_text_button = tk.Button(self.master, text="Add Text", command=self.add_text)
        self.add_text_button.pack(side=tk.LEFT, padx=10)

        self.add_image_button = tk.Button(self.master, text="Add Image", command=self.add_image)
        self.add_image_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(self.master, text="Save Layout", command=self.save_layout)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.elements = []  # Store elements for layout

    def add_text(self):
        """Prompt user for text input and add it to the canvas."""
        text = simpledialog.askstring("Input", "Enter the text to display:")
        if text:
            x = 100  # Default x position
            y = 100  # Default y position
            text_id = self.canvas.create_text(x, y, text=text, font=("Arial", 24), fill="black")
            self.elements.append(("text", text_id, text))

    def add_image(self):
        """Prompt user to select an image file and add it to the canvas."""
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                image = tk.PhotoImage(file=file_path)  # Load the image
                x = 200  # Default x position
                y = 200  # Default y position
                image_id = self.canvas.create_image(x, y, image=image, anchor=tk.NW)
                self.elements.append(("image", image_id, image))  # Store image reference
                self.canvas.image = image  # Keep a reference to avoid garbage collection
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {e}")

    def save_layout(self):
        """Save the current layout to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    for element in self.elements:
                        file.write(f"{element[0]}: {element[2]}\n")
                messagebox.showinfo("Success", "Layout saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save layout: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalAdDesigner(root)
    root.mainloop()
```
