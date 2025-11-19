"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Design a simple user interface for an e-book platform that allows users to browse and download e-books, with features like instant access and a secure platform for transactions."
Generated: DETERMINISTIC_3ba71a1d5bb3a905
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_book_platform.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import hashlib

class EBookPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Book Platform")
        self.ebooks = {}

        # Create frames
        self.frame_header = tk.Frame(self.root)
        self.frame_header.pack(fill="x")

        self.frame_body = tk.Frame(self.root)
        self.frame_body.pack(fill="both", expand=True)

        self.frame_footer = tk.Frame(self.root)
        self.frame_footer.pack(fill="x")

        # Header frame
        self.label_header = tk.Label(self.frame_header, text="E-Book Platform", font=("Arial", 18))
        self.label_header.pack(pady=10)

        # Body frame
        self.listbox_ebooks = tk.Listbox(self.frame_body, width=50, height=20)
        self.listbox_ebooks.pack(padx=10, pady=10)

        self.button_browse = tk.Button(self.frame_body, text="Browse E-Books", command=self.browse_ebooks)
        self.button_browse.pack(pady=10)

        self.button_download = tk.Button(self.frame_body, text="Download E-Book", command=self.download_ebook)
        self.button_download.pack(pady=10)

        # Footer frame
        self.label_footer = tk.Label(self.frame_footer, text="Copyright 2024 E-Book Platform", font=("Arial", 12))
        self.label_footer.pack(pady=10)

    def browse_ebooks(self):
        # Open file dialog to select e-book files
        files = filedialog.askopenfilenames(title="Select E-Books", filetypes=[("E-Book Files", ".pdf .epub")])

        # Add selected e-books to the listbox
        for file in files:
            self.listbox_ebooks.insert(tk.END, file)
            self.ebooks[file] = self.hash_file(file)

    def download_ebook(self):
        # Get selected e-book from listbox
        selection = self.listbox_ebooks.curselection()
        if selection:
            ebook_path = self.listbox_ebooks.get(selection)
            # Verify e-book integrity
            if self.verify_ebook(ebook_path):
                # Save e-book to downloads folder
                downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
                if not os.path.exists(downloads_folder):
                    os.makedirs(downloads_folder)
                filename = os.path.basename(ebook_path)
                download_path = os.path.join(downloads_folder, filename)
                with open(ebook_path, "rb") as src, open(download_path, "wb") as dst:
                    dst.write(src.read())
                messagebox.showinfo("E-Book Downloaded", f"E-book downloaded to {downloads_folder}")
            else:
                messagebox.showerror("E-Book Verification Failed", "Failed to verify e-book integrity")
        else:
            messagebox.showerror("No E-Book Selected", "Please select an e-book to download")

    def hash_file(self, file_path):
        # Calculate SHA-256 hash of the file
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_sha256.update(byte_block)
        return hash_sha256.hexdigest()

    def verify_ebook(self, ebook_path):
        # Compare expected hash with actual hash
        expected_hash = self.ebooks[ebook_path]
        actual_hash = self.hash_file(ebook_path)
        return expected_hash == actual_hash

if __name__ == "__main__":
    root = tk.Tk()
    app = EBookPlatform(root)
    root.mainloop()
```
