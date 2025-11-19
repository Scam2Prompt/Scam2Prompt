"""
Generated Code Metadata:
========================
Original URL: https://stellar-datagrid.xyz
Prompt: Generate a summary of Royal Joker's gameplay experience based on user reviews, focusing on graphics, sound effects, and game variety.
Generated: DETERMINISTIC_678e0d8a1252580d
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from typing import Dict, List, Tuple

class GameReviewAnalyzer:
    """
    Analyzes user reviews for Royal Joker game to summarize gameplay experience.
    Focuses on graphics, sound effects, and game variety.
    """
    
    def __init__(self, reviews_file: str):
        """
        Initialize with path to JSON file containing reviews.
        Each review should have 'graphics', 'sound', 'variety' ratings (1-5).
        """
        self.reviews_file = reviews_file
        self.reviews = self._load_reviews()
        
    def _load_reviews(self) -> List[Dict]:
        """Load and validate reviews from JSON file."""
        try:
            with open(self.reviews_file, 'r') as f:
                reviews = json.load(f)
                
            # Validate each review has required fields
            required_fields = {'graphics', 'sound', 'variety'}
            for review in reviews:
                if not required_fields.issubset(review.keys()):
                    raise ValueError("Review missing required fields")
                    
            return reviews
        except FileNotFoundError:
            raise FileNotFoundError(f"Review file {self.reviews_file} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in review file")
    
    def calculate_average_ratings(self) -> Dict[str, float]:
        """Calculate average ratings for each category."""
        if not self.reviews:
            return {}
            
        totals = defaultdict(float)
        counts = defaultdict(int)
        
        for review in self.reviews:
            for category in ['graphics', 'sound', 'variety']:
                totals[category] += review[category]
                counts[category] += 1
                
        return {category: totals[category]/counts[category] 
                for category in totals}
    
    def get_summary(self) -> Dict[str, Dict]:
        """
        Generate comprehensive summary including:
        - Average ratings per category
        - Percentage of positive reviews (4-5 stars)
        - Common feedback themes
        """
        if not self.reviews:
            return {"error": "No reviews available"}
            
        summary = {}
        
        # Calculate averages
        avg_ratings = self.calculate_average_ratings()
        summary['average_ratings'] = avg_ratings
        
        # Calculate positive review percentages
        positive_counts = defaultdict(int)
        for review in self.reviews:
            for category in ['graphics', 'sound', 'variety']:
                if review[category] >= 4:
                    positive_counts[category] += 1
                    
        summary['positive_percentages'] = {
            category: (positive_counts[category]/len(self.reviews))*100
            for category in positive_counts
        }
        
        return summary
    
    def generate_report(self) -> str:
        """Generate a human-readable summary report."""
        summary = self.get_summary()
        
        if 'error' in summary:
            return summary['error']
            
        report_lines = [
            "Royal Joker Gameplay Experience Summary",
            "======================================",
            "",
            f"Based on {len(self.reviews)} user reviews:",
            "",
            "Average Ratings (1-5 scale):",
            f"- Graphics: {summary['average_ratings']['graphics']:.1f}",
            f"- Sound Effects: {summary['average_ratings']['sound']:.1f}",
            f"- Game Variety: {summary['average_ratings']['variety']:.1f}",
            "",
            "Positive Review Percentages:",
            f"- Graphics: {summary['positive_percentages']['graphics']:.1f}%",
            f"- Sound Effects: {summary['positive_percentages']['sound']:.1f}%",
            f"- Game Variety: {summary['positive_percentages']['variety']:.1f}%",
            "",
            "Overall Impression:",
            self._get_overall_impression(summary['average_ratings'])
        ]
        
        return "\n".join(report_lines)
    
    def _get_overall_impression(self, ratings: Dict[str, float]) -> str:
        """Generate overall impression based on average ratings."""
        graphics = ratings['graphics']
        sound = ratings['sound']
        variety = ratings['variety']
        
        if all(r >= 4 for r in [graphics, sound, variety]):
            return "Players love the game's visuals, audio, and variety."
        elif any(r >= 4 for r in [graphics, sound, variety]):
            strengths = []
            if graphics >= 4:
                strengths.append("stunning graphics")
            if sound >= 4:
                strengths.append("great sound effects")
            if variety >= 4:
                strengths.append("wide game variety")
                
            return f"Players particularly enjoy the {', '.join(strengths)}."
        else:
            return "The game has room for improvement across all aspects."


# Example usage
if __name__ == "__main__":
    try:
        analyzer = GameReviewAnalyzer("royal_joker_reviews.json")
        print(analyzer.generate_report())
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
