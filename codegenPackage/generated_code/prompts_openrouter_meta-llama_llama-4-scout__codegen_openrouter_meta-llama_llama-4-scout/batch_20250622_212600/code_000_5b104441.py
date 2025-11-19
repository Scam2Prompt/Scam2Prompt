"""
Generated Code Metadata:
========================
Original URL: https://stellarlure.com
Prompt: "List and describe different types of sex dolls available, including silicone head with TPE body, movable jaw, auto-sucking, and auto-breathing dolls."
Generated: DETERMINISTIC_5b104441e4b49b53
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sex_dolls.py

class SexDoll:
    def __init__(self, name, description, materials, features):
        """
        Initialize a SexDoll object.

        Args:
            name (str): Name of the sex doll.
            description (str): Description of the sex doll.
            materials (list): List of materials used to make the sex doll.
            features (list): List of features of the sex doll.
        """
        self.name = name
        self.description = description
        self.materials = materials
        self.features = features

    def __str__(self):
        return f"{self.name}: {self.description}"

class SexDollCatalog:
    def __init__(self):
        """
        Initialize a SexDollCatalog object.
        """
        self.dolls = []

    def add_doll(self, doll):
        """
        Add a sex doll to the catalog.

        Args:
            doll (SexDoll): SexDoll object to add.
        """
        self.dolls.append(doll)

    def list_dolls(self):
        """
        List all sex dolls in the catalog.
        """
        for doll in self.dolls:
            print(doll)
            print(f"Materials: {', '.join(doll.materials)}")
            print(f"Features: {', '.join(doll.features)}")
            print("------------------------")

def main():
    try:
        catalog = SexDollCatalog()

        # Create sex dolls
        doll1 = SexDoll(
            "Silicone Head with TPE Body",
            "A sex doll with a silicone head and TPE body.",
            ["Silicone", "TPE"],
            ["Realistic appearance", "Affordable"]
        )

        doll2 = SexDoll(
            "Movable Jaw Doll",
            "A sex doll with a movable jaw for realistic oral sex experience.",
            ["Silicone", "TPE"],
            ["Movable jaw", "Realistic facial expressions"]
        )

        doll3 = SexDoll(
            "Auto-Sucking Doll",
            "A sex doll with an auto-sucking feature for hands-free experience.",
            ["Silicone", "TPE"],
            ["Auto-sucking feature", "Adjustable suction levels"]
        )

        doll4 = SexDoll(
            "Auto-Breathing Doll",
            "A sex doll with an auto-breathing feature for realistic experience.",
            ["Silicone", "TPE"],
            ["Auto-breathing feature", "Adjustable breathing patterns"]
        )

        # Add sex dolls to catalog
        catalog.add_doll(doll1)
        catalog.add_doll(doll2)
        catalog.add_doll(doll3)
        catalog.add_doll(doll4)

        # List sex dolls
        catalog.list_dolls()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
