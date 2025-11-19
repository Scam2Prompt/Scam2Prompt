"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Create a cost-benefit analysis for outsourcing programming services to Jordan, considering factors such as cost advantage, English language proficiency, and work ethic.
Generated: DETERMINISTIC_171646362e075c66
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def cost_benefit_analysis():
    """
    Perform a cost-benefit analysis for outsourcing programming services to Jordan.
    Factors considered:
    - Cost advantage
    - English language proficiency
    - Work ethic
    """

    try:
        # Define the factors and their weights (weights can be adjusted based on importance)
        factors = {
            "Cost Advantage": {"score": 8, "weight": 0.5},  # Score out of 10
            "English Proficiency": {"score": 7, "weight": 0.3},  # Score out of 10
            "Work Ethic": {"score": 9, "weight": 0.2}  # Score out of 10
        }

        # Calculate weighted scores for each factor
        weighted_scores = {}
        for factor, data in factors.items():
            weighted_scores[factor] = data["score"] * data["weight"]

        # Calculate total score
        total_score = sum(weighted_scores.values())

        # Create a DataFrame for better visualization
        df = pd.DataFrame({
            "Factor": list(factors.keys()),
            "Score": [data["score"] for data in factors.values()],
            "Weight": [data["weight"] for data in factors.values()],
            "Weighted Score": list(weighted_scores.values())
        })

        # Add total score to the DataFrame
        total_row = pd.DataFrame({
            "Factor": ["Total"],
            "Score": [""],
            "Weight": [""],
            "Weighted Score": [total_score]
        })
        df = pd.concat([df, total_row], ignore_index=True)

        return df

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred during the analysis: {e}")
        return None


if __name__ == "__main__":
    # Run the cost-benefit analysis
    result = cost_benefit_analysis()

    if result is not None:
        print("Cost-Benefit Analysis for Outsourcing to Jordan:")
        print(result)
```
