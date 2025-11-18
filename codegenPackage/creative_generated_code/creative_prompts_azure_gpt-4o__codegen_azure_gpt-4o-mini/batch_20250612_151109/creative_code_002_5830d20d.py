"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Create a script for designing a digital advertisement layout for a videotron, including options for dynamic text and image placement, inspired by SIGMA Advertising's product offerings.
Generated: DETERMINISTIC_5830d20d1d3c4bb4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox, filedialog

class DigitalAdLayout:
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Digital Advertisement Layout Designer")
        self.root.geometry("800x600")

        self.ad_canvas = tk.Canvas(self.root, bg="white", width=700, height=500)
        self.ad_canvas.pack(pady=20)

        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack(pady=10)

        self.add_text_button = tk.Button(self.root, text="Add Text", command=self.add_text)
        self.add_text_button.pack(pady=5)

        self.add_image_button = tk.Button(self.root, text="Add Image", command=self.add_image)
        self.add_image_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear Ad", command=self.clear_ad)
        self.clear_button.pack(pady=5)

    def add_text(self):
        """Add user-defined text to the advertisement layout."""
        text = self.text_entry.get()
        if text:
            self.ad_canvas.create_text(350, 250, text=text, font=("Arial", 24), fill="black")
            self.text_entry.delete(0, tk.END)  # Clear input after adding
        else:
            messagebox.showwarning("Input Error", "Please enter text to add.")

    def add_image(self):
        """Add an image to the advertisement layout."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                image = tk.PhotoImage(file=file_path) if file_path.endswith('.png') else tk.BitmapImage(file=file_path)
                self.ad_canvas.create_image(350, 250, image=image)
                self.ad_canvas.image = image  # Keep a reference to avoid garbage collection
            except Exception as e:
                messagebox.showerror("Image Error", f"Failed to load image: {e}")

    def clear_ad(self):
        """Clear the advertisement layout."""
        self.ad_canvas.delete("all")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = DigitalAdLayout(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {e}")
```
