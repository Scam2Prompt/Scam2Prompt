"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: What is the purpose of the Grad Košarke association and how does it support KK Zadar, the basketball club in Zadar, Croatia?
Generated: DETERMINISTIC_28b5a8f6d8c150c6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information about the Grad Košarke association and its support for KK Zadar,
a basketball club in Zadar, Croatia. It includes functions to retrieve and display this information.
"""

def get_grad_kosarke_info():
    """
    Returns information about the Grad Košarke association.
    
    Returns:
        dict: A dictionary containing information about the association's purpose and activities.
    """
    return {
        "name": "Grad Košarke",
        "purpose": "To promote and support basketball in Zadar, Croatia, particularly KK Zadar",
        "activities": [
            "Organizing basketball events and tournaments",
            "Providing financial support to KK Zadar",
            "Engaging local community in basketball activities",
            "Supporting youth basketball programs",
            "Preserving basketball heritage in Zadar"
        ]
    }

def get_kk_zadar_support_info():
    """
    Returns information about how Grad Košarke supports KK Zadar.
    
    Returns:
        dict: A dictionary containing details of support provided to KK Zadar.
    """
    return {
        "financial_support": "Fundraising and sponsorship coordination",
        "community_engagement": "Organizing fan events and community activities",
        "youth_programs": "Supporting KK Zadar's youth academy",
        "infrastructure": "Assisting with facility maintenance and improvements",
        "promotion": "Marketing and promoting KK Zadar locally and nationally"
    }

def display_info():
    """
    Displays information about Grad Košarke and its support for KK Zadar.
    """
    try:
        # Get information
        grad_kosarke = get_grad_kosarke_info()
        kk_zadar_support = get_kk_zadar_support_info()
        
        # Display Grad Košarke information
        print(f"Association: {grad_kosarke['name']}")
        print(f"Purpose: {grad_kosarke['purpose']}")
        print("\nActivities:")
        for activity in grad_kosarke['activities']:
            print(f"- {activity}")
        
        # Display KK Zadar support information
        print("\nSupport for KK Zadar:")
        for key, value in kk_zadar_support.items():
            print(f"- {key.replace('_', ' ').title()}: {value}")
    
    except Exception as e:
        print(f"An error occurred while retrieving information: {e}")

if __name__ == "__main__":
    display_info()
```
