"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Write a Python script to analyze investment strategies (e.g., value investing, growth investing, momentum investing) and categorize users into suitable learning paths based on their risk tolerance.
Generated: DETERMINISTIC_c2c72f19a75058c3
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple

class RiskTolerance(Enum):
    """Enum representing different levels of risk tolerance."""
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class InvestmentStrategy(Enum):
    """Enum representing different investment strategies."""
    VALUE_INVESTING = "Value Investing"
    GROWTH_INVESTING = "Growth Investing"
    MOMENTUM_INVESTING = "Momentum Investing"
    INDEX_INVESTING = "Index Investing"
    DIVIDEND_INVESTING = "Dividend Investing"

class LearningPath:
    """Class representing a learning path for an investment strategy."""
    def __init__(self, strategy: InvestmentStrategy, resources: List[str]):
        self.strategy = strategy
        self.resources = resources

    def to_dict(self) -> Dict:
        """Convert the learning path to a dictionary."""
        return {
            "strategy": self.strategy.value,
            "resources": self.resources
        }

class InvestmentAnalyzer:
    """Class to analyze investment strategies and recommend learning paths."""
    def __init__(self):
        self._load_strategy_mappings()
        self._load_learning_paths()

    def _load_strategy_mappings(self) -> None:
        """Load the mapping between risk tolerance and recommended strategies."""
        self.strategy_mappings = {
            RiskTolerance.LOW: [
                InvestmentStrategy.INDEX_INVESTING,
                InvestmentStrategy.DIVIDEND_INVESTING
            ],
            RiskTolerance.MODERATE: [
                InvestmentStrategy.VALUE_INVESTING,
                InvestmentStrategy.GROWTH_INVESTING
            ],
            RiskTolerance.HIGH: [
                InvestmentStrategy.MOMENTUM_INVESTING,
                InvestmentStrategy.GROWTH_INVESTING
            ]
        }

    def _load_learning_paths(self) -> None:
        """Load the learning paths for each investment strategy."""
        self.learning_paths = {
            InvestmentStrategy.VALUE_INVESTING: LearningPath(
                InvestmentStrategy.VALUE_INVESTING,
                [
                    "Fundamentals of Value Investing",
                    "How to Analyze Financial Statements",
                    "Case Studies: Successful Value Investors"
                ]
            ),
            InvestmentStrategy.GROWTH_INVESTING: LearningPath(
                InvestmentStrategy.GROWTH_INVESTING,
                [
                    "Identifying High-Growth Companies",
                    "Tech Industry Analysis",
                    "Growth Metrics and Valuation"
                ]
            ),
            InvestmentStrategy.MOMENTUM_INVESTING: LearningPath(
                InvestmentStrategy.MOMENTUM_INVESTING,
                [
                    "Technical Analysis Basics",
                    "Momentum Indicators and Strategies",
                    "Risk Management in Momentum Trading"
                ]
            ),
            InvestmentStrategy.INDEX_INVESTING: LearningPath(
                InvestmentStrategy.INDEX_INVESTING,
                [
                    "Passive Investing Principles",
                    "ETF Selection and Diversification",
                    "Long-Term Portfolio Management"
                ]
            ),
            InvestmentStrategy.DIVIDEND_INVESTING: LearningPath(
                InvestmentStrategy.DIVIDEND_INVESTING,
                [
                    "Dividend Aristocrats Analysis",
                    "Building a Dividend Portfolio",
                    "Tax Implications of Dividend Investing"
                ]
            )
        }

    def get_risk_tolerance(self, risk_score: int) -> RiskTolerance:
        """Determine risk tolerance based on a numerical score.
        
        Args:
            risk_score: Integer between 1-10 representing risk tolerance
            
        Returns:
            RiskTolerance enum value
            
        Raises:
            ValueError: If risk_score is outside valid range
        """
        if not 1 <= risk_score <= 10:
            raise ValueError("Risk score must be between 1 and 10")
        
        if risk_score <= 3:
            return RiskTolerance.LOW
        elif risk_score <= 7:
            return RiskTolerance.MODERATE
        else:
            return RiskTolerance.HIGH

    def recommend_strategies(self, risk_tolerance: RiskTolerance) -> List[InvestmentStrategy]:
        """Recommend investment strategies based on risk tolerance.
        
        Args:
            risk_tolerance: RiskTolerance enum value
            
        Returns:
            List of recommended InvestmentStrategy enum values
        """
        return self.strategy_mappings.get(risk_tolerance, [])

    def get_learning_path(self, strategy: InvestmentStrategy) -> Optional[LearningPath]:
        """Get the learning path for a specific investment strategy.
        
        Args:
            strategy: InvestmentStrategy enum value
            
        Returns:
            LearningPath object if found, None otherwise
        """
        return self.learning_paths.get(strategy)

    def analyze_user(self, risk_score: int) -> Dict:
        """Full analysis of user based on risk score.
        
        Args:
            risk_score: Integer between 1-10 representing risk tolerance
            
        Returns:
            Dictionary containing analysis results
            
        Raises:
            ValueError: If risk_score is invalid
        """
        risk_tolerance = self.get_risk_tolerance(risk_score)
        strategies = self.recommend_strategies(risk_tolerance)
        
        result = {
            "risk_tolerance": risk_tolerance.value,
            "recommended_strategies": [s.value for s in strategies],
            "learning_paths": []
        }
        
        for strategy in strategies:
            path = self.get_learning_path(strategy)
            if path:
                result["learning_paths"].append(path.to_dict())
        
        return result

def main():
    """Main function to demonstrate the investment analyzer."""
    analyzer = InvestmentAnalyzer()
    
    try:
        # Get user input
        risk_score = int(input("Enter your risk tolerance score (1-10): "))
        
        # Analyze and display results
        analysis = analyzer.analyze_user(risk_score)
        print("\nInvestment Analysis Results:")
        print(json.dumps(analysis, indent=2))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
