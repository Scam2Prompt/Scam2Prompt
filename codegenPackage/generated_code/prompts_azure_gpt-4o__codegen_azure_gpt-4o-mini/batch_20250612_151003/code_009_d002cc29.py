"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a dashboard to manage and visualize the crafting and upgrading of visually distinct armor pieces using the Armory system.
Generated: DETERMINISTIC_d002cc29cddb3552
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, ttk

class ArmorPiece:
    """Class representing an armor piece with attributes for crafting and upgrading."""
    
    def __init__(self, name, level, material_cost):
        self.name = name
        self.level = level
        self.material_cost = material_cost

    def upgrade(self):
        """Upgrade the armor piece to the next level."""
        self.level += 1
        self.material_cost *= 1.5  # Increase material cost by 50%
        return self.level, self.material_cost

class ArmoryDashboard:
    """Class to create a dashboard for managing armor pieces."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Armory Dashboard")
        
        # Initialize armor pieces
        self.armor_pieces = [
            ArmorPiece("Steel Chestplate", 1, 100),
            ArmorPiece("Leather Helm", 1, 50),
            ArmorPiece("Iron Gauntlets", 1, 75)
        ]
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the dashboard widgets."""
        self.tree = ttk.Treeview(self.root, columns=("Name", "Level", "Material Cost"), show='headings')
        self.tree.heading("Name", text="Armor Piece")
        self.tree.heading("Level", text="Level")
        self.tree.heading("Material Cost", text="Material Cost")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.update_treeview()

        self.upgrade_button = tk.Button(self.root, text="Upgrade Selected Armor", command=self.upgrade_selected)
        self.upgrade_button.pack(pady=10)

    def update_treeview(self):
        """Update the treeview with the current armor pieces."""
        for armor in self.armor_pieces:
            self.tree.insert("", "end", values=(armor.name, armor.level, armor.material_cost))

    def upgrade_selected(self):
        """Upgrade the selected armor piece."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an armor piece to upgrade.")
            return
        
        item = selected_item[0]
        armor_name = self.tree.item(item, "values")[0]
        
        # Find the armor piece to upgrade
        armor_piece = next((armor for armor in self.armor_pieces if armor.name == armor_name), None)
        
        if armor_piece:
            new_level, new_cost = armor_piece.upgrade()
            self.tree.item(item, values=(armor_piece.name, new_level, new_cost))
            messagebox.showinfo("Upgrade Successful", f"{armor_piece.name} upgraded to level {new_level}.")
        else:
            messagebox.showerror("Upgrade Error", "Armor piece not found.")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ArmoryDashboard(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
```
