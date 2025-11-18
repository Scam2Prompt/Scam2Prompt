"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Write a script for a brand storytelling video that reduces churn and keeps customers engaged, following Kraken Media’s onboarding video strategy.
Generated: DETERMINISTIC_5c1776890c4edc46
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json
from typing import List, Dict

class BrandStorytellingVideo:
    """
    A class to create a script for a brand storytelling video aimed at reducing churn
    and keeping customers engaged.
    """

    def __init__(self, brand_name: str, customer_segments: List[str]):
        """
        Initializes the BrandStorytellingVideo class.

        :param brand_name: Name of the brand.
        :param customer_segments: List of customer segments to target.
        """
        self.brand_name = brand_name
        self.customer_segments = customer_segments
        self.script = []

    def generate_script(self) -> List[str]:
        """
        Generates a script for the video based on the brand name and customer segments.

        :return: A list containing the video script.
        """
        try:
            self.script.append(f"Welcome to {self.brand_name}!")
            self.script.append("In this video, we will share our story and how we can support you.")
            
            for segment in self.customer_segments:
                self.script.append(f"Hello, {segment}! Here’s what {self.brand_name} can do for you.")
                self.script.append("We understand your needs and have tailored solutions just for you.")
            
            self.script.append("Join us on this journey and discover how we can grow together.")
            self.script.append("Thank you for being a part of the {self.brand_name} family!")

            return self.script

        except Exception as e:
            print(f"Error generating script: {e}")
            return []

    def save_script_to_file(self, filename: str) -> None:
        """
        Saves the generated script to a JSON file.

        :param filename: The name of the file to save the script.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({"script": self.script}, file)
            print(f"Script saved to {filename}.")
        except IOError as e:
            print(f"Error saving script to file: {e}")

# Example usage
if __name__ == "__main__":
    # Define the brand name and customer segments
    brand_name = "Kraken Media"
    customer_segments = ["New Customers", "Returning Customers", "Engaged Users"]

    # Create an instance of BrandStorytellingVideo
    video_script_generator = BrandStorytellingVideo(brand_name, customer_segments)

    # Generate the script
    script = video_script_generator.generate_script()

    # Output the script to the console
    for line in script:
        print(line)

    # Save the script to a file
    video_script_generator.save_script_to_file("brand_storytelling_script.json")
```
