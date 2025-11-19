"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Recommend a library or API for developing Windows screen savers that can handle .RAR or .ZIP file formats, as discussed on feedoy.org.
Generated: DETERMINISTIC_3c2d4c5c89f45ab3
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import rarfile
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ScreenSaverExtractor:
    """
    A class to handle the extraction of screen saver files
    from ZIP and RAR archives.
    """

    def __init__(self, archive_path):
        """
        Initialize the ScreenSaverExtractor with the path to the archive.

        :param archive_path: Path to the ZIP or RAR file.
        """
        self.archive_path = archive_path

    def extract(self, output_dir):
        """
        Extract the contents of the archive to the specified output directory.

        :param output_dir: Directory to which the files will be extracted.
        :raises FileNotFoundError: If the archive does not exist.
        :raises ValueError: If the archive format is unsupported.
        """
        if not os.path.exists(self.archive_path):
            logging.error(f"File not found: {self.archive_path}")
            raise FileNotFoundError(f"The specified archive does not exist: {self.archive_path}")

        try:
            if self.archive_path.endswith('.zip'):
                self._extract_zip(output_dir)
            elif self.archive_path.endswith('.rar'):
                self._extract_rar(output_dir)
            else:
                logging.error("Unsupported file format. Only .zip and .rar files are supported.")
                raise ValueError("Unsupported file format. Only .zip and .rar files are supported.")
        except Exception as e:
            logging.exception("An error occurred during extraction.")
            raise e

    def _extract_zip(self, output_dir):
        """
        Extract files from a ZIP archive.

        :param output_dir: Directory to which the files will be extracted.
        """
        logging.info(f"Extracting ZIP file: {self.archive_path} to {output_dir}")
        with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            logging.info(f"Extraction complete: {self.archive_path}")

    def _extract_rar(self, output_dir):
        """
        Extract files from a RAR archive.

        :param output_dir: Directory to which the files will be extracted.
        """
        logging.info(f"Extracting RAR file: {self.archive_path} to {output_dir}")
        with rarfile.RarFile(self.archive_path) as rar_ref:
            rar_ref.extractall(output_dir)
            logging.info(f"Extraction complete: {self.archive_path}")

# Example usage:
# if __name__ == "__main__":
#     extractor = ScreenSaverExtractor('path/to/archive.zip')
#     extractor.extract('output/directory')

```

**Note:** Make sure to install the necessary libraries using pip:
```bash
pip install rarfile
```
