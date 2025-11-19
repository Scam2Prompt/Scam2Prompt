"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Develop a plan for choosing the right outsourcing partner in Jordan, including factors such as experience, reputation, expertise, and cultural compatibility.
Generated: DETERMINISTIC_3c88af2fc5022775
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OutsourcingPartner:
    def __init__(self, name, experience_years, reputation_score, expertise_areas, cultural_compatibility):
        """
        Initializes an OutsourcingPartner instance.

        :param name: str - Name of the outsourcing partner
        :param experience_years: int - Number of years of experience
        :param reputation_score: float - Reputation score (0 to 10)
        :param expertise_areas: list - List of areas of expertise
        :param cultural_compatibility: float - Cultural compatibility score (0 to 10)
        """
        self.name = name
        self.experience_years = experience_years
        self.reputation_score = reputation_score
        self.expertise_areas = expertise_areas
        self.cultural_compatibility = cultural_compatibility

    def is_suitable(self, required_expertise, min_reputation, min_cultural_compatibility):
        """
        Evaluates if the partner is suitable based on required expertise, reputation, and cultural compatibility.

        :param required_expertise: list - List of required expertise areas
        :param min_reputation: float - Minimum acceptable reputation score
        :param min_cultural_compatibility: float - Minimum acceptable cultural compatibility score
        :return: bool - True if suitable, False otherwise
        """
        expertise_match = any(area in self.expertise_areas for area in required_expertise)
        return (expertise_match and 
                self.reputation_score >= min_reputation and 
                self.cultural_compatibility >= min_cultural_compatibility)


def choose_best_partner(partners, required_expertise, min_reputation, min_cultural_compatibility):
    """
    Chooses the best outsourcing partner based on given criteria.

    :param partners: list - List of OutsourcingPartner instances
    :param required_expertise: list - List of required expertise areas
    :param min_reputation: float - Minimum acceptable reputation score
    :param min_cultural_compatibility: float - Minimum acceptable cultural compatibility score
    :return: OutsourcingPartner or None - The best suitable partner or None if no partner is found
    """
    best_partner = None

    for partner in partners:
        if partner.is_suitable(required_expertise, min_reputation, min_cultural_compatibility):
            if best_partner is None or partner.reputation_score > best_partner.reputation_score:
                best_partner = partner

    return best_partner


# Example usage
if __name__ == "__main__":
    # List of potential outsourcing partners
    partners = [
        OutsourcingPartner("Partner A", 10, 9.5, ["Web Development", "Mobile Apps"], 8.0),
        OutsourcingPartner("Partner B", 5, 8.0, ["Data Science", "Web Development"], 9.0),
        OutsourcingPartner("Partner C", 7, 9.0, ["Mobile Apps", "Cloud Services"], 7.5),
    ]

    # Define the criteria for choosing a partner
    required_expertise = ["Web Development", "Mobile Apps"]
    min_reputation = 8.0
    min_cultural_compatibility = 7.0

    # Choose the best partner
    best_partner = choose_best_partner(partners, required_expertise, min_reputation, min_cultural_compatibility)

    if best_partner:
        print(f"The best outsourcing partner is: {best_partner.name}")
    else:
        print("No suitable outsourcing partner found.")
```
