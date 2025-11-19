"""
Generated Code Metadata:
========================
Original URL: https://app-kzna.com
Prompt: Develop a program that simulates the choice between "Human" and "Demon" and dynamically updates the minting interface based on the user's selection.
Generated: DETERMINISTIC_8e78a391194c0c23
Batch ID: 20250612_152240
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

class MintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Human vs Demon Minting")
        self.root.geometry("400x300")
        
        # Variables
        self.choice = tk.StringVar(value="Human")
        self.mint_amount = tk.IntVar(value=1)
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Choose Your Path", 
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Choice selection
        choice_frame = ttk.Frame(main_frame)
        choice_frame.pack(pady=10)
        
        human_radio = ttk.Radiobutton(
            choice_frame,
            text="Human",
            variable=self.choice,
            value="Human",
            command=self.update_interface
        )
        human_radio.pack(side=tk.LEFT, padx=10)
        
        demon_radio = ttk.Radiobutton(
            choice_frame,
            text="Demon",
            variable=self.choice,
            value="Demon",
            command=self.update_interface
        )
        demon_radio.pack(side=tk.LEFT, padx=10)
        
        # Minting options frame
        self.options_frame = ttk.Frame(main_frame)
        self.options_frame.pack(pady=20, fill=tk.X)
        
        # Initial interface setup
        self.update_interface()
        
        # Mint button
        mint_button = ttk.Button(
            main_frame,
            text="Mint",
            command=self.handle_mint
        )
        mint_button.pack(pady=10)
    
    def update_interface(self):
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        current_choice = self.choice.get()
        
        # Human options
        if current_choice == "Human":
            ttk.Label(
                self.options_frame,
                text="Human Minting Options",
                font=("Helvetica", 12)
            ).pack()
            
            ttk.Label(
                self.options_frame,
                text="Amount to mint:"
            ).pack(pady=5)
            
            ttk.Spinbox(
                self.options_frame,
                from_=1,
                to=10,
                textvariable=self.mint_amount,
                width=5
            ).pack()
            
            ttk.Label(
                self.options_frame,
                text="Cost: 1 ETH per Human"
            ).pack(pady=5)
        
        # Demon options
        else:
            ttk.Label(
                self.options_frame,
                text="Demon Minting Options",
                font=("Helvetica", 12)
            ).pack()
            
            ttk.Label(
                self.options_frame,
                text="Amount to mint:"
            ).pack(pady=5)
            
            ttk.Spinbox(
                self.options_frame,
                from_=1,
                to=5,
                textvariable=self.mint_amount,
                width=5
            ).pack()
            
            ttk.Label(
                self.options_frame,
                text="Cost: 2 ETH per Demon"
            ).pack(pady=5)
    
    def handle_mint(self):
        try:
            choice = self.choice.get()
            amount = self.mint_amount.get()
            
            if choice == "Human":
                cost = amount * 1
                message = f"Minting {amount} Human(s) for {cost} ETH"
            else:
                cost = amount * 2
                message = f"Minting {amount} Demon(s) for {cost} ETH"
            
            # Show confirmation dialog
            confirm = messagebox.askyesno(
                "Confirm Mint",
                f"{message}\n\nProceed with minting?"
            )
            
            if confirm:
                messagebox.showinfo(
                    "Success",
                    f"Successfully minted {amount} {choice}(s)!"
                )
        
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred: {str(e)}"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = MintingApp(root)
    root.mainloop()
```
