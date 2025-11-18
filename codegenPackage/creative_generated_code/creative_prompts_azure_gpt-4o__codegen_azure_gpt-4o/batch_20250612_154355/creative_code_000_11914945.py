"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Write Python code to generate a list of welding electrodes and filler metals offered by Roshako, such as ENiCrMo-3 and ERNiCr-3, and organize them by category.
Generated: DETERMINISTIC_119149453e331dec
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script generates a categorized list of welding electrodes and filler metals
offered by Roshako, such as ENiCrMo-3 and ERNiCr-3. The welding materials are
organized by their respective categories for better clarity and usability.
"""

# Define the categories and relevant welding materials
def get_welding_materials():
    """
    Creates a dictionary containing welding electrodes and filler metals categorized by type.

    Returns:
        dict: A dictionary where keys are categories and values are lists of materials.
    """
    return {
        "Nickel-Based Electrodes": [
            "ENiCrMo-3",  # Nickel-chromium-molybdenum electrode
            "ENiCrFe-2",  # Nickel-chromium-iron electrode
        ],
        "Nickel-Based Filler Metals": [
            "ERNiCr-3",   # Nickel-chromium filler metal
            "ERNiCrMo-3", # Nickel-chromium-molybdenum filler metal
        ],
        "Stainless Steel Electrodes": [
            "E308L",  # Stainless steel electrode for 304/308
            "E316L",  # Stainless steel electrode for 316
        ],
        "Stainless Steel Filler Metals": [
            "ER308L",  # Stainless steel filler metal for 304/308
            "ER316L",  # Stainless steel filler metal for 316
        ],
    }

# Display the categorized list
def display_welding_materials(materials):
    """
    Prints a categorized list of welding electrodes and filler metals.

    Args:
        materials (dict): Dictionary of welding materials organized by category.
    """
    print("Welding Electrodes and Filler Metals Offered by Roshako:")
    print("=" * 50)
    for category, items in materials.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print("-" * 50)

def main():
    """
    Main entry point of the script.
    Generates and displays the list of welding materials.
    """
    try:
        # Generate the categorized list of welding materials
        welding_materials = get_welding_materials()
        
        # Display the materials
        display_welding_materials(welding_materials)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
