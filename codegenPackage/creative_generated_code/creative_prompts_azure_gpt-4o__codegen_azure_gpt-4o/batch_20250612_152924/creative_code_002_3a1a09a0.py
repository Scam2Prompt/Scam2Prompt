"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Generate a script in Python to calculate eligibility for Spanish nationality based on residency duration, marital status, or ancestry, referencing specific legal requirements.
Generated: DETERMINISTIC_3a1a09a0fce16cfe
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to determine eligibility for Spanish nationality based on residency duration, marital status, or ancestry.

Spanish nationality eligibility is determined by:
1. Residency: At least 10 years of legal residence in Spain (exceptions apply for specific cases).
2. Marital Status: Married to a Spanish citizen and lived with the spouse for at least 1 year.
3. Ancestry: Direct descendants of a Spanish citizen (e.g., parents or grandparents born in Spain).
"""

def check_spanish_nationality_eligibility(residency_years, married_to_spanish_citizen, years_married, has_spanish_ancestry):
    """
    Function to calculate eligibility for Spanish nationality.

    Args:
        residency_years (int): Number of years the person has legally resided in Spain.
        married_to_spanish_citizen (bool): Whether the person is married to a Spanish citizen.
        years_married (int): Number of years married to the Spanish citizen (if applicable).
        has_spanish_ancestry (bool): Whether the person has Spanish ancestry.

    Returns:
        str: Message indicating eligibility status.
    """
    try:
        # Check eligibility based on residency duration
        if residency_years >= 10:
            return "Eligible for Spanish nationality based on residency duration."

        # Check eligibility based on marital status
        if married_to_spanish_citizen and years_married >= 1:
            return "Eligible for Spanish nationality based on marital status."

        # Check eligibility based on ancestry
        if has_spanish_ancestry:
            return "Eligible for Spanish nationality based on ancestry."

        # Not eligible if none of the conditions are met
        return "Not eligible for Spanish nationality based on the provided criteria."

    except Exception as e:
        return f"An error occurred while determining eligibility: {e}"


# Example usage
if __name__ == "__main__":
    # Input values (these would typically come from a user or external system)
    residency_years = 10
    married_to_spanish_citizen = True
    years_married = 2
    has_spanish_ancestry = False

    # Check eligibility
    eligibility_message = check_spanish_nationality_eligibility(
        residency_years,
        married_to_spanish_citizen,
        years_married,
        has_spanish_ancestry
    )

    # Output the result
    print(eligibility_message)
```
