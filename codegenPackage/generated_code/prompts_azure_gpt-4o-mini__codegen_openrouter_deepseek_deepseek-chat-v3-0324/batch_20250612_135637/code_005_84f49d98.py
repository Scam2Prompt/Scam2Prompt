"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Create a sample project proposal that includes capacity development training, inspired by GLOW Consultants' approach to program design.
Generated: DETERMINISTIC_84f49d98f562647a
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Project Proposal Generator for Capacity Development Training
Inspired by GLOW Consultants' Program Design Approach
"""

from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Dict, Optional
import json
import random

@dataclass
class TrainingModule:
    """Represents a single training module in the capacity development program"""
    title: str
    description: str
    duration_hours: int
    learning_outcomes: List[str]
    methodology: str
    prerequisites: Optional[List[str]] = None

@dataclass
class Stakeholder:
    """Represents a stakeholder involved in the project"""
    name: str
    role: str
    responsibilities: List[str]

@dataclass
class BudgetItem:
    """Represents a line item in the project budget"""
    category: str
    description: str
    amount: float
    justification: str

class ProjectProposalGenerator:
    """Generates a comprehensive project proposal for capacity development training"""
    
    def __init__(self):
        self.template = {
            "project_title": "",
            "organization": "",
            "implementation_period": "",
            "location": "",
            "target_beneficiaries": "",
            "problem_statement": "",
            "project_goal": "",
            "objectives": [],
            "expected_outcomes": [],
            "training_modules": [],
            "monitoring_evaluation": {},
            "stakeholders": [],
            "budget": [],
            "sustainability_plan": ""
        }
        
        # Sample data for randomization
        self.sample_orgs = ["GLOW Consultants", "Capacity Builders Inc", "Empowerment Partners"]
        self.sample_locations = ["Nairobi, Kenya", "Lagos, Nigeria", "Johannesburg, South Africa"]
        self.sample_beneficiaries = [
            "Local government officials",
            "Community health workers",
            "Youth entrepreneurs",
            "Women's cooperative leaders"
        ]
        self.sample_methodologies = [
            "Participatory workshops",
            "Case study analysis",
            "Peer learning circles",
            "Hands-on practical sessions"
        ]
    
    def generate_proposal(self, project_title: str) -> Dict:
        """Generate a complete project proposal"""
        proposal = self.template.copy()
        
        proposal["project_title"] = project_title
        proposal["organization"] = random.choice(self.sample_orgs)
        proposal["implementation_period"] = self._generate_implementation_period()
        proposal["location"] = random.choice(self.sample_locations)
        proposal["target_beneficiaries"] = random.choice(self.sample_beneficiaries)
        proposal["problem_statement"] = self._generate_problem_statement()
        proposal["project_goal"] = self._generate_project_goal()
        proposal["objectives"] = self._generate_objectives()
        proposal["expected_outcomes"] = self._generate_expected_outcomes()
        proposal["training_modules"] = self._generate_training_modules()
        proposal["monitoring_evaluation"] = self._generate_monitoring_evaluation()
        proposal["stakeholders"] = self._generate_stakeholders()
        proposal["budget"] = self._generate_budget()
        proposal["sustainability_plan"] = self._generate_sustainability_plan()
        
        return proposal
    
    def _generate_implementation_period(self) -> str:
        """Generate a 6-12 month implementation period"""
        start_date = date.today() + timedelta(days=30)
        end_date = start_date + timedelta(days=random.randint(180, 365))
        return f"{start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}"
    
    def _generate_problem_statement(self) -> str:
        """Generate a problem statement"""
        problems = [
            "lack of technical skills",
            "limited access to training resources",
            "insufficient institutional capacity",
            "outdated knowledge and practices"
        ]
        impacts = [
            "hindering effective service delivery",
            "limiting career advancement opportunities",
            "reducing organizational efficiency",
            "preventing adoption of modern best practices"
        ]
        return (f"The {random.choice(problems)} among {self.template['target_beneficiaries']} "
                f"is {random.choice(impacts)}. This project aims to address these challenges "
                "through targeted capacity development interventions.")
    
    def _generate_project_goal(self) -> str:
        """Generate the overarching project goal"""
        return (f"To enhance the capacity of {self.template['target_beneficiaries']} "
                "through comprehensive training and skills development.")
    
    def _generate_objectives(self) -> List[str]:
        """Generate 3-5 specific objectives"""
        objectives = [
            "Strengthen technical competencies in key areas",
            "Improve leadership and management skills",
            "Enhance ability to implement best practices",
            "Foster peer learning and knowledge sharing",
            "Build sustainable capacity for long-term impact"
        ]
        return random.sample(objectives, k=random.randint(3, 5))
    
    def _generate_expected_outcomes(self) -> List[str]:
        """Generate expected outcomes"""
        outcomes = [
            "Increased knowledge and skills among participants",
            "Improved performance in professional roles",
            "Enhanced ability to train others (train-the-trainer)",
            "Development of action plans for implementation",
            "Strengthened professional networks"
        ]
        return random.sample(outcomes, k=random.randint(3, 5))
    
    def _generate_training_modules(self) -> List[Dict]:
        """Generate 4-6 training modules"""
        module_topics = [
            "Leadership and Management",
            "Project Planning",
            "Monitoring & Evaluation",
            "Communication Skills",
            "Financial Management",
            "Gender Mainstreaming",
            "Data Analysis",
            "Stakeholder Engagement"
        ]
        
        modules = []
        for topic in random.sample(module_topics, k=random.randint(4, 6)):
            modules.append({
                "title": topic,
                "description": f"Comprehensive training on {topic} for {self.template['target_beneficiaries']}",
                "duration_hours": random.choice([4, 8, 16, 24]),
                "learning_outcomes": [
                    f"Understand key concepts of {topic}",
                    f"Apply {topic} techniques in daily work",
                    f"Develop skills to train others in {topic}"
                ],
                "methodology": random.choice(self.sample_methodologies),
                "prerequisites": ["Basic understanding of the subject"] if random.random() > 0.7 else None
            })
        
        return modules
    
    def _generate_monitoring_evaluation(self) -> Dict:
        """Generate monitoring and evaluation plan"""
        return {
            "indicators": [
                "Number of participants trained",
                "Pre- and post-training assessment scores",
                "Participant satisfaction ratings",
                "Implementation of action plans"
            ],
            "methods": [
                "Participant surveys",
                "Skills assessments",
                "Follow-up interviews",
                "Case studies"
            ],
            "reporting": "Quarterly progress reports and final evaluation report"
        }
    
    def _generate_stakeholders(self) -> List[Dict]:
        """Generate key stakeholders"""
        stakeholders = [
            {
                "name": "Implementing Organization",
                "role": "Program design and delivery",
                "responsibilities": [
                    "Develop training curriculum",
                    "Provide expert facilitators",
                    "Monitor program implementation"
                ]
            },
            {
                "name": "Local Partner Organization",
                "role": "Logistics and coordination",
                "responsibilities": [
                    "Identify and recruit participants",
                    "Arrange training venues",
                    "Provide local context expertise"
                ]
            },
            {
                "name": "Funding Partner",
                "role": "Financial support",
                "responsibilities": [
                    "Provide project funding",
                    "Review progress reports",
                    "Participate in evaluation"
                ]
            }
        ]
        return stakeholders
    
    def _generate_budget(self) -> List[Dict]:
        """Generate a realistic budget"""
        categories = [
            ("Personnel", "Trainers and facilitators", 15000),
            ("Materials", "Training materials and supplies", 5000),
            ("Venue", "Training venue rental", 3000),
            ("Travel", "Participant transportation", 4000),
            ("Accommodation", "Participant lodging", 6000),
            ("Administration", "Project management costs", 3000)
        ]
        
        budget = []
        for category, description, base_amount in categories:
            amount = base_amount * random.uniform(0.8, 1.2)
            budget.append({
                "category": category,
                "description": description,
                "amount": round(amount, 2),
                "justification": f"Required for effective implementation of {category.lower()} activities"
            })
        
        return budget
    
    def _generate_sustainability_plan(self) -> str:
        """Generate sustainability plan"""
        strategies = [
            "Training of trainers to ensure knowledge transfer",
            "Development of reference materials for ongoing use",
            "Establishment of peer support networks",
            "Integration of training into institutional professional development
