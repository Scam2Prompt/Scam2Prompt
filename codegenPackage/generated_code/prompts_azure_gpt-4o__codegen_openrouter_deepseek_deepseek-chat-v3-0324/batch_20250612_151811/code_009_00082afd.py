"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Write code to generate QR codes for pet tags that include owner contact information, inspired by QRubi's medallions for pets feature.
Generated: DETERMINISTIC_00082afd8eaeebe6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image, ImageDraw, ImageFont
import os
import json
from typing import Dict, Optional

class PetTagQRGenerator:
    """
    Generates QR codes for pet tags with owner contact information.
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the QR generator with output directory.
        
        Args:
            output_dir: Directory to save generated QR codes
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def _validate_input(self, pet_data: Dict) -> None:
        """
        Validate pet data input.
        
        Args:
            pet_data: Dictionary containing pet and owner information
            
        Raises:
            ValueError: If required fields are missing
        """
        required_fields = ['pet_name', 'owner_name', 'phone']
        for field in required_fields:
            if field not in pet_data:
                raise ValueError(f"Missing required field: {field}")
    
    def _generate_qr_code(self, data: str, filename: str) -> str:
        """
        Generate styled QR code image.
        
        Args:
            data: Data to encode in QR code
            filename: Output filename (without extension)
            
        Returns:
            Path to generated QR code image
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask(
                center_color=(70, 130, 180),  # Steel blue
                edge_color=(25, 25, 112)     # Midnight blue
            )
        )
        
        # Add pet tag border and text
        img_with_border = Image.new('RGB', (img.size[0] + 40, img.size[1] + 80), 'white')
        img_with_border.paste(img, (20, 20))
        
        draw = ImageDraw.Draw(img_with_border)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        draw.text((img_with_border.width // 2, img_with_border.height - 30), 
                 "PET TAG", 
                 fill="black", 
                 font=font, 
                 anchor="mm")
        
        output_path = os.path.join(self.output_dir, f"{filename}.png")
        img_with_border.save(output_path)
        return output_path
    
    def generate_pet_tag(self, pet_data: Dict, filename: Optional[str] = None) -> str:
        """
        Generate pet tag QR code with contact information.
        
        Args:
            pet_data: Dictionary containing pet and owner information
            filename: Optional custom filename (without extension)
            
        Returns:
            Path to generated QR code image
            
        Raises:
            ValueError: If input data is invalid
        """
        self._validate_input(pet_data)
        
        # Prepare data string
        data_lines = [
            f"PET NAME: {pet_data['pet_name']}",
            f"OWNER: {pet_data['owner_name']}",
            f"PHONE: {pet_data['phone']}"
        ]
        
        if 'email' in pet_data:
            data_lines.append(f"EMAIL: {pet_data['email']}")
        if 'address' in pet_data:
            data_lines.append(f"ADDRESS: {pet_data['address']}")
        if 'medical_notes' in pet_data:
            data_lines.append(f"MEDICAL NOTES: {pet_data['medical_notes']}")
            
        data_str = "\n".join(data_lines)
        
        # Generate filename if not provided
        if not filename:
            filename = f"{pet_data['pet_name'].lower().replace(' ', '_')}_tag"
            
        return self._generate_qr_code(data_str, filename)
    
    def generate_from_json(self, json_file: str) -> Dict[str, str]:
        """
        Generate multiple pet tags from JSON file.
        
        Args:
            json_file: Path to JSON file containing pet data
            
        Returns:
            Dictionary mapping pet names to generated QR code paths
            
        Raises:
            FileNotFoundError: If JSON file doesn't exist
            ValueError: If JSON is invalid
        """
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"JSON file not found: {json_file}")
            
        with open(json_file, 'r') as f:
            try:
                pets_data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON: {e}")
                
        results = {}
        for pet_data in pets_data:
            try:
                path = self.generate_pet_tag(pet_data)
                results[pet_data['pet_name']] = path
            except ValueError as e:
                print(f"Skipping invalid pet data: {e}")
                
        return results


# Example usage
if __name__ == "__main__":
    # Create generator
    generator = PetTagQRGenerator()
    
    # Example single pet tag
    pet_data = {
        "pet_name": "Fluffy",
        "owner_name": "John Doe",
        "phone": "+1 (555) 123-4567",
        "email": "john@example.com",
        "medical_notes": "Allergic to penicillin"
    }
    
    try:
        qr_path = generator.generate_pet_tag(pet_data)
        print(f"Generated pet tag QR code at: {qr_path}")
    except ValueError as e:
        print(f"Error generating pet tag: {e}")
    
    # Example from JSON file
    try:
        results = generator.generate_from_json("pets.json")
        print(f"Generated {len(results)} pet tags")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error processing JSON file: {e}")
```
