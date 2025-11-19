"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Provide recommendations for designing sprinkler systems compliant with modern safety codes for one- and two-family homes, as highlighted by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1e382ed805ef07d5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sprinkler System Design Recommendations for One- and Two-Family Homes
Compliant with modern safety codes as per Independence Fire Sprinkler Company.
"""

class SprinklerSystemDesign:
    """
    Provides recommendations for designing sprinkler systems compliant with safety codes.
    """

    def __init__(self):
        """Initialize with default code references."""
        self.code_references = {
            "NFPA_13D": "Standard for the Installation of Sprinkler Systems in One- and Two-Family Dwellings",
            "NFPA_13R": "Standard for the Installation of Sprinkler Systems in Low-Rise Residential Occupancies",
            "IRC_P2904": "International Residential Code Section P2904 - Fire Sprinkler Systems"
        }

    def get_design_recommendations(self, home_type: str) -> dict:
        """
        Get sprinkler system design recommendations based on home type.

        Args:
            home_type (str): Type of home ('one-family' or 'two-family')

        Returns:
            dict: Dictionary containing design recommendations and code references

        Raises:
            ValueError: If home_type is not 'one-family' or 'two-family'
        """
        if home_type not in ['one-family', 'two-family']:
            raise ValueError("Invalid home type. Must be 'one-family' or 'two-family'")

        recommendations = {
            "general_requirements": {
                "coverage": "All habitable areas including basements, attics with storage, and attached garages",
                "water_supply": "Dedicated or combined with domestic supply (minimum 10-minute duration)",
                "freeze_protection": "Required in areas subject to freezing temperatures"
            },
            "specific_recommendations": {
                "one-family": {
                    "system_type": "Residential sprinkler system (NFPA 13D compliant)",
                    "spacing": "Maximum 12 ft between sprinklers in living areas",
                    "water_flow": "Minimum 18 GPM for most residential sprinklers"
                },
                "two-family": {
                    "system_type": "Residential sprinkler system (NFPA 13R compliant for buildings ≤ 4 stories)",
                    "spacing": "Maximum 12 ft between sprinklers in living areas",
                    "water_flow": "Minimum 26 GPM for most residential sprinklers",
                    "separation": "Systems should be independently controllable for each dwelling unit"
                }
            },
            "code_references": self.code_references
        }

        result = {
            "general_recommendations": recommendations["general_requirements"],
            "specific_recommendations": recommendations["specific_recommendations"][home_type],
            "code_references": recommendations["code_references"]
        }

        return result

    def get_installation_checklist(self) -> list:
        """
        Returns a checklist for proper sprinkler system installation.

        Returns:
            list: Installation checklist items
        """
        return [
            "Obtain necessary permits before installation",
            "Use listed residential sprinklers (UL or FM approved)",
            "Ensure proper pipe sizing based on hydraulic calculations",
            "Install control valves in accessible locations",
            "Label all system components clearly",
            "Provide adequate support for piping (maximum spacing per code)",
            "Test system after installation (hydrostatic test at 200 psi for 2 hours)",
            "Conduct final inspection with authority having jurisdiction"
        ]


# Example usage
if __name__ == "__main__":
    try:
        design = SprinklerSystemDesign()
        
        # Get recommendations for a one-family home
        one_family_recs = design.get_design_recommendations("one-family")
        print("One-Family Home Recommendations:")
        print(one_family_recs)
        
        # Get installation checklist
        checklist = design.get_installation_checklist()
        print("\nInstallation Checklist:")
        for item in checklist:
            print(f"- {item}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
