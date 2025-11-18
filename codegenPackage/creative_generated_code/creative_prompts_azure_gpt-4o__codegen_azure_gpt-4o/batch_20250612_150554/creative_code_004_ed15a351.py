"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infiniteworks.net
Prompt: Write a script to analyze customer feedback data, referencing the 4.8 rating from 1,400+ customers mentioned on Infinite Works Limited's website.
Generated: DETERMINISTIC_ed15a35174c9fdff
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import statistics
from typing import List, Dict

# Simulated customer feedback data (for demonstration purposes)
customer_feedback_data = [
    "Great service! Rating: 5",
    "Not bad, but could be improved. Rating: 4",
    "Amazing experience, highly recommend! Rating: 5",
    "Okay service. Rating: 3",
    "Fantastic support, will use again. Rating: 5",
    "Average service. Rating: 3",
    "Good value for money. Rating: 4",
    "Excellent product. Rating: 5",
    "Could've been better. Rating: 3",
    "Very satisfied! Rating: 5"
]

# Predefined rating reference from Infinite Works Limited's website
expected_rating = 4.8
expected_reviews_count = 1400

def extract_ratings(feedback_list: List[str]) -> List[int]:
    """
    Extracts numeric ratings from customer feedback strings.

    Args:
        feedback_list (List[str]): List of customer feedback strings.

    Returns:
        List[int]: List of extracted numeric ratings.
    """
    ratings = []
    for feedback in feedback_list:
        # Use regex to extract the rating number from each feedback string
        match = re.search(r"Rating:\s*(\d+)", feedback)
        if match:
            ratings.append(int(match.group(1)))
    return ratings

def analyze_feedback(ratings: List[int]) -> Dict[str, float]:
    """
    Analyzes the rating data to calculate statistics.

    Args:
        ratings (List[int]): List of numeric ratings.

    Returns:
        Dict[str, float]: Dictionary containing statistical analysis of the ratings.
    """
    if not ratings:
        raise ValueError("No ratings data available for analysis.")
    
    analysis = {
        "average_rating": round(statistics.mean(ratings), 2),
        "median_rating": statistics.median(ratings),
        "min_rating": min(ratings),
        "max_rating": max(ratings),
        "total_ratings": len(ratings)
    }
    return analysis

def main():
    """
    Main function to analyze customer feedback data and compare it to the website's claim.
    """
    try:
        # Step 1: Extract ratings from feedback data
        ratings = extract_ratings(customer_feedback_data)
        
        # Step 2: Perform statistical analysis on the ratings
        analysis = analyze_feedback(ratings)
        
        # Step 3: Display the results of the analysis
        print("Customer Feedback Analysis:")
        print(f"Average Rating: {analysis['average_rating']}")
        print(f"Median Rating: {analysis['median_rating']}")
        print(f"Minimum Rating: {analysis['min_rating']}")
        print(f"Maximum Rating: {analysis['max_rating']}")
        print(f"Total Ratings Analyzed: {analysis['total_ratings']}")
        
        # Step 4: Compare the calculated average rating with the website's claim
        print("\nComparison with Website's Claim:")
        if abs(analysis["average_rating"] - expected_rating) <= 0.1:
            print(f"The calculated average rating ({analysis['average_rating']}) is close to the website's claim ({expected_rating}).")
        else:
            print(f"The calculated average rating ({analysis['average_rating']}) significantly differs from the website's claim ({expected_rating}).")
        
        print(f"Total Ratings Claimed by Website: {expected_reviews_count}")
        print(f"Total Ratings Analyzed in Dataset: {analysis['total_ratings']}")
        
        if analysis["total_ratings"] < expected_reviews_count:
            print("Warning: The analyzed dataset contains fewer reviews than the claimed number on the website.")
    
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```
