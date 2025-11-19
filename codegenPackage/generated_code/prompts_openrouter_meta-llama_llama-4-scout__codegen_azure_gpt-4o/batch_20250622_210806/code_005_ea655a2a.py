"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Design a function to evaluate the eligibility of an AI start-up for listing on the InQubeta NFT marketplace, based on the platform's evaluation criteria.
Generated: DETERMINISTIC_ea655a2aca1b2348
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict

def evaluate_startup_eligibility(startup_data: Dict) -> Dict:
    """
    Evaluates the eligibility of an AI start-up for listing on the InQubeta NFT marketplace.

    Parameters:
        startup_data (Dict): A dictionary containing the start-up's information. 
                             Expected keys: 'name', 'founders', 'funding', 'technology', 'market_fit', 'compliance'

    Returns:
        Dict: A dictionary containing the evaluation result with keys:
              'eligible' (bool): Whether the start-up is eligible.
              'reason' (str): Reason for eligibility/ineligibility.
    """
    try:
        # Define evaluation criteria
        MIN_FUNDING = 50000  # Minimum funding required in USD
        REQUIRED_TECHNOLOGIES = {'AI', 'ML', 'Blockchain'}  # Required technologies
        MIN_MARKET_FIT_SCORE = 7  # Minimum market fit score (out of 10)
        COMPLIANCE_REQUIRED = True  # Compliance with regulations is mandatory

        # Validate input data
        if not all(key in startup_data for key in ['name', 'founders', 'funding', 'technology', 'market_fit', 'compliance']):
            return {'eligible': False, 'reason': 'Missing required startup data.'}

        # Check funding criteria
        if startup_data['funding'] < MIN_FUNDING:
            return {'eligible': False, 'reason': 'Insufficient funding.'}

        # Check technology criteria
        if not REQUIRED_TECHNOLOGIES.intersection(startup_data['technology']):
            return {'eligible': False, 'reason': 'Required technologies not met.'}

        # Check market fit criteria
        if startup_data['market_fit'] < MIN_MARKET_FIT_SCORE:
            return {'eligible': False, 'reason': 'Market fit score is too low.'}

        # Check compliance criteria
        if startup_data['compliance'] != COMPLIANCE_REQUIRED:
            return {'eligible': False, 'reason': 'Non-compliance with regulations.'}

        # If all criteria are met
        return {'eligible': True, 'reason': 'Startup meets all eligibility criteria.'}

    except Exception as e:
        # Handle unexpected errors
        return {'eligible': False, 'reason': f'Error during evaluation: {str(e)}'}

# Example usage:
# startup_info = {
#     'name': 'AI Innovators',
#     'founders': ['Alice', 'Bob'],
#     'funding': 100000,
#     'technology': {'AI', 'Blockchain'},
#     'market_fit': 8,
#     'compliance': True
# }
# result = evaluate_startup_eligibility(startup_info)
# print(result)
```
