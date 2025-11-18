"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write Python code to recommend a computer configuration based on user requirements (e.g., gaming or office use) using specifications similar to those listed for Londritech computers, such as processor type, memory size, and graphics card.
Generated: DETERMINISTIC_8807f66a2df60c2e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for data handling
import sys

# Define the computer configurations available
COMPUTER_CONFIGURATIONS = {
    "gaming": {
        "Processor": "Intel Core i7",
        "Memory": "16GB DDR4",
        "Graphics Card": "NVIDIA GeForce RTX 3060",
        "Storage": "1TB SSD",
        "Price": "$1500"
    },
    "office": {
        "Processor": "Intel Core i5",
        "Memory": "8GB DDR4",
        "Graphics Card": "Integrated Graphics",
        "Storage": "512GB SSD",
        "Price": "$800"
    },
    "video_editing": {
        "Processor": "AMD Ryzen 9",
        "Memory": "32GB DDR4",
        "Graphics Card": "NVIDIA GeForce RTX 3080",
        "Storage": "2TB SSD",
        "Price": "$2000"
    },
    "casual_use": {
        "Processor": "Intel Core i3",
        "Memory": "4GB DDR4",
        "Graphics Card": "Integrated Graphics",
        "Storage": "256GB SSD",
        "Price": "$500"
    }
}

def recommend_computer(use_case):
    """
    Recommend a computer configuration based on the user's use case.

    Parameters:
        use_case (str): The intended use of the computer (e.g., gaming, office, etc.).

    Returns:
        dict: The recommended computer configuration.
    """
    try:
        # Look up the configuration based on the use case
        recommendation = COMPUTER_CONFIGURATIONS.get(use_case.lower())
        
        if recommendation:
            return recommendation
        else:
            raise ValueError(f"Invalid use case '{use_case}'. Supported use cases: {', '.join(COMPUTER_CONFIGURATIONS.keys())}")
    except Exception as e:
        # Handle any unexpected errors
        return {"Error": str(e)}

if __name__ == "__main__":
    # Main script execution

    # Get user input for intended use case
    print("Welcome to the computer configuration recommender!")
    user_input = input("Enter your intended use for the computer (e.g., gaming, office, video_editing, casual_use): ").strip()

    # Recommend a configuration based on the user input
    recommendation = recommend_computer(user_input)

    # Display the recommendation to the user
    if "Error" in recommendation:
        print(f"Error: {recommendation['Error']}")
        sys.exit(1)
    else:
        print("\nRecommended Configuration:")
        for key, value in recommendation.items():
            print(f"{key}: {value}")
```
