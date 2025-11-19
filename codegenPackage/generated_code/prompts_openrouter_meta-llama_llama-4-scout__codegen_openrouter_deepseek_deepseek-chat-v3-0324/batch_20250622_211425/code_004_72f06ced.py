"""
Generated Code Metadata:
========================
Original URL: https://gen-da6.pages.dev
Prompt: Describe the role of partners in the $ENTS ecosystem and how they contribute to its tokenomics.
Generated: DETERMINISTIC_72f06ced573a96ba
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# $ENTS Ecosystem Partner Role and Tokenomics Contribution Documentation

class ENTS_Ecosystem:
    """
    Represents the $ENTS ecosystem and its tokenomics.
    Describes the role of partners and their contributions.
    """
    
    def __init__(self):
        """
        Initialize the $ENTS ecosystem with default parameters.
        """
        self.total_supply = 0
        self.partners = []
        self.tokenomics = {
            'staking_rewards': 0,
            'liquidity_provision': 0,
            'governance': 0,
            'ecosystem_fund': 0
        }
    
    def add_partner(self, partner_name: str, contribution_type: str, contribution_value: float):
        """
        Add a partner to the ecosystem with their contribution details.
        
        Args:
            partner_name (str): Name of the partner
            contribution_type (str): Type of contribution (e.g., 'liquidity', 'development', 'marketing')
            contribution_value (float): Value of contribution in $ENTS tokens
            
        Raises:
            ValueError: If contribution type is invalid or value is negative
        """
        if contribution_value < 0:
            raise ValueError("Contribution value cannot be negative")
            
        valid_contributions = ['liquidity', 'development', 'marketing', 'governance', 'staking']
        if contribution_type.lower() not in valid_contributions:
            raise ValueError(f"Invalid contribution type. Must be one of: {valid_contributions}")
            
        self.partners.append({
            'name': partner_name,
            'type': contribution_type.lower(),
            'value': contribution_value
        })
        
        # Update tokenomics based on contribution type
        if contribution_type.lower() == 'liquidity':
            self.tokenomics['liquidity_provision'] += contribution_value
        elif contribution_type.lower() == 'staking':
            self.tokenomics['staking_rewards'] += contribution_value
        elif contribution_type.lower() == 'governance':
            self.tokenomics['governance'] += contribution_value
        else:
            self.tokenomics['ecosystem_fund'] += contribution_value
            
        self.total_supply += contribution_value
    
    def get_partner_contributions(self, partner_name: str) -> dict:
        """
        Get contribution details for a specific partner.
        
        Args:
            partner_name (str): Name of the partner to query
            
        Returns:
            dict: Partner's contribution details
            
        Raises:
            KeyError: If partner doesn't exist
        """
        for partner in self.partners:
            if partner['name'] == partner_name:
                return partner
        raise KeyError(f"Partner {partner_name} not found in ecosystem")
    
    def get_tokenomics_distribution(self) -> dict:
        """
        Get current tokenomics distribution percentages.
        
        Returns:
            dict: Tokenomics distribution as percentages of total supply
        """
        if self.total_supply == 0:
            return {k: 0 for k in self.tokenomics.keys()}
            
        return {
            'staking_rewards': (self.tokenomics['staking_rewards'] / self.total_supply) * 100,
            'liquidity_provision': (self.tokenomics['liquidity_provision'] / self.total_supply) * 100,
            'governance': (self.tokenomics['governance'] / self.total_supply) * 100,
            'ecosystem_fund': (self.tokenomics['ecosystem_fund'] / self.total_supply) * 100
        }
    
    def __str__(self) -> str:
        """
        String representation of the ecosystem state.
        
        Returns:
            str: Formatted string showing partners and tokenomics
        """
        tokenomics_percent = self.get_tokenomics_distribution()
        partners_list = "\n".join([f"- {p['name']}: {p['type']} ({p['value']} $ENTS)" 
                                 for p in self.partners])
        
        return (
            f"$ENTS Ecosystem Status:\n"
            f"Total Supply: {self.total_supply} $ENTS\n\n"
            f"Partners:\n{partners_list}\n\n"
            f"Tokenomics Distribution:\n"
            f"- Staking Rewards: {tokenomics_percent['staking_rewards']:.2f}%\n"
            f"- Liquidity Provision: {tokenomics_percent['liquidity_provision']:.2f}%\n"
            f"- Governance: {tokenomics_percent['governance']:.2f}%\n"
            f"- Ecosystem Fund: {tokenomics_percent['ecosystem_fund']:.2f}%"
        )


# Example usage
if __name__ == "__main__":
    ecosystem = ENTS_Ecosystem()
    
    try:
        ecosystem.add_partner("DEX Partner", "liquidity", 500000)
        ecosystem.add_partner("Staking Platform", "staking", 300000)
        ecosystem.add_partner("Marketing Agency", "marketing", 200000)
        ecosystem.add_partner("Governance DAO", "governance", 100000)
        
        print(ecosystem)
        
        # Example query
        print("\nPartner details for 'DEX Partner':")
        print(ecosystem.get_partner_contributions("DEX Partner"))
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
```
