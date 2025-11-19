"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Generate a script to automate the conversion of monetary values into text format, referencing the "Convertir de números a letras" tool mentioned on AulaContable.
Generated: DETERMINISTIC_bf12b4d76bff1911
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to convert monetary values into text format (Spanish).
Inspired by "Convertir de números a letras" tool from AulaContable.
"""

import re

class NumberToWordsConverter:
    """
    Converts a numerical value into its textual representation in Spanish.
    Handles both integer and decimal parts (for currency).
    """
    
    def __init__(self):
        self.unidades = ['', 'un', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
        self.decenas = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis',
                       'diecisiete', 'dieciocho', 'diecinueve']
        self.decenas_completas = ['', '', 'veinte', 'treinta', 'cuarenta', 'cincuenta',
                                'sesenta', 'setenta', 'ochenta', 'noventa']
        self.centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos',
                        'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
        self.miles = ['', 'mil', 'millón', 'mil millones', 'billón']
        
    def convert_number_to_words(self, number):
        """
        Convert a number to its Spanish textual representation.
        
        Args:
            number (float or int): The number to convert
            
        Returns:
            str: The textual representation of the number
        """
        try:
            if not isinstance(number, (int, float)):
                raise ValueError("Input must be a number")
                
            if number == 0:
                return "cero"
                
            if number < 0:
                return "menos " + self.convert_number_to_words(abs(number))
                
            # Split into integer and decimal parts
            int_part = int(number)
            decimal_part = round((number - int_part) * 100)
            
            result = self.convert_integer_part(int_part)
            
            if decimal_part > 0:
                result += " con " + self.convert_integer_part(decimal_part)
                
            return result
        except Exception as e:
            raise ValueError(f"Error converting number: {str(e)}")
    
    def convert_integer_part(self, number):
        """
        Convert the integer part of a number to words.
        
        Args:
            number (int): The integer to convert
            
        Returns:
            str: The textual representation
        """
        if number == 0:
            return ""
            
        if number < 10:
            return self.unidades[number]
        elif 10 <= number < 20:
            return self.decenas[number - 10]
        elif 20 <= number < 100:
            decena = number // 10
            unidad = number % 10
            if unidad == 0:
                return self.decenas_completas[decena]
            else:
                if decena == 2:
                    return f"veinti{self.unidades[unidad]}"
                else:
                    return f"{self.decenas_completas[decena]} y {self.unidades[unidad]}"
        elif 100 <= number < 1000:
            centena = number // 100
            resto = number % 100
            if centena == 1 and resto == 0:
                return "cien"
            else:
                return f"{self.centenas[centena]} {self.convert_integer_part(resto)}".strip()
        else:
            # Handle larger numbers (thousands, millions, etc.)
            for i, valor in enumerate([1000, 1000000, 1000000000, 1000000000000]):
                if number < valor * 1000:
                    parte_superior = number // valor
                    resto = number % valor
                    
                    if valor == 1000:
                        palabra = "mil"
                    else:
                        palabra = self.miles[i+1]
                        
                    if parte_superior == 1 and valor != 1000:
                        parte_texto = "un " + palabra
                    else:
                        parte_texto = self.convert_integer_part(parte_superior) + " " + palabra
                        
                    resto_texto = self.convert_integer_part(resto)
                    
                    if resto_texto:
                        return f"{parte_texto} {resto_texto}"
                    else:
                        return parte_texto
            return "número muy grande"

def format_currency(number, currency="pesos", cents="centavos"):
    """
    Format a monetary value with currency units.
    
    Args:
        number (float): The monetary value
        currency (str): Name of the currency unit
        cents (str): Name of the cents unit
        
    Returns:
        str: Formatted monetary value in words
    """
    try:
        converter = NumberToWordsConverter()
        words = converter.convert_number_to_words(number)
        
        # Split into main and decimal parts
        parts = words.split(" con ")
        
        result = parts[0] + " " + currency
        if len(parts) > 1:
            result += " con " + parts[1] + " " + cents
            
        # Clean up multiple spaces
        result = re.sub(r'\s+', ' ', result).strip()
        
        # Capitalize first letter
        return result[0].upper() + result[1:]
    except Exception as e:
        raise ValueError(f"Error formatting currency: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        test_values = [0, 1, 10, 15, 23, 100, 123, 1000, 1234, 1000000, 1234567.89]
        
        for value in test_values:
            print(f"{value:15,.2f} => {format_currency(value)}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
