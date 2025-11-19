"""
Generated Code Metadata:
========================
Original URL: https://grandchemuyil.com
Prompt: Write code to analyze user reviews of mobile casinos and generate a sentiment score for each casino, using the criteria listed on the Grand Chemuyil page.
Generated: DETERMINISTIC_2d59806eb411c7b7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
from textblob import TextBlob
from typing import List, Dict, Tuple

class CasinoReviewAnalyzer:
    """
    Analyzes user reviews of mobile casinos and generates sentiment scores based on specified criteria.
    """
    
    def __init__(self, criteria: Dict[str, float]):
        """
        Initialize with criteria weights for sentiment analysis.
        
        Args:
            criteria: Dictionary of criteria and their weights (e.g., {"bonuses": 0.3, "game_variety": 0.2})
        """
        self.criteria = criteria
        self.normalized_criteria = self._normalize_criteria()
        
    def _normalize_criteria(self) -> Dict[str, float]:
        """
        Normalize criteria weights to sum to 1.
        
        Returns:
            Normalized criteria weights.
        """
        total = sum(self.criteria.values())
        return {k: v/total for k, v in self.criteria.items()}
    
    def _extract_criteria_mentions(self, text: str) -> Dict[str, List[str]]:
        """
        Extract mentions of each criteria in the review text.
        
        Args:
            text: Review text to analyze.
            
        Returns:
            Dictionary with criteria as keys and list of mentions as values.
        """
        mentions = {criterion: [] for criterion in self.criteria}
        
        for criterion in self.criteria:
            # Simple pattern matching for criteria mentions
            pattern = re.compile(rf'\b{criterion}\b|\b{criterion[:-1]}\b', re.IGNORECASE)
            matches = pattern.findall(text)
            if matches:
                mentions[criterion] = matches
                
        return mentions
    
    def _calculate_criterion_sentiment(self, text: str, criterion: str) -> float:
        """
        Calculate sentiment score for a specific criterion in the text.
        
        Args:
            text: Review text.
            criterion: Criterion to analyze.
            
        Returns:
            Sentiment polarity score between -1 and 1.
        """
        # Focus on sentences mentioning the criterion
        sentences = [sentence for sentence in TextBlob(text).sentences 
                    if criterion.lower() in sentence.lower()]
        
        if not sentences:
            return 0.0
        
        # Average sentiment of relevant sentences
        sentiment = sum(s.sentiment.polarity for s in sentences) / len(sentences)
        return sentiment
    
    def analyze_review(self, review: str) -> Dict[str, float]:
        """
        Analyze a single review and return sentiment scores per criterion.
        
        Args:
            review: Text of the user review.
            
        Returns:
            Dictionary with criterion as key and sentiment score as value.
        """
        results = {}
        mentions = self._extract_criteria_mentions(review)
        
        for criterion in self.criteria:
            if mentions[criterion]:
                sentiment = self._calculate_criterion_sentiment(review, criterion)
                results[criterion] = sentiment
            else:
                results[criterion] = 0.0
                
        return results
    
    def calculate_overall_score(self, review_scores: Dict[str, float]) -> float:
        """
        Calculate weighted overall sentiment score for a review.
        
        Args:
            review_scores: Dictionary of criterion scores from analyze_review().
            
        Returns:
            Weighted average sentiment score.
        """
        return sum(score * self.normalized_criteria[criterion] 
                  for criterion, score in review_scores.items())
    
    def analyze_casino(self, reviews: List[str]) -> Dict[str, float]:
        """
        Analyze multiple reviews for a casino and return average scores.
        
        Args:
            reviews: List of review texts for a casino.
            
        Returns:
            Dictionary with average criterion scores and overall score.
        """
        if not reviews:
            raise ValueError("No reviews provided for analysis")
            
        all_scores = []
        for review in reviews:
            all_scores.append(self.analyze_review(review))
            
        # Calculate average scores per criterion
        avg_scores = {}
        for criterion in self.criteria:
            criterion_scores = [score[criterion] for score in all_scores]
            avg_scores[criterion] = sum(criterion_scores) / len(criterion_scores)
            
        # Calculate overall average
        avg_scores['overall'] = self.calculate_overall_score(avg_scores)
        
        return avg_scores
    
    def analyze_multiple_casinos(self, casino_reviews: Dict[str, List[str]]) -> pd.DataFrame:
        """
        Analyze reviews for multiple casinos and return results in a DataFrame.
        
        Args:
            casino_reviews: Dictionary with casino names as keys and list of reviews as values.
            
        Returns:
            DataFrame with sentiment analysis results.
        """
        results = []
        
        for casino, reviews in casino_reviews.items():
            try:
                scores = self.analyze_casino(reviews)
                scores['casino'] = casino
                results.append(scores)
            except Exception as e:
                print(f"Error analyzing {casino}: {str(e)}")
                continue
                
        return pd.DataFrame(results)


# Example usage
if __name__ == "__main__":
    # Example criteria from Grand Chemuyil (replace with actual criteria)
    criteria = {
        "bonuses": 0.3,
        "game_variety": 0.2,
        "user_interface": 0.15,
        "customer_support": 0.15,
        "payout_speed": 0.2
    }
    
    analyzer = CasinoReviewAnalyzer(criteria)
    
    # Example reviews data
    casino_reviews = {
        "Lucky Casino": [
            "Great bonuses and fast payouts. The game variety could be better though.",
            "Customer support is responsive. The user interface is clean and easy to use."
        ],
        "Fortune Palace": [
            "Terrible experience. Slow payouts and unhelpful support.",
            "The bonuses are decent but the games keep crashing."
        ]
    }
    
    results = analyzer.analyze_multiple_casinos(casino_reviews)
    print(results)
```
