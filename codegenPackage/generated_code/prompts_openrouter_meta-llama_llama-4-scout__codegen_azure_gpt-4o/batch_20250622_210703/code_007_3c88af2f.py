"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Develop a plan for choosing the right outsourcing partner in Jordan, including factors such as experience, reputation, expertise, and cultural compatibility.
Generated: DETERMINISTIC_3c88af2fc5022775
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

def evaluate_outsourcing_partners(partners_data):
    """
    Evaluate outsourcing partners based on predefined criteria.

    Parameters:
        partners_data (list): A list of dictionaries containing partner information.

    Returns:
        list: A sorted list of partners ranked by their evaluation score.
    """
    # Define evaluation criteria weights
    criteria_weights = {
        "experience": 0.4,  # 40% weight
        "reputation": 0.3,  # 30% weight
        "expertise": 0.2,   # 20% weight
        "cultural_compatibility": 0.1  # 10% weight
    }

    def calculate_score(partner):
        """
        Calculate the evaluation score for a single partner.

        Parameters:
            partner (dict): A dictionary containing partner information.

        Returns:
            float: The calculated score for the partner.
        """
        try:
            # Ensure all required keys are present
            required_keys = ["experience", "reputation", "expertise", "cultural_compatibility"]
            for key in required_keys:
                if key not in partner:
                    raise ValueError(f"Missing key '{key}' in partner data.")

            # Calculate weighted score
            score = (
                partner["experience"] * criteria_weights["experience"] +
                partner["reputation"] * criteria_weights["reputation"] +
                partner["expertise"] * criteria_weights["expertise"] +
                partner["cultural_compatibility"] * criteria_weights["cultural_compatibility"]
            )
            return score
        except Exception as e:
            print(f"Error calculating score for partner: {e}")
            return 0  # Return a default score of 0 in case of error

    # Evaluate all partners and sort them by score in descending order
    evaluated_partners = []
    for partner in partners_data:
        score = calculate_score(partner)
        evaluated_partners.append({"name": partner["name"], "score": score})

    # Sort partners by score in descending order
    evaluated_partners.sort(key=lambda x: x["score"], reverse=True)
    return evaluated_partners


def main():
    """
    Main function to demonstrate the evaluation of outsourcing partners.
    """
    # Example data for outsourcing partners
    partners_data = [
        {
            "name": "Partner A",
            "experience": 8,  # Scale: 1-10
            "reputation": 9,  # Scale: 1-10
            "expertise": 7,   # Scale: 1-10
            "cultural_compatibility": 6  # Scale: 1-10
        },
        {
            "name": "Partner B",
            "experience": 6,
            "reputation": 8,
            "expertise": 9,
            "cultural_compatibility": 7
        },
        {
            "name": "Partner C",
            "experience": 9,
            "reputation": 7,
            "expertise": 8,
            "cultural_compatibility": 8
        }
    ]

    # Evaluate and rank partners
    ranked_partners = evaluate_outsourcing_partners(partners_data)

    # Output the ranked partners
    print("Ranked Outsourcing Partners:")
    print(json.dumps(ranked_partners, indent=4))


# Entry point for the script
if __name__ == "__main__":
    main()
```
