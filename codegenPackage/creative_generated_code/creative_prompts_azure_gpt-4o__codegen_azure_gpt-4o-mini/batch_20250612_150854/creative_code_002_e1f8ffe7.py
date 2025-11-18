"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-prime.com
Prompt: Generate a script to display multilingual investment education options, ensuring support for languages mentioned on Immediate Prime (e.g., EN, BR, DA, DE, ES, FR, HU, IT, NL, NO, PL, SV).
Generated: DETERMINISTIC_e1f8ffe71cfcba80
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentEducation:
    """
    A class to manage and display multilingual investment education options.
    """

    def __init__(self):
        # Supported languages and their respective education options
        self.education_options = {
            'EN': "Investment Basics, Market Analysis, Risk Management",
            'BR': "Noções Básicas de Investimento, Análise de Mercado, Gestão de Risco",
            'DA': "Investeringsgrundlag, Markedsanalyse, Risikostyring",
            'DE': "Investitionsgrundlagen, Marktanalyse, Risikomanagement",
            'ES': "Conceptos Básicos de Inversión, Análisis de Mercado, Gestión de Riesgos",
            'FR': "Notions de base en investissement, Analyse de marché, Gestion des risques",
            'HU': "Befektetési Alapok, Piacelemzés, Kockázatkezelés",
            'IT': "Nozioni di Investimento, Analisi di Mercato, Gestione del Rischio",
            'NL': "Basisprincipes van Investeren, Marktanalyse, Risicobeheer",
            'NO': "Investeringsgrunnlag, Markedsanalyse, Risikostyring",
            'PL': "Podstawy Inwestowania, Analiza Rynku, Zarządzanie Ryzykiem",
            'SV': "Investeringsgrunder, Marknadsanalys, Riskhantering"
        }

    def display_options(self, language_code):
        """
        Displays the investment education options for the given language code.

        Args:
            language_code (str): The language code to display options for.

        Raises:
            ValueError: If the language code is not supported.
        """
        try:
            options = self.education_options[language_code]
            print(f"Investment Education Options in {language_code}: {options}")
        except KeyError:
            raise ValueError(f"Language code '{language_code}' is not supported. "
                             "Please use one of the following: " +
                             ', '.join(self.education_options.keys()))

def main():
    """
    Main function to execute the InvestmentEducation class functionality.
    """
    investment_education = InvestmentEducation()

    # List of supported languages
    supported_languages = investment_education.education_options.keys()
    
    # User input for language selection
    print("Please select a language code from the following options:")
    print(", ".join(supported_languages))

    selected_language = input("Enter language code: ").strip().upper()

    # Display the investment education options based on user selection
    try:
        investment_education.display_options(selected_language)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
