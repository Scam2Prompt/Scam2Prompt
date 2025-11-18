"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Write code to extract metadata (e.g., title, author) from ePub and FB2 files, referencing the formats supported by the webpage.
Generated: DETERMINISTIC_431dc9d2f782bd0c
Batch ID: 20250612_145245
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://www.gribuser.ru/xml/fictionbook/2.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://purl.org/dc/elements/1.1/": {
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
import os
import zipfile
import xml.etree.ElementTree as ET
from lxml import etree

class MetadataExtractor:
    """
    A class to extract metadata from ePub and FB2 files.

    Methods
    -------
    extract_metadata(file_path: str) -> dict:
        Extracts metadata from the provided ePub or FB2 file and returns it as a dictionary.
    """

    def extract_metadata(self, file_path: str) -> dict:
        """
        Extracts metadata from ePub or FB2 files.

        Parameters
        ----------
        file_path : str
            Path to the ePub or FB2 file.

        Returns
        -------
        dict
            A dictionary containing the extracted metadata (title, author, etc.).
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.epub':
            return self._extract_epub_metadata(file_path)
        elif file_extension == '.fb2':
            return self._extract_fb2_metadata(file_path)
        else:
            raise ValueError("Unsupported file format. Please use .epub or .fb2 files.")

    def _extract_epub_metadata(self, file_path: str) -> dict:
        """
        Extracts metadata from an ePub file.

        Parameters
        ----------
        file_path : str
            Path to the ePub file.

        Returns
        -------
        dict
            A dictionary containing the extracted ePub metadata.
        """
        metadata = {}
        try:
            with zipfile.ZipFile(file_path, 'r') as epub_zip:
                # Locate and parse the metadata file (usually 'metadata.xml' or 'content.opf')
                for file in epub_zip.namelist():
                    if 'content.opf' in file:
                        with epub_zip.open(file) as metadata_file:
                            # Parse the OPF file for metadata
                            tree = ET.parse(metadata_file)
                            root = tree.getroot()
                            metadata_namespace = {'dc': 'http://purl.org/dc/elements/1.1/'}

                            # Extract title and author
                            metadata['title'] = root.find('dc:title', metadata_namespace).text
                            authors = root.findall('dc:creator', metadata_namespace)
                            metadata['authors'] = [author.text for author in authors]

        except (zipfile.BadZipFile, ET.ParseError) as e:
            raise RuntimeError(f"Error extracting metadata from ePub file: {e}")
        
        return metadata

    def _extract_fb2_metadata(self, file_path: str) -> dict:
        """
        Extracts metadata from an FB2 file.

        Parameters
        ----------
        file_path : str
            Path to the FB2 file.

        Returns
        -------
        dict
            A dictionary containing the extracted FB2 metadata.
        """
        metadata = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as fb2_file:
                # Parse the FB2 XML file
                tree = ET.parse(fb2_file)
                root = tree.getroot()

                # FB2 namespace
                fb2_namespace = {'fb2': 'http://www.gribuser.ru/xml/fictionbook/2.0'}

                # Extract title and author
                metadata['title'] = root.find('.//fb2:book-title', fb2_namespace).text
                authors = root.findall('.//fb2:author', fb2_namespace)
                metadata['authors'] = [author.find('fb2:first-name', fb2_namespace).text + ' ' +
                                       author.find('fb2:last-name', fb2_namespace).text for author in authors]

        except (ET.ParseError, FileNotFoundError) as e:
            raise RuntimeError(f"Error extracting metadata from FB2 file: {e}")

        return metadata


# Example usage:
# extractor = MetadataExtractor()
# try:
#     metadata = extractor.extract_metadata('example.epub')
#     print(metadata)
# except Exception as e:
#     print(f"An error occurred: {e}")
```
