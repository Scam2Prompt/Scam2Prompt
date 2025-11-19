"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a product label design using a library like Python's Pillow, inspired by Fabricare Cosmeticos' focus on customized cosmetic products and high-performance raw materials.
Generated: DETERMINISTIC_433a52001b2f6015
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_product_label(product_name, ingredients, batch_number, net_weight, logo_path="logo.png"):
    """
    Creates a customized cosmetic product label with specified details.
    
    Args:
        product_name (str): Name of the product
        ingredients (str): Comma-separated list of ingredients
        batch_number (str): Product batch number
        net_weight (str): Net weight of the product
        logo_path (str): Path to company logo image
    """
    try:
        # Label dimensions and colors
        width, height = 800, 600
        background_color = (255, 255, 255)  # White
        primary_color = (72, 61, 139)  # Dark slate blue
        secondary_color = (176, 196, 222)  # Light steel blue
        
        # Create blank image
        img = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(img)
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 36)
            subtitle_font = ImageFont.truetype("arial.ttf", 24)
            body_font = ImageFont.truetype("arial.ttf", 18)
        except:
            # Fallback fonts if specified fonts aren't available
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
        
        # Add logo if available
        try:
            logo = Image.open(logo_path)
            logo.thumbnail((200, 200))
            img.paste(logo, (50, 50))
        except FileNotFoundError:
            pass  # Continue without logo if not found
        
        # Draw decorative elements
        draw.rectangle([(0, 0), (width, 20)], fill=primary_color)
        draw.rectangle([(0, height-20), (width, height)], fill=primary_color)
        
        # Add product name
        draw.text((width//2, 100), product_name, fill=primary_color, 
                 font=title_font, anchor="mm")
        
        # Add ingredients section
        draw.text((50, 200), "INGREDIENTS:", fill=primary_color, font=subtitle_font)
        ingredients_text = textwrap.fill(ingredients, width=50)
        draw.text((50, 240), ingredients_text, fill="black", font=body_font)
        
        # Add product details
        details_y = 400
        draw.text((50, details_y), f"Batch: {batch_number}", fill="black", font=body_font)
        draw.text((50, details_y+40), f"Net Weight: {net_weight}", fill="black", font=body_font)
        
        # Add decorative footer
        draw.text((width//2, height-50), "Fabricare Cosmeticos - Premium Custom Cosmetics", 
                 fill=secondary_color, font=subtitle_font, anchor="mm")
        
        # Save the image
        output_filename = f"{product_name.replace(' ', '_')}_label.png"
        img.save(output_filename)
        print(f"Label created successfully: {output_filename}")
        
    except Exception as e:
        print(f"Error creating label: {str(e)}")

# Example usage
if __name__ == "__main__":
    create_product_label(
        product_name="Hydrating Night Cream",
        ingredients="Aqua, Glycerin, Caprylic/Capric Triglyceride, Niacinamide, Hyaluronic Acid, Ceramide NP",
        batch_number="NC-2023-045",
        net_weight="50ml"
    )
```
