"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Create a script to model ethical financial consulting practices, ensuring compliance with international standards and the values described by GCap Markets.
Generated: DETERMINISTIC_bdaa458af7b6aa67
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ethical Financial Consulting Compliance Script

This script models ethical financial consulting practices in compliance with 
international standards and GCap Markets values. It includes functions for:
- Client suitability assessment
- Conflict of interest checks
- Regulatory compliance verification
- Ethical guidelines enforcement
"""

import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ComplianceStandard(Enum):
    """Enum for international compliance standards"""
    MIFID_II = "MiFID II"
    GDPR = "GDPR"
    FCA = "FCA Principles"
    GCAP = "GCap Markets Values"

class RiskTolerance(Enum):
    """Enum for client risk tolerance levels"""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class ClientProfile:
    """Class representing a client profile for suitability assessment"""
    
    def __init__(
        self,
        client_id: str,
        risk_tolerance: RiskTolerance,
        investment_goals: List[str],
        financial_situation: Dict[str, float],
        ethical_preferences: List[str]
    ):
        self.client_id = client_id
        self.risk_tolerance = risk_tolerance
        self.investment_goals = investment_goals
        self.financial_situation = financial_situation
        self.ethical_preferences = ethical_preferences
        self.last_updated = datetime.now()

    def to_dict(self) -> Dict:
        """Convert client profile to dictionary for serialization"""
        return {
            "client_id": self.client_id,
            "risk_tolerance": self.risk_tolerance.name,
            "investment_goals": self.investment_goals,
            "financial_situation": self.financial_situation,
            "ethical_preferences": self.ethical_preferences,
            "last_updated": self.last_updated.isoformat()
        }

class EthicalConsultingModel:
    """Main class for ethical financial consulting compliance checks"""
    
    def __init__(self, standards: List[ComplianceStandard]):
        self.standards = standards
        self.client_profiles: Dict[str, ClientProfile] = {}
        self.conflicts_of_interest: Dict[str, List[str]] = {}
        
        # Load default ethical guidelines
        self.ethical_guidelines = self._load_default_guidelines()
        
    def _load_default_guidelines(self) -> Dict:
        """Load default ethical guidelines based on GCap Markets values"""
        return {
            "transparency": "Full disclosure of all fees and conflicts",
            "fairness": "Equal treatment of all clients",
            "sustainability": "Promotion of sustainable investments",
            "compliance": "Adherence to all regulatory requirements"
        }
    
    def add_client_profile(self, profile: ClientProfile) -> bool:
        """Add a new client profile after validation"""
        if not self._validate_client_profile(profile):
            logger.error(f"Invalid profile for client {profile.client_id}")
            return False
            
        self.client_profiles[profile.client_id] = profile
        logger.info(f"Added profile for client {profile.client_id}")
        return True
    
    def _validate_client_profile(self, profile: ClientProfile) -> bool:
        """Validate client profile data"""
        if not profile.client_id:
            return False
        if not isinstance(profile.risk_tolerance, RiskTolerance):
            return False
        if not all(isinstance(goal, str) for goal in profile.investment_goals):
            return False
        return True
    
    def check_suitability(
        self,
        client_id: str,
        investment_product: Dict[str, any]
    ) -> Tuple[bool, List[str]]:
        """
        Check if an investment product is suitable for a client
        Returns tuple of (is_suitable, reasons)
        """
        if client_id not in self.client_profiles:
            raise ValueError(f"Client {client_id} not found")
            
        profile = self.client_profiles[client_id]
        reasons = []
        is_suitable = True
        
        # Risk tolerance check
        product_risk = investment_product.get("risk_level")
        if product_risk and product_risk > profile.risk_tolerance.value:
            reasons.append(f"Product risk ({product_risk}) exceeds client tolerance ({profile.risk_tolerance.value})")
            is_suitable = False
            
        # Ethical preferences check
        product_categories = investment_product.get("categories", [])
        client_avoidances = [p for p in profile.ethical_preferences if p.startswith("avoid:")]
        
        for avoidance in client_avoidances:
            category = avoidance.split(":")[1]
            if category in product_categories:
                reasons.append(f"Product conflicts with client's ethical preference to avoid {category}")
                is_suitable = False
                
        return (is_suitable, reasons)
    
    def record_conflict_of_interest(
        self,
        consultant_id: str,
        conflicting_entity: str,
        nature: str
    ) -> bool:
        """Record a conflict of interest for a consultant"""
        if consultant_id not in self.conflicts_of_interest:
            self.conflicts_of_interest[consultant_id] = []
            
        conflict_record = {
            "entity": conflicting_entity,
            "nature": nature,
            "recorded_date": datetime.now().isoformat()
        }
        
        self.conflicts_of_interest[consultant_id].append(conflict_record)
        logger.info(f"Recorded conflict for consultant {consultant_id} with {conflicting_entity}")
        return True
    
    def check_conflicts(
        self,
        consultant_id: str,
        client_id: str,
        product_id: str
    ) -> Tuple[bool, List[Dict]]:
        """
        Check for conflicts of interest
        Returns tuple of (has_conflicts, conflicts_found)
        """
        conflicts = self.conflicts_of_interest.get(consultant_id, [])
        relevant_conflicts = []
        
        for conflict in conflicts:
            if (conflict["entity"] == client_id or 
                conflict["entity"] == product_id):
                relevant_conflicts.append(conflict)
                
        return (len(relevant_conflicts) > 0, relevant_conflicts)
    
    def generate_compliance_report(self, client_id: str) -> Dict:
        """Generate a compliance report for a client engagement"""
        if client_id not in self.client_profiles:
            raise ValueError(f"Client {client_id} not found")
            
        profile = self.client_profiles[client_id]
        
        return {
            "client_id": client_id,
            "standards_applied": [standard.value for standard in self.standards],
            "profile_summary": {
                "risk_tolerance": profile.risk_tolerance.name,
                "investment_goals": profile.investment_goals,
                "ethical_preferences": profile.ethical_preferences
            },
            "compliance_checks": {
                "profile_valid": self._validate_client_profile(profile),
                "last_updated": profile.last_updated.isoformat(),
                "guidelines_adhered": list(self.ethical_guidelines.keys())
            },
            "report_generated": datetime.now().isoformat()
        }
    
    def save_to_json(self, file_path: str) -> bool:
        """Save current state to JSON file"""
        try:
            data = {
                "client_profiles": {cid: prof.to_dict() for cid, prof in self.client_profiles.items()},
                "conflicts_of_interest": self.conflicts_of_interest,
                "standards": [standard.value for standard in self.standards]
            }
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
                
            logger.info(f"Saved data to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            return False
    
    @classmethod
    def load_from_json(cls, file_path: str) -> Optional['EthicalConsultingModel']:
        """Load state from JSON file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            standards = [ComplianceStandard(standard) for standard in data["standards"]]
            model = cls(standards)
            
            for cid, profile_data in data["client_profiles"].items():
                profile = ClientProfile(
                    client_id=cid,
                    risk_tolerance=RiskTolerance[profile_data["risk_tolerance"]],
                    investment_goals=profile_data["investment_goals"],
                    financial_situation=profile_data["financial_situation"],
                    ethical_preferences=profile_data["ethical_preferences"]
                )
                model.client_profiles[cid] = profile
                
            model.conflicts_of_interest = data["conflicts_of_interest"]
            logger.info(f"Loaded data from {file_path}")
            return model
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            return None

# Example usage
