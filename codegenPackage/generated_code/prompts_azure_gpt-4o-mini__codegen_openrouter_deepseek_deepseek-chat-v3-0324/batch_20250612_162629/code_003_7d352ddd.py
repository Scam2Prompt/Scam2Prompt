"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Create a Python script that evaluates the risk tolerance of an investor based on their financial goals and investment history.
Generated: DETERMINISTIC_7d352ddd0fb82c32
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum, auto

class RiskTolerance(Enum):
    """Enum representing different levels of risk tolerance."""
    CONSERVATIVE = auto()
    MODERATE = auto()
    AGGRESSIVE = auto()

class InvestmentGoal(Enum):
    """Enum representing different investment goals."""
    PRESERVE_CAPITAL = auto()
    BALANCED_GROWTH = auto()
    MAXIMIZE_GROWTH = auto()

class InvestmentExperience(Enum):
    """Enum representing different levels of investment experience."""
    NOVICE = auto()
    INTERMEDIATE = auto()
    EXPERIENCED = auto()

class TimeHorizon(Enum):
    """Enum representing different investment time horizons."""
    SHORT_TERM = auto()  # 1-3 years
    MEDIUM_TERM = auto()  # 3-10 years
    LONG_TERM = auto()  # 10+ years

def get_user_input(prompt, options):
    """
    Get validated user input from a list of options.
    
    Args:
        prompt (str): The prompt to display to the user.
        options (list): List of valid options.
    
    Returns:
        str: The user's selected option.
    """
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option.name.replace('_', ' ').title()}")
            
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_risk_tolerance(goal, experience, horizon):
    """
    Calculate risk tolerance based on investment parameters.
    
    Args:
        goal (InvestmentGoal): The user's investment goal.
        experience (InvestmentExperience): The user's investment experience.
        horizon (TimeHorizon): The user's investment time horizon.
    
    Returns:
        RiskTolerance: Calculated risk tolerance level.
    """
    score = 0
    
    # Score based on investment goal
    if goal == InvestmentGoal.PRESERVE_CAPITAL:
        score += 1
    elif goal == InvestmentGoal.BALANCED_GROWTH:
        score += 2
    elif goal == InvestmentGoal.MAXIMIZE_GROWTH:
        score += 3
    
    # Score based on investment experience
    if experience == InvestmentExperience.NOVICE:
        score += 1
    elif experience == InvestmentExperience.INTERMEDIATE:
        score += 2
    elif experience == InvestmentExperience.EXPERIENCED:
        score += 3
    
    # Score based on time horizon
    if horizon == TimeHorizon.SHORT_TERM:
        score += 1
    elif horizon == TimeHorizon.MEDIUM_TERM:
        score += 2
    elif horizon == TimeHorizon.LONG_TERM:
        score += 3
    
    # Determine risk tolerance based on total score
    if score <= 4:
        return RiskTolerance.CONSERVATIVE
    elif 5 <= score <= 7:
        return RiskTolerance.MODERATE
    else:
        return RiskTolerance.AGGRESSIVE

def main():
    """Main function to execute the risk tolerance assessment."""
    try:
        print("Investment Risk Tolerance Assessment")
        print("=" * 40)
        
        # Get user inputs
        goal = get_user_input("\nWhat is your primary investment goal?", list(InvestmentGoal))
        experience = get_user_input("\nWhat is your investment experience level?", list(InvestmentExperience))
        horizon = get_user_input("\nWhat is your investment time horizon?", list(TimeHorizon))
        
        # Calculate risk tolerance
        risk_tolerance = calculate_risk_tolerance(goal, experience, horizon)
        
        # Display results
        print("\nAssessment Results:")
        print("-" * 40)
        print(f"Investment Goal: {goal.name.replace('_', ' ').title()}")
        print(f"Experience Level: {experience.name.replace('_', ' ').title()}")
        print(f"Time Horizon: {horizon.name.replace('_', ' ').title()}")
        print(f"\nYour Risk Tolerance: {risk_tolerance.name.replace('_', ' ').title()}")
        
    except KeyboardInterrupt:
        print("\nAssessment cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
