"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: What strategies can be used for recruitment in the IT and E-commerce sectors according to Strive's recruitment solutions?
Generated: DETERMINISTIC_7f7edc562336f83d
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates strategies for recruitment in the IT and E-commerce sectors,
as outlined by Strive's recruitment solutions. It provides a function that returns
a list of recruitment strategies based on the sector specified.
"""

def get_recruitment_strategies(sector):
    """
    Returns a list of recruitment strategies for the given sector.

    Args:
        sector (str): The sector for which recruitment strategies are needed.
                      Valid values are 'IT' and 'E-commerce'.

    Returns:
        list: A list of recruitment strategies specific to the sector.

    Raises:
        ValueError: If the sector is not valid (not 'IT' or 'E-commerce').
    """
    # Define recruitment strategies for IT sector
    it_strategies = [
        "Host hackathons to identify top tech talent.",
        "Partner with coding bootcamps and universities.",
        "Leverage professional platforms like LinkedIn and GitHub.",
        "Offer competitive salaries and benefits to attract top candidates.",
        "Focus on employer branding to showcase company culture."
    ]

    # Define recruitment strategies for E-commerce sector
    ecommerce_strategies = [
        "Use data-driven recruitment to target specific skill sets.",
        "Collaborate with industry-specific job boards.",
        "Offer flexible work arrangements to attract diverse talent.",
        "Use social media campaigns to reach a broader audience.",
        "Highlight opportunities for career growth in the organization."
    ]

    # Determine strategies based on sector
    if sector.lower() == "it":
        return it_strategies
    elif sector.lower() == "e-commerce":
        return ecommerce_strategies
    else:
        # Raise an error if the sector is invalid
        raise ValueError(f"Invalid sector: {sector}. Valid sectors are 'IT' and 'E-commerce'.")

# Example usage
if __name__ == "__main__":
    try:
        # Get recruitment strategies for IT sector
        print("Recruitment Strategies for IT Sector:")
        it_strategies = get_recruitment_strategies("IT")
        for strategy in it_strategies:
            print(f"- {strategy}")

        print("\nRecruitment Strategies for E-commerce Sector:")
        ecommerce_strategies = get_recruitment_strategies("E-commerce")
        for strategy in ecommerce_strategies:
            print(f"- {strategy}")

    except ValueError as e:
        # Handle invalid sector error
        print(f"Error: {e}")
```
