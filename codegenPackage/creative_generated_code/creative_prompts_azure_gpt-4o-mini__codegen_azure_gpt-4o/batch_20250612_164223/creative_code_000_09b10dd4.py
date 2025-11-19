"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Generate a Python function that recommends the best mattress firmness for back pain relief based on user input regarding their body type and sleeping posture, referencing the Spinetress medium-firm mattress guidelines.
Generated: DETERMINISTIC_09b10dd424a3d754
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def recommend_mattress_firmness(body_type: str, sleeping_posture: str) -> str:
    """
    Recommend the best mattress firmness for back pain relief based on user input.
    References Spinetress medium-firm mattress guidelines.

    Parameters:
    - body_type (str): User's body type, e.g., 'lightweight', 'average', or 'heavyweight'.
    - sleeping_posture (str): User's sleeping posture, e.g., 'back', 'side', or 'stomach'.

    Returns:
    - str: Recommended mattress firmness.
    """
    # Valid options for body type and sleeping posture
    valid_body_types = {'lightweight', 'average', 'heavyweight'}
    valid_sleeping_postures = {'back', 'side', 'stomach'}

    # Input validation
    if body_type.lower() not in valid_body_types:
        return "Error: Invalid body type. Choose from 'lightweight', 'average', or 'heavyweight'."
    if sleeping_posture.lower() not in valid_sleeping_postures:
        return "Error: Invalid sleeping posture. Choose from 'back', 'side', or 'stomach'."

    # Normalize inputs
    body_type = body_type.lower()
    sleeping_posture = sleeping_posture.lower()

    # Recommendation logic based on Spinetress guidelines
    if sleeping_posture == 'back':
        if body_type == 'lightweight':
            return "Recommendation: Medium-firm mattress for optimal support and comfort."
        elif body_type == 'average':
            return "Recommendation: Medium-firm mattress supports spinal alignment effectively."
        elif body_type == 'heavyweight':
            return "Recommendation: Firm mattress provides better support to prevent sinking."

    elif sleeping_posture == 'side':
        if body_type == 'lightweight':
            return "Recommendation: Medium-soft mattress to cushion pressure points."
        elif body_type == 'average':
            return "Recommendation: Medium mattress balances comfort and support."
        elif body_type == 'heavyweight':
            return "Recommendation: Medium-firm mattress prevents excessive sinking and supports the spine."

    elif sleeping_posture == 'stomach':
        if body_type == 'lightweight':
            return "Recommendation: Medium-firm mattress keeps the spine aligned."
        elif body_type == 'average':
            return "Recommendation: Firm mattress minimizes lower back strain."
        elif body_type == 'heavyweight':
            return "Recommendation: Extra-firm mattress prevents sagging and supports the spine."

    # Fallback for unexpected cases (should never reach here due to input validation)
    return "Error: Unable to provide a recommendation. Please check your input."

# Example Usage:
# print(recommend_mattress_firmness("Average", "Side"))
```
