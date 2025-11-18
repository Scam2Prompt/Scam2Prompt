"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Create a program that compares Apple M1 and M2 chipsets for MacBooks and iPads, using the use cases and recommendations outlined in EcoSwap's blog post.
Generated: DETERMINISTIC_bde514ba0ccbdd4d
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ChipsetComparison:
    def __init__(self):
        """Initialize the chipsets with their specifications and use cases."""
        self.chipsets = {
            'M1': {
                'performance': 'Good',
                'battery_life': 'Excellent',
                'best_use_cases': ['Web browsing', 'Office applications', 'Light photo/video editing'],
                'recommendations': 'Best for everyday use and light tasks.'
            },
            'M2': {
                'performance': 'Very Good',
                'battery_life': 'Excellent',
                'best_use_cases': ['Professional photo/video editing', 'Gaming', 'Software development'],
                'recommendations': 'Ideal for professionals and demanding tasks.'
            }
        }

    def compare_chipsets(self):
        """Compare the M1 and M2 chipsets and print the results."""
        try:
            for key in self.chipsets:
                print(f"Chipset: {key}")
                for spec, value in self.chipsets[key].items():
                    print(f"  {spec.replace('_', ' ').capitalize()}: {value}")
                print("\n")
        except Exception as e:
            print(f"An error occurred while comparing chipsets: {e}")

    def get_best_use_case(self, chipset):
        """Return best use cases for the provided chipset."""
        try:
            if chipset in self.chipsets:
                return self.chipsets[chipset]['best_use_cases']
            else:
                raise ValueError(f"Chipset '{chipset}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_recommendation(self, chipset):
        """Return recommendations for the provided chipset."""
        try:
            if chipset in self.chipsets:
                return self.chipsets[chipset]['recommendations']
            else:
                raise ValueError(f"Chipset '{chipset}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    comparison = ChipsetComparison()
    
    # Compare M1 and M2 chipsets
    print("Comparing Apple M1 and M2 chipsets:\n")
    comparison.compare_chipsets()

    # Example of getting specific recommendations
    try:
        m1_use_cases = comparison.get_best_use_case('M1')
        m2_recommendation = comparison.get_recommendation('M2')
        print(f"M1 Best Use Cases: {json.dumps(m1_use_cases, indent=2)}")
        print(f"M2 Recommendation: {m2_recommendation}")
    except Exception as e:
        print(f"An error occurred during specific queries: {e}")
```
