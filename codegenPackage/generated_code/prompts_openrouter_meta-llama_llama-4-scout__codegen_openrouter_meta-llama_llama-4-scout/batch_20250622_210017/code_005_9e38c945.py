"""
Generated Code Metadata:
========================
Original URL: https://web3.ca
Prompt: "Compare the benefits and drawbacks of using a proprietary content management system (CMS) versus an open-source platform like WordPress, which Web3 uses in combination with their Framework."
Generated: DETERMINISTIC_9e38c945a55e0e51
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cms_comparator.py

class CMS:
    """Base class for Content Management Systems"""

    def __init__(self, name, cost, scalability, security, community_support):
        """
        Initialize a CMS object.

        Args:
            name (str): Name of the CMS
            cost (str): Cost of the CMS (e.g., free, paid)
            scalability (str): Scalability of the CMS (e.g., high, low)
            security (str): Security of the CMS (e.g., high, low)
            community_support (str): Community support for the CMS (e.g., large, small)
        """
        self.name = name
        self.cost = cost
        self.scalability = scalability
        self.security = security
        self.community_support = community_support

    def __str__(self):
        return f"{self.name}: Cost - {self.cost}, Scalability - {self.scalability}, Security - {self.security}, Community Support - {self.community_support}"


class ProprietaryCMS(CMS):
    """Class for Proprietary Content Management Systems"""

    def __init__(self, name, cost, scalability, security, community_support, vendor_lock_in):
        """
        Initialize a Proprietary CMS object.

        Args:
            name (str): Name of the CMS
            cost (str): Cost of the CMS (e.g., free, paid)
            scalability (str): Scalability of the CMS (e.g., high, low)
            security (str): Security of the CMS (e.g., high, low)
            community_support (str): Community support for the CMS (e.g., large, small)
            vendor_lock_in (bool): Whether the CMS has vendor lock-in
        """
        super().__init__(name, cost, scalability, security, community_support)
        self.vendor_lock_in = vendor_lock_in

    def __str__(self):
        return super().__str__() + f", Vendor Lock-in - {self.vendor_lock_in}"


class OpenSourceCMS(CMS):
    """Class for Open-Source Content Management Systems"""

    def __init__(self, name, cost, scalability, security, community_support, customizability):
        """
        Initialize an Open-Source CMS object.

        Args:
            name (str): Name of the CMS
            cost (str): Cost of the CMS (e.g., free, paid)
            scalability (str): Scalability of the CMS (e.g., high, low)
            security (str): Security of the CMS (e.g., high, low)
            community_support (str): Community support for the CMS (e.g., large, small)
            customizability (str): Customizability of the CMS (e.g., high, low)
        """
        super().__init__(name, cost, scalability, security, community_support)
        self.customizability = customizability

    def __str__(self):
        return super().__str__() + f", Customizability - {self.customizability}"


def compare_cms(proprietary_cms, open_source_cms):
    """
    Compare the benefits and drawbacks of a proprietary CMS and an open-source CMS.

    Args:
        proprietary_cms (ProprietaryCMS): Proprietary CMS object
        open_source_cms (OpenSourceCMS): Open-Source CMS object

    Returns:
        None
    """
    print("Proprietary CMS:")
    print(proprietary_cms)
    print("\nOpen-Source CMS:")
    print(open_source_cms)

    print("\nComparison:")
    print(f"Cost: {proprietary_cms.cost} vs {open_source_cms.cost}")
    print(f"Scalability: {proprietary_cms.scalability} vs {open_source_cms.scalability}")
    print(f"Security: {proprietary_cms.security} vs {open_source_cms.security}")
    print(f"Community Support: {proprietary_cms.community_support} vs {open_source_cms.community_support}")
    print(f"Vendor Lock-in: {proprietary_cms.vendor_lock_in} (Proprietary) vs No (Open-Source)")
    print(f"Customizability: N/A (Proprietary) vs {open_source_cms.customizability} (Open-Source)")


def main():
    try:
        # Create proprietary CMS object
        proprietary_cms = ProprietaryCMS(
            "Adobe Experience Manager",
            "Paid",
            "High",
            "High",
            "Medium",
            True
        )

        # Create open-source CMS object
        open_source_cms = OpenSourceCMS(
            "WordPress",
            "Free",
            "High",
            "Medium",
            "Large",
            "High"
        )

        # Compare CMS
        compare_cms(proprietary_cms, open_source_cms)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
