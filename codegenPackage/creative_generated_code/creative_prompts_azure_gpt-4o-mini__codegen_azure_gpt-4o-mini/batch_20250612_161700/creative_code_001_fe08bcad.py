"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: What are the steps to apply for Spanish nationality, and what specific requirements must I meet based on residency or marriage?
Generated: DETERMINISTIC_fe08bcad1f7458fc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SpanishNationalityApplication:
    """
    A class to manage the application process for Spanish nationality.
    """

    def __init__(self, residency_years, married_to_spanish, is_eu_national):
        """
        Initializes the application with the necessary parameters.

        :param residency_years: Number of years of legal residency in Spain
        :param married_to_spanish: Boolean indicating if the applicant is married to a Spanish citizen
        :param is_eu_national: Boolean indicating if the applicant is an EU national
        """
        self.residency_years = residency_years
        self.married_to_spanish = married_to_spanish
        self.is_eu_national = is_eu_national

    def apply_for_nationality(self):
        """
        Determines the eligibility and steps to apply for Spanish nationality
        based on residency or marriage status.
        """
        try:
            if self.married_to_spanish:
                return self._apply_through_marriage()
            elif self.is_eu_national:
                return self._apply_as_eu_national()
            else:
                return self._apply_based_on_residency()
        except Exception as e:
            return f"An error occurred during application: {str(e)}"

    def _apply_through_marriage(self):
        """
        Application process for those married to a Spanish citizen.

        :return: Steps and requirements for application
        """
        if self.residency_years < 1:
            return "You must have been a resident in Spain for at least 1 year."
        
        return ("Steps to apply for nationality through marriage:\n"
                "1. Gather required documents (marriage certificate, residency proof).\n"
                "2. Submit application to the Civil Registry.\n"
                "3. Pass language and cultural knowledge tests if required.\n"
                "4. Await approval (6-12 months).")

    def _apply_as_eu_national(self):
        """
        Application process for EU nationals.

        :return: Steps and requirements for application
        """
        if self.residency_years < 2:
            return "You must have been a resident in Spain for at least 2 years."
        
        return ("Steps to apply for nationality as an EU national:\n"
                "1. Gather required documents (residency proof, ID).\n"
                "2. Submit application to the Civil Registry.\n"
                "3. Await approval (6-12 months).")

    def _apply_based_on_residency(self):
        """
        Application process based on general residency.

        :return: Steps and requirements for application
        """
        if self.residency_years < 10:
            return "You must have been a resident in Spain for at least 10 years."
        
        return ("Steps to apply for nationality based on residency:\n"
                "1. Gather required documents (residency proof, ID).\n"
                "2. Submit application to the Civil Registry.\n"
                "3. Pass language and cultural knowledge tests.\n"
                "4. Await approval (1-2 years).")

# Example usage
if __name__ == "__main__":
    applicant = SpanishNationalityApplication(residency_years=3, married_to_spanish=False, is_eu_national=True)
    print(applicant.apply_for_nationality())
```
