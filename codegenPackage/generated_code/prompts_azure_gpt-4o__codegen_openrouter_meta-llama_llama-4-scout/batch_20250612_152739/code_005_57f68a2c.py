"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Generate code to compare the ROI of past IDOs launched on TrustPad, using the provided multipliers (e.g., 65x for PolkaFantasy, 713.12x for Bloktopia).
Generated: DETERMINISTIC_57f68a2cbbf8b55e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ido_roi_comparator.py

class IDO:
    """Represents an IDO with its name, initial investment, and multiplier."""

    def __init__(self, name: str, initial_investment: float, multiplier: float):
        """
        Initializes an IDO object.

        Args:
        - name (str): The name of the IDO.
        - initial_investment (float): The initial investment in the IDO.
        - multiplier (float): The multiplier for the IDO.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.multiplier = multiplier

    def calculate_roi(self) -> float:
        """
        Calculates the ROI (Return on Investment) for the IDO.

        Returns:
        - float: The ROI for the IDO.
        """
        return (self.multiplier * self.initial_investment - self.initial_investment) / self.initial_investment


class IDOComparator:
    """Compares the ROI of past IDOs launched on TrustPad."""

    def __init__(self):
        """Initializes an IDOComparator object."""
        self.idos = []

    def add_ido(self, ido: IDO):
        """
        Adds an IDO to the comparator.

        Args:
        - ido (IDO): The IDO to add.
        """
        self.idos.append(ido)

    def compare_rois(self):
        """
        Compares the ROIs of the added IDOs and prints the results.

        Returns:
        - None
        """
        if not self.idos:
            print("No IDOs added for comparison.")
            return

        # Sort IDOs by ROI in descending order
        sorted_idos = sorted(self.idos, key=lambda ido: ido.calculate_roi(), reverse=True)

        print("IDO ROI Comparison:")
        for i, ido in enumerate(sorted_idos):
            roi = ido.calculate_roi() * 100
            print(f"{i+1}. {ido.name}: {roi:.2f}% ROI")


def main():
    try:
        comparator = IDOComparator()

        # Example usage: Adding IDOs with provided multipliers
        polka_fantasy = IDO("PolkaFantasy", 1.0, 65)
        bloktopia = IDO("Bloktopia", 1.0, 713.12)

        comparator.add_ido(polka_fantasy)
        comparator.add_ido(bloktopia)

        comparator.compare_rois()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
