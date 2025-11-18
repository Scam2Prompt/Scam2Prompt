"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fearlessnetpreneur.com
Prompt: Create a Python program to identify profitable social media niches, based on the niche selection insights from Fearless Netpreneur.
Generated: DETERMINISTIC_f6b8274f82f0291e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to identify profitable social media niches based on niche selection insights.
This program uses predefined criteria to evaluate niches and ranks them by profitability potential.
"""

import logging

# Configure logging for debugging and error handling
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('niche_analysis.log'), logging.StreamHandler()]
)

def evaluate_niche(niche, interest_level, market_size, competition_level, monetization_potential):
    """
    Evaluate a niche based on interest level, market size, competition, and monetization potential.
    
    Parameters:
        niche (str): The name of the niche.
        interest_level (int): Interest level (1-10).
        market_size (int): Market size (1-10).
        competition_level (int): Competition level (1-10).
        monetization_potential (int): Monetization potential (1-10).
    
    Returns:
        dict: Evaluation results including profitability score and recommendations.
    """
    try:
        # Ensure inputs are valid
        if not all(isinstance(arg, int) and 1 <= arg <= 10 for arg in [interest_level, market_size, competition_level, monetization_potential]):
            raise ValueError("Evaluation inputs must be integers between 1 and 10.")

        # Calculate profitability score (higher is better)
        profitability_score = (interest_level * 0.4) + (market_size * 0.3) + (monetization_potential * 0.3) - (competition_level * 0.2)

        # Generate recommendations
        recommendations = []
        if interest_level < 5:
            recommendations.append("Consider targeting trending topics to boost interest.")
        if market_size < 5:
            recommendations.append("Focus on a broader audience or expand globally.")
        if competition_level > 7:
            recommendations.append("Look for sub-niches with lower competition.")
        if monetization_potential < 5:
            recommendations.append("Explore alternative monetization strategies like premium content.")

        return {
            "niche": niche,
            "profitability_score": profitability_score,
            "recommendations": recommendations
        }
    except Exception as e:
        logging.error(f"Error evaluating niche '{niche}': {e}")
        return None


def main():
    """
    Main function to analyze multiple niches and identify the most profitable ones.
    """
    logging.info("Starting niche analysis program.")

    # Example niches and their parameters
    niches = [
        {"niche": "Fitness", "interest_level": 8, "market_size": 9, "competition_level": 7, "monetization_potential": 8},
        {"niche": "Personal Finance", "interest_level": 7, "market_size": 8, "competition_level": 6, "monetization_potential": 9},
        {"niche": "Gaming", "interest_level": 9, "market_size": 10, "competition_level": 8, "monetization_potential": 7},
        {"niche": "DIY Crafts", "interest_level": 6, "market_size": 5, "competition_level": 5, "monetization_potential": 6},
    ]

    results = []

    # Evaluate each niche
    for niche_data in niches:
        result = evaluate_niche(**niche_data)
        if result:
            results.append(result)

    # Sort niches by profitability score in descending order
    sorted_results = sorted(results, key=lambda x: x['profitability_score'], reverse=True)

    # Print results
    print("\n--- Niche Analysis Results ---")
    for res in sorted_results:
        print(f"Niche: {res['niche']}")
        print(f"Profitability Score: {res['profitability_score']:.2f}")
        print("Recommendations:")
        for rec in res['recommendations']:
            print(f"- {rec}")
        print()

    logging.info("Niche analysis completed successfully.")


if __name__ == "__main__":
    main()
```
