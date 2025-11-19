"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write a Python script to manage customer satisfaction surveys for a computer repair service like Geeks on Repair.
Generated: DETERMINISTIC_db544ee3ef00e008
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class SurveyManager:
    """Manages customer satisfaction surveys for a computer repair service."""
    
    def __init__(self, data_file: str = "survey_data.json"):
        """Initialize the SurveyManager with a data file.
        
        Args:
            data_file: Path to the JSON file storing survey data.
        """
        self.data_file = data_file
        self.surveys = self._load_data()
        
    def _load_data(self) -> Dict[str, List[Dict]]:
        """Load survey data from the JSON file.
        
        Returns:
            Dictionary containing survey data.
            
        Raises:
            FileNotFoundError: If the data file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}: {e}")
            
    def _save_data(self) -> None:
        """Save survey data to the JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.surveys, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save data to {self.data_file}: {e}")
            
    def add_survey(self, customer_id: str, rating: int, comments: Optional[str] = None) -> None:
        """Add a new survey response.
        
        Args:
            customer_id: Unique identifier for the customer.
            rating: Satisfaction rating (1-5 scale).
            comments: Optional comments from the customer.
            
        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
            
        survey = {
            "timestamp": datetime.now().isoformat(),
            "rating": rating,
            "comments": comments
        }
        
        if customer_id not in self.surveys:
            self.surveys[customer_id] = []
            
        self.surveys[customer_id].append(survey)
        self._save_data()
        
    def get_customer_surveys(self, customer_id: str) -> List[Dict]:
        """Get all survey responses for a customer.
        
        Args:
            customer_id: Customer identifier to look up.
            
        Returns:
            List of survey responses for the customer, or empty list if none exist.
        """
        return self.surveys.get(customer_id, [])
        
    def get_average_rating(self) -> float:
        """Calculate the average satisfaction rating across all surveys.
        
        Returns:
            Average rating (0 if no surveys exist).
        """
        total = 0
        count = 0
        
        for surveys in self.surveys.values():
            for survey in surveys:
                total += survey["rating"]
                count += 1
                
        return total / count if count > 0 else 0
        
    def get_feedback_comments(self, min_rating: Optional[int] = None, max_rating: Optional[int] = None) -> List[str]:
        """Get all feedback comments filtered by rating range.
        
        Args:
            min_rating: Minimum rating to include (inclusive).
            max_rating: Maximum rating to include (inclusive).
            
        Returns:
            List of comments matching the rating filter.
        """
        comments = []
        
        for surveys in self.surveys.values():
            for survey in surveys:
                if "comments" in survey and survey["comments"]:
                    rating = survey["rating"]
                    if ((min_rating is None or rating >= min_rating) and 
                        (max_rating is None or rating <= max_rating)):
                        comments.append(survey["comments"])
                        
        return comments
        
    def export_to_csv(self, output_file: str) -> None:
        """Export survey data to a CSV file.
        
        Args:
            output_file: Path to the output CSV file.
            
        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(output_file, 'w') as f:
                f.write("customer_id,timestamp,rating,comments\n")
                for customer_id, surveys in self.surveys.items():
                    for survey in surveys:
                        comments = survey.get("comments", "").replace('"', '""')
                        f.write(f'"{customer_id}","{survey["timestamp"]}",{survey["rating"]},"{comments}"\n')
        except IOError as e:
            raise IOError(f"Failed to export to {output_file}: {e}")


def main():
    """Example usage of the SurveyManager."""
    try:
        manager = SurveyManager()
        
        # Add some sample surveys
        manager.add_survey("cust001", 5, "Great service! Fixed my laptop quickly.")
        manager.add_survey("cust001", 4, "Good service but a bit expensive.")
        manager.add_survey("cust002", 3, "Average experience.")
        manager.add_survey("cust003", 1, "Terrible service. Didn't fix my issue.")
        
        # Print average rating
        print(f"Average rating: {manager.get_average_rating():.1f}")
        
        # Print all low-rating comments
        print("\nLow-rating feedback:")
        for comment in manager.get_feedback_comments(max_rating=2):
            print(f"- {comment}")
            
        # Export data
        manager.export_to_csv("survey_export.csv")
        print("\nData exported to survey_export.csv")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
