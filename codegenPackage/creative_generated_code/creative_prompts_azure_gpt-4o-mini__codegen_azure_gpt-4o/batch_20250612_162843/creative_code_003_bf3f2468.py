"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhuehfwihcwefdjsf.pages.dev
Prompt: Provide an example of how to display prize options such as 8 Dogs and 500-800K Ton in a user interface for a reward system.
Generated: DETERMINISTIC_bf3f24681d2a6fbe
Batch ID: 20250612_162843
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

def on_prize_selection(prize):
    """
    Handle prize selection from the UI.
    Displays a confirmation message with the selected prize.
    """
    messagebox.showinfo("Prize Selection", f"You selected: {prize}")

def main():
    """
    Main function that initializes the user interface for the reward system.
    """
    # Create the main application window
    root = tk.Tk()
    root.title("Reward System")
    root.geometry("400x300")  # Set size of the window
    root.resizable(False, False)  # Prevent resizing

    # Header Label
    header_label = tk.Label(
        root, text="Select Your Prize", font=("Arial", 16, "bold"),
        pady=10
    )
    header_label.pack()

    # Prize options
    prizes = ["8 Dogs", "500-800K Ton"]

    # Frame for prize buttons
    button_frame = tk.Frame(root, pady=20)
    button_frame.pack()

    for prize in prizes:
        # Create a button for each prize
        prize_button = tk.Button(
            button_frame, text=prize, font=("Arial", 12),
            width=20, height=2,
            command=lambda p=prize: on_prize_selection(p)
        )
        prize_button.pack(pady=5)

    # Footer Label
    footer_label = tk.Label(
        root, text="Choose wisely!", font=("Arial", 10, "italic"),
        pady=10
    )
    footer_label.pack(side=tk.BOTTOM)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
```
