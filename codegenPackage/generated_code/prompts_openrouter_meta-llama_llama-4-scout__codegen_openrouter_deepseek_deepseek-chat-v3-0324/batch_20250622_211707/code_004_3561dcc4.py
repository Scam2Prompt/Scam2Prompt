"""
Generated Code Metadata:
========================
Original URL: https://rexas-net.web.app
Prompt: "Generate a Rexas Finance-style tokenomics document for a hypothetical blockchain-based art investment platform, including details on token supply, distribution, and utility."
Generated: DETERMINISTIC_3561dcc41bd266ad
Batch ID: 20250622_211707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tokenomics Document Generator for Art Investment Platform
This script generates a Rexas Finance-style tokenomics document for a blockchain-based art investment platform.
"""

import json
from datetime import datetime
from typing import Dict, List

class TokenomicsDocumentGenerator:
    """
    Generates a comprehensive tokenomics document with supply, distribution, and utility details.
    """
    
    def __init__(self, project_name: str, token_symbol: str):
        """
        Initialize the generator with project details.
        
        Args:
            project_name: Name of the art investment platform
            token_symbol: Symbol of the platform's native token
        """
        self.project_name = project_name
        self.token_symbol = token_symbol
        self.document = {
            "meta": {
                "version": "1.0",
                "generated_at": datetime.utcnow().isoformat(),
                "project": project_name,
                "token": token_symbol
            },
            "tokenomics": {}
        }
    
    def set_token_supply(self, total_supply: int, decimals: int = 18) -> None:
        """
        Set token supply details.
        
        Args:
            total_supply: Total number of tokens to be minted
            decimals: Number of decimal places for token (default: 18)
        """
        self.document["tokenomics"]["supply"] = {
            "total_supply": total_supply,
            "circulating_supply": 0,  # To be calculated based on distribution
            "decimals": decimals,
            "initial_mint": total_supply,
            "inflation_rate": "0%",  # Fixed supply by default
            "burn_mechanism": "Optional deflationary mechanism"
        }
    
    def set_distribution(self, distribution_breakdown: Dict[str, float]) -> None:
        """
        Set token distribution details.
        
        Args:
            distribution_breakdown: Dictionary of allocation categories and percentages
                                 (e.g., {"Team": 20.0, "Investors": 30.0})
        """
        if not self._validate_distribution(distribution_breakdown):
            raise ValueError("Distribution percentages must sum to 100%")
            
        allocations = []
        total_supply = self.document["tokenomics"]["supply"]["total_supply"]
        
        for category, percentage in distribution_breakdown.items():
            amount = int(total_supply * (percentage / 100))
            allocations.append({
                "category": category,
                "percentage": f"{percentage}%",
                "amount": amount,
                "vesting": self._get_vesting_schedule(category)
            })
        
        self.document["tokenomics"]["distribution"] = allocations
        self._calculate_circulating_supply()
    
    def set_token_utility(self, utilities: List[Dict[str, str]]) -> None:
        """
        Set token utility details.
        
        Args:
            utilities: List of dictionaries describing token utilities
                     (e.g., [{"purpose": "Governance", "description": "Voting rights"}])
        """
        self.document["tokenomics"]["utility"] = utilities
    
    def generate_document(self) -> Dict:
        """
        Generate the final tokenomics document.
        
        Returns:
            Complete tokenomics document as a dictionary
        """
        return self.document
    
    def save_to_file(self, filename: str = "tokenomics.json") -> None:
        """
        Save the tokenomics document to a JSON file.
        
        Args:
            filename: Output filename (default: tokenomics.json)
        """
        with open(filename, 'w') as f:
            json.dump(self.document, f, indent=4)
    
    def _validate_distribution(self, distribution: Dict[str, float]) -> bool:
        """Validate that distribution percentages sum to 100%."""
        return abs(sum(distribution.values()) - 100.0) < 0.001
    
    def _get_vesting_schedule(self, category: str) -> Dict:
        """Generate appropriate vesting schedule based on allocation category."""
        vesting_templates = {
            "Team": {"type": "linear", "duration": "36 months", "cliff": "12 months"},
            "Investors": {"type": "linear", "duration": "24 months", "cliff": "6 months"},
            "Advisors": {"type": "linear", "duration": "24 months", "cliff": "6 months"},
            "Community": {"type": "immediate", "duration": "0 months", "cliff": "0 months"},
            "Treasury": {"type": "progressive", "duration": "60 months", "cliff": "0 months"},
            "Marketing": {"type": "quarterly", "duration": "24 months", "cliff": "3 months"}
        }
        return vesting_templates.get(category, {"type": "custom", "duration": "TBD", "cliff": "TBD"})
    
    def _calculate_circulating_supply(self) -> None:
        """Calculate initial circulating supply based on immediate distributions."""
        circulating = 0
        for allocation in self.document["tokenomics"]["distribution"]:
            if allocation["vesting"]["type"] == "immediate":
                circulating += allocation["amount"]
        self.document["tokenomics"]["supply"]["circulating_supply"] = circulating


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize generator
        generator = TokenomicsDocumentGenerator(
            project_name="ArtBlock Invest",
            token_symbol="ABI"
        )
        
        # Set token supply
        generator.set_token_supply(total_supply=1_000_000_000)
        
        # Set distribution
        distribution = {
            "Team": 15.0,
            "Investors": 25.0,
            "Advisors": 5.0,
            "Community": 30.0,
            "Treasury": 20.0,
            "Marketing": 5.0
        }
        generator.set_distribution(distribution)
        
        # Set token utilities
        utilities = [
            {
                "purpose": "Governance",
                "description": "Token holders can vote on platform decisions and proposals"
            },
            {
                "purpose": "Staking",
                "description": "Tokens can be staked to earn platform fees and rewards"
            },
            {
                "purpose": "Access",
                "description": "Required for premium features and early access to art offerings"
            },
            {
                "purpose": "Payment",
                "description": "Used for transaction fees and purchasing fractional art shares"
            }
        ]
        generator.set_token_utility(utilities)
        
        # Generate and save document
        doc = generator.generate_document()
        generator.save_to_file()
        
        print("Tokenomics document generated successfully!")
        
    except Exception as e:
        print(f"Error generating tokenomics document: {str(e)}")
```
