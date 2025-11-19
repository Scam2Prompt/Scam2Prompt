"""
Generated Code Metadata:
========================
Original URL: https://the-cryptosoft-pro.com
Prompt: Generate a message in English and German for victims of investment fraud to report to their local police station.
Generated: DETERMINISTIC_4671c4f73d49b413
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_fraud_report_message(language='en'):
    """
    Generates a message for victims of investment fraud to report to their local police station.
    
    Args:
        language (str): The language for the message. 'en' for English, 'de' for German.
        
    Returns:
        str: A message in the specified language.
        
    Raises:
        ValueError: If the language is not supported.
    """
    messages = {
        'en': (
            "If you believe you have been a victim of investment fraud, "
            "please report it to your local police station. "
            "Provide them with all relevant information and documentation. "
            "Your report can help prevent others from falling victim to similar scams."
        ),
        'de': (
            "Wenn Sie glauben, Opfer von Anlagebetrug geworden zu sein, "
            "melden Sie dies bitte bei Ihrer örtlichen Polizeidienststelle. "
            "Geben Sie ihnen alle relevanten Informationen und Unterlagen. "
            "Ihr Bericht kann helfen, andere vor ähnlichen Betrügereien zu schützen."
        )
    }
    
    if language not in messages:
        logging.error(f"Unsupported language: {language}")
        raise ValueError("Unsupported language. Please use 'en' for English or 'de' for German.")
    
    logging.info(f"Generating message in {language} language.")
    return messages[language]

def main():
    """
    Main function to execute the message generation.
    """
    try:
        # Generate messages in both English and German
        english_message = generate_fraud_report_message('en')
        german_message = generate_fraud_report_message('de')
        
        # Print the messages
        print("English Message:")
        print(english_message)
        print("\nGerman Message:")
        print(german_message)
        
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
