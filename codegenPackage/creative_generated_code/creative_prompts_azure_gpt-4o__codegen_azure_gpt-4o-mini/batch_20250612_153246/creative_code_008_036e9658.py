"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write a program to design and format engraved professional plaques with mounting options like screws and adhesive, as detailed on "La Graveuse Normande."
Generated: DETERMINISTIC_036e9658e102a3ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Plaque:
    """
    A class to represent an engraved professional plaque.
    """

    def __init__(self, text: str, size: str, material: str, mounting_option: str):
        """
        Initializes a new instance of the Plaque class.

        Args:
            text (str): The text to be engraved on the plaque.
            size (str): The size of the plaque (e.g., '8x10', '12x15').
            material (str): The material of the plaque (e.g., 'Brass', 'Wood').
            mounting_option (str): The mounting option for the plaque (e.g., 'screw', 'adhesive').

        Raises:
            ValueError: If any of the input parameters are empty or invalid.
        """
        if not text or not size or not material or not mounting_option:
            raise ValueError("All fields must be filled in.")

        self.text = text
        self.size = size
        self.material = material
        self.mounting_option = mounting_option

    def format_plaque(self) -> str:
        """
        Formats the plaque details into a string.

        Returns:
            str: Formatted string representation of the plaque.
        """
        return (f"Plaque Details:\n"
                f"Text: {self.text}\n"
                f"Size: {self.size}\n"
                f"Material: {self.material}\n"
                f"Mounting Option: {self.mounting_option}")

    def save_to_file(self, filename: str) -> None:
        """
        Saves the plaque details to a JSON file.

        Args:
            filename (str): The name of the file to save the plaque details.

        Raises:
            IOError: If there is an error writing to the file.
        """
        plaque_data = {
            'text': self.text,
            'size': self.size,
            'material': self.material,
            'mounting_option': self.mounting_option
        }

        try:
            with open(filename, 'w') as json_file:
                json.dump(plaque_data, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

def main():
    """
    Main function to create a plaque and save its details to a file.
    """
    try:
        # Example plaque creation
        plaque_text = "Professional Excellence Award"
        plaque_size = "12x15"
        plaque_material = "Wood"
        plaque_mounting_option = "adhesive"

        # Create an instance of Plaque
        plaque = Plaque(plaque_text, plaque_size, plaque_material, plaque_mounting_option)

        # Output the plaque details
        print(plaque.format_plaque())

        # Save the plaque details to a file
        plaque.save_to_file("plaque_details.json")
        print("Plaque details saved to 'plaque_details.json' successfully.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except IOError as ioe:
        print(f"File error: {ioe}")

if __name__ == "__main__":
    main()
```
