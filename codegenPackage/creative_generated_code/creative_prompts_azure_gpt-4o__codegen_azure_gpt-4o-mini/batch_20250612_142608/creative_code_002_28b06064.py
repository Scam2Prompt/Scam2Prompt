"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Recommend libraries or APIs for embedding interactive media blocks into a GitBook documentation site, as described in the Polymarket GitBook template.
Generated: DETERMINISTIC_28b06064a0df482c
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://polymarket.com/": {
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
import requests
from bs4 import BeautifulSoup

class GitBookMediaEmbedder:
    """
    A class to handle embedding interactive media blocks into a GitBook documentation site.
    
    Attributes:
        media_sources (dict): A dictionary to store media source configurations.
    """

    def __init__(self):
        """Initializes the media_sources with predefined options."""
        self.media_sources = {
            'polymarket': {
                'url': 'https://polymarket.com/',
                'embed_code': self.get_polymarket_embed_code,
            },
            # Add more media sources as needed
        }

    def get_polymarket_embed_code(self, market_id):
        """
        Constructs the embed code for Polymarket given a market ID.
        
        Args:
            market_id (str): The ID of the market to embed.
        
        Returns:
            str: The HTML embed code for the specified market.
        """
        return f'<iframe src="{self.media_sources["polymarket"]["url"]}market/{market_id}" ' \
               'width="100%" height="500px" frameborder="0"></iframe>'

    def embed_media(self, source_name, *args):
        """
        Retrieves the embed code for the specified media source.
        
        Args:
            source_name (str): The name of the media source (e.g., 'polymarket').
            *args: Additional arguments required for the specific media source.
        
        Returns:
            str: The generated embed code or an error message.
        """
        try:
            if source_name in self.media_sources:
                return self.media_sources[source_name]['embed_code'](*args)
            else:
                raise ValueError(f"Media source '{source_name}' is not defined.")
        except Exception as e:
            return f"Error embedding media: {str(e)}"

# Example usage
if __name__ == "__main__":
    embedder = GitBookMediaEmbedder()
    
    # Example market ID for Polymarket
    market_id = 'example-market-id'
    
    embed_code = embedder.embed_media('polymarket', market_id)
    print(embed_code)  # This will print the embed code for the specified market
```
