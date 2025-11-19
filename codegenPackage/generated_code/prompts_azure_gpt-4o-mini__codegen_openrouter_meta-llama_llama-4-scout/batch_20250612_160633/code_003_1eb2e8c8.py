"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Develop a function that crafts compelling online ad copy, inspired by the techniques outlined on Star Shot 90.
Generated: DETERMINISTIC_1eb2e8c8dcd8acac
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def craft_ad_copy(product_name: str, key_benefit: str, target_audience: str, call_to_action: str) -> str:
    """
    Crafts compelling online ad copy inspired by Star Shot 90 techniques.

    Args:
    - product_name (str): The name of the product.
    - key_benefit (str): The key benefit of the product.
    - target_audience (str): The target audience for the ad.
    - call_to_action (str): The call to action for the ad.

    Returns:
    - str: The crafted ad copy.
    """

    # Define a list of attention-grabbing opening sentences
    openings = [
        f"Are you tired of {get_negative_target_audience_phrase(target_audience)}?",
        f"Want to {get_desired_outcome(target_audience)}?",
        f"Get ready to {get_exciting_verb(target_audience)} with {product_name}!"
    ]

    # Define a list of benefit-focused sentences
    benefits = [
        f"With {product_name}, you can enjoy {key_benefit} and transform your life.",
        f"{product_name} is designed to help you achieve {key_benefit} and more.",
        f"Experience the power of {key_benefit} with {product_name}."
    ]

    # Define a list of social proof and credibility sentences
    social_proofs = [
        f"Join the thousands of satisfied {target_audience} who have already discovered {product_name}.",
        f"Don't just take our word for it - {product_name} has been proven to deliver {key_benefit}.",
        f"As a trusted leader in {get_industry(target_audience)}, we know what it takes to deliver {key_benefit}."
    ]

    # Define a list of calls to action
    ctas = [
        f"Sign up now and start {call_to_action}!",
        f"Get instant access to {product_name} and start {call_to_action} today!",
        f"Learn more about {product_name} and how you can {call_to_action}."
    ]

    # Craft the ad copy
    ad_copy = f"{random.choice(openings)}\n"
    ad_copy += f"{random.choice(benefits)}\n"
    ad_copy += f"{random.choice(social_proofs)}\n"
    ad_copy += f"{random.choice(ctas)}"

    return ad_copy


def get_negative_target_audience_phrase(target_audience: str) -> str:
    """
    Returns a negative phrase related to the target audience.

    Args:
    - target_audience (str): The target audience.

    Returns:
    - str: A negative phrase.
    """
    negative_phrases = {
        "entrepreneurs": "struggling to grow your business",
        "marketers": "wasting time on ineffective campaigns",
        "small business owners": "feeling overwhelmed with work"
    }
    return negative_phrases.get(target_audience, "struggling with your goals")


def get_desired_outcome(target_audience: str) -> str:
    """
    Returns a desired outcome related to the target audience.

    Args:
    - target_audience (str): The target audience.

    Returns:
    - str: A desired outcome.
    """
    desired_outcomes = {
        "entrepreneurs": "scale your business quickly",
        "marketers": "drive more conversions",
        "small business owners": "increase productivity"
    }
    return desired_outcomes.get(target_audience, "achieve success")


def get_exciting_verb(target_audience: str) -> str:
    """
    Returns an exciting verb related to the target audience.

    Args:
    - target_audience (str): The target audience.

    Returns:
    - str: An exciting verb.
    """
    exciting_verbs = {
        "entrepreneurs": "launch",
        "marketers": "boost",
        "small business owners": "grow"
    }
    return exciting_verbs.get(target_audience, "succeed")


def get_industry(target_audience: str) -> str:
    """
    Returns an industry related to the target audience.

    Args:
    - target_audience (str): The target audience.

    Returns:
    - str: An industry.
    """
    industries = {
        "entrepreneurs": "e-commerce",
        "marketers": "digital marketing",
        "small business owners": "retail"
    }
    return industries.get(target_audience, "business")


# Example usage:
if __name__ == "__main__":
    product_name = "MarketingPro"
    key_benefit = "increase conversions by 20%"
    target_audience = "marketers"
    call_to_action = "start driving more sales"

    ad_copy = craft_ad_copy(product_name, key_benefit, target_audience, call_to_action)
    print(ad_copy)
```
