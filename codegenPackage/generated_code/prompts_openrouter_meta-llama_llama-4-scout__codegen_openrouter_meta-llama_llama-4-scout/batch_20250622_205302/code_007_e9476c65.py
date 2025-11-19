"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: "List the key features of HV-MTL NFTs, such as their skills, personality, and roles, and suggest a database schema to store these features."
Generated: DETERMINISTIC_e9476c6561ac07b8
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hv_mtl_nft.py

class HVMTL:
    """
    Represents an HV-MTL NFT with its key features.
    """

    def __init__(self, name, skills=None, personality=None, role=None):
        """
        Initializes an HV-MTL NFT.

        Args:
            name (str): The name of the NFT.
            skills (list[str], optional): The skills of the NFT. Defaults to None.
            personality (str, optional): The personality of the NFT. Defaults to None.
            role (str, optional): The role of the NFT. Defaults to None.
        """
        self.name = name
        self.skills = skills if skills is not None else []
        self.personality = personality
        self.role = role

    def __str__(self):
        return f"HV-MTL NFT: {self.name}"

    def to_dict(self):
        """
        Converts the HV-MTL NFT to a dictionary.

        Returns:
            dict: A dictionary representation of the HV-MTL NFT.
        """
        return {
            "name": self.name,
            "skills": self.skills,
            "personality": self.personality,
            "role": self.role,
        }


class HVMTLDatabase:
    """
    A simple database to store HV-MTL NFTs.
    """

    def __init__(self):
        """
        Initializes an empty database.
        """
        self.nfts = {}

    def add_nft(self, nft):
        """
        Adds an HV-MTL NFT to the database.

        Args:
            nft (HVMTL): The HV-MTL NFT to add.

        Raises:
            ValueError: If an NFT with the same name already exists.
        """
        if nft.name in self.nfts:
            raise ValueError("NFT with the same name already exists")
        self.nfts[nft.name] = nft.to_dict()

    def get_nft(self, name):
        """
        Retrieves an HV-MTL NFT from the database.

        Args:
            name (str): The name of the HV-MTL NFT.

        Returns:
            HVMTL: The HV-MTL NFT with the given name, or None if not found.
        """
        nft_data = self.nfts.get(name)
        if nft_data:
            return HVMTL(**nft_data)
        return None

    def list_nfts(self):
        """
        Lists all HV-MTL NFTs in the database.

        Returns:
            list[HVMTL]: A list of HV-MTL NFTs.
        """
        return [HVMTL(**nft_data) for nft_data in self.nfts.values()]


# Example usage
if __name__ == "__main__":
    db = HVMTLDatabase()

    nft1 = HVMTL(
        "NFT1",
        skills=["Skill1", "Skill2"],
        personality="Friendly",
        role="Warrior",
    )
    nft2 = HVMTL(
        "NFT2",
        skills=["Skill3", "Skill4"],
        personality="Aggressive",
        role="Mage",
    )

    db.add_nft(nft1)
    db.add_nft(nft2)

    print("List of HV-MTL NFTs:")
    for nft in db.list_nfts():
        print(nft)
        print(f"Skills: {nft.skills}")
        print(f"Personality: {nft.personality}")
        print(f"Role: {nft.role}")
        print("------------------------")

    try:
        db.add_nft(nft1)  # Attempt to add a duplicate NFT
    except ValueError as e:
        print(f"Error: {e}")
```

```sql
-- hv_mtl_nft_schema.sql

CREATE TABLE hv_mtl_nfts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    skills TEXT[],
    personality VARCHAR(255),
    role VARCHAR(255)
);

CREATE INDEX idx_hv_mtl_nfts_name ON hv_mtl_nfts (name);

-- Example usage
INSERT INTO hv_mtl_nfts (name, skills, personality, role)
VALUES
    ('NFT1', ARRAY['Skill1', 'Skill2'], 'Friendly', 'Warrior'),
    ('NFT2', ARRAY['Skill3', 'Skill4'], 'Aggressive', 'Mage');

SELECT * FROM hv_mtl_nfts;
```
