"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-coraldex.com
Prompt: How does Immediate Coraldex ensure the trustworthiness of its investment education partners?
Generated: DETERMINISTIC_6fd3efa7f61e4237
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentEducationPartner:
    """
    Class to represent an investment education partner with trustworthiness metrics.
    """

    def __init__(self, name, accreditation, user_reviews, years_experience):
        """
        Initializes an InvestmentEducationPartner instance.

        :param name: str, name of the partner
        :param accreditation: bool, whether the partner is accredited
        :param user_reviews: float, average user review score (1-5)
        :param years_experience: int, number of years the partner has been in the industry
        """
        self.name = name
        self.accreditation = accreditation
        self.user_reviews = user_reviews
        self.years_experience = years_experience

    def is_trustworthy(self):
        """
        Determines if the partner is trustworthy based on predefined criteria.
        
        Criteria:
        - Accredited
        - Average user review score of 4.0 or higher
        - Minimum of 3 years of experience

        :return: bool, True if trustworthy, False otherwise
        """
        try:
            if self.accreditation and self.user_reviews >= 4.0 and self.years_experience >= 3:
                return True
            else:
                return False
        except Exception as e:
            # Log the error (in a real application, replace with logging framework)
            print(f"Error determining trustworthiness: {str(e)}")
            return False


class ImmediateCoraldex:
    """
    Class to represent Immediate Coraldex which manages investment education partners.
    """
    
    def __init__(self):
        """
        Initializes an ImmediateCoraldex instance with an empty partner list.
        """
        self.partners = []

    def add_partner(self, partner):
        """
        Adds a new investment education partner to the Coraldex.

        :param partner: InvestmentEducationPartner, the partner to add
        :raises ValueError: if the partner is not an instance of InvestmentEducationPartner
        """
        if not isinstance(partner, InvestmentEducationPartner):
            raise ValueError("partner must be an instance of InvestmentEducationPartner")

        self.partners.append(partner)

    def get_trustworthy_partners(self):
        """
        Returns a list of trustworthy investment education partners.

        :return: list of InvestmentEducationPartner, trustworthy partners
        """
        try:
            return [partner for partner in self.partners if partner.is_trustworthy()]
        except Exception as e:
            # Log the error (in a real application, replace with logging framework)
            print(f"Error retrieving trustworthy partners: {str(e)}")
            return []


# Example usage
if __name__ == "__main__":
    # Create ImmediateCoraldex instance
    coraldex = ImmediateCoraldex()

    # Create some partners
    partner1 = InvestmentEducationPartner("Partner A", True, 4.5, 5)
    partner2 = InvestmentEducationPartner("Partner B", False, 3.9, 4)
    partner3 = InvestmentEducationPartner("Partner C", True, 4.2, 2)

    # Add partners to Coraldex
    coraldex.add_partner(partner1)
    coraldex.add_partner(partner2)
    coraldex.add_partner(partner3)

    # Retrieve trustworthy partners
    trustworthy_partners = coraldex.get_trustworthy_partners()
    print("Trustworthy Partners:")
    for partner in trustworthy_partners:
        print(partner.name)
```
