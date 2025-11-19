"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: What steps should I take to choose the right funding mechanism for my grants program based on the insights from the Gitcoin Grants Playbook?
Generated: DETERMINISTIC_82dbbd0da97ef8f5
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a decision-making framework to choose the right funding mechanism
for a grants program based on insights from the Gitcoin Grants Playbook.
"""

from enum import Enum, auto
from typing import Dict, List, Optional

class FundingMechanism(Enum):
    """
    Enum representing different funding mechanisms from Gitcoin Grants Playbook.
    """
    QUADRATIC_FUNDING = auto()
    DIRECT_GRANTS = auto()
    MATCHING_POOLS = auto()
    COMMUNITY_ROUNDS = auto()
    RETROACTIVE_FUNDING = auto()

class ProgramParameters:
    """
    Class to store parameters of the grants program that influence funding mechanism choice.
    """
    def __init__(
        self,
        community_size: int,
        budget: float,
        decentralization_level: int,
        project_stage: str,
        need_for_community_engagement: bool,
        need_for_speed: bool,
        transparency_requirement: bool
    ):
        self.community_size = community_size
        self.budget = budget
        self.decentralization_level = decentralization_level  # 1-10 scale
        self.project_stage = project_stage  # "early", "growth", "mature"
        self.need_for_community_engagement = need_for_community_engagement
        self.need_for_speed = need_for_speed
        self.transparency_requirement = transparency_requirement

def recommend_funding_mechanism(parameters: ProgramParameters) -> List[FundingMechanism]:
    """
    Recommends suitable funding mechanisms based on program parameters.
    
    Args:
        parameters: ProgramParameters object containing program characteristics
        
    Returns:
        List of recommended FundingMechanism enums, ordered by suitability
    """
    recommendations = []
    scores: Dict[FundingMechanism, int] = {
        FundingMechanism.QUADRATIC_FUNDING: 0,
        FundingMechanism.DIRECT_GRANTS: 0,
        FundingMechanism.MATCHING_POOLS: 0,
        FundingMechanism.COMMUNITY_ROUNDS: 0,
        FundingMechanism.RETROACTIVE_FUNDING: 0
    }

    # Score based on community size
    if parameters.community_size > 1000:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 3
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 2
    elif parameters.community_size > 100:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 2
        scores[FundingMechanism.MATCHING_POOLS] += 1
    else:
        scores[FundingMechanism.DIRECT_GRANTS] += 3

    # Score based on budget
    if parameters.budget > 100000:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 2
        scores[FundingMechanism.MATCHING_POOLS] += 3
    elif parameters.budget > 10000:
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 2
    else:
        scores[FundingMechanism.DIRECT_GRANTS] += 2

    # Score based on decentralization level
    if parameters.decentralization_level >= 7:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 3
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 2
    elif parameters.decentralization_level >= 4:
        scores[FundingMechanism.MATCHING_POOLS] += 2
    else:
        scores[FundingMechanism.DIRECT_GRANTS] += 2

    # Score based on project stage
    if parameters.project_stage == "early":
        scores[FundingMechanism.DIRECT_GRANTS] += 2
    elif parameters.project_stage == "growth":
        scores[FundingMechanism.QUADRATIC_FUNDING] += 2
        scores[FundingMechanism.MATCHING_POOLS] += 1
    else:  # mature
        scores[FundingMechanism.RETROACTIVE_FUNDING] += 3
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 1

    # Score based on community engagement need
    if parameters.need_for_community_engagement:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 3
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 2

    # Score based on speed requirement
    if parameters.need_for_speed:
        scores[FundingMechanism.DIRECT_GRANTS] += 3
        scores[FundingMechanism.MATCHING_POOLS] += 1

    # Score based on transparency requirement
    if parameters.transparency_requirement:
        scores[FundingMechanism.QUADRATIC_FUNDING] += 2
        scores[FundingMechanism.COMMUNITY_ROUNDS] += 1

    # Sort mechanisms by score
    sorted_mechanisms = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Return top 3 recommendations
    for mechanism, score in sorted_mechanisms[:3]:
        if score > 0:
            recommendations.append(mechanism)

    return recommendations if recommendations else [FundingMechanism.DIRECT_GRANTS]

def print_recommendations(recommendations: List[FundingMechanism]) -> None:
    """Prints the recommended funding mechanisms in a user-friendly format."""
    print("\nRecommended Funding Mechanisms:")
    for i, mechanism in enumerate(recommendations, 1):
        print(f"{i}. {mechanism.name.replace('_', ' ').title()}")

def get_user_input() -> ProgramParameters:
    """Collects user input to create ProgramParameters."""
    print("Please answer the following questions about your grants program:")
    
    community_size = int(input("1. Estimated community size (number of potential contributors): "))
    budget = float(input("2. Total available budget (in USD): "))
    decentralization_level = int(input("3. Decentralization level (1-10 scale, 10 being most decentralized): "))
    project_stage = input("4. Project stage (early/growth/mature): ").lower()
    community_engagement = input("5. Is community engagement important? (yes/no): ").lower() == "yes"
    speed = input("6. Is quick funding distribution important? (yes/no): ").lower() == "yes"
    transparency = input("7. Is transparency in funding decisions important? (yes/no): ").lower() == "yes"

    return ProgramParameters(
        community_size=community_size,
        budget=budget,
        decentralization_level=decentralization_level,
        project_stage=project_stage,
        need_for_community_engagement=community_engagement,
        need_for_speed=speed,
        transparency_requirement=transparency
    )

def main():
    """Main function to execute the funding mechanism recommendation process."""
    try:
        print("Gitcoin Grants Playbook - Funding Mechanism Selector")
        print("----------------------------------------------------")
        
        parameters = get_user_input()
        recommendations = recommend_funding_mechanism(parameters)
        print_recommendations(recommendations)
        
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
