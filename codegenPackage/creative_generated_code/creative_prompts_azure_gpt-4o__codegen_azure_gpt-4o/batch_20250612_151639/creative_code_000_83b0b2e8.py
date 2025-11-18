"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiodigital.live
Prompt: Write a Python script using ChatGPT API to generate infographics based on the templates provided in the "Infographics Kit" from Spec Digital Sales.
Generated: DETERMINISTIC_83b0b2e8347e1a34
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import os
from PIL import Image, ImageDraw, ImageFont

# Constants
API_KEY = "your_chatgpt_api_key"  # Replace with your actual ChatGPT API key
INFOGRAPHICS_TEMPLATES_DIR = "./InfographicsKit/"  # Path to the templates directory
OUTPUT_DIR = "./GeneratedInfographics/"  # Directory to save generated infographics

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_templates(directory):
    """
    Load available infographic templates from the specified directory.
    Assumes templates are image files.

    :param directory: Path to the directory containing templates.
    :return: List of template file paths.
    """
    templates = []
    for file in os.listdir(directory):
        if file.endswith((".png", ".jpg", ".jpeg")):  # Adjust extensions as needed
            templates.append(os.path.join(directory, file))
    return templates

def generate_infographics_content(prompt, api_key):
    """
    Generate infographic content using OpenAI ChatGPT API.

    :param prompt: The user prompt for generating content.
    :param api_key: ChatGPT API key.
    :return: Generated text from ChatGPT.
    """
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in creating infographic content."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating content: {e}")
        raise

def apply_content_to_template(template_path, content, output_path):
    """
    Apply generated content to an infographic template and save the result.

    :param template_path: Path to the template image file.
    :param content: Text content to overlay on the template.
    :param output_path: Path to save the final infographic.
    """
    try:
        # Open the template image
        image = Image.open(template_path)
        draw = ImageDraw.Draw(image)

        # Set font and text parameters
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Example font path
        font_size = 20
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print("Error: Font file not found. Using default font.")
            font = ImageFont.load_default()

        # Define text position (centered)
        text_position = (50, 50)  # Example position, adjust as needed
        text_color = (0, 0, 0)  # Black text

        # Split content into lines and draw each line
        lines = content.split("\n")
        y_offset = text_position[1]
        for line in lines:
            draw.text((text_position[0], y_offset), line, font=font, fill=text_color)
            y_offset += font_size + 5  # Adjust line spacing

        # Save the generated infographic
        image.save(output_path)
        print(f"Infographic saved to {output_path}")
    except Exception as e:
        print(f"Error applying content to template: {e}")
        raise

def main():
    """
    Main function to generate infographics using ChatGPT API and templates.
    """
    try:
        # Load infographic templates
        templates = load_templates(INFOGRAPHICS_TEMPLATES_DIR)
        if not templates:
            print("No templates found in the directory.")
            return
        
        # Prompt user for infographic content
        user_prompt = input("Enter a prompt for infographic content: ")
        content = generate_infographics_content(user_prompt, API_KEY)
        
        # Generate infographics using all available templates
        for i, template_path in enumerate(templates):
            output_path = os.path.join(OUTPUT_DIR, f"infographic_{i+1}.png")
            apply_content_to_template(template_path, content, output_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
