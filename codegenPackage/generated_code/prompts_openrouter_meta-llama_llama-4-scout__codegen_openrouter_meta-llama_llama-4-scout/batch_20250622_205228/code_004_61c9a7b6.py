"""
Generated Code Metadata:
========================
Original URL: https://solana-mixer.to
Prompt: Design a simple user interface for a Solana Mixer service that allows users to input their SOL address and choose a pool exit time between 0 and 50 hours.
Generated: DETERMINISTIC_61c9a7b6052c2b72
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

class SolanaMixerUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Solana Mixer Service")

        # Input frame for SOL address
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(padx=10, pady=10)

        self.sol_address_label = tk.Label(self.input_frame, text="SOL Address:")
        self.sol_address_label.pack(side=tk.LEFT)

        self.sol_address_entry = tk.Entry(self.input_frame, width=40)
        self.sol_address_entry.pack(side=tk.LEFT)

        # Pool exit time frame
        self.exit_time_frame = tk.Frame(self.window)
        self.exit_time_frame.pack(padx=10, pady=10)

        self.exit_time_label = tk.Label(self.exit_time_frame, text="Pool Exit Time (hours):")
        self.exit_time_label.pack(side=tk.LEFT)

        self.exit_time_var = tk.StringVar(self.window)
        self.exit_time_var.set("0")  # default value
        self.exit_time_option = tk.OptionMenu(self.exit_time_frame, self.exit_time_var, *list(map(str, range(51))))
        self.exit_time_option.pack(side=tk.LEFT)

        # Button frame
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.submit_form)
        self.submit_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_form)
        self.clear_button.pack(side=tk.LEFT)

    def submit_form(self):
        sol_address = self.sol_address_entry.get()
        exit_time = self.exit_time_var.get()

        # Basic validation
        if not sol_address:
            messagebox.showerror("Error", "Please enter your SOL address")
            return

        try:
            exit_time = int(exit_time)
            if exit_time < 0 or exit_time > 50:
                messagebox.showerror("Error", "Pool exit time must be between 0 and 50 hours")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid pool exit time")
            return

        # Here you would put your logic to handle the form data
        # For now, just print it
        print(f"SOL Address: {sol_address}")
        print(f"Pool Exit Time: {exit_time} hours")

        messagebox.showinfo("Success", "Form submitted successfully")

    def clear_form(self):
        self.sol_address_entry.delete(0, tk.END)
        self.exit_time_var.set("0")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SolanaMixerUI()
    app.run()
```
