"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: Write code to generate QR codes for links and categorize them using tags, inspired by Fli.so's smart organization and QR code generation features.
Generated: DETERMINISTIC_31da34eb8a834abc
Batch ID: 20250612_154010
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://another-example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
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
import qrcode
from typing import List, Dict


class QRCodeManager:
    """
    A class to manage QR Code generation and categorization using tags.
    """

    def __init__(self):
        # Dictionary to store QR code data categorized by tags
        # Structure: {tag: [list of links]}
        self.tagged_links: Dict[str, List[str]] = {}

    def add_link(self, link: str, tags: List[str]) -> None:
        """
        Add a link to the categorized collection, associated with tags.

        :param link: The URL to be categorized and converted into a QR code.
        :param tags: A list of tags to associate with the link.
        """
        for tag in tags:
            if tag not in self.tagged_links:
                self.tagged_links[tag] = []
            if link not in self.tagged_links[tag]:
                self.tagged_links[tag].append(link)

    def generate_qr_code(self, link: str, output_file: str) -> None:
        """
        Generate a QR code for the given link and save it to a file.

        :param link: The URL to be converted into a QR code.
        :param output_file: The file path to save the generated QR code image.
        :raises ValueError: If the link is empty or invalid.
        """
        if not link:
            raise ValueError("The link cannot be empty.")
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")
            img.save(output_file)
        except Exception as e:
            raise RuntimeError(f"Failed to generate QR code for link '{link}': {e}")

    def get_links_by_tag(self, tag: str) -> List[str]:
        """
        Retrieve all links associated with a specific tag.

        :param tag: The tag to search for.
        :return: A list of links associated with the tag.
        """
        return self.tagged_links.get(tag, [])

    def generate_qr_codes_for_tag(self, tag: str, output_dir: str) -> None:
        """
        Generate QR codes for all links associated with a specific tag.

        :param tag: The tag whose links will be converted into QR codes.
        :param output_dir: The directory to save the QR code images.
        :raises FileNotFoundError: If the output directory does not exist.
        """
        import os

        if not os.path.isdir(output_dir):
            raise FileNotFoundError(f"The directory '{output_dir}' does not exist.")

        links = self.get_links_by_tag(tag)
        for i, link in enumerate(links, start=1):
            output_file = os.path.join(output_dir, f"{tag}_qr_{i}.png")
            try:
                self.generate_qr_code(link, output_file)
                print(f"QR code saved: {output_file}")
            except Exception as e:
                print(f"Error generating QR code for link '{link}': {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the QR Code Manager
    manager = QRCodeManager()

    # Add links with tags
    manager.add_link("https://example.com", ["example", "website"])
    manager.add_link("https://another-example.com", ["example", "another"])

    # Generate and save QR codes for all links under the tag "example"
    manager.generate_qr_codes_for_tag("example", "./qrcodes")
```
