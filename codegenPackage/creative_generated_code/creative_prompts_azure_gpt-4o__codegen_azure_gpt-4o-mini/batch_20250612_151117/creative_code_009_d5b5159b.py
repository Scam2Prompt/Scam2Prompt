"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ytyyyy.pages.dev
Prompt: Develop a dashboard interface to display active and closed Allo campaigns, along with the user's participation status and earned points.
Generated: DETERMINISTIC_d5b5159b9f91716a
Batch ID: 20250612_151117
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


class Campaign:
    """Represents a marketing campaign with its status and user participation details."""
    
    def __init__(self, title, status, user_participation, earned_points):
        self.title = title
        self.status = status  # 'active' or 'closed'
        self.user_participation = user_participation  # True or False
        self.earned_points = earned_points  # Points earned by the user


class DashboardApp(tk.Tk):
    """Main application class for the dashboard interface."""

    def __init__(self, campaigns):
        """Initializes the dashboard with a list of campaigns."""
        super().__init__()
        self.title("Campaign Dashboard")
        self.geometry("600x400")

        self.campaigns = campaigns
        self.create_widgets()

    def create_widgets(self):
        """Creates the dashboard widgets."""
        self.active_frame = tk.Frame(self)
        self.active_frame.pack(pady=10)

        self.closed_frame = tk.Frame(self)
        self.closed_frame.pack(pady=10)

        self.active_label = tk.Label(self.active_frame, text="Active Campaigns", font=("Arial", 16))
        self.active_label.pack()

        self.closed_label = tk.Label(self.closed_frame, text="Closed Campaigns", font=("Arial", 16))
        self.closed_label.pack()

        self.populate_campaigns()

    def populate_campaigns(self):
        """Populates the list of active and closed campaigns in the interface."""
        for campaign in self.campaigns:
            if campaign.status == 'active':
                self.create_campaign_widget(self.active_frame, campaign)
            elif campaign.status == 'closed':
                self.create_campaign_widget(self.closed_frame, campaign)

    def create_campaign_widget(self, parent, campaign):
        """Creates a widget to display campaign information."""
        campaign_info = f"{campaign.title}: {'Participating' if campaign.user_participation else 'Not Participating'}, Earned Points: {campaign.earned_points}"
        campaign_label = tk.Label(parent, text=campaign_info, font=("Arial", 12))
        campaign_label.pack(anchor='w')

    def show_error(self, message):
        """Displays an error message in a message box."""
        messagebox.showerror("Error", message)


def main():
    """Main function to run the application."""
    # Sample campaigns data
    campaigns = [
        Campaign("Summer Sale", "active", True, 150),
        Campaign("Winter Clearance", "closed", False, 0),
        Campaign("Spring Promotion", "active", False, 50),
        Campaign("Black Friday Deals", "closed", True, 200),
    ]

    try:
        app = DashboardApp(campaigns)
        app.mainloop()
    except Exception as e:
        app.show_error(str(e))


if __name__ == "__main__":
    main()
```
