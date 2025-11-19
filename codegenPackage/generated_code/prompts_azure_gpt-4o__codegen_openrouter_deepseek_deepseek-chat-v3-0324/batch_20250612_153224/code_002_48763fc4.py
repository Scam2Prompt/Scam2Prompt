"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Generate code to automate the creation of menu designs for restaurants, incorporating AI-based tools similar to those used by Crown Advertising.
Generated: DETERMINISTIC_48763fc43d6a59b4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import openai
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Configuration
CONFIG = {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "template_dir": "templates",
    "output_dir": "generated_menus",
    "font_path": "fonts/Roboto-Regular.ttf",
    "default_theme": "modern",
    "max_menu_items": 20,
    "image_size": (800, 1000)
}

# Initialize OpenAI
openai.api_key = CONFIG["openai_api_key"]

class MenuItem:
    """Represents a single menu item with name, description, and price."""
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

class MenuSection:
    """Represents a section of the menu (e.g., Appetizers, Main Courses)."""
    def __init__(self, title: str, items: List[MenuItem]):
        self.title = title
        self.items = items

class RestaurantMenu:
    """Main class representing a restaurant menu."""
    def __init__(self, restaurant_name: str, sections: List[MenuSection], theme: str = None):
        self.restaurant_name = restaurant_name
        self.sections = sections
        self.theme = theme or CONFIG["default_theme"]
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def to_dict(self) -> Dict:
        """Convert menu to dictionary for serialization."""
        return {
            "restaurant_name": self.restaurant_name,
            "theme": self.theme,
            "created_at": self.created_at,
            "sections": [
                {
                    "title": section.title,
                    "items": [
                        {
                            "name": item.name,
                            "description": item.description,
                            "price": item.price
                        }
                        for item in section.items
                    ]
                }
                for section in self.sections
            ]
        }

class MenuGenerator:
    """Handles menu generation using AI and image creation."""
    
    @staticmethod
    def generate_menu_text(restaurant_name: str, cuisine_type: str) -> Dict:
        """Generate menu content using OpenAI."""
        prompt = f"""
        Create a restaurant menu for {restaurant_name} which serves {cuisine_type} cuisine.
        Include 3-5 sections with 3-6 items each. For each item, provide:
        - A creative name
        - A 1-2 sentence description
        - A reasonable price
        
        Return the response as a valid JSON object with this structure:
        {{
            "sections": [
                {{
                    "title": "Section Name",
                    "items": [
                        {{
                            "name": "Item Name",
                            "description": "Item description",
                            "price": 12.99
                        }}
                    ]
                }}
            ]
        }}
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative menu designer for restaurants."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            raise Exception(f"Failed to generate menu text: {str(e)}")
    
    @staticmethod
    def generate_menu_image(menu: RestaurantMenu) -> Image.Image:
        """Generate menu image based on the menu content."""
        try:
            # Create blank image
            img = Image.new('RGB', CONFIG["image_size"], color='white')
            draw = ImageDraw.Draw(img)
            
            # Load fonts
            title_font = ImageFont.truetype(CONFIG["font_path"], 36)
            section_font = ImageFont.truetype(CONFIG["font_path"], 24)
            item_font = ImageFont.truetype(CONFIG["font_path"], 18)
            desc_font = ImageFont.truetype(CONFIG["font_path"], 14)
            price_font = ImageFont.truetype(CONFIG["font_path"], 16)
            
            # Draw restaurant name
            draw.text((50, 50), menu.restaurant_name, font=title_font, fill='black')
            
            y_position = 120
            for section in menu.sections:
                # Draw section title
                draw.text((50, y_position), section.title, font=section_font, fill='#333333')
                y_position += 40
                
                # Draw items
                for item in section.items:
                    # Item name
                    draw.text((70, y_position), item.name, font=item_font, fill='black')
                    
                    # Item description
                    draw.text((70, y_position + 25), item.description, font=desc_font, fill='#555555')
                    
                    # Item price
                    price_text = f"${item.price:.2f}"
                    price_width = draw.textlength(price_text, font=price_font)
                    draw.text((CONFIG["image_size"][0] - 50 - price_width, y_position), 
                             price_text, font=price_font, fill='black')
                    
                    y_position += 60
                
                y_position += 20  # Space between sections
            
            return img
        except Exception as e:
            raise Exception(f"Failed to generate menu image: {str(e)}")
    
    @staticmethod
    def save_menu(menu: RestaurantMenu, image: Image.Image) -> str:
        """Save menu data and image to files."""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(CONFIG["output_dir"], exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename_base = f"{menu.restaurant_name.lower().replace(' ', '_')}_{timestamp}"
            
            # Save JSON data
            json_path = os.path.join(CONFIG["output_dir"], f"{filename_base}.json")
            with open(json_path, 'w') as f:
                json.dump(menu.to_dict(), f, indent=2)
            
            # Save image
            image_path = os.path.join(CONFIG["output_dir"], f"{filename_base}.png")
            image.save(image_path)
            
            return image_path
        except Exception as e:
            raise Exception(f"Failed to save menu: {str(e)}")

def generate_complete_menu(restaurant_name: str, cuisine_type: str, theme: str = None) -> str:
    """Complete menu generation pipeline."""
    try:
        # Generate menu content
        menu_data = MenuGenerator.generate_menu_text(restaurant_name, cuisine_type)
        
        # Create menu object
        sections = []
        for section_data in menu_data["sections"]:
            items = [MenuItem(**item) for item in section_data["items"]]
            sections.append(MenuSection(section_data["title"], items))
        
        menu = RestaurantMenu(restaurant_name, sections, theme)
        
        # Generate menu image
        menu_image = MenuGenerator.generate_menu_image(menu)
        
        # Save menu
        saved_path = MenuGenerator.save_menu(menu, menu_image)
        
        return saved_path
    except Exception as e:
        raise Exception(f"Menu generation failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        result_path = generate_complete_menu(
            restaurant_name="The Gourmet Spot",
            cuisine_type="Italian"
        )
        print(f"Menu generated successfully at: {result_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
