"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Write a program to analyze client testimonials and extract key performance metrics related to MM Group Nepal's packaging solutions.
Generated: DETERMINISTIC_fb203ad13325a6da
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict
from typing import Dict, List, Tuple
import json

class TestimonialAnalyzer:
    """
    A class to analyze client testimonials and extract key performance metrics
    related to MM Group Nepal's packaging solutions.
    """

    def __init__(self):
        """
        Initialize the analyzer with predefined metrics and patterns.
        """
        self.metrics = {
            'delivery_time': r'deliver(y|ies|ed)?\s*(in|within|of)?\s*(\d+)\s*(days|day|hours|hour|hrs|hr)',
            'cost_reduction': r'(cost|price|expense)(\s*reduction|\s*savings|\s*cut|\s*decrease)\s*(of|by)?\s*(\d+%|\$\d+)',
            'customer_satisfaction': r'(satisfaction|happy|pleased|impressed)\s*(rate|rating|score)?\s*(of|at)?\s*(\d+%|\d+\s*out\s*of\s*\d+)',
            'product_quality': r'(quality|durability|strength)\s*(rate|rating|score)?\s*(of|at)?\s*(\d+%|\d+\s*out\s*of\s*\d+|excellent|good|great)',
            'repeat_business': r'(repeat|returning)\s*(customer|business|order|purchase)'
        }

    def analyze_testimonials(self, testimonials: List[str]) -> Dict[str, Dict[str, List[str]]]:
        """
        Analyze a list of testimonials and extract key performance metrics.

        Args:
            testimonials: List of testimonial strings to analyze

        Returns:
            Dictionary containing extracted metrics grouped by metric type
        """
        results = defaultdict(lambda: defaultdict(list))

        for testimonial in testimonials:
            for metric, pattern in self.metrics.items():
                matches = re.finditer(pattern, testimonial, re.IGNORECASE)
                for match in matches:
                    results[metric]['matches'].append(match.group())
                    results[metric]['context'].append(self._get_context(testimonial, match.start(), match.end()))

        return dict(results)

    def _get_context(self, text: str, start: int, end: int, window: int = 50) -> str:
        """
        Extract context around a matched pattern.

        Args:
            text: The full text
            start: Start index of match
            end: End index of match
            window: Number of characters to include before and after match

        Returns:
            String containing the match with surrounding context
        """
        context_start = max(0, start - window)
        context_end = min(len(text), end + window)
        return text[context_start:context_end]

    def save_results(self, results: Dict, filename: str) -> None:
        """
        Save analysis results to a JSON file.

        Args:
            results: Analysis results dictionary
            filename: Output filename
        """
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
        except IOError as e:
            print(f"Error saving results: {e}")

    def load_testimonials(self, filename: str) -> List[str]:
        """
        Load testimonials from a JSON file.

        Args:
            filename: Input filename

        Returns:
            List of testimonial strings

        Raises:
            IOError: If file cannot be read
            ValueError: If file is not valid JSON
        """
        try:
            with open(filename) as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                elif 'testimonials' in data:
                    return data['testimonials']
                else:
                    raise ValueError("Invalid JSON format: expected list or object with 'testimonials' key")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {e}")
        except IOError as e:
            raise IOError(f"Could not read file: {e}")


def main():
    """
    Main execution function for the testimonial analyzer.
    """
    analyzer = TestimonialAnalyzer()
    
    try:
        # Example usage with sample testimonials
        sample_testimonials = [
            "MM Group Nepal delivered our packaging order within 3 days, which was faster than expected.",
            "Their packaging solutions helped us achieve a cost reduction of 15% compared to our previous supplier.",
            "We're extremely pleased with the quality - 9 out of 10! Will definitely be a returning customer.",
            "The durability of their packaging materials is excellent, and we've seen a 20% decrease in damaged goods."
        ]
        
        # Analyze sample testimonials
        results = analyzer.analyze_testimonials(sample_testimonials)
        
        # Save results to file
        analyzer.save_results(results, 'testimonial_analysis.json')
        print("Analysis completed successfully. Results saved to testimonial_analysis.json")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
