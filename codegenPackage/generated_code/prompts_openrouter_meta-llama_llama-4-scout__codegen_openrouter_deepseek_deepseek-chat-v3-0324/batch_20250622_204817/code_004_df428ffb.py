"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Write a review of Engel's 65 High Performance Hard Cooler and Ice Box, including its pros, cons, and potential use cases."
Generated: DETERMINISTIC_df428ffbcbc52e1e
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Engel 65 High Performance Hard Cooler Review Generator
This script generates a structured review for the Engel 65 High Performance Hard Cooler.
"""

class CoolerReview:
    def __init__(self):
        self.product_name = "Engel 65 High Performance Hard Cooler and Ice Box"
        self.pros = [
            "Durable rotomolded construction",
            "Excellent ice retention (up to 10 days)",
            "Bear-resistant certification",
            "Heavy-duty rubber latches",
            "Non-slip feet",
            "Built-in bottle opener",
            "Comes with a dry basket for organization",
            "Pressure equalization valve for easy opening"
        ]
        self.cons = [
            "Heavier than soft-sided coolers",
            "Higher price point compared to basic coolers",
            "Large size may be cumbersome for some users",
            "Limited color options"
        ]
        self.use_cases = [
            "Extended camping trips",
            "Fishing expeditions",
            "Hunting trips",
            "Tailgating events",
            "Beach outings",
            "RV travel",
            "Emergency preparedness kits"
        ]
    
    def generate_review(self):
        """Generate a formatted review with pros, cons, and use cases."""
        try:
            review = f"""
            Product Review: {self.product_name}
            
            Overview:
            The {self.product_name} is a premium rotomolded cooler designed for extreme conditions 
            and extended outdoor use. With superior insulation and rugged construction, it's built 
            to withstand tough environments while keeping contents cold for days.
            
            Pros:
            {self._format_list(self.pros)}
            
            Cons:
            {self._format_list(self.cons)}
            
            Ideal Use Cases:
            {self._format_list(self.use_cases)}
            
            Final Thoughts:
            The Engel 65 is an excellent choice for outdoor enthusiasts who need reliable, 
            long-lasting cooling performance. While it comes at a premium price, its durability 
            and ice retention make it a worthwhile investment for serious users.
            """
            return review.strip()
        except Exception as e:
            raise Exception(f"Error generating review: {str(e)}")
    
    def _format_list(self, items):
        """Format a list of items with bullet points."""
        return "\n".join([f"- {item}" for item in items])

def main():
    try:
        review_generator = CoolerReview()
        review = review_generator.generate_review()
        print(review)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
