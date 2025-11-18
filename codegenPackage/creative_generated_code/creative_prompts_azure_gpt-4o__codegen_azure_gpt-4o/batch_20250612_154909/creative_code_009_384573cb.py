"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Write a script to analyze and compare the visual branding impact of TS Fonts' "Tarek Font" versus other display fonts.
Generated: DETERMINISTIC_384573cbfffed914
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def load_fonts(font_directory):
    """
    Load font file paths from the given directory.
    
    Args:
        font_directory (str): Path to the directory containing font files.
    
    Returns:
        dict: Dictionary of font names and their file paths.
    """
    fonts = {}
    try:
        for file in os.listdir(font_directory):
            if file.endswith('.ttf') or file.endswith('.otf'):
                font_name = os.path.splitext(file)[0]
                fonts[font_name] = os.path.join(font_directory, file)
    except Exception as e:
        print(f"Error loading fonts: {e}")
    return fonts

def generate_word_cloud(text, font_path, output_file):
    """
    Generate a word cloud using a specific font and save it as an image file.
    
    Args:
        text (str): Text to generate the word cloud from.
        font_path (str): Path to the font file to be used for the word cloud.
        output_file (str): Path to save the generated word cloud image.
    """
    try:
        wordcloud = WordCloud(font_path=font_path, background_color="white", width=800, height=400).generate(text)
        wordcloud.to_file(output_file)
    except Exception as e:
        print(f"Error generating word cloud: {e}")

def compare_fonts(text, font_directory, target_font_name):
    """
    Compare the visual branding impact of a target font versus other fonts in a directory.
    
    Args:
        text (str): Text for generating word clouds.
        font_directory (str): Path to the directory containing font files.
        target_font_name (str): Name of the target font to compare against.
    """
    fonts = load_fonts(font_directory)
    
    if target_font_name not in fonts:
        print(f"Target font '{target_font_name}' not found in the directory.")
        return
    
    output_dir = 'wordclouds'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate word cloud for the target font
    print(f"Generating word cloud for target font '{target_font_name}'...")
    generate_word_cloud(text, fonts[target_font_name], os.path.join(output_dir, f"{target_font_name}_wordcloud.png"))
    
    # Generate word clouds for other fonts and compare
    for font_name, font_path in fonts.items():
        if font_name == target_font_name:
            continue
        print(f"Generating word cloud for font '{font_name}'...")
        generate_word_cloud(text, font_path, os.path.join(output_dir, f"{font_name}_wordcloud.png"))

    print(f"Word clouds saved in '{output_dir}' directory for comparison.")

if __name__ == "__main__":
    # Sample text for branding analysis
    sample_text = """
    Tarek Font is the pinnacle of modern display fonts, offering exceptional readability and branding opportunities.
    Compare it with other display fonts for unique visual impact.
    """
    
    # Directory containing font files (update with your directory path)
    font_directory = "fonts"
    
    # Name of the target font to compare against
    target_font_name = "Tarek_Font"
    
    # Perform comparison
    compare_fonts(sample_text, font_directory, target_font_name)
```
