"""
Generated Code Metadata:
========================
Original URL: https://staylodu.io
Prompt: Generate code to calculate the perpetual incentives for Loud contributors based on weekly trading fees and social engagement metrics.
Generated: DETERMINISTIC_abd0d97d76f887e3
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional

class LoudContributor:
    """
    Represents a Loud contributor with their trading and social metrics.
    """
    def __init__(self, contributor_id: str, weekly_trading_fees: float, social_engagement_score: float):
        """
        Initialize a Loud contributor with their metrics.
        
        Args:
            contributor_id: Unique identifier for the contributor
            weekly_trading_fees: Trading fees generated in the week (in USD)
            social_engagement_score: Normalized score (0-100) representing social engagement
        """
        self.contributor_id = contributor_id
        self.weekly_trading_fees = weekly_trading_fees
        self.social_engagement_score = social_engagement_score

class IncentiveCalculator:
    """
    Calculates perpetual incentives for Loud contributors based on trading fees and social engagement.
    """
    def __init__(self, 
                 trading_fee_weight: float = 0.7, 
                 social_weight: float = 0.3,
                 max_incentive_pool: float = 100000.0,
                 min_trading_fees: float = 1000.0):
        """
        Initialize the incentive calculator with configuration parameters.
        
        Args:
            trading_fee_weight: Weight for trading fees in incentive calculation (0-1)
            social_weight: Weight for social engagement in incentive calculation (0-1)
            max_incentive_pool: Maximum weekly incentive pool (in USD)
            min_trading_fees: Minimum trading fees required to be eligible for incentives (in USD)
        """
        if not math.isclose(trading_fee_weight + social_weight, 1.0, rel_tol=1e-9):
            raise ValueError("Weights must sum to 1.0")
        
        self.trading_fee_weight = trading_fee_weight
        self.social_weight = social_weight
        self.max_incentive_pool = max_incentive_pool
        self.min_trading_fees = min_trading_fees

    def calculate_incentives(self, contributors: List[LoudContributor]) -> Dict[str, float]:
        """
        Calculate incentives for all contributors based on their metrics.
        
        Args:
            contributors: List of LoudContributor objects
            
        Returns:
            Dictionary mapping contributor IDs to their incentive amounts
        """
        if not contributors:
            return {}
        
        # Filter eligible contributors (meet minimum trading fees)
        eligible_contributors = [
            c for c in contributors 
            if c.weekly_trading_fees >= self.min_trading_fees
        ]
        
        if not eligible_contributors:
            return {}
        
        # Calculate normalized scores for each metric
        trading_fees = [c.weekly_trading_fees for c in eligible_contributors]
        social_scores = [c.social_engagement_score for c in eligible_contributors]
        
        max_trading = max(trading_fees) if trading_fees else 0
        max_social = max(social_scores) if social_scores else 0
        
        # Calculate weighted scores for each contributor
        weighted_scores = []
        for contributor in eligible_contributors:
            normalized_trading = (contributor.weekly_trading_fees / max_trading) if max_trading > 0 else 0
            normalized_social = (contributor.social_engagement_score / max_social) if max_social > 0 else 0
            
            weighted_score = (normalized_trading * self.trading_fee_weight + 
                             normalized_social * self.social_weight)
            weighted_scores.append(weighted_score)
        
        total_weight = sum(weighted_scores)
        if total_weight <= 0:
            return {}
        
        # Distribute incentives proportionally
        incentives = {}
        for i, contributor in enumerate(eligible_contributors):
            incentive = (weighted_scores[i] / total_weight) * self.max_incentive_pool
            incentives[contributor.contributor_id] = round(incentive, 2)
        
        return incentives

class IncentiveReportGenerator:
    """
    Generates reports for incentive calculations.
    """
    @staticmethod
    def generate_weekly_report(incentives: Dict[str, float], week_start_date: datetime) -> str:
        """
        Generate a human-readable weekly incentive report.
        
        Args:
            incentives: Dictionary of contributor incentives
            week_start_date: Start date of the reporting week
            
        Returns:
            Formatted report string
        """
        week_end_date = week_start_date + timedelta(days=6)
        report_lines = [
            f"Weekly Incentive Report ({week_start_date.strftime('%Y-%m-%d')} to {week_end_date.strftime('%Y-%m-%d')})",
            "=" * 60,
            f"{'Contributor ID':<20} {'Incentive (USD)':>15}",
            "-" * 60
        ]
        
        total_incentives = 0.0
        for contributor_id, amount in incentives.items():
            report_lines.append(f"{contributor_id:<20} {amount:>15.2f}")
            total_incentives += amount
        
        report_lines.extend([
            "-" * 60,
            f"{'Total Distributed':<20} {total_incentives:>15.2f}",
            f"{'Remaining Pool':<20} {max(0, 100000 - total_incentives):>15.2f}",
            "=" * 60
        ])
        
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Configuration
    calculator = IncentiveCalculator(
        trading_fee_weight=0.7,
        social_weight=0.3,
        max_incentive_pool=100000.0,
        min_trading_fees=1000.0
    )
    
    # Sample contributors
    contributors = [
        LoudContributor("contributor1", 5000.0, 80.0),
        LoudContributor("contributor2", 3000.0, 90.0),
        LoudContributor("contributor3", 7000.0, 70.0),
        LoudContributor("contributor4", 500.0, 50.0)  # Will be filtered out (below min_trading_fees)
    ]
    
    # Calculate incentives
    incentives = calculator.calculate_incentives(contributors)
    
    # Generate report
    report = IncentiveReportGenerator.generate_weekly_report(
        incentives,
        datetime(2023, 1, 1)  # Example week start date
    )
    
    print(report)
```
