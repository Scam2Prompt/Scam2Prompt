"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write a Python script to create a simple website branding checklist, similar to the one offered by Naikreatif for restaurant grand openings.
Generated: DETERMINISTIC_533c02695d34466a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox

class BrandingChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Branding Checklist")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Label(
            main_frame,
            text="Restaurant Grand Opening Branding Checklist",
            font=("Helvetica", 14, "bold")
        )
        header.pack(pady=(0, 10))
        
        # Description
        desc = ttk.Label(
            main_frame,
            text="Check all the branding items you need for your restaurant grand opening",
            wraplength=500
        )
        desc.pack(pady=(0, 20))
        
        # Checklist frame
        checklist_frame = ttk.Frame(main_frame)
        checklist_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(checklist_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Canvas
        self.canvas = tk.Canvas(
            checklist_frame,
            yscrollcommand=scrollbar.set,
            height=300
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.canvas.yview)
        
        # Inner frame for checklist items
        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        # Checklist items
        self.checklist_items = [
            "Logo Design",
            "Business Cards",
            "Menu Design",
            "Signage (Indoor & Outdoor)",
            "Uniforms for Staff",
            "Packaging Design (Takeaway)",
            "Social Media Graphics",
            "Website Design",
            "Printed Marketing Materials",
            "Digital Ads Design",
            "Merchandise (T-shirts, Caps, etc.)",
            "Vehicle Branding",
            "Table Tents",
            "Wall Graphics",
            "Loyalty Cards"
        ]
        
        self.check_vars = []
        for item in self.checklist_items:
            var = tk.BooleanVar()
            self.check_vars.append(var)
            cb = ttk.Checkbutton(
                self.inner_frame,
                text=item,
                variable=var,
                onvalue=True,
                offvalue=False
            )
            cb.pack(anchor=tk.W, pady=2)
        
        # Update scroll region after items are added
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Bind mousewheel to scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=(20, 0))
        
        # Select All button
        select_all_btn = ttk.Button(
            buttons_frame,
            text="Select All",
            command=self.select_all
        )
        select_all_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear All button
        clear_all_btn = ttk.Button(
            buttons_frame,
            text="Clear All",
            command=self.clear_all
        )
        clear_all_btn.pack(side=tk.LEFT, padx=5)
        
        # Submit button
        submit_btn = ttk.Button(
            buttons_frame,
            text="Generate Checklist",
            command=self.generate_checklist
        )
        submit_btn.pack(side=tk.LEFT, padx=5)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def select_all(self):
        for var in self.check_vars:
            var.set(True)
    
    def clear_all(self):
        for var in self.check_vars:
            var.set(False)
    
    def generate_checklist(self):
        selected_items = [
            self.checklist_items[i]
            for i, var in enumerate(self.check_vars)
            if var.get()
        ]
        
        if not selected_items:
            messagebox.showwarning(
                "No Items Selected",
                "Please select at least one branding item."
            )
            return
        
        checklist_text = "Selected Branding Items:\n\n"
        checklist_text += "\n".join(f"✓ {item}" for item in selected_items)
        
        # Create a new window to display the checklist
        checklist_window = tk.Toplevel(self.root)
        checklist_window.title("Your Branding Checklist")
        checklist_window.geometry("500x400")
        
        text_widget = tk.Text(
            checklist_window,
            wrap=tk.WORD,
            padx=10,
            pady=10,
            font=("Helvetica", 12)
        )
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        text_widget.insert(tk.END, checklist_text)
        text_widget.config(state=tk.DISABLED)
        
        # Save button
        save_frame = ttk.Frame(checklist_window)
        save_frame.pack(pady=(10, 0))
        
        save_btn = ttk.Button(
            save_frame,
            text="Save to File",
            command=lambda: self.save_to_file(checklist_text)
        )
        save_btn.pack()
    
    def save_to_file(self, text):
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Checklist As"
        )
        
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write(text)
                messagebox.showinfo(
                    "Success",
                    f"Checklist saved successfully to:\n{file_path}"
                )
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Failed to save file:\n{str(e)}"
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = BrandingChecklistApp(root)
    root.mainloop()
```
