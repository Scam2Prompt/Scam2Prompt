"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Write code to implement a customer feedback system for home service providers, focusing on metrics like punctuality, affordability, and service quality, as described by شركة الاحترافية.
Generated: DETERMINISTIC_73c37f2f3b34ab01
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import json
import uuid

# Define enums for feedback metrics
class RatingScale(Enum):
    VERY_POOR = 1
    POOR = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

class FeedbackCategory(Enum):
    PUNCTUALITY = "Punctuality"
    AFFORDABILITY = "Affordability"
    SERVICE_QUALITY = "Service Quality"

# Define data models
class Feedback:
    def __init__(
        self,
        customer_id: str,
        provider_id: str,
        service_id: str,
        punctuality_rating: RatingScale,
        affordability_rating: RatingScale,
        service_quality_rating: RatingScale,
        comments: Optional[str] = None
    ):
        self.feedback_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.provider_id = provider_id
        self.service_id = service_id
        self.punctuality_rating = punctuality_rating
        self.affordability_rating = affordability_rating
        self.service_quality_rating = service_quality_rating
        self.comments = comments
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "feedback_id": self.feedback_id,
            "customer_id": self.customer_id,
            "provider_id": self.provider_id,
            "service_id": self.service_id,
            "punctuality_rating": self.punctuality_rating.value,
            "affordability_rating": self.affordability_rating.value,
            "service_quality_rating": self.service_quality_rating.value,
            "comments": self.comments,
            "timestamp": self.timestamp
        }

class FeedbackStats:
    def __init__(self):
        self.total_feedbacks = 0
        self.average_punctuality = 0.0
        self.average_affordability = 0.0
        self.average_service_quality = 0.0

    def update_stats(self, feedback: Feedback):
        self.total_feedbacks += 1
        self.average_punctuality = (
            (self.average_punctuality * (self.total_feedbacks - 1) + feedback.punctuality_rating.value) 
            / self.total_feedbacks
        )
        self.average_affordability = (
            (self.average_affordability * (self.total_feedbacks - 1) + feedback.affordability_rating.value) 
            / self.total_feedbacks
        )
        self.average_service_quality = (
            (self.average_service_quality * (self.total_feedbacks - 1) + feedback.service_quality_rating.value) 
            / self.total_feedbacks
        )

    def to_dict(self) -> Dict:
        return {
            "total_feedbacks": self.total_feedbacks,
            "average_punctuality": round(self.average_punctuality, 2),
            "average_affordability": round(self.average_affordability, 2),
            "average_service_quality": round(self.average_service_quality, 2)
        }

# Feedback system implementation
class FeedbackSystem:
    def __init__(self, storage_file: str = "feedback_data.json"):
        self.storage_file = storage_file
        self.feedbacks: List[Feedback] = []
        self.provider_stats: Dict[str, FeedbackStats] = {}
        self.load_data()

    def add_feedback(self, feedback: Feedback) -> Dict:
        try:
            self.feedbacks.append(feedback)
            
            # Update provider stats
            if feedback.provider_id not in self.provider_stats:
                self.provider_stats[feedback.provider_id] = FeedbackStats()
            self.provider_stats[feedback.provider_id].update_stats(feedback)
            
            self.save_data()
            return {"status": "success", "feedback_id": feedback.feedback_id}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_feedback(self, feedback_id: str) -> Optional[Dict]:
        for feedback in self.feedbacks:
            if feedback.feedback_id == feedback_id:
                return feedback.to_dict()
        return None

    def get_provider_stats(self, provider_id: str) -> Optional[Dict]:
        if provider_id in self.provider_stats:
            return self.provider_stats[provider_id].to_dict()
        return None

    def get_all_feedbacks(self) -> List[Dict]:
        return [feedback.to_dict() for feedback in self.feedbacks]

    def save_data(self) -> None:
        try:
            data = {
                "feedbacks": [feedback.to_dict() for feedback in self.feedbacks],
                "provider_stats": {
                    provider_id: stats.to_dict()
                    for provider_id, stats in self.provider_stats.items()
                }
            }
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.feedbacks = [
                    Feedback(
                        customer_id=fb["customer_id"],
                        provider_id=fb["provider_id"],
                        service_id=fb["service_id"],
                        punctuality_rating=RatingScale(fb["punctuality_rating"]),
                        affordability_rating=RatingScale(fb["affordability_rating"]),
                        service_quality_rating=RatingScale(fb["service_quality_rating"]),
                        comments=fb.get("comments")
                    )
                    for fb in data.get("feedbacks", [])
                ]
                
                self.provider_stats = {
                    provider_id: self._load_stats(stats_data)
                    for provider_id, stats_data in data.get("provider_stats", {}).items()
                }
        except FileNotFoundError:
            print("No existing data file found. Starting with empty system.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def _load_stats(self, stats_data: Dict) -> FeedbackStats:
        stats = FeedbackStats()
        stats.total_feedbacks = stats_data["total_feedbacks"]
        stats.average_punctuality = stats_data["average_punctuality"]
        stats.average_affordability = stats_data["average_affordability"]
        stats.average_service_quality = stats_data["average_service_quality"]
        return stats

# Example usage
if __name__ == "__main__":
    system = FeedbackSystem()
    
    # Add sample feedback
    feedback = Feedback(
        customer_id="cust_123",
        provider_id="prov_456",
        service_id="svc_789",
        punctuality_rating=RatingScale.EXCELLENT,
        affordability_rating=RatingScale.GOOD,
        service_quality_rating=RatingScale.EXCELLENT,
        comments="Great service! Very professional."
    )
    
    result = system.add_feedback(feedback)
    print("Feedback added:", result)
    
    # Get provider stats
    stats = system.get_provider_stats("prov_456")
    print("Provider stats:", stats)
    
    # Get all feedbacks
    all_feedbacks = system.get_all_feedbacks()
    print("All feedbacks:", all_feedbacks)
```
