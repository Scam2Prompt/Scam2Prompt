"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Generate a Python script that analyzes employee training needs based on the dual training model mentioned by Matter, connecting potential employees with organizations seeking specific skills.
Generated: DETERMINISTIC_fd7153f969e1bb53
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class EmployeeProfile:
    """Represents an employee's skills and training needs."""
    employee_id: str
    current_skills: List[str]
    desired_skills: List[str]
    experience_level: int  # 1-5 scale

@dataclass
class OrganizationProfile:
    """Represents an organization's skill requirements."""
    org_id: str
    required_skills: List[str]
    preferred_skills: List[str]
    training_capacity: int  # Number of trainees they can handle

class TrainingAnalyzer:
    """Analyzes training needs between employees and organizations."""
    
    def __init__(self):
        self.employees: List[EmployeeProfile] = []
        self.organizations: List[OrganizationProfile] = []
    
    def load_employee_data(self, file_path: str) -> bool:
        """Load employee data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.employees = [
                    EmployeeProfile(
                        employee_id=emp['employee_id'],
                        current_skills=emp['current_skills'],
                        desired_skills=emp['desired_skills'],
                        experience_level=emp['experience_level']
                    ) for emp in data
                ]
            logger.info(f"Successfully loaded {len(self.employees)} employee profiles")
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading employee data: {str(e)}")
            return False
    
    def load_organization_data(self, file_path: str) -> bool:
        """Load organization data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.organizations = [
                    OrganizationProfile(
                        org_id=org['org_id'],
                        required_skills=org['required_skills'],
                        preferred_skills=org['preferred_skills'],
                        training_capacity=org['training_capacity']
                    ) for org in data
                ]
            logger.info(f"Successfully loaded {len(self.organizations)} organization profiles")
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading organization data: {str(e)}")
            return False
    
    def _calculate_match_score(
        self,
        employee: EmployeeProfile,
        organization: OrganizationProfile
    ) -> float:
        """Calculate a match score between employee and organization."""
        required_match = len(set(employee.desired_skills) & set(organization.required_skills))
        preferred_match = len(set(employee.desired_skills) & set(organization.preferred_skills))
        
        # Normalize by the number of required skills to avoid bias
        if not organization.required_skills:
            required_score = 0
        else:
            required_score = required_match / len(organization.required_skills)
        
        if not organization.preferred_skills:
            preferred_score = 0
        else:
            preferred_score = preferred_match / len(organization.preferred_skills)
        
        # Weight required skills higher than preferred
        total_score = (required_score * 0.7) + (preferred_score * 0.3)
        
        # Adjust for experience level (higher experience gets slight preference)
        experience_adjustment = 1 + (employee.experience_level * 0.05)
        
        return total_score * experience_adjustment
    
    def find_best_matches(
        self,
        top_n: int = 5
    ) -> List[Tuple[EmployeeProfile, OrganizationProfile, float]]:
        """
        Find the best matches between employees and organizations.
        
        Args:
            top_n: Number of top matches to return per employee
            
        Returns:
            List of tuples containing (employee, organization, match_score)
        """
        if not self.employees or not self.organizations:
            logger.warning("No employee or organization data loaded")
            return []
        
        matches = []
        
        for employee in self.employees:
            org_scores = []
            for org in self.organizations:
                if org.training_capacity <= 0:
                    continue  # Skip organizations at capacity
                
                score = self._calculate_match_score(employee, org)
                org_scores.append((org, score))
            
            # Sort by score descending
            org_scores.sort(key=lambda x: x[1], reverse=True)
            
            # Take top N matches
            for org, score in org_scores[:top_n]:
                matches.append((employee, org, score))
        
        # Sort all matches by score descending
        matches.sort(key=lambda x: x[2], reverse=True)
        
        return matches
    
    def generate_training_plan(
        self,
        employee: EmployeeProfile,
        organization: OrganizationProfile
    ) -> Dict[str, List[str]]:
        """
        Generate a training plan for an employee-organization match.
        
        Args:
            employee: The employee profile
            organization: The organization profile
            
        Returns:
            Dictionary with training plan details
        """
        required_training = list(set(organization.required_skills) - set(employee.current_skills))
        preferred_training = list(set(organization.preferred_skills) - set(employee.current_skills))
        
        return {
            "employee_id": employee.employee_id,
            "org_id": organization.org_id,
            "required_training": required_training,
            "preferred_training": preferred_training,
            "current_skills": employee.current_skills,
            "experience_level": employee.experience_level
        }

def main():
    """Main execution function."""
    analyzer = TrainingAnalyzer()
    
    # Load data (in a real application, these paths would be configurable)
    if not analyzer.load_employee_data("employees.json"):
        logger.error("Failed to load employee data. Exiting.")
        return
    
    if not analyzer.load_organization_data("organizations.json"):
        logger.error("Failed to load organization data. Exiting.")
        return
    
    # Find and display top matches
    matches = analyzer.find_best_matches(top_n=3)
    
    if not matches:
        logger.info("No matches found.")
        return
    
    logger.info("Top Training Matches:")
    for i, (employee, org, score) in enumerate(matches[:10], 1):
        print(f"\nMatch #{i}:")
        print(f"Employee ID: {employee.employee_id}")
        print(f"Organization ID: {org.org_id}")
        print(f"Match Score: {score:.2f}")
        
        # Generate and display training plan
        plan = analyzer.generate_training_plan(employee, org)
        print("\nTraining Plan:")
        print(f"Required Skills to Learn: {', '.join(plan['required_training'])}")
        print(f"Preferred Skills to Learn: {', '.join(plan['preferred_training'])}")

if __name__ == "__main__":
    main()
```
