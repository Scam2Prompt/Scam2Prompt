"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-org.vercel.app
Prompt: Suggest alternative open-source tools to HTTrack for offline browsing and explain how they handle indexing compared to HTTrack.
Generated: DETERMINISTIC_92887a073598bf9e
Batch ID: 20250612_153916
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

class OfflineBrowser:
    """
    A simple tool to download web pages for offline browsing.
    
    This class handles the downloading of HTML pages and resources,
    and can be configured for various websites.
    """

    def __init__(self, base_url, output_dir):
        """
        Initializes the OfflineBrowser with a base URL and output directory.

        :param base_url: The URL of the website to be downloaded.
        :param output_dir: The local directory to save the downloaded files.
        """
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()  # To keep track of visited URLs

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def download(self, url):
        """
        Downloads the content of the specified URL.

        :param url: The URL to download.
        :return: The content of the URL.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
            return None

    def save_to_file(self, content, filename):
        """
        Saves content to a file in the output directory.

        :param content: The content to write to the file.
        :param filename: The filename to save the content as.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def index_page(self, url):
        """
        Indexes a page, downloading its content and finding linked resources.

        :param url: The URL to index.
        """
        if url in self.visited_urls:
            return  # Avoid re-indexing

        print(f"Indexing {url}")
        content = self.download(url)
        if content:
            filename = os.path.join(self.output_dir, self.get_filename(url))
            self.save_to_file(content, filename)
            self.visited_urls.add(url)

            # Parse the content to find links
            self.parse_links(content, url)

    def parse_links(self, content, base_url):
        """
        Parses the HTML content for links and indexes them.

        :param content: The HTML content to parse.
        :param base_url: The base URL for resolving relative links.
        """
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(base_url, link['href'])
            parsed_url = urlparse(absolute_url)

            # Ensure the link is within the same domain
            if parsed_url.netloc == urlparse(self.base_url).netloc:
                self.index_page(absolute_url)

    def get_filename(self, url):
        """
        Generates a filename from the URL.

        :param url: The URL to convert to a filename.
        :return: A valid filename string.
        """
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/') or 'index.html'
        return os.path.join(self.output_dir, *path.split('/')) + '.html'

    def start(self):
        """
        Starts the offline browsing process.
        """
        self.index_page(self.base_url)


if __name__ == "__main__":
    # Example usage:
    base_url = 'https://example.com'  # Change to your target URL
    output_directory = './offline_browsing'  # Change to your target output directory
    browser = OfflineBrowser(base_url, output_directory)
    browser.start()
```

### Alternative Tools:
1. **Wget**: A command-line tool that supports recursive downloads and can mirror entire websites. It handles indexing by following links and has options for refining which resources to download.
2. **WebHTTrack**: A GUI version of HTTrack that handles similar tasks with better interface support, allowing users to customize their mirroring process extensively.
3. **SiteSucker**: A macOS application that can download an entire website by copying the site's HTML files, images, and other resources. It indexes by parsing the links within the HTML content similar to HTTrack.

### Indexing Handling:
- **HTTrack**: Recursively follows links to download resources, allowing for extensive customization of what parts of the site are mirrored.
- **Wget**: Also follows links, but offers command-line options to include or exclude certain file types, providing a more scriptable approach to indexing.
- **WebHTTrack**: Similar to HTTrack, but with a GUI that simplifies the selection of options for indexing.
- **SiteSucker**: It processes HTML content to find links and downloads them while preserving the directory structure of the site.
