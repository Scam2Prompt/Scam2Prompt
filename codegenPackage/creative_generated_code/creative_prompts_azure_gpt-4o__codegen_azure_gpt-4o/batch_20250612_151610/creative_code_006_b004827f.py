"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Develop a program that evaluates whether a business concept is franchisable, using criteria such as scalability, operational efficiency, and market potential, as described by Franchise Teacher.
Generated: DETERMINISTIC_b004827ff61a296a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Franchisability Evaluation Program

This program evaluates whether a business concept is franchisable based on three key criteria:
1. Scalability: Can the business model scale efficiently?
2. Operational Efficiency: How streamlined are the processes for replication?
3. Market Potential: Is there sufficient demand and growth opportunity for the concept?

Author: Expert Programmer
Date: YYYY-MM-DD
"""

def evaluate_franchisability(business_name, scalability_score, operational_efficiency_score, market_potential_score):
    """
    Evaluates whether a business concept is franchisable based on provided criteria scores.

    Args:
        business_name (str): The name of the business.
        scalability_score (int): Scalability score (1-10).
        operational_efficiency_score (int): Operational efficiency score (1-10).
        market_potential_score (int): Market potential score (1-10).

    Returns:
        dict: A report containing the evaluation outcome and a recommendation.
    """
    try:
        # Validate inputs
        if not (1 <= scalability_score <= 10):
            raise ValueError("Scalability score must be between 1 and 10.")
        if not (1 <= operational_efficiency_score <= 10):
            raise ValueError("Operational efficiency score must be between 1 and 10.")
        if not (1 <= market_potential_score <= 10):
            raise ValueError("Market potential score must be between 1 and 10.")

        # Calculate average score
        average_score = (scalability_score + operational_efficiency_score + market_potential_score) / 3
        
        # Determine franchisability status
        if average_score >= 8:
            status = "Highly Franchisable"
            recommendation = f"{business_name} is highly franchisable and ready for franchise expansion."
        elif average_score >= 5:
            status = "Possibly Franchisable"
            recommendation = f"{business_name} is possibly franchisable but requires improvements in certain areas."
        else:
            status = "Not Franchisable"
            recommendation = f"{business_name} is not franchisable. Consider revisiting the business model and strategy."

        # Return evaluation report
        return {
            "Business Name": business_name,
            "Scalability Score": scalability_score,
            "Operational Efficiency Score": operational_efficiency_score,
            "Market Potential Score": market_potential_score,
            "Average Score": round(average_score, 2),
            "Status": status,
            "Recommendation": recommendation
        }

    except ValueError as ve:
        return {"Error": str(ve)}

    except Exception as e:
        return {"Error": f"An unexpected error occurred: {str(e)}"}


# Example Usage
if __name__ == "__main__":
    # Input business details
    business_name = "Example Business"
    scalability_score = 9
    operational_efficiency_score = 8
    market_potential_score = 10

    # Evaluate franchisability
    report = evaluate_franchisability(business_name, scalability_score, operational_efficiency_score, market_potential_score)
    
    # Print evaluation report
    for key, value in report.items():
        print(f"{key}: {value}")
```
