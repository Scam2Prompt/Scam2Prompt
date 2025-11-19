"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write a script to analyze customer preferences for products like high-visibility gloves, fire-resistant gloves, and impact gloves, based on Rising Star International's product descriptions.
Generated: DETERMINISTIC_1abdc4c05a2482bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from collections import defaultdict
from typing import Dict, List, Tuple
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ProductAnalyzer:
    """
    A class to analyze customer preferences based on product descriptions.
    """
    
    def __init__(self, product_data: List[Dict[str, str]]):
        """
        Initialize the analyzer with product data.
        
        Args:
            product_data: List of dictionaries containing product information.
                         Each dictionary should have at least 'name' and 'description' keys.
        """
        self.product_data = product_data
        self.keywords = {
            'high_visibility': ['high visibility', 'high-visibility', 'reflective', 'bright'],
            'fire_resistant': ['fire resistant', 'fire-resistant', 'flame resistant', 'flame-resistant'],
            'impact': ['impact', 'protective', 'safety', 'durable']
        }
        
    def _clean_text(self, text: str) -> str:
        """
        Clean and preprocess text for analysis.
        
        Args:
            text: Input text to clean.
            
        Returns:
            Cleaned text.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return text
    
    def _count_keywords(self, description: str) -> Dict[str, int]:
        """
        Count occurrences of keywords in a product description.
        
        Args:
            description: Product description to analyze.
            
        Returns:
            Dictionary with keyword counts.
        """
        cleaned_text = self._clean_text(description)
        counts = defaultdict(int)
        
        for category, terms in self.keywords.items():
            for term in terms:
                term = self._clean_text(term)
                counts[category] += cleaned_text.count(term)
                
        return counts
    
    def analyze_preferences(self) -> pd.DataFrame:
        """
        Analyze customer preferences based on product descriptions.
        
        Returns:
            DataFrame with analysis results.
        """
        try:
            results = []
            
            for product in self.product_data:
                if not all(key in product for key in ['name', 'description']):
                    logger.warning(f"Product missing required fields: {product}")
                    continue
                    
                counts = self._count_keywords(product['description'])
                results.append({
                    'product_name': product['name'],
                    'high_visibility_mentions': counts['high_visibility'],
                    'fire_resistant_mentions': counts['fire_resistant'],
                    'impact_mentions': counts['impact'],
                    'total_mentions': sum(counts.values())
                })
            
            df = pd.DataFrame(results)
            
            if df.empty:
                logger.warning("No valid products found for analysis")
                return df
                
            # Calculate preference scores (normalized by total mentions)
            for category in self.keywords.keys():
                df[f'{category}_score'] = df[f'{category}_mentions'] / df['total_mentions'].replace(0, 1)
            
            return df.sort_values(by='total_mentions', ascending=False)
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample product data (in production, this would come from a database or API)
    sample_products = [
        {
            "name": "Pro-Vis High Visibility Gloves",
            "description": "These high-visibility gloves feature reflective strips for maximum visibility in low-light conditions."
        },
        {
            "name": "FireMaster FR Gloves",
            "description": "Fire-resistant gloves designed for high-temperature environments with flame-resistant materials."
        },
        {
            "name": "ImpactPro Safety Gloves",
            "description": "Durable impact-resistant gloves with protective padding for heavy-duty work."
        },
        {
            "name": "All-Purpose Work Gloves",
            "description": "General purpose gloves for various tasks."
        }
    ]
    
    try:
        analyzer = ProductAnalyzer(sample_products)
        results = analyzer.analyze_preferences()
        print("\nCustomer Preference Analysis Results:")
        print(results.to_string(index=False))
    except Exception as e:
        logger.error(f"Failed to analyze products: {str(e)}")
```
