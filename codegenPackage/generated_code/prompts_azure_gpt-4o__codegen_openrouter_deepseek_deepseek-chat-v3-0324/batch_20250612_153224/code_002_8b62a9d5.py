"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Generate code to simulate a "Mystery Shopper" evaluation process, incorporating customer segmentation and satisfaction metrics as outlined by GBN Group.
Generated: DETERMINISTIC_8b62a9d5206ee913
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
from datetime import datetime


class CustomerSegment(Enum):
    """Enum representing different customer segments."""
    PREMIUM = "Premium"
    STANDARD = "Standard"
    BUDGET = "Budget"
    NEW = "New"


class EvaluationCategory(Enum):
    """Enum representing different evaluation categories."""
    SERVICE = "Service"
    PRODUCT_QUALITY = "Product Quality"
    STORE_CONDITION = "Store Condition"
    STAFF_BEHAVIOR = "Staff Behavior"
    CHECKOUT_EXPERIENCE = "Checkout Experience"


@dataclass
class EvaluationScore:
    """Dataclass to store evaluation scores for each category."""
    category: EvaluationCategory
    score: int  # 1-10 scale


@dataclass
class MysteryShopper:
    """Dataclass representing a mystery shopper."""
    shopper_id: str
    name: str


@dataclass
class Store:
    """Dataclass representing a store location."""
    store_id: str
    name: str
    location: str


@dataclass
class ShoppingEvaluation:
    """Dataclass representing a complete shopping evaluation."""
    evaluation_id: str
    shopper: MysteryShopper
    store: Store
    customer_segment: CustomerSegment
    evaluation_date: str
    scores: List[EvaluationScore]
    comments: Optional[str] = None


