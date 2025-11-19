"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Recommend a suitable hot tub model from Oasis Hot Tubs for a customer with a specific budget and desired features, and provide a justification for the recommendation.
Generated: DETERMINISTIC_600ec1ed5a4e61b3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HotTub:
    """
    Represents a hot tub model with its features and price.
    """
    def __init__(self, model_name, capacity, jets, seating_type, price, energy_efficiency):
        self.model_name = model_name
        self.capacity = capacity  # in gallons
        self.jets = jets  # number of jets
        self.seating_type = seating_type  # e.g., "lounge", "upright", "mixed"
        self.price = price
        self.energy_efficiency = energy_efficiency  # rating from 1-5

class HotTubRecommender:
    """
    Recommends hot tub models based on customer preferences and budget.
    """
    def __init__(self):
        self.inventory = self._load_inventory()

    def _load_inventory(self):
        """
        Loads the available hot tub models from Oasis Hot Tubs.
        """
        return [
            HotTub("Serenity 200", 250, 35, "lounge", 4500, 4),
            HotTub("Tranquility 300", 350, 50, "mixed", 6500, 5),
            HotTub("Harmony 150", 200, 25, "upright", 3500, 3),
            HotTub("Bliss 400", 400, 70, "mixed", 8000, 4),
            HotTub("Escape 250", 300, 40, "lounge", 5500, 5)
        ]

    def recommend_hot_tub(self, budget, min_jets=None, seating_preference=None, min_efficiency=None):
        """
        Recommends hot tubs based on customer criteria.
        
        Args:
            budget: Maximum budget in dollars
            min_jets: Minimum number of jets desired (optional)
            seating_preference: Preferred seating type (optional)
            min_efficiency: Minimum energy efficiency rating (1-5, optional)
        
        Returns:
            dict: {
                'recommendation': HotTub object or None,
                'justification': str,
                'alternatives': list[HotTub]
            }
        """
        try:
            # Filter by budget first
            affordable_tubs = [tub for tub in self.inventory if tub.price <= budget]
            
            if not affordable_tubs:
                return {
                    'recommendation': None,
                    'justification': f"No hot tubs available within budget of ${budget}",
                    'alternatives': []
                }

            # Apply additional filters
            filtered_tubs = affordable_tubs
            if min_jets is not None:
                filtered_tubs = [tub for tub in filtered_tubs if tub.jets >= min_jets]
            if seating_preference is not None:
                filtered_tubs = [tub for tub in filtered_tubs if tub.seating_type == seating_preference]
            if min_efficiency is not None:
                filtered_tubs = [tub for tub in filtered_tubs if tub.energy_efficiency >= min_efficiency]

            if not filtered_tubs:
                # Return closest match with justification
                best_match = max(affordable_tubs, key=lambda x: (
                    (1 if min_jets is None or x.jets >= min_jets else 0) +
                    (1 if seating_preference is None or x.seating_type == seating_preference else 0) +
                    (1 if min_efficiency is None or x.energy_efficiency >= min_efficiency else 0)
                ))
                
                justification_parts = []
                if min_jets is not None and best_match.jets < min_jets:
                    justification_parts.append(f"only has {best_match.jets} jets (wanted {min_jets}+)")
                if seating_preference is not None and best_match.seating_type != seating_preference:
                    justification_parts.append(f"has {best_match.seating_type} seating (wanted {seating_preference})")
                if min_efficiency is not None and best_match.energy_efficiency < min_efficiency:
                    justification_parts.append(f"has efficiency rating {best_match.energy_efficiency} (wanted {min_efficiency}+)")
                
                justification = f"Best available match: {best_match.model_name}. " + ", ".join(justification_parts)
                
                return {
                    'recommendation': best_match,
                    'justification': justification,
                    'alternatives': affordable_tubs
                }

            # Sort by price ascending, then by number of jets descending
            filtered_tubs.sort(key=lambda x: (x.price, -x.jets))
            recommendation = filtered_tubs[0]
            
            justification = f"Recommended {recommendation.model_name} because it fits your budget of ${budget}"
            if min_jets is not None:
                justification += f", has {recommendation.jets} jets"
            if seating_preference is not None:
                justification += f", has {recommendation.seating_type} seating"
            if min_efficiency is not None:
                justification += f", and has energy efficiency rating of {recommendation.energy_efficiency}"
            
            return {
                'recommendation': recommendation,
                'justification': justification,
                'alternatives': filtered_tubs[1:] if len(filtered_tubs) > 1 else []
            }

        except Exception as e:
            return {
                'recommendation': None,
                'justification': f"Error occurred while processing recommendation: {str(e)}",
                'alternatives': []
            }

# Example usage
if __name__ == "__main__":
    recommender = HotTubRecommender()
    recommendation = recommender.recommend_hot_tub(
        budget=5000,
        min_jets=30,
        seating_preference="lounge",
        min_efficiency=4
    )
    
    if recommendation['recommendation']:
        print(f"Recommendation: {recommendation['recommendation'].model_name}")
        print(f"Justification: {recommendation['justification']}")
        if recommendation['alternatives']:
            print("\nAlternatives:")
            for alt in recommendation['alternatives']:
                print(f"- {alt.model_name} (${alt.price})")
    else:
        print(recommendation['justification'])
```
