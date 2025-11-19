"""
Generated Code Metadata:
========================
Original URL: https://terraclassic.app
Prompt: What is the purpose of TerraScan, and how does it relate to TerraClassic?
Generated: DETERMINISTIC_d368975a9ccc4f57
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# terra_scan_info.py

class TerraScanInfo:
    """
    Provides information about TerraScan and its relation to TerraClassic.
    """

    def __init__(self):
        pass

    def get_terra_scan_purpose(self) -> str:
        """
        Returns the purpose of TerraScan.

        Returns:
            str: The purpose of TerraScan.
        """
        return "TerraScan is a blockchain explorer and analytics platform for Terra and Terra Classic."

    def get_terra_classic_relation(self) -> str:
        """
        Returns the relation between TerraScan and TerraClassic.

        Returns:
            str: The relation between TerraScan and TerraClassic.
        """
        return "TerraScan supports both Terra and Terra Classic, providing a unified platform for exploring and analyzing both chains."


def main():
    try:
        terra_scan_info = TerraScanInfo()
        print("Purpose of TerraScan:")
        print(terra_scan_info.get_terra_scan_purpose())
        print("\nRelation to TerraClassic:")
        print(terra_scan_info.get_terra_classic_relation())
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