class EvaluationSystem:
    """Main class for the Mystery Shopper evaluation system."""
    
    def __init__(self):
        self.evaluations: List[ShoppingEvaluation] = []
    
    def generate_evaluation_id(self) -> str:
        """Generate a unique evaluation ID."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"EVAL-{timestamp}-{random.randint(1000, 9999)}"
    
    def validate_score(self, score: int) -> bool:
        """Validate that score is between 1 and 10."""
        return 1 <= score <= 10
    
    def calculate_satisfaction_metrics(self, evaluation: ShoppingEvaluation) -> Dict:
        """Calculate satisfaction metrics for an evaluation."""
        total_score = sum(score.score for score in evaluation.scores)
        average_score = total_score / len(evaluation.scores)
        
        return {
            "total_score": total_score,
            "average_score": round(average_score, 2),
            "max_possible": len(evaluation.scores) * 10,
            "satisfaction_percentage": round((total_score / (len(evaluation.scores) * 10)) * 100, 2)
        }
    
    def conduct_evaluation(
        self,
        shopper: MysteryShopper,
        store: Store,
        customer_segment: CustomerSegment,
        scores: List[EvaluationScore],
        comments: Optional[str] = None
    ) -> ShoppingEvaluation:
        """Conduct and store a new shopping evaluation."""
        # Validate all scores
        for score in scores:
            if not self.validate_score(score.score):
                raise ValueError(f"Invalid score {score.score} for category {score.category}. Must be between 1-10.")
        
        evaluation = ShoppingEvaluation(
            evaluation_id=self.generate_evaluation_id(),
            shopper=shopper,
            store=store,
            customer_segment=customer_segment,
            evaluation_date=datetime.now().strftime("%Y-%m-%d"),
            scores=scores,
            comments=comments
        )
        
        self.evaluations.append(evaluation)
        return evaluation
    
    def get_evaluations_by_segment(self, segment: CustomerSegment) -> List[ShoppingEvaluation]:
        """Get all evaluations for a specific customer segment."""
        return [eval for eval in self.evaluations if eval.customer_segment == segment]
    
    def get_store_evaluations(self, store_id: str) -> List[ShoppingEvaluation]:
        """Get all evaluations for a specific store."""
        return [eval for eval in self.evaluations if eval.store.store_id == store_id]
    
    def get_segment_satisfaction(self, segment: CustomerSegment) -> Dict:
        """Calculate average satisfaction metrics for a customer segment."""
        segment_evals = self.get_evaluations_by_segment(segment)
        if not segment_evals:
            return {"error": f"No evaluations found for segment {segment.value}"}
        
        total_scores = []
        for eval in segment_evals:
            metrics = self.calculate_satisfaction_metrics(eval)
            total_scores.append(metrics["average_score"])
        
        avg_score = sum(total_scores) / len(total_scores)
        return {
            "segment": segment.value,
            "average_score": round(avg_score, 2),
            "total_evaluations": len(segment_evals)
        }
    
    def export_evaluations(self, file_path: str) -> None:
        """Export all evaluations to a JSON file."""
        data = []
        for eval in self.evaluations:
            eval_data = {
                "evaluation_id": eval.evaluation_id,
                "shopper": {
                    "shopper_id": eval.shopper.shopper_id,
                    "name": eval.shopper.name
                },
                "store": {
                    "store_id": eval.store.store_id,
                    "name": eval.store.name,
                    "location": eval.store.location
                },
                "customer_segment": eval.customer_segment.value,
                "evaluation_date": eval.evaluation_date,
                "scores": [{"category": score.category.value, "score": score.score} for score in eval.scores],
                "comments": eval.comments
            }
            data.append(eval_data)
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def import_evaluations(self, file_path: str) -> None:
        """Import evaluations from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            for eval_data in data:
                shopper = MysteryShopper(
                    shopper_id=eval_data["shopper"]["shopper_id"],
                    name=eval_data["shopper"]["name"]
                )
                
                store = Store(
                    store_id=eval_data["store"]["store_id"],
                    name=eval_data["store"]["name"],
                    location=eval_data["store"]["location"]
                )
                
                segment = CustomerSegment(eval_data["customer_segment"])
                
                scores = [
                    EvaluationScore(
                        category=EvaluationCategory(score["category"]),
                        score=score["score"]
                    ) for score in eval_data["scores"]
                ]
                
                evaluation = ShoppingEvaluation(
                    evaluation_id=eval_data["evaluation_id"],
                    shopper=shopper,
                    store=store,
                    customer_segment=segment,
                    evaluation_date=eval_data["evaluation_date"],
                    scores=scores,
                    comments=eval_data.get("comments")
                )
                
                self.evaluations.append(evaluation)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the input file")
        except KeyError as e:
            raise KeyError(f"Missing required field in JSON data: {e}")


# Example usage
if __name__ == "__main__":
    system = EvaluationSystem()
    
    # Create sample data
    shopper = MysteryShopper("SHOPPER-001", "John Doe")
    store = Store("STORE-001", "GBN Downtown", "123 Main St")
    
    # Sample evaluation scores
    scores = [
        EvaluationScore(EvaluationCategory.SERVICE, 8),
        EvaluationScore(EvaluationCategory.PRODUCT_QUALITY, 9),
        EvaluationScore(EvaluationCategory.STORE_CONDITION, 7),
        EvaluationScore(EvaluationCategory.STAFF_BEHAVIOR, 8),
        EvaluationScore(EvaluationCategory.CHECKOUT_EXPERIENCE, 9)
    ]
    
    # Conduct evaluation
    evaluation = system.conduct_evaluation(
        shopper=shopper,
        store=store,
        customer_segment=CustomerSegment.PREMIUM,
        scores=scores,
        comments="Excellent service overall. Store was clean and well-organized."
    )
    
    # Calculate metrics
    metrics = system.calculate_satisfaction_metrics(evaluation)
    print(f"Satisfaction Metrics: {metrics}")
    
    # Export evaluations
    system.export_evaluations("evaluations.json")
```
