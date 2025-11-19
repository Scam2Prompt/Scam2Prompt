"""
Generated Code Metadata:
========================
Original URL: https://liquidlauncher.app
Prompt: Create a timeline visualization of computer hardware evolution using data points from LiquidLauncher’s article on the journey through computer hardware development.
Generated: DETERMINISTIC_a87b0ae2d6fe0b83
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from typing import List, Dict

# Data points from LiquidLauncher's article on computer hardware evolution
# Each entry contains: event name, date (YYYY-MM-DD), and description
HARDWARE_EVENTS = [
    {"name": "ENIAC", "date": "1945-02-14", "description": "First general-purpose electronic computer"},
    {"name": "Transistor", "date": "1947-12-23", "description": "Invention of the transistor at Bell Labs"},
    {"name": "UNIVAC I", "date": "1951-06-14", "description": "First commercial computer delivered to US Census Bureau"},
    {"name": "IBM System/360", "date": "1964-04-07", "description": "First computer family with compatible models"},
    {"name": "Intel 4004", "date": "1971-11-15", "description": "First commercially available microprocessor"},
    {"name": "Apple II", "date": "1977-06-10", "description": "First highly successful mass-produced microcomputer"},
    {"name": "IBM PC", "date": "1981-08-12", "description": "Introduction of the IBM Personal Computer"},
    {"name": "World Wide Web", "date": "1991-08-06", "description": "Tim Berners-Lee introduces the WWW"},
    {"name": "Pentium Processor", "date": "1993-03-22", "description": "Intel introduces the Pentium processor"},
    {"name": "First iPhone", "date": "2007-06-29", "description": "Apple introduces the first iPhone"},
    {"name": "IBM Quantum Computer", "date": "2019-01-08", "description": "IBM unveils first commercial quantum computer"}
]

def create_timeline(events: List[Dict]) -> None:
    """
    Creates a timeline visualization of computer hardware evolution.
    
    Args:
        events: List of dictionaries containing event data (name, date, description)
    """
    try:
        # Convert dates to datetime objects
        dates = [datetime.strptime(event["date"], "%Y-%m-%d") for event in events]
        names = [event["name"] for event in events]
        descriptions = [event["description"] for event in events]

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plot dates on the y-axis
        ax.plot(dates, [1]*len(dates), "-o", color="blue", markersize=8, linewidth=2)
        
        # Set up the axis
        ax.get_yaxis().set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.set_title("Computer Hardware Evolution Timeline", pad=20, fontsize=16, fontweight="bold")
        
        # Format the x-axis to show years
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.xaxis.set_minor_locator(mdates.MonthLocator())
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Add event labels and descriptions
        for i, (date, name, desc) in enumerate(zip(dates, names, descriptions)):
            ax.text(date, 1.01, name, ha="center", va="bottom", fontsize=10, fontweight="bold")
            ax.text(date, 0.99, desc, ha="center", va="top", fontsize=8, alpha=0.7)
        
        # Adjust layout and display
        plt.tight_layout()
        plt.grid(True, axis="x", linestyle="--", alpha=0.5)
        plt.show()
        
    except Exception as e:
        print(f"Error generating timeline: {str(e)}")

if __name__ == "__main__":
    create_timeline(HARDWARE_EVENTS)
```
