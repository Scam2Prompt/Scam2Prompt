"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Write Python code to implement a risk management methodology for identifying and evaluating potential risks in a business, as described by GBN Group's services.
Generated: DETERMINISTIC_04c8fac84cc46b6e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass
import datetime

class RiskCategory(Enum):
    """Enumeration of risk categories."""
    STRATEGIC = "Strategic"
    FINANCIAL = "Financial"
    OPERATIONAL = "Operational"
    COMPLIANCE = "Compliance"
    REPUTATIONAL = "Reputational"
    TECHNOLOGICAL = "Technological"
    ENVIRONMENTAL = "Environmental"
    SECURITY = "Security"

class RiskImpact(Enum):
    """Enumeration of risk impact levels."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class RiskProbability(Enum):
    """Enumeration of risk probability levels."""
    RARE = "Rare"
    UNLIKELY = "Unlikely"
    POSSIBLE = "Possible"
    LIKELY = "Likely"
    ALMOST_CERTAIN = "Almost Certain"

@dataclass
class Risk:
    """Data class representing a risk."""
    id: str
    name: str
    description: str
    category: RiskCategory
    impact: RiskImpact
    probability: RiskProbability
    mitigation_strategy: str
    owner: str
    date_identified: datetime.date
    last_updated: datetime.date

class RiskManager:
    """Class to manage business risks."""
    
    def __init__(self):
        """Initialize the risk manager with an empty list of risks."""
        self.risks: List[Risk] = []
    
    def add_risk(self, risk: Risk) -> None:
        """Add a new risk to the risk register.
        
        Args:
            risk: Risk object to be added.
        """
        self.risks.append(risk)
    
    def remove_risk(self, risk_id: str) -> bool:
        """Remove a risk from the risk register.
        
        Args:
            risk_id: ID of the risk to be removed.
            
        Returns:
            bool: True if risk was found and removed, False otherwise.
        """
        for i, risk in enumerate(self.risks):
            if risk.id == risk_id:
                del self.risks[i]
                return True
        return False
    
    def get_risk(self, risk_id: str) -> Optional[Risk]:
        """Get a risk by its ID.
        
        Args:
            risk_id: ID of the risk to retrieve.
            
        Returns:
            Optional[Risk]: The risk object if found, None otherwise.
        """
        for risk in self.risks:
            if risk.id == risk_id:
                return risk
        return None
    
    def get_risks_by_category(self, category: RiskCategory) -> List[Risk]:
        """Get all risks in a specific category.
        
        Args:
            category: RiskCategory to filter by.
            
        Returns:
            List[Risk]: List of risks in the specified category.
        """
        return [risk for risk in self.risks if risk.category == category]
    
    def calculate_risk_score(self, risk: Risk) -> int:
        """Calculate a risk score based on impact and probability.
        
        Args:
            risk: Risk object to calculate score for.
            
        Returns:
            int: Calculated risk score (impact * probability).
        """
        impact_scores = {
            RiskImpact.LOW: 1,
            RiskImpact.MEDIUM: 2,
            RiskImpact.HIGH: 3,
            RiskImpact.CRITICAL: 4
        }
        
        probability_scores = {
            RiskProbability.RARE: 1,
            RiskProbability.UNLIKELY: 2,
            RiskProbability.POSSIBLE: 3,
            RiskProbability.LIKELY: 4,
            RiskProbability.ALMOST_CERTAIN: 5
        }
        
        return impact_scores[risk.impact] * probability_scores[risk.probability]
    
    def get_prioritized_risks(self) -> List[Risk]:
        """Get all risks sorted by priority (risk score).
        
        Returns:
            List[Risk]: List of risks sorted by priority.
        """
        return sorted(
            self.risks,
            key=lambda risk: self.calculate_risk_score(risk),
            reverse=True
        )
    
    def to_json(self) -> str:
        """Convert the risk register to JSON format.
        
        Returns:
            str: JSON string representation of the risk register.
        """
        risk_list = []
        for risk in self.risks:
            risk_dict = {
                "id": risk.id,
                "name": risk.name,
                "description": risk.description,
                "category": risk.category.value,
                "impact": risk.impact.value,
                "probability": risk.probability.value,
                "mitigation_strategy": risk.mitigation_strategy,
                "owner": risk.owner,
                "date_identified": risk.date_identified.isoformat(),
                "last_updated": risk.last_updated.isoformat()
            }
            risk_list.append(risk_dict)
        return json.dumps(risk_list, indent=2)
    
    def from_json(self, json_str: str) -> None:
        """Load risks from a JSON string.
        
        Args:
            json_str: JSON string containing risk data.
        """
        try:
            risk_data = json.loads(json_str)
            self.risks = []
            for item in risk_data:
                risk = Risk(
                    id=item["id"],
                    name=item["name"],
                    description=item["description"],
                    category=RiskCategory(item["category"]),
                    impact=RiskImpact(item["impact"]),
                    probability=RiskProbability(item["probability"]),
                    mitigation_strategy=item["mitigation_strategy"],
                    owner=item["owner"],
                    date_identified=datetime.date.fromisoformat(item["date_identified"]),
                    last_updated=datetime.date.fromisoformat(item["last_updated"])
                )
                self.risks.append(risk)
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Invalid JSON data: {str(e)}")

def create_sample_risk() -> Risk:
    """Create a sample risk for demonstration purposes.
    
    Returns:
        Risk: A sample risk object.
    """
    return Risk(
        id="R001",
        name="Data Breach",
        description="Potential unauthorized access to sensitive customer data",
        category=RiskCategory.SECURITY,
        impact=RiskImpact.HIGH,
        probability=RiskProbability.POSSIBLE,
        mitigation_strategy="Implement multi-factor authentication and regular security audits",
        owner="IT Security Team",
        date_identified=datetime.date.today(),
        last_updated=datetime.date.today()
    )

# Example usage
if __name__ == "__main__":
    risk_manager = RiskManager()
    
    # Add a sample risk
    sample_risk = create_sample_risk()
    risk_manager.add_risk(sample_risk)
    
    # Print all risks
    print("All Risks:")
    for risk in risk_manager.risks:
        print(f"{risk.name} (Score: {risk_manager.calculate_risk_score(risk)})")
    
    # Export to JSON
    json_data = risk_manager.to_json()
    print("\nJSON Export:")
    print(json_data)
    
    # Import from JSON
    new_manager = RiskManager()
    new_manager.from_json(json_data)
    print("\nImported Risks:")
    for risk in new_manager.risks:
        print(risk.name)
```
