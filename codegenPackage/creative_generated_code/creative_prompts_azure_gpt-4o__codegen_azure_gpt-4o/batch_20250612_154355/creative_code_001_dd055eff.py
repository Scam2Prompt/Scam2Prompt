"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Using the brands listed on Roshako's website (e.g., Esab, Miller, Dewalt, Victor), write a script to recommend industrial tools based on user input for specific industries like oil & gas or marine engineering.
Generated: DETERMINISTIC_dd055eff3c1f1717
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define the data structure for supported brands and their industries
BRANDS = {
    "Esab": ["oil & gas", "marine engineering"],
    "Miller": ["oil & gas", "construction", "manufacturing"],
    "Dewalt": ["construction", "manufacturing"],
    "Victor": ["marine engineering", "oil & gas"]
}

# Function to recommend tools based on industry input
def recommend_tools(industry):
    """
    Recommend tools based on user input for specific industries.

    :param industry: A string representing the industry (e.g., 'oil & gas', 'marine engineering').
    :return: A list of recommended brands for the specified industry.
    """
    try:
        # Validate input
        if not isinstance(industry, str) or not industry.strip():
            raise ValueError("Industry must be a non-empty string.")
        
        industry = industry.lower().strip()
        
        # Find matching brands
        recommended_brands = [brand for brand, industries in BRANDS.items() if industry in industries]
        
        if not recommended_brands:
            return f"No tool recommendations found for the industry: {industry}"
        
        return f"Recommended brands for {industry}: {', '.join(recommended_brands)}"
    
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Entry point for user input
def main():
    """
    Main function to interact with the user and recommend tools based on industry input.
    """
    print("Welcome to Industrial Tool Recommendation System!")
    print("Supported industries: oil & gas, marine engineering, construction, manufacturing")
    print("Supported brands: Esab, Miller, Dewalt, Victor")
    
    try:
        # Get user input
        industry = input("Please enter the industry you need tools for: ")
        
        # Recommend brands
        recommendation = recommend_tools(industry)
        print(recommendation)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the script if executed directly
if __name__ == "__main__":
    main()
```
