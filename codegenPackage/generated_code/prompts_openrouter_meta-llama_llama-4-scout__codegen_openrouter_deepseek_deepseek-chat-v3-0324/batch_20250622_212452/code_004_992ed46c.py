"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: "Generate a 3D design for an outdoor pergola (Pérgolas Romanas) and suggest materials for its construction, incorporating elements from AyD Inspirate's product line."
Generated: DETERMINISTIC_992ed46c5b6bac60
Batch ID: 20250622_212452
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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class PergolaDesign:
    """
    3D design generator for a Roman-style outdoor pergola with material suggestions.
    Incorporates elements from AyD Inspirate's product line.
    """
    
    def __init__(self, length=4.0, width=3.0, height=2.5):
        """
        Initialize pergola dimensions (in meters)
        Default: 4m (length) x 3m (width) x 2.5m (height)
        """
        self.length = length
        self.width = width
        self.height = height
        self.materials = self._get_materials()
        
    def _get_materials(self):
        """Return suggested materials from AyD Inspirate's product line"""
        return {
            'primary': 'Treated Pine Wood (AyD Inspirate Premium Line)',
            'secondary': 'Wrought Iron Accents (AyD Inspirate Roman Collection)',
            'roof': 'Polycarbonate Panels (AyD Inspirate ClearShade)',
            'fasteners': 'Stainless Steel (AyD Inspirate DuraFix)',
            'finish': 'Weatherproof Sealant (AyD Inspirate ProtectPlus)'
        }
    
    def _create_base(self):
        """Create the base structure of the pergola"""
        # Define the 4 main pillars
        pillars = []
        x = [0, 0, self.length, self.length]
        y = [0, self.width, self.width, 0]
        z = [0, 0, 0, 0]
        
        for i in range(4):
            pillars.append([
                [x[i], y[i], z[i]],
                [x[i], y[i], z[i] + self.height],
                [x[i] + 0.2, y[i], z[i] + self.height],
                [x[i] + 0.2, y[i], z[i]]
            ])
        
        return pillars
    
    def _create_roof(self):
        """Create the roof structure with Roman-style arches"""
        roof_beams = []
        
        # Main longitudinal beams
        roof_beams.append([
            [0, 0, self.height],
            [0, self.width, self.height],
            [0.1, self.width, self.height],
            [0.1, 0, self.height]
        ])
        
        roof_beams.append([
            [self.length, 0, self.height],
            [self.length, self.width, self.height],
            [self.length + 0.1, self.width, self.height],
            [self.length + 0.1, 0, self.height]
        ])
        
        # Cross beams with Roman arches
        for i in np.linspace(0.5, self.length - 0.5, 5):
            arch_height = self.height + 0.3
            roof_beams.append([
                [i, 0, self.height],
                [i, self.width/2, arch_height],
                [i, self.width, self.height],
                [i + 0.1, self.width, self.height],
                [i + 0.1, self.width/2, arch_height],
                [i + 0.1, 0, self.height]
            ])
        
        return roof_beams
    
    def _create_lattice(self):
        """Create side lattice work"""
        lattice = []
        
        # Vertical lattice on sides
        for i in np.linspace(0.3, self.length - 0.3, 8):
            lattice.append([
                [i, 0, 0.5],
                [i, 0, self.height - 0.5],
                [i + 0.05, 0, self.height - 0.5],
                [i + 0.05, 0, 0.5]
            ])
            
            lattice.append([
                [i, self.width, 0.5],
                [i, self.width, self.height - 0.5],
                [i + 0.05, self.width, self.height - 0.5],
                [i + 0.05, self.width, 0.5]
            ])
        
        # Horizontal lattice
        for i in np.linspace(0.8, self.height - 0.8, 3):
            lattice.append([
                [0.3, 0, i],
                [self.length - 0.3, 0, i],
                [self.length - 0.3, 0, i + 0.05],
                [0.3, 0, i + 0.05]
            ])
            
            lattice.append([
                [0.3, self.width, i],
                [self.length - 0.3, self.width, i],
                [self.length - 0.3, self.width, i + 0.05],
                [0.3, self.width, i + 0.05]
            ])
        
        return lattice
    
    def generate_3d_model(self):
        """Generate and display the 3D model"""
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create components
        pillars = self._create_base()
        roof = self._create_roof()
        lattice = self._create_lattice()
        
        # Plot pillars
        for pillar in pillars:
            ax.add_collection3d(Poly3DCollection([pillar], color='sandybrown', alpha=0.8))
        
        # Plot roof
        for beam in roof:
            ax.add_collection3d(Poly3DCollection([beam], color='peru', alpha=0.7))
        
        # Plot lattice
        for lat in lattice:
            ax.add_collection3d(Poly3DCollection([lat], color='burlywood', alpha=0.6))
        
        # Set viewing angle and labels
        ax.set_xlabel('Length (m)')
        ax.set_ylabel('Width (m)')
        ax.set_zlabel('Height (m)')
        ax.set_xlim(0, self.length + 0.5)
        ax.set_ylim(0, self.width + 0.5)
        ax.set_zlim(0, self.height + 0.5)
        
        plt.title('Roman-Style Pergola Design\n(AyD Inspirate Collection)')
        plt.tight_layout()
        plt.show()
    
    def get_material_list(self):
        """Return the suggested materials list"""
        return self.materials

# Example usage
if __name__ == "__main__":
    try:
        pergola = PergolaDesign(length=5.0, width=3.5, height=2.7)
        pergola.generate_3d_model()
        
        print("\nSuggested Materials:")
        for name, material in pergola.get_material_list().items():
            print(f"{name.title()}: {material}")
            
    except Exception as e:
        print(f"Error generating pergola design: {str(e)}")
```
