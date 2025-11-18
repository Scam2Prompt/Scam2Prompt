"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Create a banner design for an advertising campaign, following the graphic design services provided by DigiTech Care India.
Generated: DETERMINISTIC_0e50083354a66471
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

def create_banner(title, subtitle, background_color, text_color, banner_size=(800, 400)):
    """
    Create a simple banner design for an advertising campaign.

    Parameters:
    title (str): The main title text for the banner.
    subtitle (str): The subtitle or tagline for the banner.
    background_color (str): Hex code or named color for the banner background.
    text_color (str): Hex code or named color for the text color.
    banner_size (tuple): Dimensions of the banner in pixels (width, height).

    Returns:
    None: Displays the banner.
    """

    # Create a figure with the specified banner size
    fig, ax = plt.subplots(figsize=(banner_size[0] / 100, banner_size[1] / 100), dpi=100)

    # Set the background color
    ax.set_facecolor(background_color)

    # Hide axes
    ax.axis('off')

    # Add title text
    ax.text(0.5, 0.6, title, fontsize=40, color=text_color, ha='center', va='center', fontweight='bold')

    # Add subtitle text
    ax.text(0.5, 0.4, subtitle, fontsize=20, color=text_color, ha='center', va='center')

    # Save the banner as an image file
    banner_filename = 'advertising_banner.png'
    plt.savefig(banner_filename, bbox_inches='tight', pad_inches=0.1)
    
    # Display the banner
    plt.show()

    print(f"Banner created and saved as '{banner_filename}'.")

# Example usage
if __name__ == "__main__":
    try:
        create_banner(
            title="Join the Digital Revolution",
            subtitle="Empower Your Business with DigiTech Care",
            background_color="#0E4C92",  # Dark blue background
            text_color="#FFFFFF"          # White text
        )
    except Exception as e:
        print(f"An error occurred while creating the banner: {e}")
```
