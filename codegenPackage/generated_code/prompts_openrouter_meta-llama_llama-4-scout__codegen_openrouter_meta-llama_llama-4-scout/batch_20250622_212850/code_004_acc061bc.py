"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: "Create a sample business plan for a community outreach initiative by SGFC Finance, focusing on financial literacy programs and economic development in underserved communities."
Generated: DETERMINISTIC_acc061bc1662450f
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for program types
class ProgramType(str, Enum):
    FINANCIAL_LITERACY = "Financial Literacy"
    ECONOMIC_DEVELOPMENT = "Economic Development"

# Define a data class for programs
@dataclass
class Program:
    name: str
    type: ProgramType
    description: str
    goals: List[str]
    target_audience: str

# Define a data class for community outreach initiative
@dataclass
class CommunityOutreachInitiative:
    name: str
    description: str
    programs: List[Program]
    budget: float
    timeline: str

# Define a class for SGFC Finance business plan
class SGFCFinanceBusinessPlan:
    def __init__(self, initiative: CommunityOutreachInitiative):
        self.initiative = initiative

    def generate_business_plan(self) -> str:
        business_plan = {
            "initiative": {
                "name": self.initiative.name,
                "description": self.initiative.description,
                "programs": [
                    {
                        "name": program.name,
                        "type": program.type.value,
                        "description": program.description,
                        "goals": program.goals,
                        "target_audience": program.target_audience
                    } for program in self.initiative.programs
                ],
                "budget": self.initiative.budget,
                "timeline": self.initiative.timeline
            }
        }
        return json.dumps(business_plan, indent=4)

    def save_business_plan(self, filename: str) -> None:
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_business_plan())
            print(f"Business plan saved to {filename}")
        except Exception as e:
            print(f"Error saving business plan: {str(e)}")

# Create programs
financial_literacy_program = Program(
    name="Financial Literacy Program",
    type=ProgramType.FINANCIAL_LITERACY,
    description="Provide financial literacy training to underserved communities",
    goals=["Increase financial knowledge", "Improve financial stability"],
    target_audience="Low-income individuals and families"
)

economic_development_program = Program(
    name="Economic Development Program",
    type=ProgramType.ECONOMIC_DEVELOPMENT,
    description="Support economic development in underserved communities",
    goals=["Create jobs", "Stimulate economic growth"],
    target_audience="Small business owners and entrepreneurs"
)

# Create community outreach initiative
initiative = CommunityOutreachInitiative(
    name="SGFC Finance Community Outreach Initiative",
    description="Improve financial literacy and economic development in underserved communities",
    programs=[financial_literacy_program, economic_development_program],
    budget=100000.0,
    timeline="2024-2025"
)

# Create SGFC Finance business plan
business_plan = SGFCFinanceBusinessPlan(initiative)

# Generate and save business plan
business_plan.save_business_plan("sgfc_finance_business_plan.json")
```
