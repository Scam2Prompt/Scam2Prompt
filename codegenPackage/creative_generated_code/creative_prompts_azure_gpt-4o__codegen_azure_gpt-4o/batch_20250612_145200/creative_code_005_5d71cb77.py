"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jerrybeers.com
Prompt: Create code to analyze text from a travel blog like JerryBeers.com and generate a summary of the most frequently visited types of locations (e.g., historical sites, natural parks).
Generated: DETERMINISTIC_5d71cb77e899a816
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
from typing import List, Dict

def clean_text(text: str) -> str:
    """
    Clean the input text by removing special characters and converting to lowercase.
    
    Args:
        text (str): Raw text to clean.
        
    Returns:
        str: Cleaned text.
    """
    # Remove special characters and numbers, and convert to lowercase
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()

def extract_location_types(text: str, keywords: List[str]) -> List[str]:
    """
    Extract location types based on given keywords from the text.
    
    Args:
        text (str): Cleaned text to analyze.
        keywords (List[str]): List of keywords to identify location types.
        
    Returns:
        List[str]: List of extracted location types.
    """
    # Split the text into words
    words = text.split()
    # Keep only the words that match the keywords for location types
    return [word for word in words if word in keywords]

def generate_summary(location_types: List[str]) -> Dict[str, int]:
    """
    Generate a summary of the most frequently visited types of locations.
    
    Args:
        location_types (List[str]): List of location types extracted from the text.
        
    Returns:
        Dict[str, int]: A dictionary with location types as keys and their frequency as values.
    """
    # Count the frequency of each location type
    return dict(Counter(location_types))

def analyze_blog_text(blog_text: str) -> None:
    """
    Analyze the travel blog text and summarize the most frequently visited location types.
    
    Args:
        blog_text (str): Raw text from the travel blog.
    """
    try:
        # List of keywords for location types
        location_keywords = [
            'historical', 'museum', 'park', 'natural', 'beach', 'city', 
            'landmark', 'mountain', 'lake', 'forest', 'cultural', 'island'
        ]
        
        # Clean the raw blog text
        cleaned_text = clean_text(blog_text)
        
        # Extract location types from the text
        location_types = extract_location_types(cleaned_text, location_keywords)
        
        # Generate a summary of the most frequently visited location types
        summary = generate_summary(location_types)
        
        # Display the summary
        print("Most Frequently Visited Location Types:")
        for location, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{location.capitalize()}: {count} times")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample blog text
    sample_blog_text = """
    I visited many wonderful places during my vacation. The natural park was breathtaking, 
    and I spent a lot of time hiking in the mountain areas. Historical landmarks were also 
    part of the journey, and I took a guided tour of a museum. The beach was relaxing, 
    and the cultural events in the city were fascinating.
    """
    
    # Analyze the blog text
    analyze_blog_text(sample_blog_text)
```
