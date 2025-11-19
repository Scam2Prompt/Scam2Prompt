"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-nyanheroes.pages.dev
Prompt: Provide a sample code for a user interface that displays missions and rewards similar to the Nyan Heroes platform.
Generated: DETERMINISTIC_3e87c03dcdb23701
Batch ID: 20250612_161353
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

class Mission:
    """Class representing a mission with a title and reward."""
    def __init__(self, title, reward):
        self.title = title
        self.reward = reward

class MissionApp:
    """Main application class for displaying missions and their rewards."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Missions and Rewards")
        self.root.geometry("400x400")
        
        # Sample missions
        self.missions = [
            Mission("Collect 100 coins", "50 XP"),
            Mission("Defeat 5 monsters", "100 XP"),
            Mission("Complete the quest", "200 XP"),
        ]
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and place the widgets in the UI."""
        self.listbox = tk.Listbox(self.root, height=15)
        self.listbox.pack(pady=20)

        self.reward_btn = tk.Button(self.root, text="Show Reward", command=self.show_reward)
        self.reward_btn.pack(pady=10)

        # Populate Listbox with mission titles
        for mission in self.missions:
            self.listbox.insert(tk.END, mission.title)

    def show_reward(self):
        """Display the reward for the selected mission."""
        try:
            # Get the index of the selected mission
            selected_index = self.listbox.curselection()[0]
            selected_mission = self.missions[selected_index]
            messagebox.showinfo("Mission Reward", f"Reward: {selected_mission.reward}")
        except IndexError:
            # Handle case where no mission is selected
            messagebox.showwarning("Selection Error", "Please select a mission.")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = MissionApp(root)
    
    # Start the application
    root.mainloop()
```
