"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a script to automate the process of selecting residential carpets based on user input for room type and traffic flow, using the guidelines provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_79b9b1fb38f49355
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to automate the process of selecting residential carpets 
based on user input for room type and traffic flow.

Guidelines are based on Perfect Melbourne Carpet recommendations.

Author: Perfect Melbourne Carpet Automation Tool
"""

# Import necessary libraries
import sys

def get_carpet_recommendation(room_type, traffic_flow):
    """
    Function to recommend carpet type based on room type and traffic flow.

    Args:
        room_type (str): Type of the room (e.g., bedroom, living room, hallway, etc.).
        traffic_flow (str): Traffic flow level (e.g., low, medium, high).
    
    Returns:
        str: Recommended carpet type.
    """
    # Guidelines for carpet selection
    recommendations = {
        "bedroom": {
            "low": "Plush Carpet - Soft and luxurious for comfort.",
            "medium": "Textured Carpet - Durable yet cozy for moderate use.",
            "high": "Loop Pile Carpet - Tough and resilient for high usage."
        },
        "living room": {
            "low": "Textured Carpet - Comfortable with aesthetic appeal.",
            "medium": "Patterned Carpet - Durable and stylish for active spaces.",
            "high": "Berber Carpet - Highly durable for heavy traffic."
        },
        "hallway": {
            "low": "Loop Pile Carpet - Suitable for light use areas.",
            "medium": "Berber Carpet - Resilient for frequent foot traffic.",
            "high": "Commercial Grade Carpet - Designed for maximum durability."
        }
    }

    # Validate user input and provide a recommendation
    room_type = room_type.lower()
    traffic_flow = traffic_flow.lower()

    if room_type in recommendations:
        if traffic_flow in recommendations[room_type]:
            return recommendations[room_type][traffic_flow]
        else:
            return "Error: Invalid traffic flow level. Please choose from 'low', 'medium', or 'high'."
    else:
        return "Error: Invalid room type. Please choose from 'bedroom', 'living room', or 'hallway'."

def main():
    """
    Main function to handle user input and provide carpet recommendations.
    """
    print("Welcome to Perfect Melbourne Carpet Recommendation Tool!")
    print("Please provide the details below to get a carpet recommendation.")

    try:
        # Get user inputs
        room_type = input("Enter the room type (e.g., bedroom, living room, hallway): ").strip()
        traffic_flow = input("Enter the traffic flow level (low, medium, high): ").strip()

        # Get carpet recommendation
        recommendation = get_carpet_recommendation(room_type, traffic_flow)
        
        # Display the recommendation
        print("\nCarpet Recommendation:")
        print(recommendation)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
