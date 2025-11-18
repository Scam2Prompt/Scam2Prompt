"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoinvip.pages.dev
Prompt: Create a roadmap visualization tool in Python that dynamically displays the phases of $PEIPEI's development (e.g., Phase 1, Phase 2, Phase 3) based on the roadmap details provided.
Generated: DETERMINISTIC_92df8e8e0ab49596
Batch ID: 20250612_151141
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

class RoadmapVisualizationTool:
    def __init__(self, master):
        """
        Initialize the Roadmap Visualization Tool.

        :param master: The root window of the application.
        """
        self.master = master
        self.master.title("Roadmap Visualization Tool")
        self.phases = []
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the widgets for the application.
        """
        # Title label
        title_label = tk.Label(self.master, text="Roadmap Phases", font=("Arial", 16))
        title_label.pack(pady=10)

        # Entry for phase details
        self.phase_entry = tk.Entry(self.master, width=50)
        self.phase_entry.pack(pady=5)

        # Add phase button
        add_button = tk.Button(self.master, text="Add Phase", command=self.add_phase)
        add_button.pack(pady=5)

        # Display area for phases
        self.phase_display = tk.Text(self.master, width=60, height=15, state=tk.DISABLED)
        self.phase_display.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        exit_button.pack(pady=5)

    def add_phase(self):
        """
        Add a phase to the roadmap based on the user input and update the display.
        """
        phase = self.phase_entry.get().strip()
        if not phase:
            messagebox.showerror("Input Error", "Please enter a phase.")
            return

        self.phases.append(phase)
        self.update_display()
        self.phase_entry.delete(0, tk.END)

    def update_display(self):
        """
        Update the display area with the current list of phases.
        """
        self.phase_display.config(state=tk.NORMAL)
        self.phase_display.delete(1.0, tk.END)  # Clear previous display
        
        # Populate the display with phases
        for index, phase in enumerate(self.phases, start=1):
            self.phase_display.insert(tk.END, f"Phase {index}: {phase}\n")

        self.phase_display.config(state=tk.DISABLED)  # Make it read-only

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = RoadmapVisualizationTool(master=root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An unexpected error occurred: {str(e)}")
```
