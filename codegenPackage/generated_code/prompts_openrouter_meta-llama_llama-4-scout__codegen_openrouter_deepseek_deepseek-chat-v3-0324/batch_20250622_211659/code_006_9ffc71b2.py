"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Create a sample warranty policy for an HVAC company based in Fayetteville, AR, inspired by RJW Mechanical's 10-year warranty offer.
Generated: DETERMINISTIC_9ffc71b23ac43910
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warranty_policy.py

class WarrantyPolicy:
    """
    A class representing the warranty policy for an HVAC company.
    Inspired by RJW Mechanical's 10-year warranty offer.
    """

    def __init__(self):
        self.company_name = "Your HVAC Company Name"
        self.location = "Fayetteville, AR"
        self.base_warranty_years = 10
        self.parts_coverage = "All manufacturer parts"
        self.labor_coverage = "Full labor coverage"
        self.transferable = True
        self.registration_required = True
        self.exclusions = [
            "Damage caused by improper installation",
            "Damage caused by lack of maintenance",
            "Damage from external factors (e.g., power surges, natural disasters)",
            "Normal wear and tear",
            "Unauthorized repairs or modifications"
        ]
        self.terms = [
            "Warranty valid only for original purchaser",
            "Proper maintenance records must be maintained",
            "Service must be performed by authorized technicians",
            "Warranty becomes void if equipment is relocated without proper reinstallation"
        ]

    def generate_policy_document(self):
        """
        Generates a formatted warranty policy document.
        
        Returns:
            str: The complete warranty policy text
        """
        try:
            policy = f"""
            {self.company_name} - HVAC Warranty Policy
            Location: {self.location}
            ------------------------------------------------------------
            
            WARRANTY TERMS:
            
            This equipment is covered by a {self.base_warranty_years}-year warranty that includes:
            - {self.parts_coverage}
            - {self.labor_coverage}
            
            The warranty is {'transferable' if self.transferable else 'non-transferable'} to subsequent owners.
            {'Registration is required within 30 days of installation.' if self.registration_required else ''}
            
            EXCLUSIONS:
            {self._format_list(self.exclusions)}
            
            TERMS AND CONDITIONS:
            {self._format_list(self.terms)}
            
            For warranty claims, please contact:
            {self.company_name}
            Phone: [Your Contact Number]
            Email: [Your Email Address]
            Address: [Your Business Address]
            
            This warranty gives you specific legal rights, and you may have other rights which vary by state.
            """
            return policy
        except Exception as e:
            raise RuntimeError(f"Error generating warranty policy: {str(e)}")

    def _format_list(self, items):
        """Helper method to format list items with bullet points"""
        return "\n".join(f"- {item}" for item in items)

    def display_policy(self):
        """Prints the warranty policy to console"""
        try:
            print(self.generate_policy_document())
        except RuntimeError as e:
            print(f"Error displaying warranty policy: {e}")


# Example usage
if __name__ == "__main__":
    try:
        warranty = WarrantyPolicy()
        warranty.display_policy()
    except Exception as e:
        print(f"Failed to initialize warranty policy: {e}")
```
