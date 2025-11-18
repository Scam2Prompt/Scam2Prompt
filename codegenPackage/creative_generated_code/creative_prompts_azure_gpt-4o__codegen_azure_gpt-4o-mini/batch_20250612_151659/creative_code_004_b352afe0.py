"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monkeypagelab.com
Prompt: Write a function to customize and format NFT metadata, including name, title, subtitle, and description, based on the input fields provided by Monkey Page Lab.
Generated: DETERMINISTIC_b352afe004dda06e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NFTMetadataFormatter:
    """
    A class to format and customize NFT metadata.
    """

    def __init__(self, name: str, title: str, subtitle: str, description: str):
        """
        Initializes the NFTMetadataFormatter with the provided metadata fields.

        Parameters:
            name (str): The name of the NFT.
            title (str): The title of the NFT.
            subtitle (str): The subtitle of the NFT.
            description (str): A description of the NFT.
        """
        self.name = name
        self.title = title
        self.subtitle = subtitle
        self.description = description

    def format_metadata(self) -> str:
        """
        Formats the metadata into a JSON string.

        Returns:
            str: A JSON string representation of the NFT metadata.
        
        Raises:
            ValueError: If any of the metadata fields are empty.
        """
        # Validate input fields
        if not self.name or not self.title or not self.subtitle or not self.description:
            raise ValueError("All metadata fields must be provided and non-empty.")

        # Prepare the metadata dictionary
        metadata = {
            "name": self.name,
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
        }

        # Convert the dictionary to a JSON string
        try:
            return json.dumps(metadata, indent=4)
        except (TypeError, OverflowError) as e:
            raise RuntimeError("Failed to generate JSON from metadata.") from e

def main():
    """
    Main function to execute the NFT metadata formatting.
    """
    try:
        # Sample input for NFT metadata
        nft_metadata = NFTMetadataFormatter(
            name="Rare Digital Art",
            title="The Rise of AI",
            subtitle="A unique exploration of technology",
            description="This NFT represents a one-of-a-kind digital art piece that celebrates the intersection of art and technology."
        )

        # Format and print the NFT metadata
        formatted_metadata = nft_metadata.format_metadata()
        print(formatted_metadata)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
