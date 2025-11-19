"""
Generated Code Metadata:
========================
Original URL: https://agora-next-jlesgw0mi-voteagora.vercel.app
Prompt: "Compare the features of Optimism Agora with other on-chain governance platforms, focusing on RetroPGF and proposal voting mechanisms."
Generated: DETERMINISTIC_b8421e7c8c06a909
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class GovernanceFeature:
    """Dataclass to represent governance platform features."""
    name: str
    description: str
    has_retro_pgf: bool
    proposal_voting_mechanism: str
    token_requirement: Optional[str] = None

class GovernancePlatformComparator:
    """Class to compare governance platforms focusing on RetroPGF and voting mechanisms."""
    
    def __init__(self):
        self.platforms: Dict[str, GovernanceFeature] = {}
        
    def add_platform(self, name: str, feature: GovernanceFeature) -> None:
        """Add a governance platform to the comparator.
        
        Args:
            name: Name of the platform
            feature: GovernanceFeature object containing platform details
        """
        self.platforms[name] = feature
    
    def compare_retro_pgf(self) -> Dict[str, bool]:
        """Compare RetroPGF support across platforms.
        
        Returns:
            Dictionary mapping platform names to RetroPGF support status
        """
        return {name: feature.has_retro_pgf for name, feature in self.platforms.items()}
    
    def compare_voting_mechanisms(self) -> Dict[str, str]:
        """Compare voting mechanisms across platforms.
        
        Returns:
            Dictionary mapping platform names to their voting mechanisms
        """
        return {name: feature.proposal_voting_mechanism for name, feature in self.platforms.items()}
    
    def get_platform_details(self, platform_name: str) -> Optional[GovernanceFeature]:
        """Get detailed features of a specific platform.
        
        Args:
            platform_name: Name of the platform to query
            
        Returns:
            GovernanceFeature object if found, None otherwise
        """
        return self.platforms.get(platform_name)
    
    def generate_comparison_report(self) -> str:
        """Generate a formatted comparison report.
        
        Returns:
            String containing formatted comparison report
        """
        report = ["Governance Platform Comparison Report", "="*40]
        
        # RetroPGF comparison
        report.append("\nRetroactive Public Goods Funding (RetroPGF):")
        for name, feature in self.platforms.items():
            report.append(f"- {name}: {'✅' if feature.has_retro_pgf else '❌'}")
        
        # Voting mechanisms comparison
        report.append("\nProposal Voting Mechanisms:")
        for name, feature in self.platforms.items():
            report.append(f"- {name}: {feature.proposal_voting_mechanism}")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    comparator = GovernancePlatformComparator()
    
    # Add Optimism Agora
    comparator.add_platform(
        "Optimism Agora",
        GovernanceFeature(
            name="Optimism Agora",
            description="Optimism's governance platform with RetroPGF",
            has_retro_pgf=True,
            proposal_voting_mechanism="Token-weighted voting with delegation",
            token_requirement="OP token"
        )
    )
    
    # Add other platforms for comparison
    comparator.add_platform(
        "Compound Governance",
        GovernanceFeature(
            name="Compound Governance",
            description="Compound's on-chain governance system",
            has_retro_pgf=False,
            proposal_voting_mechanism="Token-weighted voting",
            token_requirement="COMP token"
        )
    )
    
    comparator.add_platform(
        "Gitcoin Grants",
        GovernanceFeature(
            name="Gitcoin Grants",
            description="Quadratic funding for public goods",
            has_retro_pgf=True,
            proposal_voting_mechanism="Quadratic funding rounds",
            token_requirement="GTC token (optional)"
        )
    )
    
    # Generate and print comparison report
    print(comparator.generate_comparison_report())
```
