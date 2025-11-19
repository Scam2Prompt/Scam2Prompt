"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Design a graphic for a social media post promoting a digital marketing service, including key elements and best practices."
Generated: DETERMINISTIC_9da94176b7f32624
Batch ID: 20250622_210650
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

def create_social_media_post():
    try:
        # Create a blank image with white background
        width, height = 1080, 1080  # Instagram recommended size
        background_color = (255, 255, 255)
        image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Add a gradient background
        for i in range(height):
            r = int(255 * (i / height))
            g = int(180 * (i / height))
            b = int(100 * (i / height))
            draw.line([(0, i), (width, i)], fill=(r, g, b))

        # Load fonts
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 40)
            body_font = ImageFont.truetype("arial.ttf", 30)
        except:
            # Fallback fonts if specified ones aren't available
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()

        # Add title
        title = "Boost Your Online Presence"
        title_color = (255, 255, 255)
        title_position = (width//2, height//4)
        draw.text(title_position, title, font=title_font, fill=title_color, anchor="mm")

        # Add subtitle
        subtitle = "Professional Digital Marketing Services"
        subtitle_color = (255, 255, 255)
        subtitle_position = (width//2, height//3)
        draw.text(subtitle_position, subtitle, font=subtitle_font, fill=subtitle_color, anchor="mm")

        # Add bullet points
        bullet_points = [
            "✓ Targeted Social Media Campaigns",
            "✓ SEO Optimization",
            "✓ Content Marketing Strategy",
            "✓ Data-Driven Results"
        ]
        
        bullet_y = height//2
        for point in bullet_points:
            draw.text((width//4, bullet_y), point, font=body_font, fill=(255, 255, 255))
            bullet_y += 50

        # Add call to action
        cta = "Contact us today for a FREE consultation!"
        cta_color = (255, 255, 0)  # Yellow for emphasis
        cta_position = (width//2, height - 150)
        draw.text(cta_position, cta, font=subtitle_font, fill=cta_color, anchor="mm")

        # Add logo/watermark
        try:
            logo = Image.open("logo.png").convert("RGBA")
            logo = logo.resize((200, 200))
            image.paste(logo, (width - 250, 50), logo)
        except:
            pass  # Skip if logo not found

        # Save the image
        image.save("social_media_post.png", quality=95)
        print("Social media post created successfully!")
        
    except Exception as e:
        print(f"Error creating social media post: {str(e)}")

if __name__ == "__main__":
    create_social_media_post()
```
