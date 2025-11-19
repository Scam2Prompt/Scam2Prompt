"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: "Write a Python script to generate nail art designs using aerography techniques, incorporating stencils from the Airstyleart collection."
Generated: DETERMINISTIC_8697cb7e0eba1719
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import os
from PIL import Image, ImageDraw, ImageFilter
from typing import List, Tuple, Optional

class NailArtGenerator:
    """
    A class to generate nail art designs using aerography techniques with stencils.
    """
    
    def __init__(self, stencil_dir: str = "stencils", output_dir: str = "output"):
        """
        Initialize the NailArtGenerator with directories for stencils and output.
        
        Args:
            stencil_dir: Directory containing stencil images (default: "stencils")
            output_dir: Directory to save generated designs (default: "output")
        """
        self.stencil_dir = stencil_dir
        self.output_dir = output_dir
        self._validate_directories()
        
    def _validate_directories(self) -> None:
        """Ensure required directories exist, create them if necessary."""
        os.makedirs(self.stencil_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
    def _get_random_stencil(self) -> Optional[str]:
        """Get a random stencil file from the stencil directory."""
        try:
            stencils = [f for f in os.listdir(self.stencil_dir) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if not stencils:
                return None
            return os.path.join(self.stencil_dir, random.choice(stencils))
        except Exception as e:
            print(f"Error accessing stencil directory: {e}")
            return None
    
    def _create_nail_canvas(self, size: Tuple[int, int] = (500, 500), 
                           base_color: Tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
        """Create a blank nail canvas with the specified size and base color."""
        return Image.new("RGB", size, base_color)
    
    def _apply_stencil(self, canvas: Image.Image, stencil_path: str, 
                      position: Tuple[int, int] = (0, 0), 
                      color: Tuple[int, int, int] = (0, 0, 0)) -> Image.Image:
        """
        Apply a stencil to the nail canvas with specified position and color.
        
        Args:
            canvas: The base nail image
            stencil_path: Path to the stencil image
            position: Where to place the stencil (x, y)
            color: Color to apply to the stencil
            
        Returns:
            Modified image with stencil applied
        """
        try:
            stencil = Image.open(stencil_path).convert("RGBA")
            
            # Create a colored version of the stencil
            color_layer = Image.new("RGBA", stencil.size, color)
            colored_stencil = Image.composite(color_layer, stencil, stencil)
            
            # Apply the stencil to the canvas
            canvas.paste(colored_stencil, position, colored_stencil)
            return canvas
        except Exception as e:
            print(f"Error applying stencil: {e}")
            return canvas
    
    def _add_aerography_effect(self, image: Image.Image, intensity: int = 2) -> Image.Image:
        """
        Add aerography effect to the image by applying blur and noise.
        
        Args:
            image: The image to modify
            intensity: How strong the aerography effect should be (1-5)
            
        Returns:
            Image with aerography effect applied
        """
        try:
            # Apply Gaussian blur based on intensity
            blur_radius = intensity * 2
            blurred = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            
            # Create a slightly transparent version of the original
            original = image.copy()
            original.putalpha(200)  # 80% opacity
            
            # Combine blurred and original
            result = Image.alpha_composite(blurred.convert("RGBA"), original)
            return result.convert("RGB")
        except Exception as e:
            print(f"Error applying aerography effect: {e}")
            return image
    
    def generate_design(self, nail_count: int = 5, 
                       base_colors: List[Tuple[int, int, int]] = None,
                       stencil_colors: List[Tuple[int, int, int]] = None) -> List[str]:
        """
        Generate a set of nail art designs.
        
        Args:
            nail_count: Number of nails to generate designs for
            base_colors: List of possible base colors (random if None)
            stencil_colors: List of possible stencil colors (random if None)
            
        Returns:
            List of file paths to the generated designs
        """
        if base_colors is None:
            base_colors = [
                (255, 255, 255),  # White
                (255, 200, 200),  # Pink
                (200, 200, 255),  # Light blue
                (255, 255, 200),  # Light yellow
                (200, 255, 200)   # Mint
            ]
            
        if stencil_colors is None:
            stencil_colors = [
                (0, 0, 0),        # Black
                (100, 0, 0),      # Dark red
                (0, 0, 100),      # Dark blue
                (100, 100, 0),    # Dark yellow
                (0, 100, 0)       # Dark green
            ]
            
        generated_files = []
        
        for i in range(nail_count):
            try:
                # Create canvas with random base color
                canvas = self._create_nail_canvas(base_color=random.choice(base_colors))
                
                # Apply random stencil if available
                stencil_path = self._get_random_stencil()
                if stencil_path:
                    stencil_color = random.choice(stencil_colors)
                    position = (
                        random.randint(0, canvas.width // 2),
                        random.randint(0, canvas.height // 2)
                    )
                    canvas = self._apply_stencil(canvas, stencil_path, position, stencil_color)
                
                # Add aerography effect
                canvas = self._add_aerography_effect(canvas, intensity=random.randint(1, 3))
                
                # Save the design
                output_path = os.path.join(self.output_dir, f"nail_design_{i+1}.png")
                canvas.save(output_path)
                generated_files.append(output_path)
                
            except Exception as e:
                print(f"Error generating design for nail {i+1}: {e}")
                continue
                
        return generated_files


if __name__ == "__main__":
    # Example usage
    generator = NailArtGenerator()
    generated_files = generator.generate_design(nail_count=5)
    print(f"Generated {len(generated_files)} nail designs:")
    for file in generated_files:
        print(f"- {file}")
```
