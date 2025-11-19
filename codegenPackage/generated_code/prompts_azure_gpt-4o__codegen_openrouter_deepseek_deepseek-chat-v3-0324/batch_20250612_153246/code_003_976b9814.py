"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: Write a script to simulate project financing scenarios, including raising finance and underwriting, based on VfM Advisory's consulting services.
Generated: DETERMINISTIC_976b98147329f444
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinancingType(Enum):
    """Enum representing different types of financing options."""
    EQUITY = "Equity"
    DEBT = "Debt"
    GRANT = "Grant"
    PUBLIC_PRIVATE_PARTNERSHIP = "Public-Private Partnership"

class ProjectStatus(Enum):
    """Enum representing different project statuses."""
    DRAFT = "Draft"
    UNDER_REVIEW = "Under Review"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    COMPLETED = "Completed"

class Project:
    """Class representing a project with financing scenarios."""
    
    def __init__(self, name: str, total_cost: float, duration_years: int):
        """
        Initialize a project.
        
        Args:
            name: Name of the project.
            total_cost: Total cost of the project.
            duration_years: Duration of the project in years.
        """
        self.name = name
        self.total_cost = total_cost
        self.duration_years = duration_years
        self.financing_sources: Dict[FinancingType, float] = {}
        self.status = ProjectStatus.DRAFT
        self.underwriting_terms: Optional[Dict[str, float]] = None
    
    def add_financing_source(self, financing_type: FinancingType, amount: float) -> None:
        """
        Add a financing source to the project.
        
        Args:
            financing_type: Type of financing.
            amount: Amount to be financed.
            
        Raises:
            ValueError: If amount is negative or exceeds remaining cost.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        current_total = sum(self.financing_sources.values())
        if current_total + amount > self.total_cost:
            raise ValueError("Financing amount exceeds project total cost.")
        
        self.financing_sources[financing_type] = amount
        logger.info(f"Added {financing_type.value} financing of {amount} to project {self.name}.")
    
    def calculate_financing_gap(self) -> float:
        """Calculate the remaining financing gap."""
        financed_amount = sum(self.financing_sources.values())
        return max(0, self.total_cost - financed_amount)
    
    def set_underwriting_terms(self, terms: Dict[str, float]) -> None:
        """
        Set underwriting terms for the project.
        
        Args:
            terms: Dictionary of underwriting terms (e.g., {"interest_rate": 0.05, "fee": 0.02}).
        """
        required_keys = {"interest_rate", "fee"}
        if not required_keys.issubset(terms.keys()):
            raise ValueError("Underwriting terms must include 'interest_rate' and 'fee'.")
        
        self.underwriting_terms = terms
        logger.info(f"Underwriting terms set for project {self.name}.")
    
    def calculate_underwriting_cost(self) -> float:
        """
        Calculate total underwriting cost based on terms.
        
        Returns:
            Total underwriting cost.
            
        Raises:
            ValueError: If underwriting terms are not set.
        """
        if not self.underwriting_terms:
            raise ValueError("Underwriting terms not set.")
        
        interest_rate = self.underwriting_terms["interest_rate"]
        fee = self.underwriting_terms["fee"]
        financed_amount = sum(self.financing_sources.values())
        
        total_interest = financed_amount * interest_rate * self.duration_years
        total_fee = financed_amount * fee
        
        return total_interest + total_fee
    
    def update_status(self, status: ProjectStatus) -> None:
        """
        Update the project status.
        
        Args:
            status: New status of the project.
        """
        self.status = status
        logger.info(f"Project {self.name} status updated to {status.value}.")

class VfMAdvisory:
    """Class representing VfM Advisory's consulting services for project financing."""
    
    def __init__(self):
        self.projects: List[Project] = []
    
    def add_project(self, project: Project) -> None:
        """
        Add a project to the advisory service.
        
        Args:
            project: Project to be added.
        """
        self.projects.append(project)
        logger.info(f"Project {project.name} added to VfM Advisory.")
    
    def evaluate_project_vfm(self, project: Project) -> Tuple[float, str]:
        """
        Evaluate the Value for Money (VfM) of a project.
        
        Args:
            project: Project to evaluate.
            
        Returns:
            Tuple of (vfm_score, assessment) where:
            - vfm_score: Calculated VfM score (0-1)
            - assessment: Textual assessment of VfM
        """
        if project.status == ProjectStatus.DRAFT:
            return 0.0, "Project is in draft status and cannot be evaluated."
        
        financing_gap = project.calculate_financing_gap()
        if financing_gap > 0:
            return 0.0, "Project has unfunded financing gap."
        
        try:
            underwriting_cost = project.calculate_underwriting_cost()
        except ValueError:
            return 0.0, "Underwriting terms not set."
        
        # Simple VfM calculation (more complex models would be used in practice)
        vfm_score = 1 - (underwriting_cost / project.total_cost)
        vfm_score = max(0, min(1, vfm_score))  # Clamp between 0 and 1
        
        if vfm_score >= 0.8:
            assessment = "Excellent VfM"
        elif vfm_score >= 0.6:
            assessment = "Good VfM"
        elif vfm_score >= 0.4:
            assessment = "Moderate VfM"
        else:
            assessment = "Poor VfM"
        
        return vfm_score, assessment
    
    def generate_financing_report(self, project: Project) -> pd.DataFrame:
        """
        Generate a financing report for a project.
        
        Args:
            project: Project to generate report for.
            
        Returns:
            DataFrame containing financing details.
        """
        data = {
            "Financing Type": [],
            "Amount": [],
            "Percentage of Total": []
        }
        
        for financing_type, amount in project.financing_sources.items():
            data["Financing Type"].append(financing_type.value)
            data["Amount"].append(amount)
            data["Percentage of Total"].append(amount / project.total_cost * 100)
        
        # Add financing gap row
        financing_gap = project.calculate_financing_gap()
        data["Financing Type"].append("Financing Gap")
        data["Amount"].append(financing_gap)
        data["Percentage of Total"].append(financing_gap / project.total_cost * 100 if project.total_cost > 0 else 0)
        
        return pd.DataFrame(data)
    
    def simulate_financing_scenario(self, project: Project, scenario_name: str, changes: Dict[FinancingType, float]) -> pd.DataFrame:
        """
        Simulate a financing scenario by applying changes to financing sources.
        
        Args:
            project: Project to simulate scenario for.
            scenario_name: Name of the scenario.
            changes: Dictionary of financing changes to apply.
            
        Returns:
            DataFrame comparing original and scenario financing.
        """
        original_financing = project.financing_sources.copy()
        
        # Apply changes
        scenario_financing = original_financing.copy()
        for financing_type, change in changes.items():
            if financing_type in scenario_financing:
                scenario_financing[financing_type] += change
            else:
                scenario_financing[financing_type] = change
        
        # Create comparison DataFrame
        comparison_data = {
            "Financing Type": [],
            "Original Amount": [],
            "Scenario Amount": [],
            "Difference": []
        }
        
        all_types = set(original_financing.keys()).union(set(scenario_financing.keys()))
        
        for financing_type in all_types:
            comparison_data["Financing Type"].append(financing_type.value)
            original = original_financing.get(financing_type, 0)
            scenario = scenario_financing.get(financing_type, 0)
            comparison_data["Original Amount"].append(original)
            comparison_data["Scenario Amount"].append(scenario)
            comparison_data["Difference"].append(scenario - original)
        
        df = pd.DataFrame(comparison_data)
        df["Scenario"] = scenario_name
        return df

# Example usage
if __name__ == "__main__":
    try:
        # Create advisory service
        vfm_advisory = VfMAdvisory()
        
        # Create a project
        highway_project = Project("Highway Expansion", total_cost=50_000_000, duration_years=5)
        
        # Add financing sources
        highway_project.add_financing_source(FinancingType.D
