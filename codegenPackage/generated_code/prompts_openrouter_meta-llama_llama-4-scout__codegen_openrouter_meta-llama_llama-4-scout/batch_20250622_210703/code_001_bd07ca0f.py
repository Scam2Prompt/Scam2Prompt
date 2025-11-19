"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Compare and contrast the benefits of using single essential oils versus oil blends, such as those offered by dōTERRA, for aromatherapy and wellness.
Generated: DETERMINISTIC_bd07ca0ff5f27d51
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aromatherapy_comparator.py

class EssentialOil:
    """Represents an essential oil with its properties and benefits."""

    def __init__(self, name, benefits, caution=None):
        """
        Initializes an EssentialOil instance.

        Args:
            name (str): The name of the essential oil.
            benefits (list[str]): A list of benefits associated with the oil.
            caution (str, optional): Any caution or warning for the oil. Defaults to None.
        """
        self.name = name
        self.benefits = benefits
        self.caution = caution

    def __str__(self):
        return f"{self.name}: {', '.join(self.benefits)}"


class OilBlend:
    """Represents a blend of essential oils."""

    def __init__(self, name, oils):
        """
        Initializes an OilBlend instance.

        Args:
            name (str): The name of the oil blend.
            oils (dict[EssentialOil, float]): A dictionary of essential oils and their proportions in the blend.
        """
        self.name = name
        self.oils = oils

    def get_benefits(self):
        """
        Returns a set of benefits associated with the oil blend.

        Returns:
            set[str]: A set of benefits.
        """
        benefits = set()
        for oil, _ in self.oils.items():
            benefits.update(oil.benefits)
        return benefits

    def __str__(self):
        oil_str = "\n".join(f"  - {oil.name}: {proportion}%" for oil, proportion in self.oils.items())
        return f"{self.name}:\n{oil_str}"


def compare_oils(single_oil, oil_blend):
    """
    Compares the benefits of a single essential oil and an oil blend.

    Args:
        single_oil (EssentialOil): The single essential oil.
        oil_blend (OilBlend): The oil blend.

    Returns:
        dict[str, str]: A dictionary highlighting the differences and similarities.
    """
    comparison = {
        "Single Oil Benefits": ", ".join(single_oil.benefits),
        "Oil Blend Benefits": ", ".join(oil_blend.get_benefits()),
    }

    if single_oil.caution:
        comparison["Single Oil Caution"] = single_oil.caution
    if any(oil.caution for oil in oil_blend.oils.keys()):
        comparison["Oil Blend Caution"] = ", ".join(
            oil.caution for oil in oil_blend.oils.keys() if oil.caution
        )

    return comparison


def main():
    try:
        # Create essential oils
        lavender = EssentialOil("Lavender", ["Promotes relaxation", "Improves sleep"])
        peppermint = EssentialOil("Peppermint", ["Boosts energy", "Aids digestion"])
        frankincense = EssentialOil(
            "Frankincense", ["Reduces inflammation", "Promotes skin health"], "May cause skin irritation"
        )

        # Create oil blends
        calming_blend = OilBlend(
            "Calming Blend",
            {
                lavender: 50,
                frankincense: 30,
                EssentialOil("Bergamot", ["Uplifts mood"]): 20,
            },
        )

        invigorating_blend = OilBlend(
            "Invigorating Blend",
            {
                peppermint: 60,
                EssentialOil("Eucalyptus", ["Relieves congestion"]): 20,
                EssentialOil("Rosemary", ["Improves focus"]): 20,
            },
        )

        # Compare oils
        comparison_lavender_calming = compare_oils(lavender, calming_blend)
        comparison_peppermint_invigorating = compare_oils(peppermint, invigorating_blend)

        # Print comparisons
        print("Comparison 1: Lavender vs. Calming Blend")
        for key, value in comparison_lavender_calming.items():
            print(f"{key}: {value}")

        print("\nComparison 2: Peppermint vs. Invigorating Blend")
        for key, value in comparison_peppermint_invigorating.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
