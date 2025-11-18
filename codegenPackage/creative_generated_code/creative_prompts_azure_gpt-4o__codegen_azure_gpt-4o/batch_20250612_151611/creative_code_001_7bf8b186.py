"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Create a script to recommend suitable metal pipes and fittings (e.g., Duplex Steel Pipes, Alloy Steel Pipes) based on user input for specific industrial requirements, referencing the product categories on the Dinkar Alloys website.
Generated: DETERMINISTIC_7bf8b1860082a501
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def recommend_pipes_and_fittings(industry_type, pressure_rating, temperature_range, corrosion_resistance):
    """
    Recommend suitable metal pipes and fittings based on user input.

    Parameters:
    - industry_type (str): The type of industry (e.g., "Oil and Gas", "Chemical", "Construction").
    - pressure_rating (str): Required pressure handling capacity (e.g., "High", "Medium", "Low").
    - temperature_range (tuple): Operating temperature range in Celsius (e.g., (-20, 200)).
    - corrosion_resistance (bool): Whether corrosion resistance is necessary.

    Returns:
    - list: Recommended pipes and fittings with details.
    """
    # Database of pipes and fittings
    products = [
        {
            "name": "Duplex Steel Pipes",
            "industry": ["Oil and Gas", "Chemical"],
            "pressure_rating": "High",
            "temperature_range": (-50, 300),
            "corrosion_resistance": True,
        },
        {
            "name": "Alloy Steel Pipes",
            "industry": ["Construction", "Chemical"],
            "pressure_rating": "Medium",
            "temperature_range": (-20, 250),
            "corrosion_resistance": False,
        },
        {
            "name": "Carbon Steel Pipes",
            "industry": ["Construction", "Water Supply"],
            "pressure_rating": "Low",
            "temperature_range": (0, 150),
            "corrosion_resistance": False,
        },
        {
            "name": "Stainless Steel Fittings",
            "industry": ["Oil and Gas", "Chemical", "Food Processing"],
            "pressure_rating": "High",
            "temperature_range": (-20, 400),
            "corrosion_resistance": True,
        },
    ]
    
    recommendations = []

    for product in products:
        # Check if the product matches criteria
        if (industry_type in product["industry"] and
                product["pressure_rating"] == pressure_rating and
                product["temperature_range"][0] <= temperature_range[0] and
                product["temperature_range"][1] >= temperature_range[1] and
                product["corrosion_resistance"] == corrosion_resistance):
            recommendations.append(product["name"])

    return recommendations


def main():
    try:
        # Collect user input
        print("Welcome to the Metal Pipes and Fittings Recommender.")
        industry_type = input("Enter your industry type (e.g., Oil and Gas, Chemical, Construction): ").strip()
        pressure_rating = input("Enter pressure rating (High, Medium, Low): ").strip()
        temperature_min = float(input("Enter minimum operating temperature (in Celsius): ").strip())
        temperature_max = float(input("Enter maximum operating temperature (in Celsius): ").strip())
        corrosion_resistance_input = input("Is corrosion resistance required? (yes/no): ").strip().lower()
        corrosion_resistance = True if corrosion_resistance_input == "yes" else False

        # Validate temperature range
        if temperature_min > temperature_max:
            raise ValueError("Minimum temperature cannot be greater than maximum temperature.")

        # Get recommendations
        temperature_range = (temperature_min, temperature_max)
        recommendations = recommend_pipes_and_fittings(industry_type, pressure_rating, temperature_range, corrosion_resistance)

        # Display recommendations
        if recommendations:
            print("\nRecommended Pipes and Fittings:")
            for recommendation in recommendations:
                print(f"- {recommendation}")
        else:
            print("\nNo suitable products found based on your input.")
    except ValueError as ve:
        # Handle invalid numeric input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Metal Pipes and Fittings Recommender.")


if __name__ == "__main__":
    main()
```
