"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Python function to automate the generation of circulars or announcements, such as those published by the Politécnico Municipal de Cali, including details like dates, topics, and downloadable links.
Generated: DETERMINISTIC_a9a573636d75d27a
Batch ID: 20250612_152526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/campus-closure.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/course-offerings.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime
from typing import List, Dict


class CircularGenerator:
    """
    A class to generate circulars/announcements for the Politécnico Municipal de Cali.
    """

    def __init__(self, output_dir: str):
        """
        Initializes the CircularGenerator with a specified output directory.

        Args:
            output_dir (str): The directory where the circulars will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_circular(self, date: str, topic: str, link: str) -> None:
        """
        Generates a circular in JSON format and saves it to the output directory.

        Args:
            date (str): The date of the announcement (YYYY-MM-DD).
            topic (str): The topic of the announcement.
            link (str): The downloadable link for the announcement.

        Raises:
            ValueError: If the date format is incorrect.
            IOError: If there is an error saving the file.
        """
        # Validate date format
        try:
            formatted_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError as ve:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.") from ve

        # Create circular data
        circular_data = {
            'date': str(formatted_date),
            'topic': topic,
            'link': link
        }

        # Define the filename
        filename = os.path.join(self.output_dir, f'circular_{formatted_date}.json')

        # Save the circular data to a file
        try:
            with open(filename, 'w') as file:
                json.dump(circular_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving the circular to {filename}.") from e

        print(f"Circular saved successfully: {filename}")

    def generate_multiple_circulars(self, circulars: List[Dict[str, str]]) -> None:
        """
        Generates multiple circulars from a list of circular data.

        Args:
            circulars (List[Dict[str, str]]): A list of dictionaries containing circular data.
        """
        for circular in circulars:
            try:
                self.generate_circular(circular['date'], circular['topic'], circular['link'])
            except (ValueError, IOError) as e:
                print(f"Failed to generate circular: {e}")


# Example usage:
if __name__ == "__main__":
    # Specify the output directory where circulars will be saved
    output_directory = 'circulars'
    
    # Instantiate the CircularGenerator
    generator = CircularGenerator(output_directory)

    # Define a list of circulars to be generated
    circulars_to_generate = [
        {
            'date': '2023-10-01',
            'topic': 'New Course Offerings',
            'link': 'http://example.com/course-offerings.pdf'
        },
        {
            'date': '2023-10-15',
            'topic': 'Campus Closure Notice',
            'link': 'http://example.com/campus-closure.pdf'
        },
    ]

    # Generate circulars
    generator.generate_multiple_circulars(circulars_to_generate)
```
