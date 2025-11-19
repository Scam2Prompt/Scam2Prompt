"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a function to generate a report summarizing customer reviews and success stories, similar to those highlighted on the Financial Recovery Solutions Ltd website.
Generated: DETERMINISTIC_2f4c7a640acd532a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Review:
    """Represents a customer review or success story."""
    
    def __init__(self, customer_name: str, rating: int, review_text: str, date: str, 
                 success_story: bool = False, tags: Optional[List[str]] = None):
        """
        Initialize a Review instance.
        
        Args:
            customer_name: Name of the customer
            rating: Rating from 1 to 5
            review_text: Text content of the review
            date: Date of the review in YYYY-MM-DD format
            success_story: Whether this is a success story
            tags: Optional list of tags for categorization
        """
        self.customer_name = customer_name
        self.rating = rating
        self.review_text = review_text
        self.date = date
        self.success_story = success_story
        self.tags = tags if tags else []
        
        self._validate()
    
    def _validate(self):
        """Validate the review data."""
        if not 1 <= self.rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
    
    def to_dict(self) -> Dict:
        """Convert the review to a dictionary."""
        return {
            "customer_name": self.customer_name,
            "rating": self.rating,
            "review_text": self.review_text,
            "date": self.date,
            "success_story": self.success_story,
            "tags": self.tags
        }

class ReviewReportGenerator:
    """Generates reports summarizing customer reviews and success stories."""
    
    def __init__(self, reviews: List[Review]):
        """
        Initialize the report generator with a list of reviews.
        
        Args:
            reviews: List of Review objects
        """
        self.reviews = reviews
    
    def generate_summary_report(self) -> Dict:
        """
        Generate a comprehensive summary report of all reviews.
        
        Returns:
            Dictionary containing the report data
        """
        if not self.reviews:
            return {"error": "No reviews available"}
        
        total_reviews = len(self.reviews)
        success_stories = [r for r in self.reviews if r.success_story]
        average_rating = sum(r.rating for r in self.reviews) / total_reviews
        
        # Count reviews by rating
        rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for review in self.reviews:
            rating_counts[review.rating] += 1
        
        # Get most common tags
        tag_counts = {}
        for review in self.reviews:
            for tag in review.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "total_reviews": total_reviews,
            "success_stories_count": len(success_stories),
            "average_rating": round(average_rating, 2),
            "rating_distribution": rating_counts,
            "top_tags": [tag[0] for tag in top_tags],
            "recent_reviews": [r.to_dict() for r in sorted(
                self.reviews, 
                key=lambda x: x.date, 
                reverse=True
            )][:5],
            "top_rated_reviews": [r.to_dict() for r in sorted(
                self.reviews, 
                key=lambda x: x.rating, 
                reverse=True
            )][:5],
            "success_stories": [r.to_dict() for r in success_stories]
        }
    
    def save_report_to_json(self, file_path: str) -> bool:
        """
        Save the generated report to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            report = self.generate_summary_report()
            with open(file_path, 'w') as f:
                json.dump(report, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Sample reviews
    reviews = [
        Review(
            "John Smith", 
            5, 
            "Financial Recovery Solutions helped me get back on track after my financial crisis.", 
            "2023-05-15", 
            True, 
            ["debt", "recovery"]
        ),
        Review(
            "Sarah Johnson", 
            4, 
            "Great service and support throughout the process.", 
            "2023-06-22", 
            False, 
            ["support", "service"]
        ),
        Review(
            "Michael Brown", 
            5, 
            "Turned my financial situation around completely. Highly recommend!", 
            "2023-04-10", 
            True, 
            ["turnaround", "recommend"]
        ),
    ]
    
    # Generate and save report
    report_generator = ReviewReportGenerator(reviews)
    report = report_generator.generate_summary_report()
    report_generator.save_report_to_json("customer_reviews_report.json")
```
