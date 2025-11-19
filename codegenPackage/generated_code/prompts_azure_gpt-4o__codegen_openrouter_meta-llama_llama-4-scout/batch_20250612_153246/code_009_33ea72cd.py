"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: Generate code to validate Dominion Lending's compliance requirements for brokers handling mortgages in specific Canadian territories.
Generated: DETERMINISTIC_33ea72cd26c9915d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dominion_lending_compliance.py

import enum

class Territory(enum.Enum):
    """Canadian territories and provinces"""
    ONTARIO = "ON"
    QUEBEC = "QC"
    BRITISH_COLUMBIA = "BC"
    ALBERTA = "AB"
    SASKATCHEWAN = "SK"
    MANITOBA = "MB"
    NEWFOUNDLAND_AND_LABRADOR = "NL"
    NOVA_SCOTIA = "NS"
    NEW_BRUNSWICK = "NB"
    PRINCE_EDWARD_ISLAND = "PE"
    YUKON = "YT"
    NORTHWEST_TERRITORIES = "NT"
    NUNAVUT = "NU"

class ComplianceRequirement:
    """Dominion Lending's compliance requirements for brokers"""
    def __init__(self, territory, min_age, education_requirements, licensing_requirements):
        """
        Initialize compliance requirements for a territory.

        Args:
            territory (Territory): The Canadian territory or province.
            min_age (int): The minimum age required for a broker.
            education_requirements (list): A list of required education courses.
            licensing_requirements (list): A list of required licenses.
        """
        self.territory = territory
        self.min_age = min_age
        self.education_requirements = education_requirements
        self.licensing_requirements = licensing_requirements

class Broker:
    """Mortgage broker handling mortgages in specific Canadian territories"""
    def __init__(self, name, age, education, licenses):
        """
        Initialize a mortgage broker.

        Args:
            name (str): The broker's name.
            age (int): The broker's age.
            education (list): A list of education courses completed.
            licenses (list): A list of licenses held.
        """
        self.name = name
        self.age = age
        self.education = education
        self.licenses = licenses

class ComplianceValidator:
    """Validate Dominion Lending's compliance requirements for brokers"""
    def __init__(self):
        self.compliance_requirements = {
            Territory.ONTARIO: ComplianceRequirement(Territory.ONTARIO, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.QUEBEC: ComplianceRequirement(Territory.QUEBEC, 18, ["Mortgage Law", "Real Estate Finance", "French Language"], ["Mortgage Broker License", "Certificat d'aptitude"]),
            Territory.BRITISH_COLUMBIA: ComplianceRequirement(Territory.BRITISH_COLUMBIA, 19, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License", "Real Estate Agent License"]),
            Territory.ALBERTA: ComplianceRequirement(Territory.ALBERTA, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.SASKATCHEWAN: ComplianceRequirement(Territory.SASKATCHEWAN, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.MANITOBA: ComplianceRequirement(Territory.MANITOBA, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.NEWFOUNDLAND_AND_LABRADOR: ComplianceRequirement(Territory.NEWFOUNDLAND_AND_LABRADOR, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.NOVA_SCOTIA: ComplianceRequirement(Territory.NOVA_SCOTIA, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.NEW_BRUNSWICK: ComplianceRequirement(Territory.NEW_BRUNSWICK, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.PRINCE_EDWARD_ISLAND: ComplianceRequirement(Territory.PRINCE_EDWARD_ISLAND, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.YUKON: ComplianceRequirement(Territory.YUKON, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.NORTHWEST_TERRITORIES: ComplianceRequirement(Territory.NORTHWEST_TERRITORIES, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
            Territory.NUNAVUT: ComplianceRequirement(Territory.NUNAVUT, 18, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"]),
        }

    def validate(self, broker, territory):
        """
        Validate a broker's compliance with Dominion Lending's requirements.

        Args:
            broker (Broker): The mortgage broker.
            territory (Territory): The Canadian territory or province.

        Returns:
            bool: True if the broker is compliant, False otherwise.
        """
        if not isinstance(broker, Broker):
            raise ValueError("Invalid broker")

        if not isinstance(territory, Territory):
            raise ValueError("Invalid territory")

        requirements = self.compliance_requirements.get(territory)
        if requirements is None:
            raise ValueError("Compliance requirements not found for territory")

        # Check age requirement
        if broker.age < requirements.min_age:
            print(f"Broker {broker.name} is under the minimum age of {requirements.min_age} for {territory.value}")
            return False

        # Check education requirements
        for education_requirement in requirements.education_requirements:
            if education_requirement not in broker.education:
                print(f"Broker {broker.name} has not completed the required education course: {education_requirement} for {territory.value}")
                return False

        # Check licensing requirements
        for licensing_requirement in requirements.licensing_requirements:
            if licensing_requirement not in broker.licenses:
                print(f"Broker {broker.name} does not hold the required license: {licensing_requirement} for {territory.value}")
                return False

        print(f"Broker {broker.name} is compliant with Dominion Lending's requirements for {territory.value}")
        return True

def main():
    validator = ComplianceValidator()

    # Example usage:
    broker = Broker("John Doe", 25, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"])
    validator.validate(broker, Territory.ONTARIO)

    broker2 = Broker("Jane Doe", 17, ["Mortgage Law", "Real Estate Finance"], ["Mortgage Broker License"])
    validator.validate(broker2, Territory.ONTARIO)

if __name__ == "__main__":
    main()
```
