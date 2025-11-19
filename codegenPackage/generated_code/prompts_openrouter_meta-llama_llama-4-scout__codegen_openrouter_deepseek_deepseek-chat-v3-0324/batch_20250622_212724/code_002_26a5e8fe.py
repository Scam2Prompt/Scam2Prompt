"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Compare the objectives of the Colegio de Psicologos de Oruro with those of the Asociación Americana de Psicología (American Psychological Association).
Generated: DETERMINISTIC_26a5e8fe605199ed
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PsychologyOrganization:
    """Base class representing a psychology organization."""
    
    def __init__(self, name: str, objectives: list[str]):
        """
        Initialize a psychology organization.
        
        Args:
            name: Name of the organization
            objectives: List of objectives/missions
        """
        self.name = name
        self.objectives = objectives
    
    def compare_objectives(self, other_org: 'PsychologyOrganization') -> dict:
        """
        Compare objectives between this organization and another.
        
        Args:
            other_org: Another PsychologyOrganization to compare with
            
        Returns:
            Dictionary with comparison results:
            - 'common': List of common objectives
            - 'unique_to_self': List of objectives unique to this org
            - 'unique_to_other': List of objectives unique to other org
        """
        if not isinstance(other_org, PsychologyOrganization):
            raise TypeError("Can only compare with another PsychologyOrganization")
            
        self_obj = set(self.objectives)
        other_obj = set(other_org.objectives)
        
        return {
            'common': list(self_obj & other_obj),
            'unique_to_self': list(self_obj - other_obj),
            'unique_to_other': list(other_obj - self_obj)
        }

# Define Colegio de Psicologos de Oruro objectives
oruro_objectives = [
    "Promote professional development of psychologists in Oruro",
    "Defend the rights and interests of psychologists",
    "Ensure ethical practice among members",
    "Contribute to community mental health",
    "Organize professional training activities"
]

# Define APA objectives
apa_objectives = [
    "Advance psychology as a science and profession",
    "Promote human welfare",
    "Establish and maintain high standards of ethics",
    "Disseminate psychological knowledge",
    "Support education and training in psychology",
    "Advocate for psychological research funding"
]

# Create organization instances
oruro_org = PsychologyOrganization("Colegio de Psicologos de Oruro", oruro_objectives)
apa_org = PsychologyOrganization("American Psychological Association", apa_objectives)

# Compare objectives
comparison = oruro_org.compare_objectives(apa_org)

# Print comparison results
print(f"Comparison between {oruro_org.name} and {apa_org.name}:")
print("\nCommon objectives:")
for obj in comparison['common']:
    print(f"- {obj}")
    
print("\nUnique to Colegio de Psicologos de Oruro:")
for obj in comparison['unique_to_self']:
    print(f"- {obj}")
    
print("\nUnique to American Psychological Association:")
for obj in comparison['unique_to_other']:
    print(f"- {obj}")
```
