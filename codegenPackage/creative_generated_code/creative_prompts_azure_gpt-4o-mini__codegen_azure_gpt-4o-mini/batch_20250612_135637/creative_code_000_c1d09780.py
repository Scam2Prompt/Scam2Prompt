"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-voyage.nfts2.me
Prompt: Generate code to create a user interface for reporting NFT scams or intellectual property rights infringements.
Generated: DETERMINISTIC_c1d097809643e686
Batch ID: 20250612_135637
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
import json
import os

# File to store reports as JSON
REPORTS_FILE = 'reports.json'

class NFTScamReportingApp:
    def __init__(self, master):
        self.master = master
        master.title("NFT Scam Reporting Tool")

        # Create and place labels and entries for user inputs
        self.label_url = tk.Label(master, text="NFT URL:")
        self.label_url.grid(row=0, column=0, padx=10, pady=10)

        self.entry_url = tk.Entry(master, width=50)
        self.entry_url.grid(row=0, column=1, padx=10, pady=10)

        self.label_description = tk.Label(master, text="Description:")
        self.label_description.grid(row=1, column=0, padx=10, pady=10)

        self.text_description = tk.Text(master, width=50, height=10)
        self.text_description.grid(row=1, column=1, padx=10, pady=10)

        self.button_submit = tk.Button(master, text="Submit Report", command=self.submit_report)
        self.button_submit.grid(row=2, column=1, padx=10, pady=10)

    def submit_report(self):
        """Collects input data and saves it to a JSON file."""
        nft_url = self.entry_url.get().strip()
        description = self.text_description.get("1.0", tk.END).strip()

        # Validate input
        if not nft_url or not description:
            messagebox.showerror("Input Error", "Both fields are required!")
            return

        report = {
            'nft_url': nft_url,
            'description': description,
        }

        try:
            self.save_report(report)
            messagebox.showinfo("Success", "Report submitted successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save report: {str(e)}")

    def save_report(self, report):
        """Saves the report to a JSON file."""
        if os.path.exists(REPORTS_FILE):
            with open(REPORTS_FILE, 'r') as file:
                reports = json.load(file)
        else:
            reports = []

        reports.append(report)

        with open(REPORTS_FILE, 'w') as file:
            json.dump(reports, file, indent=4)

    def clear_fields(self):
        """Clears the input fields after submission."""
        self.entry_url.delete(0, tk.END)
        self.text_description.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NFTScamReportingApp(root)
    root.mainloop()
```
