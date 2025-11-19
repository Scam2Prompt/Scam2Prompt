"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Generate a sample warning and disclaimer text for a vape product website, including information about nicotine addiction and California Proposition 65 warnings.
Generated: DETERMINISTIC_9aa7aaeb3d0599d4
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vape_warning_disclaimer.py

def generate_vape_warning_disclaimer():
    """
    Generates a warning and disclaimer text for a vape product website.
    Includes information about nicotine addiction and California Proposition 65 warnings.

    Returns:
        str: The complete warning and disclaimer text.
    """
    try:
        # Warning about nicotine addiction
        nicotine_warning = (
            "WARNING: This product contains nicotine. Nicotine is an addictive chemical. "
            "Use of this product is intended for adults of legal smoking age only."
        )

        # California Proposition 65 warning
        prop_65_warning = (
            "CALIFORNIA PROPOSITION 65 WARNING: This product can expose you to chemicals, "
            "including nicotine, which is known to the State of California to cause birth defects "
            "or other reproductive harm. For more information, visit www.P65Warnings.ca.gov."
        )

        # Disclaimer about usage and health risks
        general_disclaimer = (
            "DISCLAIMER: Vape products are not intended for use by non-smokers, pregnant women, "
            "or individuals with pre-existing health conditions. Consult your physician before using "
            "any vape product. Keep out of reach of children and pets."
        )

        # Combine all warnings and disclaimers into a single text
        full_disclaimer = f"{nicotine_warning}\n\n{prop_65_warning}\n\n{general_disclaimer}"

        return full_disclaimer

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the disclaimer: {str(e)}"


if __name__ == "__main__":
    # Generate and display the warning and disclaimer text
    disclaimer_text = generate_vape_warning_disclaimer()
    print(disclaimer_text)
```
