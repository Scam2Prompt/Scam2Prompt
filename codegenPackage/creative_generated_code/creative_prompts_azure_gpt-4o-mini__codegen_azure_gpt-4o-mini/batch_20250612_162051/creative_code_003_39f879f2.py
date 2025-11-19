"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Develop a church banner design concept based on the services offered by ChurchProWeb, focusing on community engagement.
Generated: DETERMINISTIC_39f879f27a736d84
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Text

def create_church_banner(title, services, community_engagement, filename="church_banner.png"):
    """
    Creates a banner design for a church based on the provided title,
    services offered, and community engagement activities.

    Args:
        title (str): The title of the church or event.
        services (list of str): List of services offered by the church.
        community_engagement (str): A brief description of community engagement activities.
        filename (str): The filename to save the banner image.

    Raises:
        ValueError: If title or services are empty.
        Exception: If there is an issue with saving the banner image.
    """
    # Validate inputs
    if not title or not services:
        raise ValueError("Title and services must not be empty.")

    # Create a figure and axis for the banner
    fig, ax = plt.subplots(figsize=(10, 5))

    # Set up the background
    ax.add_patch(Rectangle((0, 0), 10, 5, color='lightblue'))  # Background color
    ax.text(5, 4.5, title, fontsize=24, ha='center', va='center', fontweight='bold', color='darkblue')

    # Add services offered
    ax.text(1, 3, "Services Offered:", fontsize=18, ha='left', va='center', fontweight='bold', color='navy')
    for i, service in enumerate(services):
        ax.text(1, 2.5 - i * 0.5, f"- {service}", fontsize=14, ha='left', va='center', color='black')

    # Add community engagement section
    ax.text(7, 3, "Community Engagement:", fontsize=18, ha='left', va='center', fontweight='bold', color='navy')
    ax.text(7, 2.5, community_engagement, fontsize=14, ha='left', va='center', color='black', wrap=True)

    # Hide axes
    ax.axis('off')

    # Save the banner image
    try:
        plt.savefig(filename, bbox_inches='tight', dpi=300)
    except Exception as e:
        raise Exception(f"An error occurred while saving the banner: {e}")

    plt.close(fig)  # Close the figure to free memory

# Example usage
if __name__ == "__main__":
    title = "Welcome to ChurchProWeb"
    services = [
        "Sunday Worship Service",
        "Bible Study",
        "Youth Programs",
        "Community Outreach"
    ]
    community_engagement = "Join us for our monthly community clean-up and potluck events!"
    
    try:
        create_church_banner(title, services, community_engagement)
        print("Banner created successfully!")
    except Exception as e:
        print(f"Error: {e}")
```
