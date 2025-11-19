"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Suggest a set of key performance indicators (KPIs) for evaluating the success of a crypto casino platform like TG.Casino, including metrics for user engagement, token adoption, and revenue growth.
Generated: DETERMINISTIC_02a96ba649e8d8d7
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kpi_evaluator.py

import datetime
from typing import Dict, List

class KPIs:
    def __init__(self, user_data: List[Dict], token_data: List[Dict], revenue_data: List[Dict]):
        """
        Initialize KPIs with user, token, and revenue data.

        Args:
        - user_data (List[Dict]): List of user engagement data.
        - token_data (List[Dict]): List of token adoption data.
        - revenue_data (List[Dict]): List of revenue growth data.
        """
        self.user_data = user_data
        self.token_data = token_data
        self.revenue_data = revenue_data

    def calculate_user_engagement_kpis(self) -> Dict:
        """
        Calculate user engagement KPIs.

        Returns:
        - Dict: Dictionary containing user engagement KPIs.
        """
        # Calculate average daily active users (ADAU)
        dau = sum(1 for data in self.user_data if data['active']) / len(self.user_data)
        
        # Calculate average session duration (ASD)
        session_durations = [data['session_duration'] for data in self.user_data]
        asd = sum(session_durations) / len(session_durations)

        # Calculate user retention rate (URR)
        retained_users = sum(1 for data in self.user_data if data['retained'])
        urr = retained_users / len(self.user_data)

        return {
            'average_daily_active_users': dau,
            'average_session_duration': asd,
            'user_retention_rate': urr
        }

    def calculate_token_adoption_kpis(self) -> Dict:
        """
        Calculate token adoption KPIs.

        Returns:
        - Dict: Dictionary containing token adoption KPIs.
        """
        # Calculate total token supply
        total_token_supply = sum(data['token_supply'] for data in self.token_data)

        # Calculate token velocity (TV)
        token_velocity = sum(data['token_velocity'] for data in self.token_data) / len(self.token_data)

        # Calculate token holder growth rate (THGR)
        token_holders = [data['token_holders'] for data in self.token_data]
        thgr = (token_holders[-1] - token_holders[0]) / token_holders[0]

        return {
            'total_token_supply': total_token_supply,
            'token_velocity': token_velocity,
            'token_holder_growth_rate': thgr
        }

    def calculate_revenue_growth_kpis(self) -> Dict:
        """
        Calculate revenue growth KPIs.

        Returns:
        - Dict: Dictionary containing revenue growth KPIs.
        """
        # Calculate total revenue
        total_revenue = sum(data['revenue'] for data in self.revenue_data)

        # Calculate revenue growth rate (RGR)
        revenues = [data['revenue'] for data in self.revenue_data]
        rgr = (revenues[-1] - revenues[0]) / revenues[0]

        # Calculate average revenue per user (ARPU)
        arpu = total_revenue / len(self.user_data)

        return {
            'total_revenue': total_revenue,
            'revenue_growth_rate': rgr,
            'average_revenue_per_user': arpu
        }

    def evaluate_kpis(self) -> Dict:
        """
        Evaluate KPIs for the crypto casino platform.

        Returns:
        - Dict: Dictionary containing all KPIs.
        """
        user_engagement_kpis = self.calculate_user_engagement_kpis()
        token_adoption_kpis = self.calculate_token_adoption_kpis()
        revenue_growth_kpis = self.calculate_revenue_growth_kpis()

        return {
            'user_engagement': user_engagement_kpis,
            'token_adoption': token_adoption_kpis,
            'revenue_growth': revenue_growth_kpis
        }

def main():
    # Example usage
    user_data = [
        {'active': True, 'session_duration': 30, 'retained': True},
        {'active': False, 'session_duration': 60, 'retained': False},
        {'active': True, 'session_duration': 90, 'retained': True}
    ]

    token_data = [
        {'token_supply': 1000000, 'token_velocity': 0.1, 'token_holders': 1000},
        {'token_supply': 1200000, 'token_velocity': 0.2, 'token_holders': 1200},
        {'token_supply': 1500000, 'token_velocity': 0.3, 'token_holders': 1500}
    ]

    revenue_data = [
        {'revenue': 10000},
        {'revenue': 12000},
        {'revenue': 15000}
    ]

    kpis = KPIs(user_data, token_data, revenue_data)
    result = kpis.evaluate_kpis()

    print(result)

if __name__ == "__main__":
    main()
```
