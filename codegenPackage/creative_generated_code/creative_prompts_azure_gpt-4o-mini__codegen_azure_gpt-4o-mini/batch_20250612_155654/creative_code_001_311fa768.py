"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: What are the best practices for publishing documentation using GitBook, as mentioned on the Polymarket site?
Generated: DETERMINISTIC_311fa768cdb084e2
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging for better debugging and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GitBookPublisher:
    """A class to handle the publishing of documentation to GitBook."""

    def __init__(self, book_path: str):
        """
        Initialize the GitBookPublisher with the path to the documentation.

        :param book_path: str - The directory path to the GitBook documentation.
        """
        self.book_path = book_path

    def build_book(self):
        """Build the GitBook from the specified book directory."""
        try:
            logging.info("Building the GitBook...")
            # Change to the book directory
            os.chdir(self.book_path)
            # Run the GitBook build command
            subprocess.run(['gitbook', 'build'], check=True)
            logging.info("GitBook built successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error building GitBook: {e}")
            raise

    def serve_book(self):
        """Serve the GitBook locally for preview."""
        try:
            logging.info("Serving the GitBook locally...")
            os.chdir(self.book_path)
            subprocess.run(['gitbook', 'serve'], check=True)
            logging.info("GitBook is being served locally.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error serving GitBook: {e}")
            raise

    def publish_book(self):
        """Publish the GitBook to the remote GitBook service."""
        try:
            logging.info("Publishing the GitBook...")
            os.chdir(self.book_path)
            subprocess.run(['gitbook', 'publish'], check=True)
            logging.info("GitBook published successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error publishing GitBook: {e}")
            raise

def main():
    """Main function to execute the GitBook publishing process."""
    book_path = '/path/to/your/gitbook'  # Replace with your actual book path
    publisher = GitBookPublisher(book_path)

    try:
        publisher.build_book()
        publisher.serve_book()
        publisher.publish_book()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `'/path/to/your/gitbook'` with the actual path to your GitBook documentation directory.
