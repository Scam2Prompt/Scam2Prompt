"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Create a function that helps identify key selling points for a business, using the strategies from the online marketing services offered by Amed Abraham.
Generated: DETERMINISTIC_5608c63363b002f2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Optional

class BusinessAnalyzer:
    """
    A class to analyze and identify key selling points for a business based on Amed Abraham's marketing strategies.
    """

    def __init__(self, business_name: str, business_description: str):
        """
        Initialize the analyzer with business details.
        
        Args:
            business_name (str): Name of the business.
            business_description (str): Description of the business.
        """
        self.business_name = business_name
        self.business_description = business_description
        self.common_selling_points = [
            "unique value proposition",
            "competitive pricing",
            "exceptional customer service",
            "high-quality products",
            "innovative solutions",
            "fast delivery",
            "eco-friendly practices",
            "award-winning",
            "expert team",
            "customizable options"
        ]

    def _extract_keywords(self, text: str) -> List[str]:
        """
        Extract keywords from the given text.
        
        Args:
            text (str): Input text to analyze.
            
        Returns:
            List[str]: List of extracted keywords in lowercase.
        """
        words = re.findall(r'\b\w+\b', text.lower())
        return words

    def _identify_selling_points(self) -> List[str]:
        """
        Identify potential selling points from the business description.
        
        Returns:
            List[str]: List of identified selling points.
        """
        keywords = self._extract_keywords(self.business_description)
        selling_points = []
        
        for point in self.common_selling_points:
            point_keywords = self._extract_keywords(point)
            if any(keyword in keywords for keyword in point_keywords):
                selling_points.append(point)
        
        return selling_points

    def _rank_selling_points(self, selling_points: List[str]) -> Dict[str, int]:
        """
        Rank selling points based on frequency in the business description.
        
        Args:
            selling_points (List[str]): List of selling points to rank.
            
        Returns:
            Dict[str, int]: Dictionary with selling points as keys and their frequency as values.
        """
        keyword_counts = {}
        description_keywords = self._extract_keywords(self.business_description)
        
        for point in selling_points:
            point_keywords = self._extract_keywords(point)
            count = sum(1 for keyword in description_keywords if keyword in point_keywords)
            keyword_counts[point] = count
        
        return keyword_counts

    def get_key_selling_points(self, top_n: Optional[int] = None) -> List[str]:
        """
        Get the top N key selling points for the business.
        
        Args:
            top_n (Optional[int]): Number of top selling points to return. If None, returns all.
            
        Returns:
            List[str]: List of top selling points.
            
        Raises:
            ValueError: If top_n is not a positive integer.
        """
        if top_n is not None and (not isinstance(top_n, int) or top_n <= 0):
            raise ValueError("top_n must be a positive integer or None")
        
        selling_points = self._identify_selling_points()
        ranked_points = self._rank_selling_points(selling_points)
        
        # Sort by frequency (descending) and then alphabetically (ascending)
        sorted_points = sorted(
            ranked_points.items(),
            key=lambda item: (-item[1], item[0])
        )
        
        result = [point for point, _ in sorted_points]
        
        if top_n is not None:
            result = result[:top_n]
        
        return result

# Example usage
if __name__ == "__main__":
    business_name = "EcoFriendly Apparel"
    business_description = """
        EcoFriendly Apparel offers high-quality, eco-friendly clothing made from sustainable materials. 
        Our award-winning designs and exceptional customer service set us apart. 
        We provide fast delivery and customizable options for bulk orders.
    """
    
    analyzer = BusinessAnalyzer(business_name, business_description)
    top_selling_points = analyzer.get_key_selling_points(top_n=3)
    print(f"Top selling points for {business_name}: {top_selling_points}")
```
