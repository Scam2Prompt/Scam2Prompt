"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Generate code to optimize property listings on platforms like Airbnb by analyzing and improving visibility through metadata and keyword strategies, as outlined by Bee Property.
Generated: DETERMINISTIC_12430f7d2e290886
Batch ID: 20250612_153224
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

class PropertyListingOptimizer:
    """
    A class to optimize property listings for better visibility on platforms like Airbnb.
    This optimization involves analyzing metadata and improving keyword strategies.
    """

    def __init__(self, listing_data):
        """
        Initialize the optimizer with property listing data.

        :param listing_data: List of dictionaries with property information.
                             Example property dictionary:
                             {
                                 "title": "Cozy Beachfront Apartment",
                                 "description": "A beautiful apartment by the sea.",
                                 "amenities": ["WiFi", "Air Conditioning", "Pool"],
                                 "location": "Miami Beach, Florida"
                             }
        """
        self.listing_data = listing_data

    def extract_keywords(self, text):
        """
        Extract keywords from a block of text. Keywords are determined by frequency of occurrence.

        :param text: A string to analyze for keywords.
        :return: List of top keywords sorted by frequency.
        """
        # Remove punctuation, convert to lowercase
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

        # Split text into words and count occurrences
        word_counts = Counter(cleaned_text.split())

        # Exclude common stop words (can be customized for better accuracy)
        stop_words = set(["the", "and", "a", "of", "to", "is", "in", "on", "by", "with"])
        filtered_words = {word: count for word, count in word_counts.items() if word not in stop_words}

        # Sort by frequency
        sorted_keywords = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
        
        # Return top 10 keywords
        return [keyword for keyword, _ in sorted_keywords[:10]]

    def optimize_metadata(self):
        """
        Analyze metadata and update listing titles and descriptions with relevant keywords
        for improved visibility.

        :return: Optimized listing data as a list of dictionaries.
        """
        optimized_listings = []
        for listing in self.listing_data:
            try:
                # Combine title, description, and amenities into a single text block
                combined_text = (
                    f"{listing.get('title', '')} {listing.get('description', '')} "
                    f"{' '.join(listing.get('amenities', []))} {listing.get('location', '')}"
                )

                # Extract relevant keywords
                keywords = self.extract_keywords(combined_text)

                # Generate optimized title and description
                optimized_title = f"{listing['title']} - {', '.join(keywords[:3])}"
                optimized_description = f"{listing['description']} Keywords: {', '.join(keywords)}"

                # Append optimized listing to the result
                optimized_listings.append({
                    "title": optimized_title,
                    "description": optimized_description,
                    "amenities": listing.get('amenities', []),
                    "location": listing.get('location', '')
                })

            except Exception as e:
                # Log the error (in production systems use a logging framework)
                print(f"Error optimizing listing: {str(e)}")

        return optimized_listings

# Example usage of the PropertyListingOptimizer
if __name__ == "__main__":
    # Sample property listings
    sample_listings = [
        {
            "title": "Cozy Beachfront Apartment",
            "description": "A beautiful apartment by the sea.",
            "amenities": ["WiFi", "Air Conditioning", "Pool"],
            "location": "Miami Beach, Florida"
        },
        {
            "title": "Modern Downtown Condo",
            "description": "A stylish condo located in the heart of the city.",
            "amenities": ["Kitchen", "Washer", "Dryer"],
            "location": "New York, New York"
        }
    ]

    optimizer = PropertyListingOptimizer(sample_listings)
    optimized_listings = optimizer.optimize_metadata()

    # Print optimized listings
    for listing in optimized_listings:
        print(listing)
```
