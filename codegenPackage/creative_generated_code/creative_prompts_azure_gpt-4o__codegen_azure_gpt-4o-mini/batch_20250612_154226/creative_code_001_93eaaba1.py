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

class FormValidator:
    """Class to validate form inputs for a client registration."""

    def __init__(self, nom, prenom, email, numero, code_postal):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.numero = numero
        self.code_postal = code_postal

    def validate(self):
        """Validate all inputs and return a dictionary of validation results."""
        results = {
            "nom": self.validate_nom(),
            "prenom": self.validate_prenom(),
            "email": self.validate_email(),
            "numero": self.validate_numero(),
            "code_postal": self.validate_code_postal(),
        }
        return results

    def validate_nom(self):
        """Validate 'Nom' field."""
        if not self.nom:
            return "Nom est requis."
        if not re.match(r"^[A-Za-zÀ-ÿ '-]+$", self.nom):
            return "Nom est invalide."
        return "Nom valide."

    def validate_prenom(self):
        """Validate 'Prénom' field."""
        if not self.prenom:
            return "Prénom est requis."
        if not re.match(r"^[A-Za-zÀ-ÿ '-]+$", self.prenom):
            return "Prénom est invalide."
        return "Prénom valide."

    def validate_email(self):
        """Validate 'Email' field."""
        if not self.email:
            return "Email est requis."
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.email):
            return "Email est invalide."
        return "Email valide."

    def validate_numero(self):
        """Validate 'Numéro' field."""
        if not self.numero:
            return "Numéro est requis."
        if not re.match(r"^\+?[0-9]{8,15}$", self.numero):
            return "Numéro est invalide."
        return "Numéro valide."

    def validate_code_postal(self):
        """Validate 'Code postal' field."""
        if not self.code_postal:
            return "Code postal est requis."
        if not re.match(r"^[0-9]{4}$", self.code_postal):
            return "Code postal est invalide."
        return "Code postal valide."


if __name__ == "__main__":
    # Sample input for testing the validator
    sample_data = {
        "nom": "Dupont",
        "prenom": "Jean",
        "email": "jean.dupont@example.com",
        "numero": "+32123456789",
        "code_postal": "1000"
    }

    # Create a FormValidator instance
    validator = FormValidator(**sample_data)

    # Validate inputs
    validation_results = validator.validate()

    # Print validation results
    for field, result in validation_results.items():
        print(f"{field.capitalize()}: {result}")
```
