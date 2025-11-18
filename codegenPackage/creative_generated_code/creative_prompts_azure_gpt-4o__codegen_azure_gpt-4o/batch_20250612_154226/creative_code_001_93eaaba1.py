"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Generate a script that validates form inputs for fields such as "Nom," "Prénom," "Email," "Numéro," and "Code postal," ensuring proper formatting and completeness as outlined on the Proximus client page.
Generated: DETERMINISTIC_93eaaba154b3cb16
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_form_inputs(form_data):
    """
    Validates form inputs for 'Nom', 'Prénom', 'Email', 'Numéro', and 'Code postal'.
    
    :param form_data: Dictionary containing form inputs with keys:
                      'Nom', 'Prénom', 'Email', 'Numéro', 'Code postal'.
    :return: A tuple (bool, dict). The first element is True if all validations pass,
             False otherwise. The second element contains error messages for invalid fields.
    """
    errors = {}

    # Validate 'Nom' (Last Name) - Required, alphabetic, and at least 2 characters
    if not form_data.get('Nom') or not re.match(r'^[A-Za-zÀ-ÿ\-]{2,}$', form_data['Nom']):
        errors['Nom'] = "Le nom est invalide. Il doit contenir au moins 2 caractères alphabétiques."

    # Validate 'Prénom' (First Name) - Required, alphabetic, and at least 2 characters
    if not form_data.get('Prénom') or not re.match(r'^[A-Za-zÀ-ÿ\-]{2,}$', form_data['Prénom']):
        errors['Prénom'] = "Le prénom est invalide. Il doit contenir au moins 2 caractères alphabétiques."

    # Validate 'Email' - Required, valid email format
    if not form_data.get('Email') or not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', form_data['Email']):
        errors['Email'] = "L'email est invalide. Veuillez fournir une adresse email correcte."

    # Validate 'Numéro' (Phone Number) - Required, valid phone number format (e.g., +32 123456789 or 0123456789)
    if not form_data.get('Numéro') or not re.match(r'^(\+?\d{1,3})?\s?\d{8,10}$', form_data['Numéro']):
        errors['Numéro'] = "Le numéro de téléphone est invalide. Veuillez fournir un numéro valide."

    # Validate 'Code postal' (Postal Code) - Required, numeric, and exactly 4 digits
    if not form_data.get('Code postal') or not re.match(r'^\d{4}$', form_data['Code postal']):
        errors['Code postal'] = "Le code postal est invalide. Il doit contenir exactement 4 chiffres."

    # Return validation result
    return (len(errors) == 0, errors)


# Example usage
if __name__ == "__main__":
    # Sample form data
    form_data_sample = {
        "Nom": "Dupont",
        "Prénom": "Jean",
        "Email": "jean.dupont@example.com",
        "Numéro": "+32 123456789",
        "Code postal": "1000"
    }

    is_valid, validation_errors = validate_form_inputs(form_data_sample)

    if is_valid:
        print("Les données du formulaire sont valides.")
    else:
        print("Les données du formulaire sont invalides. Erreurs:")
        for field, error in validation_errors.items():
            print(f"- {field}: {error}")
```
