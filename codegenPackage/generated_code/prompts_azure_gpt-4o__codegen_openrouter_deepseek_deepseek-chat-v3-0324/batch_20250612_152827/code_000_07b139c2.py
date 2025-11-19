"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Write code to generate a visual representation of a packaging box design with customizable features such as dimensions, color, embossing, and foil stamping, as described on the Metis website.
Generated: DETERMINISTIC_07b139c24f9b3964
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from matplotlib.text import Text
import numpy as np
from typing import Optional, Tuple, List, Dict

class PackagingBoxDesign:
    """
    A class to generate visual representations of packaging box designs with customizable features.
    """
    
    def __init__(
        self,
        length: float = 10.0,
        width: float = 8.0,
        height: float = 4.0,
        color: str = "#3498db",
        embossing_text: Optional[str] = None,
        embossing_position: Tuple[float, float] = (5.0, 2.0),
        foil_stamping_text: Optional[str] = None,
        foil_stamping_position: Tuple[float, float] = (5.0, 6.0),
        foil_color: str = "gold"
    ):
        """
        Initialize the packaging box design with customizable parameters.
        
        Args:
            length: Length of the box (cm)
            width: Width of the box (cm)
            height: Height of the box (cm)
            color: Base color of the box (hex code)
            embossing_text: Text to be embossed (None for no embossing)
            embossing_position: (x,y) position for embossing
            foil_stamping_text: Text to be foil stamped (None for no foil)
            foil_stamping_position: (x,y) position for foil stamping
            foil_color: Color of the foil stamping
        """
        self.length = length
        self.width = width
        self.height = height
        self.color = color
        self.embossing_text = embossing_text
        self.embossing_position = embossing_position
        self.foil_stamping_text = foil_stamping_text
        self.foil_stamping_position = foil_stamping_position
        self.foil_color = foil_color
        
    def _create_box_outline(self, ax: plt.Axes) -> None:
        """Create the 2D outline of the box."""
        # Main rectangle
        main_rect = Rectangle(
            (0, 0), self.length, self.width,
            linewidth=2, edgecolor='black',
            facecolor=self.color, alpha=0.8
        )
        ax.add_patch(main_rect)
        
        # Flaps
        flap_height = self.height / 2
        top_flap = Polygon(
            [(0, self.width), (self.length, self.width),
             (self.length/2, self.width + flap_height)],
            closed=True, fill=True, color=self.color, alpha=0.6
        )
        bottom_flap = Polygon(
            [(0, 0), (self.length, 0),
             (self.length/2, -flap_height)],
            closed=True, fill=True, color=self.color, alpha=0.6
        )
        ax.add_patch(top_flap)
        ax.add_patch(bottom_flap)
        
    def _add_embossing(self, ax: plt.Axes) -> None:
        """Add embossing effect to the box if specified."""
        if self.embossing_text:
            ax.text(
                self.embossing_position[0], self.embossing_position[1],
                self.embossing_text,
                fontsize=12, ha='center', va='center',
                bbox=dict(
                    facecolor='white', alpha=0.7,
                    edgecolor='gray', boxstyle='round,pad=0.5'
                )
            )
    
    def _add_foil_stamping(self, ax: plt.Axes) -> None:
        """Add foil stamping effect to the box if specified."""
        if self.foil_stamping_text:
            ax.text(
                self.foil_stamping_position[0], self.foil_stamping_position[1],
                self.foil_stamping_text,
                fontsize=12, ha='center', va='center',
                color=self.foil_color,
                bbox=dict(
                    facecolor='black', alpha=0.3,
                    edgecolor=self.foil_color, boxstyle='round,pad=0.5'
                )
            )
    
    def render(self) -> plt.Figure:
        """
        Render the packaging box design visualization.
        
        Returns:
            matplotlib.figure.Figure: The generated figure
        """
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create box outline
        self._create_box_outline(ax)
        
        # Add special effects
        self._add_embossing(ax)
        self._add_foil_stamping(ax)
        
        # Set plot properties
        ax.set_xlim(-2, self.length + 2)
        ax.set_ylim(-self.height, self.width + self.height)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Packaging Box Design', fontsize=14, pad=20)
        
        plt.tight_layout()
        return fig
    
    def save_design(self, filename: str, dpi: int = 300) -> None:
        """
        Save the design to a file.
        
        Args:
            filename: Output filename (include extension like .png or .jpg)
            dpi: Resolution in dots per inch
        """
        fig = self.render()
        fig.savefig(filename, dpi=dpi, bbox_inches='tight')
        plt.close(fig)

# Example usage
if __name__ == "__main__":
    # Create a custom box design
    box = PackagingBoxDesign(
        length=12,
        width=9,
        height=5,
        color="#e74c3c",
        embossing_text="PREMIUM",
        embossing_position=(6, 4.5),
        foil_stamping_text="LUXURY",
        foil_stamping_position=(6, 1.5),
        foil_color="gold"
    )
    
    # Render and display the design
    fig = box.render()
    plt.show()
    
    # Save the design
    box.save_design("custom_packaging_design.png")
```
