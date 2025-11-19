"""
Generated Code Metadata:
========================
Original URL: https://oeg-group.com
Prompt: Write a Python script that analyzes user testimonials for outdoor environment projects and categorizes them based on design, build, and nurture aspects.
Generated: DETERMINISTIC_ad195674c74b61b1
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Tuple
import json

class TestimonialAnalyzer:
    """
    A class to analyze and categorize user testimonials for outdoor environment projects.
    The testimonials are categorized into three aspects: design, build, and nurture.
    """

    def __init__(self):
        """
        Initialize the analyzer with predefined keywords for each category.
        """
        self.keywords = {
            'design': ['design', 'plan', 'layout', 'aesthetic', 'vision', 'creative', 'blueprint'],
            'build': ['build', 'construct', 'install', 'implement', 'create', 'assembl', 'erect'],
            'nurture': ['nurture', 'maintain', 'care', 'grow', 'cultivate', 'sustain', 'preserve']
        }

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess the text by converting to lowercase and removing special characters.

        Args:
            text: The input testimonial text.

        Returns:
            str: The cleaned text.
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text

    def categorize_testimonial(self, text: str) -> Dict[str, int]:
        """
        Categorize the testimonial based on keywords for design, build, and nurture.

        Args:
            text: The input testimonial text.

        Returns:
            Dict[str, int]: A dictionary with counts of matches for each category.
        """
        cleaned_text = self.preprocess_text(text)
        categories = {category: 0 for category in self.keywords.keys()}

        for category, words in self.keywords.items():
            for word in words:
                if re.search(rf'\b{word}', cleaned_text):
                    categories[category] += 1

        return categories

    def get_primary_category(self, categories: Dict[str, int]) -> str:
        """
        Determine the primary category based on the highest count.

        Args:
            categories: Dictionary with counts for each category.

        Returns:
            str: The primary category ('design', 'build', 'nurture', or 'uncategorized' if tied/no matches).
        """
        max_count = max(categories.values())
        if max_count == 0:
            return 'uncategorized'

        primary_categories = [k for k, v in categories.items() if v == max_count]
        return primary_categories[0] if len(primary_categories) == 1 else 'uncategorized'

    def analyze_testimonials(self, testimonials: List[str]) -> List[Dict[str, str]]:
        """
        Analyze a list of testimonials and return their categories.

        Args:
            testimonials: List of testimonial texts.

        Returns:
            List[Dict[str, str]]: List of dictionaries with 'testimonial' and 'category' keys.
        """
        results = []
        for testimonial in testimonials:
            if not isinstance(testimonial, str) or not testimonial.strip():
                continue

            categories = self.categorize_testimonial(testimonial)
            primary_category = self.get_primary_category(categories)
            results.append({
                'testimonial': testimonial,
                'category': primary_category,
                'category_counts': categories
            })

        return results

    def save_results(self, results: List[Dict[str, str]], output_file: str) -> None:
        """
        Save the analysis results to a JSON file.

        Args:
            results: List of analysis results.
            output_file: Path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error saving results to file: {e}")

def main():
    """
    Main function to demonstrate the testimonial analyzer.
    """
    # Example testimonials
    testimonials = [
        "The design of the park was creative and well-planned.",
        "The team did an excellent job building the playground.",
        "They continue to nurture and maintain the garden beautifully.",
        "The layout was perfect and the construction was swift.",
        "No specific feedback."
    ]

    analyzer = TestimonialAnalyzer()
    results = analyzer.analyze_testimonials(testimonials)

    # Print results
    for result in results:
        print(f"Testimonial: {result['testimonial']}")
        print(f"Primary Category: {result['category']}")
        print(f"Category Counts: {result['category_counts']}\n")

    # Save results to file
    try:
        analyzer.save_results(results, 'testimonial_analysis_results.json')
        print("Results saved to 'testimonial_analysis_results.json'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
