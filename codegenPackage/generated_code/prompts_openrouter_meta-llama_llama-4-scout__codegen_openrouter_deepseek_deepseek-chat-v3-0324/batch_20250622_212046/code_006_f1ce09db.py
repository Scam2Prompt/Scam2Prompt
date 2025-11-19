"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: "Outline a plan for a Doge-themed documentary, including potential scripts, interviewees, and funding models through cryptocurrency or merchandise sales."
Generated: DETERMINISTIC_f1ce09dbc8e2599d
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# Doge Documentary Planner

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto

class FundingModel(Enum):
    CRYPTOCURRENCY = auto()
    MERCHANDISE = auto()
    CROWDFUNDING = auto()
    SPONSORS = auto()

@dataclass
class Interviewee:
    name: str
    role: str  # e.g., "Doge Meme Creator", "Cryptocurrency Expert"
    contact_info: Optional[str] = None
    confirmed: bool = False

@dataclass
class ScriptScene:
    title: str
    description: str
    duration_minutes: float
    interviewees: List[Interviewee] = field(default_factory=list)
    required_assets: List[str] = field(default_factory=list)  # e.g., "Doge meme history footage"

@dataclass
class BudgetItem:
    description: str
    cost: float
    priority: int  # 1-5 where 5 is highest priority

@dataclass
class DocumentaryPlan:
    title: str = "The Rise of Doge: From Meme to Movement"
    description: str = "A documentary exploring the cultural and financial impact of the Doge meme and cryptocurrency."
    target_runtime_minutes: float = 60.0
    scripts: List[ScriptScene] = field(default_factory=list)
    interviewees: List[Interviewee] = field(default_factory=list)
    funding_models: List[FundingModel] = field(default_factory=list)
    budget: List[BudgetItem] = field(default_factory=list)
    merchandise_ideas: List[str] = field(default_factory=list)

    def add_scene(self, scene: ScriptScene) -> None:
        """Add a scene to the documentary script."""
        self.scripts.append(scene)

    def add_interviewee(self, person: Interviewee) -> None:
        """Add a potential interviewee."""
        self.interviewees.append(person)

    def add_funding_model(self, model: FundingModel) -> None:
        """Add a funding model option."""
        if model not in self.funding_models:
            self.funding_models.append(model)

    def add_budget_item(self, item: BudgetItem) -> None:
        """Add a budget item."""
        self.budget.append(item)

    def add_merchandise_idea(self, idea: str) -> None:
        """Add a merchandise idea."""
        self.merchandise_ideas.append(idea)

    def to_json(self) -> str:
        """Serialize the documentary plan to JSON."""
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'DocumentaryPlan':
        """Deserialize a documentary plan from JSON."""
        data = json.loads(json_str)
        plan = cls()
        for key, value in data.items():
            if key == 'funding_models':
                setattr(plan, key, [FundingModel[model] for model in value])
            elif hasattr(plan, key):
                setattr(plan, key, value)
        return plan

def create_sample_plan() -> DocumentaryPlan:
    """Create a sample documentary plan with placeholder data."""
    plan = DocumentaryPlan()

    # Add funding models
    plan.add_funding_model(FundingModel.CRYPTOCURRENCY)
    plan.add_funding_model(FundingModel.MERCHANDISE)

    # Add interviewees
    plan.add_interviewee(Interviewee(
        name="Kabosu's Owner",
        role="Original Doge Dog Owner",
        confirmed=False
    ))
    plan.add_interviewee(Interviewee(
        name="Billy Markus",
        role="Co-creator of Dogecoin",
        confirmed=False
    ))

    # Add script scenes
    plan.add_scene(ScriptScene(
        title="Origins of the Meme",
        description="Explore how the Doge meme started and went viral",
        duration_minutes=10,
        required_assets=["Original Doge photos", "Early meme examples"]
    ))

    # Add budget items
    plan.add_budget_item(BudgetItem(
        description="Camera equipment rental",
        cost=5000,
        priority=5
    ))

    # Add merchandise ideas
    plan.add_merchandise_idea("Limited Edition Doge NFT Collection")
    plan.add_merchandise_idea("Doge Documentary T-shirts")

    return plan

if __name__ == "__main__":
    # Example usage
    try:
        plan = create_sample_plan()
        print("Sample Documentary Plan:")
        print(plan.to_json())

        # Save to file
        with open("doge_documentary_plan.json", "w") as f:
            f.write(plan.to_json())
        print("\nPlan saved to 'doge_documentary_plan.json'")

    except Exception as e:
        print(f"Error creating documentary plan: {e}")
```
