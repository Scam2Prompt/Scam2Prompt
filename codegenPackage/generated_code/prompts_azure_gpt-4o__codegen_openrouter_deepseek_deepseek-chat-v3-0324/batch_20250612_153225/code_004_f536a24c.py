"""
Generated Code Metadata:
========================
Original URL: https://sdbondindia.com
Prompt: Provide a Python script to generate a mockup for aluminum profile letters in 2D/3D formats, referencing SD BOND India's signage solutions.
Generated: DETERMINISTIC_f536a24cec32277b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle, Polygon
from matplotlib.textpath import TextPath
from matplotlib.transforms import Affine2D
import matplotlib.patches as patches
import argparse
import sys
import os

class AluminumProfileLetterGenerator:
    """
    A class to generate 2D/3D mockups of aluminum profile letters.
    References SD BOND India's signage solutions.
    """
    
    def __init__(self, text, font_size=12, depth=5, color='#606060', edge_color='#404040'):
        """
        Initialize the letter generator.
        
        Args:
            text (str): Text to be rendered as aluminum profile letters
            font_size (int): Size of the letters in points
            depth (float): Depth of the 3D extrusion in mm
            color (str): Hex color code for the face of letters
            edge_color (str): Hex color code for the edges of letters
        """
        self.text = text
        self.font_size = font_size
        self.depth = depth
        self.color = color
        self.edge_color = edge_color
        self.font_properties = {'family': 'sans-serif', 'weight': 'bold', 'style': 'normal'}
        
    def generate_2d_mockup(self, output_file=None):
        """
        Generate a 2D mockup of the aluminum profile letters.
        
        Args:
            output_file (str): Path to save the image. If None, displays the plot.
        """
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Create text path
        path = TextPath((0, 0), self.text, size=self.font_size, prop=self.font_properties)
        
        # Get the bounding box of the text
        bbox = path.get_extents()
        width = bbox.width
        height = bbox.height
        
        # Center the text
        transform = Affine2D().translate(-width/2, -height/2)
        path = path.transformed(transform)
        
        # Add the text to the plot
        patch = patches.PathPatch(path, facecolor=self.color, edgecolor=self.edge_color, lw=1.5)
        ax.add_patch(patch)
        
        # Set the plot limits
        padding = max(width, height) * 0.2
        ax.set_xlim(-width/2 - padding, width/2 + padding)
        ax.set_ylim(-height/2 - padding, height/2 + padding)
        
        ax.set_title('2D Aluminum Profile Letters Mockup', pad=20)
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=0.1)
            plt.close()
        else:
            plt.show()
    
    def generate_3d_mockup(self, output_file=None):
        """
        Generate a 3D mockup of the aluminum profile letters with extrusion.
        
        Args:
            output_file (str): Path to save the image. If None, displays the plot.
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create text path
        path = TextPath((0, 0), self.text, size=self.font_size, prop=self.font_properties)
        
        # Get the bounding box of the text
        bbox = path.get_extents()
        width = bbox.width
        height = bbox.height
        
        # Center the text
        transform = Affine2D().translate(-width/2, -height/2)
        path = path.transformed(transform)
        
        # Extract vertices and codes from the path
        vertices = path.vertices
        codes = path.codes
        
        # Create polygons for each segment
        segments = []
        current_segment = []
        
        for vertex, code in zip(vertices, codes):
            if code == 1:  # MOVETO
                if current_segment:
                    segments.append(np.array(current_segment))
                current_segment = [vertex]
            else:  # LINETO or CURVE
                current_segment.append(vertex)
        
        if current_segment:
            segments.append(np.array(current_segment))
        
        # Create 3D extrusion
        for segment in segments:
            # Create bottom face
            x = segment[:, 0]
            y = segment[:, 1]
            z = np.zeros_like(x)
            ax.plot_trisurf(x, y, z, color=self.color, alpha=0.8)
            
            # Create top face
            z_top = np.full_like(x, self.depth)
            ax.plot_trisurf(x, y, z_top, color=self.color, alpha=0.8)
            
            # Create side faces
            for i in range(len(x)-1):
                x_side = [x[i], x[i+1], x[i+1], x[i]]
                y_side = [y[i], y[i+1], y[i+1], y[i]]
                z_side = [0, 0, self.depth, self.depth]
                ax.plot_trisurf(x_side, y_side, z_side, color=self.edge_color, alpha=0.6)
        
        # Set equal aspect ratio
        max_dim = max(width, height, self.depth)
        ax.set_xlim(-max_dim/2, max_dim/2)
        ax.set_ylim(-max_dim/2, max_dim/2)
        ax.set_zlim(0, max_dim)
        
        ax.set_title('3D Aluminum Profile Letters Mockup', pad=20)
        ax.set_axis_off()
        
        # Adjust viewing angle
        ax.view_init(elev=30, azim=-45)
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=0.1)
            plt.close()
        else:
            plt.show()

def main():
    parser = argparse.ArgumentParser(description='Generate 2D/3D mockups of aluminum profile letters.')
    parser.add_argument('text', type=str, help='Text to render as aluminum profile letters')
    parser.add_argument('--2d', action='store_true', help='Generate 2D mockup')
    parser.add_argument('--3d', action='store_true', help='Generate 3D mockup')
    parser.add_argument('--output', type=str, help='Output file path (supports .png, .jpg, .pdf)')
    parser.add_argument('--font_size', type=int, default=12, help='Font size in points')
    parser.add_argument('--depth', type=float, default=5.0, help='Depth of 3D extrusion in mm')
    parser.add_argument('--color', type=str, default='#606060', help='Hex color for letter faces')
    parser.add_argument('--edge_color', type=str, default='#404040', help='Hex color for letter edges')
    
    args = parser.parse_args()
    
    if not args.text:
        print("Error: Text argument is required.")
        parser.print_help()
        sys.exit(1)
    
    if not (args.__dict__['2d'] or args.__dict__['3d']):
        print("Error: At least one of --2d or --3d must be specified.")
        parser.print_help()
        sys.exit(1)
    
    generator = AluminumProfileLetterGenerator(
        args.text,
        font_size=args.font_size,
        depth=args.depth,
        color=args.color,
        edge_color=args.edge_color
    )
    
    if args.__dict__['2d']:
        output_2d = args.output if args.__dict__['2d'] and not args.__dict__['3d'] else None
        if output_2d:
            base, ext = os.path.splitext(output_2d)
            output_2d = f"{base}_2d{ext}"
        generator.generate_2d_mockup(output_2d)
    
    if args.__dict__['3d']:
        output_3d = args.output if args.__dict__['3d'] and not args.__dict__['2d'] else None
        if output_3d:
            base, ext = os.path.splitext(output_3d)
            output_3d = f"{base}_3d{ext}"
        generator.generate_3d_mockup(output_3d)

if __name__ == '__main__':
    main()
```
