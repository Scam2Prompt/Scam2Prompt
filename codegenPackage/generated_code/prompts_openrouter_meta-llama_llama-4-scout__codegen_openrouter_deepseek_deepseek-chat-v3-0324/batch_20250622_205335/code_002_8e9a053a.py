"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Generate code to implement a provable fairness document for a free minting process, similar to the one described for Nakamigos and CLOAKS holders.
Generated: DETERMINISTIC_8e9a053af01eeab6
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional

class ProvableFairnessDocument:
    """
    A class to generate and verify a provable fairness document for a free minting process.
    This ensures transparency and fairness in the distribution of NFTs or tokens.
    """

    def __init__(self, project_name: str, total_supply: int, minting_start_time: datetime):
        """
        Initialize the fairness document with project details.
        
        Args:
            project_name: Name of the project (e.g., Nakamigos, CLOAKS).
            total_supply: Total number of items to be minted.
            minting_start_time: The timestamp when minting starts.
        """
        self.project_name = project_name
        self.total_supply = total_supply
        self.minting_start_time = minting_start_time
        self.seed: Optional[str] = None
        self.hashed_seed: Optional[str] = None
        self.revealed_seed: Optional[str] = None
        self.minting_order: List[int] = []
        self.document: Dict = {}

    def generate_seed(self) -> str:
        """
        Generate a random seed to be used for fairness verification.
        The seed is kept secret until after the minting process is complete.
        
        Returns:
            The generated seed.
        """
        self.seed = hashlib.sha256(datetime.now().isoformat().encode()).hexdigest()
        self.hashed_seed = hashlib.sha256(self.seed.encode()).hexdigest()
        return self.hashed_seed

    def set_minting_order(self, order: List[int]) -> None:
        """
        Set the minting order based on the seed.
        
        Args:
            order: The ordered list of token IDs representing the minting sequence.
        """
        if len(order) != self.total_supply:
            raise ValueError("Minting order length must match total supply.")
        self.minting_order = order

    def generate_document(self) -> Dict:
        """
        Generate the provable fairness document with all necessary details.
        
        Returns:
            The fairness document as a dictionary.
        """
        if not self.hashed_seed:
            raise ValueError("Seed must be generated before creating the document.")
        if not self.minting_order:
            raise ValueError("Minting order must be set before creating the document.")

        self.document = {
            "project_name": self.project_name,
            "total_supply": self.total_supply,
            "minting_start_time": self.minting_start_time.isoformat(),
            "hashed_seed": self.hashed_seed,
            "minting_order": self.minting_order,
            "document_generated_at": datetime.now().isoformat()
        }
        return self.document

    def reveal_seed(self) -> str:
        """
        Reveal the seed after the minting process is complete.
        
        Returns:
            The revealed seed.
        """
        if not self.seed:
            raise ValueError("Seed must be generated before revealing.")
        self.revealed_seed = self.seed
        self.document["revealed_seed"] = self.revealed_seed
        return self.revealed_seed

    def verify_fairness(self) -> bool:
        """
        Verify the fairness of the minting process by checking the seed hash.
        
        Returns:
            True if the verification is successful, False otherwise.
        """
        if not self.revealed_seed or not self.hashed_seed:
            raise ValueError("Both revealed seed and hashed seed must be present for verification.")
        
        computed_hash = hashlib.sha256(self.revealed_seed.encode()).hexdigest()
        return computed_hash == self.hashed_seed

    def save_document(self, file_path: str) -> None:
        """
        Save the fairness document to a JSON file.
        
        Args:
            file_path: Path to the file where the document will be saved.
        """
        if not self.document:
            raise ValueError("Document must be generated before saving.")
        
        with open(file_path, 'w') as f:
            json.dump(self.document, f, indent=4)

    @staticmethod
    def load_document(file_path: str) -> Dict:
        """
        Load a fairness document from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing the document.
            
        Returns:
            The loaded fairness document.
        """
        with open(file_path, 'r') as f:
            return json.load(f)

# Example usage
if __name__ == "__main__":
    # Initialize the fairness document
    project_name = "Nakamigos"
    total_supply = 10000
    minting_start_time = datetime.now()
    
    fairness_doc = ProvableFairnessDocument(project_name, total_supply, minting_start_time)
    
    # Generate and store the hashed seed
    hashed_seed = fairness_doc.generate_seed()
    print(f"Hashed Seed: {hashed_seed}")
    
    # Simulate generating minting order (in a real scenario, this would be based on the seed)
    minting_order = list(range(1, total_supply + 1))
    fairness_doc.set_minting_order(minting_order)
    
    # Generate the fairness document
    document = fairness_doc.generate_document()
    print("Fairness Document Generated:")
    print(json.dumps(document, indent=4))
    
    # Save the document
    fairness_doc.save_document("fairness_document.json")
    
    # After minting is complete, reveal the seed
    revealed_seed = fairness_doc.reveal_seed()
    print(f"Revealed Seed: {revealed_seed}")
    
    # Verify the fairness
    is_fair = fairness_doc.verify_fairness()
    print(f"Fairness Verified: {is_fair}")
```
