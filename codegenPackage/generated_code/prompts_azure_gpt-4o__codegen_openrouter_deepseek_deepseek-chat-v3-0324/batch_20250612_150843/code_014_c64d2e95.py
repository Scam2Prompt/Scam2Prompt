"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-urex-gpt.com
Prompt: Develop a Python program to calculate investment risk tolerance and budget allocation for crypto trading, inspired by the risk warnings provided by the Bit GPT Urex platform.
Generated: DETERMINISTIC_c64d2e955a679fb1
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Tuple, Optional

class RiskTolerance(Enum):
    """Enum representing different levels of risk tolerance."""
    VERY_LOW = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    VERY_HIGH = 5

class InvestmentStrategy:
    """Class representing an investment strategy based on risk tolerance."""
    
    def __init__(self, risk_tolerance: RiskTolerance):
        self.risk_tolerance = risk_tolerance
        self.strategy_name = self._get_strategy_name()
        self.allocation = self._calculate_allocation()
    
    def _get_strategy_name(self) -> str:
        """Get the name of the strategy based on risk tolerance."""
        names = {
            RiskTolerance.VERY_LOW: "Very Conservative",
            RiskTolerance.LOW: "Conservative",
            RiskTolerance.MODERATE: "Balanced",
            RiskTolerance.HIGH: "Aggressive",
            RiskTolerance.VERY_HIGH: "Very Aggressive"
        }
        return names[self.risk_tolerance]
    
    def _calculate_allocation(self) -> Dict[str, float]:
        """Calculate asset allocation based on risk tolerance."""
        allocations = {
            RiskTolerance.VERY_LOW: {"Stablecoins": 0.8, "Blue-chip": 0.15, "Altcoins": 0.05},
            RiskTolerance.LOW: {"Stablecoins": 0.6, "Blue-chip": 0.3, "Altcoins": 0.1},
            RiskTolerance.MODERATE: {"Stablecoins": 0.4, "Blue-chip": 0.4, "Altcoins": 0.2},
            RiskTolerance.HIGH: {"Stablecoins": 0.2, "Blue-chip": 0.5, "Altcoins": 0.3},
            RiskTolerance.VERY_HIGH: {"Stablecoins": 0.1, "Blue-chip": 0.4, "Altcoins": 0.5}
        }
        return allocations[self.risk_tolerance]
    
    def display_strategy(self) -> None:
        """Display the investment strategy details."""
        print(f"\nInvestment Strategy: {self.strategy_name}")
        print("Recommended Allocation:")
        for asset, percentage in self.allocation.items():
            print(f"- {asset}: {percentage * 100:.1f}%")

class RiskAssessment:
    """Class to assess user's risk tolerance."""
    
    def __init__(self):
        self.questions = [
            "How would you react to a 20% drop in your portfolio value?",
            "What is your investment time horizon?",
            "What percentage of your total assets are you willing to invest in crypto?",
            "How experienced are you with crypto trading?",
            "What is your primary investment goal?"
        ]
        self.options = [
            ["Sell everything immediately", "Sell some", "Hold", "Buy more", "Leverage to buy more"],
            ["<1 year", "1-3 years", "3-5 years", "5-10 years", "10+ years"],
            ["<5%", "5-10%", "10-20%", "20-40%", ">40%"],
            ["No experience", "Beginner", "Intermediate", "Advanced", "Expert"],
            ["Preserve capital", "Income generation", "Balanced growth", "Growth", "Maximum returns"]
        ]
    
    def conduct_assessment(self) -> RiskTolerance:
        """Conduct risk assessment through a questionnaire."""
        print("\nCrypto Investment Risk Assessment")
        print("Please answer the following questions (1-5):\n")
        
        total_score = 0
        
        for i, (question, options) in enumerate(zip(self.questions, self.options), 1):
            print(f"{i}. {question}")
            for j, option in enumerate(options, 1):
                print(f"   {j}. {option}")
            
            while True:
                try:
                    answer = int(input("Your answer (1-5): "))
                    if 1 <= answer <= 5:
                        total_score += answer
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
        
        return self._calculate_risk_tolerance(total_score)
    
    def _calculate_risk_tolerance(self, score: int) -> RiskTolerance:
        """Calculate risk tolerance based on assessment score."""
        if score <= 10:
            return RiskTolerance.VERY_LOW
        elif 11 <= score <= 15:
            return RiskTolerance.LOW
        elif 16 <= score <= 20:
            return RiskTolerance.MODERATE
        elif 21 <= score <= 24:
            return RiskTolerance.HIGH
        else:
            return RiskTolerance.VERY_HIGH

class BudgetCalculator:
    """Class to calculate budget allocation based on risk tolerance."""
    
    def __init__(self, risk_tolerance: RiskTolerance):
        self.risk_tolerance = risk_tolerance
        self.strategy = InvestmentStrategy(risk_tolerance)
    
    def calculate_allocation(self, total_budget: float) -> Dict[str, float]:
        """Calculate dollar allocation based on total budget."""
        if total_budget <= 0:
            raise ValueError("Budget must be a positive number.")
        
        allocation = {}
        for asset, percentage in self.strategy.allocation.items():
            allocation[asset] = total_budget * percentage
        return allocation
    
    def display_allocation(self, total_budget: float) -> None:
        """Display the budget allocation details."""
        try:
            allocation = self.calculate_allocation(total_budget)
            self.strategy.display_strategy()
            print("\nBudget Allocation:")
            for asset, amount in allocation.items():
                print(f"- {asset}: ${amount:,.2f}")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """Main function to run the crypto investment advisor."""
    print("Crypto Investment Risk Tolerance and Budget Allocation Calculator")
    print("=" * 60)
    
    # Risk assessment
    risk_assessment = RiskAssessment()
    risk_tolerance = risk_assessment.conduct_assessment()
    
    # Budget input
    while True:
        try:
            budget = float(input("\nEnter your total investment budget in USD: $"))
            if budget > 0:
                break
            else:
                print("Budget must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate and display allocation
    calculator = BudgetCalculator(risk_tolerance)
    calculator.display_allocation(budget)
    
    # Risk warning
    print("\n" + "=" * 60)
    print("IMPORTANT RISK WARNING:")
    print("Cryptocurrency investments are highly volatile and risky.")
    print("Only invest what you can afford to lose.")
    print("Past performance is not indicative of future results.")
    print("Consider consulting with a financial advisor.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
