"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: How can Rexas GenAI assist artists in generating digital artworks for NFTs?
Generated: DETERMINISTIC_def056e730111ef6
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Rexas GenAI NFT Art Generator
# This script uses OpenAI's API to generate prompts for digital artworks and assists artists in creating NFTs.

class RexasGenAIArtGenerator:
    def __init__(self, api_key: str):
        """
        Initializes the Rexas GenAI Art Generator.
        
        :param api_key: OpenAI API key for prompt generation.
        """
        if not api_key:
            raise ValueError("API key must be provided for OpenAI.")
        self.api_key = api_key
        openai.api_key = api_key

    def generate_prompt(self, style: str, theme: str) -> str:
        """
        Generates a creative prompt for digital artwork using OpenAI API.

        :param style: The desired artistic style (e.g., "abstract", "realistic").
        :param theme: The central theme of the artwork (e.g., "space exploration").
        :return: A creative prompt for the artwork.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Generate a detailed creative prompt for an NFT artwork. Style: {style}, Theme: {theme}.",
                max_tokens=100,
                temperature=0.7
            )
            prompt = response.choices[0].text.strip()
            return prompt
        except openai.error.OpenAIError as e:
            raise RuntimeError(f"Error generating prompt: {e}")

    def create_artwork(self, prompt: str, output_path: str = "generated_art.png") -> None:
        """
        Creates a basic artwork based on the generated prompt.
        (For the purpose of demonstration, adds text to an image)

        :param prompt: The creative prompt for the artwork.
        :param output_path: Path to save the generated artwork.
        """
        try:
            # Create a blank image with white background
            img = Image.new("RGB", (800, 800), "white")
            draw = ImageDraw.Draw(img)

            # Load default font (you can specify a custom font path if needed)
            font = ImageFont.load_default()

            # Add the prompt text to the image
            draw.text((50, 50), prompt, fill="black", font=font)

            # Save the resulting artwork
            img.save(output_path)
            print(f"Artwork saved as {output_path}")
        except Exception as e:
            raise RuntimeError(f"Error creating artwork: {e}")

    def generate_nft_metadata(self, artwork_title: str, creator_name: str, description: str) -> dict:
        """
        Generates metadata for the NFT artwork.

        :param artwork_title: Title of the artwork.
        :param creator_name: Name of the artist.
        :param description: Description of the NFT artwork.
        :return: A dictionary containing NFT metadata.
        """
        metadata = {
            "title": artwork_title,
            "creator": creator_name,
            "description": description,
            "created_at": datetime.utcnow().isoformat(),
        }
        return metadata

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the generator
        api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI API key
        generator = RexasGenAIArtGenerator(api_key=api_key)

        # Generate a creative prompt
        style = "abstract"
        theme = "cosmic landscapes"
        prompt = generator.generate_prompt(style, theme)
        print(f"Generated Prompt: {prompt}")

        # Create artwork based on the prompt
        generator.create_artwork(prompt)

        # Generate NFT metadata
        metadata = generator.generate_nft_metadata(
            artwork_title="Cosmic Splendor",
            creator_name="Rexas GenAI",
            description="An abstract depiction of cosmic landscapes created using AI."
        )
        print(f"NFT Metadata: {metadata}")

    except Exception as e:
        print(f"Error: {e}")
```
