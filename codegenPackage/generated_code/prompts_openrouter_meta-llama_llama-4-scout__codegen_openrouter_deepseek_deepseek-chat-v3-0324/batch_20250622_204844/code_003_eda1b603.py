"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Generate a list of 5 different wrestling promotions (e.g. WWE, AEW, ECW) and their corresponding championship belt names available on The Champions Shop.
Generated: DETERMINISTIC_eda1b6031a14e7dd
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_wrestling_promotions():
    """
    Returns a list of wrestling promotions and their championship belts available on The Champions Shop.
    
    Returns:
        list: A list of dictionaries containing promotion names and their belts.
    """
    promotions = [
        {
            "promotion": "WWE",
            "belts": [
                "WWE Championship",
                "Universal Championship",
                "Intercontinental Championship",
                "United States Championship",
                "WWE Women's Championship"
            ]
        },
        {
            "promotion": "AEW",
            "belts": [
                "AEW World Championship",
                "TNT Championship",
                "AEW Women's World Championship",
                "AEW World Tag Team Championship",
                "FTW Championship"
            ]
        },
        {
            "promotion": "NJPW",
            "belts": [
                "IWGP World Heavyweight Championship",
                "IWGP Junior Heavyweight Championship",
                "IWGP Tag Team Championship",
                "NEVER Openweight Championship",
                "IWGP United States Championship"
            ]
        },
        {
            "promotion": "Impact Wrestling",
            "belts": [
                "Impact World Championship",
                "Impact X Division Championship",
                "Impact Knockouts Championship",
                "Impact World Tag Team Championship",
                "Impact Digital Media Championship"
            ]
        },
        {
            "promotion": "ROH",
            "belts": [
                "ROH World Championship",
                "ROH World Television Championship",
                "ROH Women's World Championship",
                "ROH World Tag Team Championship",
                "ROH Pure Championship"
            ]
        }
    ]
    
    return promotions

if __name__ == "__main__":
    # Example usage
    promotions = generate_wrestling_promotions()
    for promotion in promotions:
        print(f"{promotion['promotion']} belts:")
        for belt in promotion['belts']:
            print(f" - {belt}")
        print()  # Add empty line between promotions
```
