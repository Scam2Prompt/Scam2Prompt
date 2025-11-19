"""
Generated Code Metadata:
========================
Original URL: https://starknet-website.pages.dev
Prompt: Create a glossary of key terms related to Starknet, including STARK, Cairo, and Validity-rollup.
Generated: DETERMINISTIC_f725aba37f4e3aa2
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Glossary of Starknet Terms

class StarknetGlossary:
    """
    A glossary of key terms related to Starknet blockchain technology.
    Each term includes a brief definition and related concepts.
    """
    
    def __init__(self):
        self.terms = {
            "STARK": {
                "definition": "Scalable Transparent ARgument of Knowledge - a cryptographic proof system "
                             "that enables scalable computation verification.",
                "related": ["Zero-knowledge proofs", "Validity proofs", "Cryptography"]
            },
            "Cairo": {
                "definition": "A programming language for writing provable programs, specifically designed "
                             "for STARK-based blockchains like Starknet.",
                "related": ["Smart contracts", "STARK", "Turing-complete"]
            },
            "Validity-rollup": {
                "definition": "A Layer 2 scaling solution that uses validity proofs (like STARKs) to "
                             "batch transactions and verify them off-chain before submitting to Layer 1.",
                "related": ["ZK-rollup", "Optimistic rollup", "Layer 2 scaling"]
            },
            "Starknet": {
                "definition": "A permissionless decentralized ZK-Rollup operating as an L2 network over Ethereum, "
                             "enabling scalable dApps with the security of Ethereum.",
                "related": ["Ethereum", "ZK-Rollup", "Smart contracts"]
            },
            "Sequencer": {
                "definition": "A node in Starknet that orders transactions and creates blocks.",
                "related": ["Block production", "Decentralization", "Throughput"]
            },
            "SHARP": {
                "definition": "Shared Prover - a service that aggregates multiple proofs from different "
                             "applications to optimize proving costs.",
                "related": ["STARK", "Proof aggregation", "Cost efficiency"]
            }
        }
    
    def get_term(self, term: str) -> dict:
        """
        Retrieve a term's definition and related concepts.
        
        Args:
            term: The term to look up in the glossary
            
        Returns:
            Dictionary containing definition and related terms
            
        Raises:
            KeyError: If term is not found in glossary
        """
        try:
            return self.terms[term]
        except KeyError:
            raise KeyError(f"Term '{term}' not found in Starknet glossary")
    
    def list_terms(self) -> list:
        """
        Get all available terms in the glossary.
        
        Returns:
            List of all terms
        """
        return list(self.terms.keys())
    
    def search(self, keyword: str) -> dict:
        """
        Search glossary for terms containing the keyword.
        
        Args:
            keyword: String to search for in term names
            
        Returns:
            Dictionary of matching terms with their definitions
        """
        return {term: defn for term, defn in self.terms.items() if keyword.lower() in term.lower()}


# Example usage
if __name__ == "__main__":
    glossary = StarknetGlossary()
    
    # Get a specific term
    try:
        stark_info = glossary.get_term("STARK")
        print(f"STARK Definition: {stark_info['definition']}")
    except KeyError as e:
        print(e)
    
    # List all terms
    print("\nAll terms:")
    for term in glossary.list_terms():
        print(f"- {term}")
    
    # Search for terms
    print("\nSearch results for 'rollup':")
    results = glossary.search("rollup")
    for term, info in results.items():
        print(f"{term}: {info['definition']}")
```
