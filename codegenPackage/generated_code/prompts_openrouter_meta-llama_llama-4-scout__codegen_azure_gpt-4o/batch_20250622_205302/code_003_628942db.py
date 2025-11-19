"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Write a Python script to automatically generate a maintenance page with a given message in multiple languages.
Generated: DETERMINISTIC_628942db741eba51
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json

def generate_maintenance_page(message_dict, output_dir="maintenance_pages"):
    """
    Generates maintenance pages in multiple languages based on the provided messages.

    Args:
        message_dict (dict): A dictionary where keys are language codes (e.g., 'en', 'es') 
                             and values are the maintenance messages in those languages.
        output_dir (str): Directory where the generated HTML files will be saved.
    """
    # Ensure the output directory exists
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{output_dir}': {e}")
        return

    # HTML template for the maintenance page
    html_template = """
    <!DOCTYPE html>
    <html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Maintenance</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f8f9fa;
                color: #333;
            }}
            h1 {{
                font-size: 2em;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>Maintenance</h1>
        <p>{message}</p>
    </body>
    </html>
    """

    # Generate HTML files for each language
    for lang, message in message_dict.items():
        try:
            # Format the HTML template with the language and message
            html_content = html_template.format(lang=lang, message=message)
            
            # Define the output file path
            file_path = os.path.join(output_dir, f"maintenance_{lang}.html")
            
            # Write the HTML content to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(html_content)
            
            print(f"Generated maintenance page: {file_path}")
        except Exception as e:
            print(f"Error generating page for language '{lang}': {e}")

if __name__ == "__main__":
    # Example messages in multiple languages
    messages = {
        "en": "We are currently undergoing maintenance. Please check back later.",
        "es": "Actualmente estamos en mantenimiento. Por favor, vuelva más tarde.",
        "fr": "Nous sommes actuellement en maintenance. Veuillez revenir plus tard.",
        "de": "Wir führen derzeit Wartungsarbeiten durch. Bitte kommen Sie später wieder.",
        "it": "Siamo attualmente in manutenzione. Per favore, ricontrolla più tardi."
    }

    # Generate maintenance pages
    generate_maintenance_page(messages)
```
