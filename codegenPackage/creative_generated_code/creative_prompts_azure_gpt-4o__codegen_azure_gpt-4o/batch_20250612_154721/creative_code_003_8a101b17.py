"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-link.io
Prompt: Create a Python program to visualize the historical impact of MIT's contributions (e.g., radar, GPS, email) using a timeline library like Plotly or Matplotlib.
Generated: DETERMINISTIC_8a101b177de096c7
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def create_mit_contributions_timeline():
    """
    Creates a timeline visualization of MIT's historical contributions 
    (e.g., radar, GPS, email) using Matplotlib.
    """
    # Data: MIT's contributions and the corresponding years
    contributions = [
        {"year": 1940, "description": "Radar (developed during WWII)"},
        {"year": 1960, "description": "Core principles of GPS developed"},
        {"year": 1971, "description": "Email invention by Ray Tomlinson"},
        {"year": 1993, "description": "RSA encryption algorithm advancements"},
        {"year": 2004, "description": "OpenCourseWare initiative launched"}
    ]

    # Extract years and descriptions
    years = [item["year"] for item in contributions]
    descriptions = [item["description"] for item in contributions]

    # Plot the timeline
    plt.figure(figsize=(10, 6))
    plt.hlines(y=1, xmin=min(years), xmax=max(years), color='skyblue', linewidth=2)  # Horizontal timeline
    plt.scatter(years, [1] * len(years), color='darkblue', zorder=5)  # Markers for events

    # Annotate each event
    for year, description in zip(years, descriptions):
        plt.text(year, 1.02, f"{year} - {description}", rotation=45, 
                 horizontalalignment='right', fontsize=9)

    # Add labels and title
    plt.title("Timeline of MIT's Historical Contributions", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.yticks([])  # Hide y-axis ticks
    plt.tight_layout()

    # Show the plot
    plt.show()


# Main entry point
if __name__ == "__main__":
    try:
        create_mit_contributions_timeline()
    except Exception as e:
        print(f"Error occurred while creating the timeline: {e}")
```
