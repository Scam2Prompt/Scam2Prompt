"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Write a script to compare the tensile strength of "FAJAS PLANAS HABASIT" and "FAJAS DE TRANSMISION LINATEX-ETIQUETADORA" for textile industry use cases.
Generated: DETERMINISTIC_38e4e4effa8af241
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

# Define a function to calculate average tensile strength
def calculate_average_tensile_strength(data):
    """
    Calculate the average tensile strength from a list of values.

    Parameters:
    data (list): A list containing tensile strength values.

    Returns:
    float: The average tensile strength rounded to two decimal places.
    """
    if not data:
        raise ValueError("Data list is empty. Provide valid tensile strength values.")
    return round(sum(data) / len(data), 2)

# Define a function to compare tensile strengths of two materials
def compare_tensile_strength(material_1_data, material_2_data):
    """
    Compare the tensile strengths of two materials.

    Parameters:
    material_1_data (list): Tensile strength values of material 1.
    material_2_data (list): Tensile strength values of material 2.

    Returns:
    str: A message describing which material has higher tensile strength.
    """
    avg_material_1 = calculate_average_tensile_strength(material_1_data)
    avg_material_2 = calculate_average_tensile_strength(material_2_data)

    if avg_material_1 > avg_material_2:
        return (f"Material 1 ('FAJAS PLANAS HABASIT') has higher average tensile strength "
                f"({avg_material_1} N/mm) compared to Material 2 "
                f"('FAJAS DE TRANSMISION LINATEX-ETIQUETADORA') ({avg_material_2} N/mm).")
    elif avg_material_1 < avg_material_2:
        return (f"Material 2 ('FAJAS DE TRANSMISION LINATEX-ETIQUETADORA') has higher average tensile strength "
                f"({avg_material_2} N/mm) compared to Material 1 "
                f"('FAJAS PLANAS HABASIT') ({avg_material_1} N/mm).")
    else:
        return (f"Both materials have equal average tensile strength "
                f"({avg_material_1} N/mm).")

# Main function for execution
def main():
    """
    Main function to execute the comparison.
    """
    try:
        # Sample tensile strength data for the two materials
        # Replace these lists with actual tensile strength data for production use
        material_1_data = [450, 470, 460, 480, 490]  # FAJAS PLANAS HABASIT
        material_2_data = [440, 460, 450, 470, 480]  # FAJAS DE TRANSMISION LINATEX-ETIQUETADORA

        # Perform comparison
        result = compare_tensile_strength(material_1_data, material_2_data)
        print(result)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
