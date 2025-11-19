"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Generate a Python script that utilizes Karnataka Aromas' essential oils for creating a custom fragrance blend, incorporating their unique flavor ingredients.
Generated: DETERMINISTIC_2d8b74480121f4d7
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a collection of essential oils and their unique properties.
# Each essential oil has a name, notes, and recommended blending ratio.
ESSENTIAL_OILS = [
    {"name": "Lavender", "notes": "Floral", "recommended_ratio": 0.3},
    {"name": "Lemon", "notes": "Citrus", "recommended_ratio": 0.2},
    {"name": "Sandalwood", "notes": "Woody", "recommended_ratio": 0.2},
    {"name": "Peppermint", "notes": "Minty", "recommended_ratio": 0.1},
    {"name": "Rose", "notes": "Floral", "recommended_ratio": 0.2},
]

# Function to display available essential oils
def display_essential_oils():
    """
    Display the available essential oils with their properties.
    """
    print("Available Essential Oils:")
    for i, oil in enumerate(ESSENTIAL_OILS, start=1):
        print(
            f"{i}. {oil['name']} - Notes: {oil['notes']}, Recommended Ratio: {oil['recommended_ratio']}"
        )


# Function to create a custom fragrance blend
def create_custom_blend():
    """
    Create a custom fragrance blend by selecting essential oils and specifying their ratios.
    """
    print("\nLet's create a custom fragrance blend!")
    display_essential_oils()
    selected_oils = []

    try:
        while True:
            choice = input(
                "\nEnter the number of the essential oil to add to your blend (or 'done' to finish): "
            )
            if choice.lower() == "done":
                break

            # Validate the user's selection
            if choice.isdigit() and 1 <= int(choice) <= len(ESSENTIAL_OILS):
                oil_index = int(choice) - 1
                oil = ESSENTIAL_OILS[oil_index]

                # Ask for the ratio of the selected oil
                ratio = input(
                    f"Enter the blending ratio for {oil['name']} (recommended: {oil['recommended_ratio']}): "
                )
                try:
                    ratio = float(ratio)
                    if 0 <= ratio <= 1:
                        selected_oils.append({"name": oil["name"], "ratio": ratio})
                    else:
                        print("Error: Ratio must be between 0 and 1. Try again.")
                except ValueError:
                    print("Error: Invalid ratio. Please enter a decimal value.")

            else:
                print("Error: Invalid selection. Please choose a valid number.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Finalize the blend
    if selected_oils:
        total_ratio = sum(oil["ratio"] for oil in selected_oils)
        if total_ratio > 1:
            print(
                "Warning: Total blending ratio exceeds 1. Adjusting ratios to fit within 1."
            )
            # Normalize the ratios to fit within a total sum of 1
            selected_oils = [
                {"name": oil["name"], "ratio": oil["ratio"] / total_ratio}
                for oil in selected_oils
            ]

        print("\nYour Custom Fragrance Blend:")
        for oil in selected_oils:
            print(f"{oil['name']} - Ratio: {oil['ratio']:.2f}")
    else:
        print("No oils selected. Blend creation canceled.")

    return selected_oils


# Main entry point
def main():
    """
    Entry point for the script.
    """
    print("Welcome to Karnataka Aromas' Custom Fragrance Blend Creator!")
    blend = create_custom_blend()

    if blend:
        # Save the blend to a JSON file
        try:
            with open("custom_blend.json", "w") as file:
                json.dump(blend, file, indent=4)
                print("\nYour custom blend has been saved to 'custom_blend.json'.")
        except IOError as e:
            print(f"Error saving your blend to file: {e}")
    else:
        print("No blend created. Exiting program.")


if __name__ == "__main__":
    main()
```
