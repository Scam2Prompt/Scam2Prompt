"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Write Python code to optimize an eBook's metadata for Amazon listings, including strategic keywords and engaging descriptions, as described by Penguin Books Publishers' book marketing services.
Generated: DETERMINISTIC_bf15f53b78234f1a
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
import re
from dataclasses import dataclass, asdict
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class eBookMetadata:
    """Dataclass to hold eBook metadata for Amazon optimization."""
    title: str
    subtitle: Optional[str] = None
    authors: List[str] = None
    publisher: str = "Penguin Books"
    publication_date: str = None
    language: str = "English"
    isbn: str = None
    asin: str = None
    keywords: List[str] = None
    description: str = None
    categories: List[str] = None
    series_name: Optional[str] = None
    series_position: Optional[int] = None

    def __post_init__(self):
        """Validate fields after initialization."""
        if not self.title:
            raise ValueError("Title cannot be empty")
        if self.authors is None:
            self.authors = []
        if self.keywords is None:
            self.keywords = []
        if self.categories is None:
            self.categories = []

class MetadataOptimizer:
    """Optimizes eBook metadata for Amazon listings."""
    
    MAX_KEYWORDS = 7  # Amazon's limit for keywords
    MAX_CATEGORIES = 2  # Amazon's limit for categories
    DESCRIPTION_MAX_LENGTH = 4000  # Amazon's description character limit
    
    def __init__(self, metadata: eBookMetadata):
        self.metadata = metadata
    
    def optimize_keywords(self, additional_keywords: List[str] = None) -> List[str]:
        """
        Optimizes keywords by combining existing ones with additional strategic keywords,
        removing duplicates, and limiting to Amazon's maximum.
        """
        try:
            if additional_keywords is None:
                additional_keywords = []
            
            # Combine and deduplicate keywords
            combined = list(set(self.metadata.keywords + additional_keywords))
            
            # Remove empty or whitespace-only keywords
            combined = [kw.strip() for kw in combined if kw.strip()]
            
            # Limit to Amazon's maximum
            optimized = combined[:self.MAX_KEYWORDS]
            
            self.metadata.keywords = optimized
            return optimized
        except Exception as e:
            logger.error(f"Error optimizing keywords: {e}")
            raise
    
    def optimize_description(self, template: str = None) -> str:
        """
        Optimizes the description by ensuring it's engaging and within length limits.
        If a template is provided, it will be used to format the description.
        """
        try:
            if not self.metadata.description:
                raise ValueError("Description cannot be empty")
            
            # Apply template if provided
            if template:
                try:
                    description = template.format(
                        title=self.metadata.title,
                        authors=", ".join(self.metadata.authors),
                        keywords=", ".join(self.metadata.keywords)
                    )
                except KeyError as e:
                    logger.warning(f"Missing key in template: {e}. Using original description.")
                    description = self.metadata.description
            else:
                description = self.metadata.description
            
            # Clean up description
            description = self._clean_text(description)
            
            # Ensure length limit
            if len(description) > self.DESCRIPTION_MAX_LENGTH:
                logger.warning("Description exceeds maximum length, truncating")
                description = description[:self.DESCRIPTION_MAX_LENGTH-3] + "..."
            
            self.metadata.description = description
            return description
        except Exception as e:
            logger.error(f"Error optimizing description: {e}")
            raise
    
    def optimize_categories(self, preferred_categories: List[str] = None) -> List[str]:
        """
        Optimizes categories by prioritizing preferred categories and limiting to Amazon's maximum.
        """
        try:
            if preferred_categories is None:
                preferred_categories = []
            
            # Combine and deduplicate categories
            combined = list(set(self.metadata.categories + preferred_categories))
            
            # Prioritize preferred categories
            optimized = []
            for cat in preferred_categories:
                if cat in combined:
                    optimized.append(cat)
                    combined.remove(cat)
            
            # Add remaining categories up to the limit
            optimized.extend(combined[:self.MAX_CATEGORIES - len(optimized)])
            
            self.metadata.categories = optimized
            return optimized
        except Exception as e:
            logger.error(f"Error optimizing categories: {e}")
            raise
    
    def _clean_text(self, text: str) -> str:
        """Cleans text by removing extra whitespace and special characters."""
        # Remove HTML tags if present
        text = re.sub(r'<[^>]+>', '', text)
        # Normalize whitespace
        text = ' '.join(text.split())
        return text
    
    def to_dict(self) -> Dict:
        """Returns the optimized metadata as a dictionary."""
        return asdict(self.metadata)
    
    def to_json(self) -> str:
        """Returns the optimized metadata as a JSON string."""
        return json.dumps(self.to_dict(), indent=2)

# Example usage
if __name__ == "__main__":
    try:
        # Sample metadata
        metadata = eBookMetadata(
            title="The Great Novel",
            authors=["Jane Doe", "John Smith"],
            description="A captivating story about...",
            keywords=["fiction", "bestseller"],
            categories=["Literature & Fiction", "Mystery"]
        )
        
        # Initialize optimizer
        optimizer = MetadataOptimizer(metadata)
        
        # Optimize fields
        optimizer.optimize_keywords(["novel", "thriller", "award-winning"])
        optimizer.optimize_description()
        optimizer.optimize_categories(["Fiction"])
        
        # Output optimized metadata
        print(optimizer.to_json())
        
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
