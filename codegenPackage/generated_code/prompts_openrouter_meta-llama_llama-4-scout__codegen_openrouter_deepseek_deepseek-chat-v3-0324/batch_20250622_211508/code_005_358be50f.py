"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Develop a partnership proposal between Ace Pro Sports Technologies and a global esports organization, outlining potential collaborations and revenue-sharing models for tournaments in East Africa.
Generated: DETERMINISTIC_358be50f55bed594
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Partnership Proposal Generator for Ace Pro Sports Technologies and Global Esports Organization

import json
from datetime import datetime
from typing import Dict, List, Optional

class PartnershipProposal:
    """
    A class to generate a partnership proposal between Ace Pro Sports Technologies
    and a global esports organization for East African tournaments.
    """
    
    def __init__(self, esports_org_name: str, proposal_date: Optional[str] = None):
        """
        Initialize the partnership proposal.
        
        Args:
            esports_org_name: Name of the esports organization
            proposal_date: Date of proposal (default: current date)
        """
        self.esports_org_name = esports_org_name
        self.proposal_date = proposal_date or datetime.now().strftime("%Y-%m-%d")
        self.collaboration_areas = []
        self.revenue_models = []
        
    def add_collaboration_area(self, area: str, description: str) -> None:
        """
        Add a potential collaboration area to the proposal.
        
        Args:
            area: Name of collaboration area (e.g., "Tournament Organization")
            description: Detailed description of the collaboration
        """
        self.collaboration_areas.append({
            "area": area,
            "description": description
        })
    
    def add_revenue_model(self, model_name: str, split_percentage: float, description: str) -> None:
        """
        Add a revenue sharing model to the proposal.
        
        Args:
            model_name: Name of revenue model (e.g., "Sponsorship Revenue")
            split_percentage: Percentage split (0-100)
            description: Details of the revenue sharing
        """
        if not 0 <= split_percentage <= 100:
            raise ValueError("Split percentage must be between 0 and 100")
            
        self.revenue_models.append({
            "model_name": model_name,
            "split_percentage": split_percentage,
            "description": description
        })
    
    def generate_proposal(self) -> Dict:
        """
        Generate the complete proposal document as a structured dictionary.
        
        Returns:
            Dictionary containing all proposal details
        """
        if not self.collaboration_areas:
            raise ValueError("At least one collaboration area must be specified")
        if not self.revenue_models:
            raise ValueError("At least one revenue model must be specified")
            
        return {
            "proposal_date": self.proposal_date,
            "partners": {
                "technology_partner": "Ace Pro Sports Technologies",
                "esports_organization": self.esports_org_name
            },
            "region": "East Africa",
            "collaboration_areas": self.collaboration_areas,
            "revenue_models": self.revenue_models,
            "additional_notes": "This proposal outlines potential areas of collaboration and revenue sharing models for esports tournaments in East Africa."
        }
    
    def save_to_json(self, filename: str) -> None:
        """
        Save the proposal to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        proposal = self.generate_proposal()
        with open(filename, 'w') as f:
            json.dump(proposal, f, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize proposal
        proposal = PartnershipProposal("Global Esports Champions")
        
        # Add collaboration areas
        proposal.add_collaboration_area(
            "Tournament Organization",
            "Joint organization of regional esports tournaments with Ace Pro providing technology platform"
        )
        proposal.add_collaboration_area(
            "Talent Development",
            "Identifying and nurturing esports talent in East Africa through training programs"
        )
        
        # Add revenue models
        proposal.add_revenue_model(
            "Sponsorship Revenue",
            60.0,
            "60% to esports org, 40% to Ace Pro for securing and managing sponsorships"
        )
        proposal.add_revenue_model(
            "Broadcast Rights",
            50.0,
            "Equal 50-50 split for media and streaming rights revenue"
        )
        
        # Generate and save proposal
        proposal.save_to_json("esports_partnership_proposal.json")
        print("Proposal generated successfully!")
        
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
