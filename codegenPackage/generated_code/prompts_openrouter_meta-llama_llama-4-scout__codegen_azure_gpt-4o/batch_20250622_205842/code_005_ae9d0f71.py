"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: What are the differences between Data-Limited, Data-Moderate, and Data-Rich operating models in openMSE, and how do I choose the right approach for my use case?
Generated: DETERMINISTIC_ae9d0f71727e2089
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a concise explanation of the differences between Data-Limited, Data-Moderate, 
and Data-Rich operating models in openMSE, and includes a function to help users choose the 
appropriate approach for their use case.

openMSE is a framework for fisheries management strategy evaluation, and the choice of operating 
model depends on the availability and quality of data.
"""

def describe_operating_models():
    """
    Returns a dictionary describing the differences between Data-Limited, Data-Moderate, 
    and Data-Rich operating models in openMSE.
    """
    return {
        "Data-Limited": {
            "Description": "Used when data availability is minimal. Relies on simple indicators, such as catch trends or size composition.",
            "Use_Case": "Suitable for fisheries with limited monitoring or historical data."
        },
        "Data-Moderate": {
            "Description": "Used when moderate data is available. Incorporates more complex models, such as stock assessment methods.",
            "Use_Case": "Suitable for fisheries with some monitoring and historical data, but not comprehensive."
        },
        "Data-Rich": {
            "Description": "Used when comprehensive data is available. Utilizes advanced models and detailed stock assessments.",
            "Use_Case": "Suitable for well-monitored fisheries with extensive historical and biological data."
        }
    }

def choose_operating_model(data_availability):
    """
    Determines the appropriate operating model based on the user's data availability.

    Parameters:
        data_availability (str): The level of data availability. Must be one of:
                                 'limited', 'moderate', or 'rich'.

    Returns:
        str: The recommended operating model.
    """
    # Validate input
    if data_availability not in ['limited', 'moderate', 'rich']:
        raise ValueError("Invalid data availability. Must be 'limited', 'moderate', or 'rich'.")

    # Map data availability to operating models
    model_mapping = {
        'limited': 'Data-Limited',
        'moderate': 'Data-Moderate',
        'rich': 'Data-Rich'
    }

    return model_mapping[data_availability]

def main():
    """
    Main function to demonstrate the usage of the script.
    """
    try:
        # Describe operating models
        models = describe_operating_models()
        print("Operating Models in openMSE:")
        for model, details in models.items():
            print(f"\n{model}:")
            print(f"  Description: {details['Description']}")
            print(f"  Use Case: {details['Use_Case']}")

        # Example: Choosing an operating model
        user_data_availability = input("\nEnter your data availability ('limited', 'moderate', 'rich'): ").strip().lower()
        recommended_model = choose_operating_model(user_data_availability)
        print(f"\nRecommended Operating Model: {recommended_model}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
