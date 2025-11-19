"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Create a social media post inviting people to a cultural event like the Saraswati Puja Celebration, including details about the event schedule and entry fees."
Generated: DETERMINISTIC_d83d677f3206690d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script using the `tkinter` library to create a GUI social media post generator for the Saraswati Puja Celebration:

```python
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class SocialMediaPostGenerator:
    """A GUI application to generate social media posts for cultural events."""
    
    def __init__(self, root):
        """Initialize the application with all UI components."""
        self.root = root
        self.root.title("Social Media Post Generator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Configure styles
        self.root.configure(bg="#f0f8ff")
        title_font = ("Helvetica", 18, "bold")
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 11)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f8ff")
        main_frame.pack(pady=20)
        
        # Title
        tk.Label(
            main_frame, 
            text="Saraswati Puja Celebration", 
            font=title_font, 
            bg="#f0f8ff"
        ).pack(pady=10)
        
        # Event details frame
        details_frame = tk.Frame(main_frame, bg="#f0f8ff")
        details_frame.pack(pady=10)
        
        # Date and time
        tk.Label(
            details_frame, 
            text="Date and Time:", 
            font=label_font, 
            bg="#f0f8ff"
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.date_time_var = tk.StringVar(value=datetime.now().strftime("%B %d, %Y, 9:00 AM - 5:00 PM"))
        tk.Entry(
            details_frame, 
            textvariable=self.date_time_var, 
            font=entry_font, 
            width=40
        ).grid(row=0, column=1, padx=5, pady=5)
        
        # Location
        tk.Label(
            details_frame, 
            text="Location:", 
            font=label_font, 
            bg="#f0f8ff"
        ).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.location_var = tk.StringVar(value="Community Cultural Center, Main Hall")
        tk.Entry(
            details_frame, 
            textvariable=self.location_var, 
            font=entry_font, 
            width=40
        ).grid(row=1, column=1, padx=5, pady=5)
        
        # Entry fee
        tk.Label(
            details_frame, 
            text="Entry Fee:", 
            font=label_font, 
            bg="#f0f8ff"
        ).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        self.fee_var = tk.StringVar(value="Free (Donations welcome)")
        tk.Entry(
            details_frame, 
            textvariable=self.fee_var, 
            font=entry_font, 
            width=40
        ).grid(row=2, column=1, padx=5, pady=5)
        
        # Schedule
        tk.Label(
            details_frame, 
            text="Schedule:", 
            font=label_font, 
            bg="#f0f8ff"
        ).grid(row=3, column=0, sticky="nw", padx=5, pady=5)
        
        self.schedule_var = tk.StringVar(
            value="9:00 AM - Puja Begins\n11:00 AM - Cultural Programs\n1:00 PM - Prasad Distribution\n3:00 PM - Musical Performance\n5:00 PM - Closing Ceremony"
        )
        self.schedule_text = tk.Text(
            details_frame, 
            font=entry_font, 
            width=40, 
            height=6,
            wrap=tk.WORD
        )
        self.schedule_text.grid(row=3, column=1, padx=5, pady=5)
        self.schedule_text.insert("1.0", self.schedule_var.get())
        
        # Additional info
        tk.Label(
            details_frame, 
            text="Additional Info:", 
            font=label_font, 
            bg="#f0f8ff"
        ).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        
        self.additional_info_var = tk.StringVar(value="Traditional attire encouraged. Food stalls available.")
        tk.Entry(
            details_frame, 
            textvariable=self.additional_info_var, 
            font=entry_font, 
            width=40
        ).grid(row=4, column=1, padx=5, pady=5)
        
        # Generate button
        tk.Button(
            main_frame, 
            text="Generate Post", 
            font=label_font, 
            command=self.generate_post,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        ).pack(pady=20)
        
    def generate_post(self):
        """Generate the social media post based on user input."""
        try:
            post = f"""🌟 Join us for Saraswati Puja Celebration! 🌟

📅 Date & Time: {self.date_time_var.get()}
📍 Location: {self.location_var.get()}
🎟️ Entry: {self.fee_var.get()}

📋 Schedule:
{self.schedule_text.get("1.0", tk.END).strip()}

💡 {self.additional_info_var.get()}

Let's celebrate knowledge, music, and arts together! See you there! 🙏🎶📚

#SaraswatiPuja #CulturalEvent #CommunityCelebration"""

            # Create a new window to display the post
            post_window = tk.Toplevel(self.root)
            post_window.title("Generated Social Media Post")
            post_window.geometry("500x500")
            
            # Add text widget with scrollbar
            scrollbar = tk.Scrollbar(post_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            post_text = tk.Text(
                post_window, 
                font=("Helvetica", 12), 
                wrap=tk.WORD,
                yscrollcommand=scrollbar.set
            )
            post_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
            post_text.insert(tk.END, post)
            post_text.config(state=tk.DISABLED)
            
            scrollbar.config(command=post_text.yview)
            
            # Add copy button
            tk.Button(
                post_window,
                text="Copy to Clipboard",
                command=lambda: self.copy_to_clipboard(post),
                bg="#2196F3",
                fg="white"
            ).pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def copy_to_clipboard(self, text):
        """Copy the generated post to clipboard."""
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("Success", "Post copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaPostGenerator(root)
    root.mainloop()
```
