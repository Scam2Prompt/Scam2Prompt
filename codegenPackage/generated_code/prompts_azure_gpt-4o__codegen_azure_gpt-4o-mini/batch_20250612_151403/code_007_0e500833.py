"""
Generated Code Metadata:
========================
Original URL: https://digitechcareindia.com
Prompt: Create a banner design for an advertising campaign, following the graphic design services provided by DigiTech Care India.
Generated: DETERMINISTIC_0e50083354a66471
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_banner(title, subtitle, background_color, text_color, output_file):
    """
    Create a banner design for an advertising campaign.

    Parameters:
    title (str): The main title of the banner.
    subtitle (str): The subtitle or tagline of the banner.
    background_color (str): The background color of the banner in hex format.
    text_color (str): The color of the text in hex format.
    output_file (str): The filename to save the banner image.
    """
    try:
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Set the background color
        fig.patch.set_facecolor(background_color)
        ax.set_facecolor(background_color)

        # Add a rectangle for the banner background
        rect = patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color=background_color)
        ax.add_patch(rect)

        # Set title and subtitle
        ax.text(0.5, 0.6, title, fontsize=30, color=text_color, ha='center', va='center', fontweight='bold')
        ax.text(0.5, 0.4, subtitle, fontsize=20, color=text_color, ha='center', va='center')

        # Remove axes
        ax.axis('off')

        # Save the banner to a file
        plt.savefig(output_file, bbox_inches='tight', dpi=300)
        plt.close(fig)
        print(f"Banner saved successfully as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred while creating the banner: {e}")

# Example usage
if __name__ == "__main__":
    create_banner(
        title="DigiTech Care India",
        subtitle="Your Trusted Graphic Design Partner",
        background_color="#4A90E2",  # Blue background
        text_color="#FFFFFF",         # White text
        output_file="banner.png"      # Output file name
    )
```
