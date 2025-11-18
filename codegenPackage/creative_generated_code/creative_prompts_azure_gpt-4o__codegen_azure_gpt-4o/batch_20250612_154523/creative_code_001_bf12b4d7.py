"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Generate a script to automate the conversion of monetary values into text format, referencing the "Convertir de números a letras" tool mentioned on AulaContable.
Generated: DETERMINISTIC_bf12b4d76bff1911
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Function to convert a number into text format (Spanish representation)
def number_to_words(number):
    """
    Converts a numeric value into its textual representation in Spanish.
    Supports integers and decimal values up to two decimal places.

    Args:
        number (float): The number to convert.

    Returns:
        str: The textual representation of the number in Spanish.
    """
    # Dictionary for unit and tens mappings
    units = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    teens = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    tens = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    hundreds = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    # Special cases
    if number == 0:
        return "cero"
    if number == 100:
        return "cien"

    # Helper function to convert numbers less than 1000
    def convert_less_than_thousand(num):
        result = ""
        if num >= 100:
            result += hundreds[num // 100] + " "
            num %= 100
        if num >= 20:
            result += tens[num // 10]
            if num % 10 != 0:
                result += " y " + units[num % 10]
        elif num >= 10:
            result += teens[num - 10]
        else:
            result += units[num]
        return result.strip()

    # Split integer and decimal parts
    integer_part = math.floor(number)
    decimal_part = round((number - integer_part) * 100)

    # Convert integer part
    integer_text = convert_less_than_thousand(integer_part)

    # Convert decimal part if applicable
    if decimal_part > 0:
        decimal_text = convert_less_than_thousand(decimal_part)
        return f"{integer_text} con {decimal_text}/100"
    else:
        return integer_text

# Main function to test the number_to_words functionality
if __name__ == "__main__":
    try:
        # Example values to test the function
        values_to_convert = [0, 5, 19, 23, 105, 150, 999.99, 1234.56]

        print("Conversión de números a texto:")
        for value in values_to_convert:
            print(f"{value} -> {number_to_words(value)}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
