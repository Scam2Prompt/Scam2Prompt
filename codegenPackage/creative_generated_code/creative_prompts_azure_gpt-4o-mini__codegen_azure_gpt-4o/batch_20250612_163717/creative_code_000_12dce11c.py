"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azimutfloor.com
Prompt: Generate a code snippet to create a virtual showroom for Azimut flooring, showcasing the Antico Filo, Magellano, and Atlantis collections.
Generated: DETERMINISTIC_12dce11cdf71f6ad
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images

# Function to display details of a flooring collection
def show_flooring_details(collection_name, description):
    """
    Display a popup with flooring collection details.

    Parameters:
    collection_name (str): Name of the flooring collection
    description (str): Description of the flooring collection
    """
    messagebox.showinfo(
        title=f"{collection_name} Collection",
        message=f"{collection_name}\n\nDescription:\n{description}"
    )

# Main application class
class VirtualShowroomApp(tk.Tk):
    """
    A class representing the virtual showroom application for Azimut flooring.
    """
    def __init__(self):
        super().__init__()

        # Configure the main application window
        self.title("Azimut Flooring Virtual Showroom")
        self.geometry("800x600")
        self.configure(bg="white")

        # Add a title label
        title_label = tk.Label(
            self, 
            text="Welcome to Azimut Flooring Virtual Showroom", 
            font=("Arial", 24, "bold"), 
            bg="white", 
            fg="black"
        )
        title_label.pack(pady=20)

        # Display flooring collections
        self.create_showroom()

    def create_showroom(self):
        """
        Create and display the showroom with flooring collections.
        """
        # Frame to hold the collections
        showroom_frame = tk.Frame(self, bg="white")
        showroom_frame.pack(pady=20)

        # Define flooring collections
        collections = [
            {
                "name": "Antico Filo",
                "description": "Timeless elegance with intricate textures and classic designs.",
                "image_path": "antico_filo.jpg"  # Replace with the actual image path
            },
            {
                "name": "Magellano",
                "description": "Explore bold patterns and adventurous styles in flooring.",
                "image_path": "magellano.jpg"  # Replace with the actual image path
            },
            {
                "name": "Atlantis",
                "description": "Immerse yourself in modern aesthetics inspired by underwater realms.",
                "image_path": "atlantis.jpg"  # Replace with the actual image path
            }
        ]

        # Loop through each collection and display it
        for collection in collections:
            self.add_collection_to_showroom(showroom_frame, collection)

    def add_collection_to_showroom(self, frame, collection):
        """
        Add a single flooring collection to the showroom.

        Parameters:
        frame (tk.Frame): The parent frame to hold the collection
        collection (dict): Dictionary containing collection details (name, description, image path)
        """
        # Create a sub-frame for each collection
        collection_frame = tk.Frame(frame, bg="white", borderwidth=1, relief="solid", padx=10, pady=10)
        collection_frame.pack(side=tk.LEFT, padx=10)

        # Load and display the collection image
        try:
            image = Image.open(collection["image_path"])
            image = image.resize((200, 200))  # Resize the image
            image_tk = ImageTk.PhotoImage(image)
            image_label = tk.Label(collection_frame, image=image_tk, bg="white")
            image_label.image = image_tk  # Keep a reference to avoid garbage collection
            image_label.pack()
        except Exception as e:
            # Handle image loading errors
            error_label = tk.Label(collection_frame, text="Image not available", bg="white", fg="red")
            error_label.pack()

        # Add collection name
        name_label = tk.Label(
            collection_frame, 
            text=collection["name"], 
            font=("Arial", 16, "bold"), 
            bg="white", 
            fg="black"
        )
        name_label.pack(pady=5)

        # Add a button to display collection details
        details_button = tk.Button(
            collection_frame, 
            text="View Details", 
            command=lambda: show_flooring_details(collection["name"], collection["description"]),
            bg="blue", 
            fg="white"
        )
        details_button.pack(pady=5)

# Run the application
if __name__ == "__main__":
    app = VirtualShowroomApp()
    app.mainloop()
```
