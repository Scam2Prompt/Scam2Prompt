"""
Generated Code Metadata:
========================
Original URL: https://beamtoken.org
Prompt: Suggest a set of keywords and tags that could be used to categorize and search content on https://beamtoken.org, and provide a sample Python script for implementing a simple search function.
Generated: DETERMINISTIC_19cf653199c12265
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

# Suggested keywords and tags for beamtoken.org content categorization
SUGGESTED_KEYWORDS = {
    "categories": [
        "blockchain",
        "cryptocurrency",
        "privacy",
        "finance",
        "technology",
        "decentralization",
        "security",
        "tokens",
        "wallet",
        "mining",
        "staking",
        "defi",
        "nft",
        "smart-contracts",
        "governance"
    ],
    "tags": [
        "beam",
        "mimblewimble",
        "confidential",
        "scalable",
        "lightning",
        "atomic-swap",
        "dapp",
        "ecosystem",
        "mainnet",
        "testnet",
        "updates",
        "roadmap",
        "partnerships",
        "community",
        "developers"
    ]
}

class ContentSearch:
    def __init__(self, content_data: List[Dict]):
        """
        Initialize the search engine with content data.
        
        Args:
            content_data: List of dictionaries containing content with 'title', 'body', and 'tags' keys
        """
        self.content = content_data
        self.index = self._build_index()

    def _build_index(self) -> Dict[str, List[int]]:
        """
        Build an inverted index mapping keywords to content indices.
        
        Returns:
            Dictionary with keywords as keys and list of content indices as values
        """
        index = {}
        for idx, item in enumerate(self.content):
            text = f"{item.get('title', '')} {item.get('body', '')}".lower()
            tags = [tag.lower() for tag in item.get('tags', [])]
            
            # Index all words in text
            for word in text.split():
                if word not in index:
                    index[word] = []
                if idx not in index[word]:
                    index[word].append(idx)
            
            # Index all tags
            for tag in tags:
                if tag not in index:
                    index[tag] = []
                if idx not in index[tag]:
                    index[tag].append(idx)
        
        return index

    def search(self, query: str, category: Optional[str] = None) -> List[Dict]:
        """
        Search content based on query and optional category filter.
        
        Args:
            query: Search string
            category: Optional category filter
            
        Returns:
            List of matching content items
        """
        query = query.lower()
        results = set()
        
        # Find all content indices that match any word in the query
        for word in query.split():
            if word in self.index:
                results.update(self.index[word])
        
        # Convert indices back to content items
        matched_content = [self.content[idx] for idx in results]
        
        # Apply category filter if provided
        if category:
            category = category.lower()
            matched_content = [
                item for item in matched_content 
                if category in [tag.lower() for tag in item.get('tags', [])]
            ]
        
        return matched_content

def load_sample_content() -> List[Dict]:
    """Load sample content data for demonstration purposes."""
    return [
        {
            "title": "Beam Privacy Features",
            "body": "Beam implements Mimblewimble protocol for confidential transactions.",
            "tags": ["privacy", "mimblewimble", "beam"]
        },
        {
            "title": "Beam Wallet Update",
            "body": "New version of Beam wallet with improved security and UI.",
            "tags": ["wallet", "updates", "security"]
        },
        {
            "title": "Beam DeFi Integration",
            "body": "Beam announces partnership with major DeFi platform.",
            "tags": ["defi", "partnerships", "ecosystem"]
        }
    ]

# Example usage
if __name__ == "__main__":
    # Load sample content
    content = load_sample_content()
    
    # Initialize search engine
    search_engine = ContentSearch(content)
    
    # Perform searches
    print("Search results for 'beam':")
    print(json.dumps(search_engine.search("beam"), indent=2))
    
    print("\nSearch results for 'security' in category 'wallet':")
    print(json.dumps(search_engine.search("security", category="wallet"), indent=2))
```
