"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "How to choose the right tire for a retroexcavadora, considering factors like TKPH and usage conditions?"
Generated: DETERMINISTIC_4462248b643062bb
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to help choose the right tire for a retroexcavadora (backhoe loader)
# considering factors like TKPH (Ton-Kilometer Per Hour) and usage conditions.

def calculate_tkph(weight, distance, hours):
    """
    Calculate TKPH (Ton-Kilometer Per Hour) based on weight, distance, and hours of operation.

    Parameters:
        weight (float): The weight of the retroexcavadora in tons.
        distance (float): The distance traveled in kilometers.
        hours (float): The hours of operation.

    Returns:
        float: The calculated TKPH value.
    """
    try:
        if hours <= 0:
            raise ValueError("Hours of operation must be greater than zero.")
        tkph = (weight * distance) / hours
        return tkph
    except Exception as e:
        print(f"Error calculating TKPH: {e}")
        return None


def recommend_tire(tkph, usage_conditions):
    """
    Recommend a tire based on TKPH and usage conditions.

    Parameters:
        tkph (float): The calculated TKPH value.
        usage_conditions (str): The usage conditions (e.g., "rocky", "soft soil", "wet").

    Returns:
        str: Recommended tire type.
    """
    try:
        if tkph is None:
            raise ValueError("TKPH value is invalid.")

        # Example tire recommendations based on TKPH and usage conditions
        if tkph < 50:
            if usage_conditions == "rocky":
                return "Heavy-duty tire for rocky terrain"
            elif usage_conditions == "soft soil":
                return "Wide tire for soft soil"
            elif usage_conditions == "wet":
                return "Tire with deep tread for wet conditions"
            else:
                return "Standard tire for general use"
        elif 50 <= tkph <= 100:
            if usage_conditions == "rocky":
                return "Reinforced tire for moderate rocky terrain"
            elif usage_conditions == "soft soil":
                return "All-terrain tire for soft soil"
            elif usage_conditions == "wet":
                return "All-weather tire for wet conditions"
            else:
                return "All-purpose tire for mixed use"
        else:
            return "High-performance tire for heavy-duty operations"
    except Exception as e:
        print(f"Error recommending tire: {e}")
        return "Unable to recommend a tire."


def main():
    """
    Main function to interact with the user and recommend a tire.
    """
    try:
        print("Welcome to the Retroexcavadora Tire Recommendation System!")

        # Get user input
        weight = float(input("Enter the weight of the retroexcavadora (in tons): "))
        distance = float(input("Enter the distance traveled per day (in kilometers): "))
        hours = float(input("Enter the hours of operation per day: "))
        usage_conditions = input("Enter the usage conditions (e.g., rocky, soft soil, wet): ").strip().lower()

        # Calculate TKPH
        tkph = calculate_tkph(weight, distance, hours)
        if tkph is not None:
            print(f"Calculated TKPH: {tkph}")

        # Recommend tire
        recommendation = recommend_tire(tkph, usage_conditions)
        print(f"Tire Recommendation: {recommendation}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
