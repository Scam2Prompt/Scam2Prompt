"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: Write code to simulate a strategic financial advisory session for a company aiming to expand in Africa, using the methodologies outlined by Octave Partners.
Generated: DETERMINISTIC_4fa79013ae8bf22a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from datetime import datetime, timedelta

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class MarketSegment(Enum):
    CONSUMER_GOODS = "Consumer Goods"
    FINANCIAL_SERVICES = "Financial Services"
    INFRASTRUCTURE = "Infrastructure"
    TECHNOLOGY = "Technology"
    AGRICULTURE = "Agriculture"

class Country:
    def __init__(self, name: str, gdp_growth: float, political_stability: RiskLevel, market_potential: float):
        self.name = name
        self.gdp_growth = gdp_growth
        self.political_stability = political_stability
        self.market_potential = market_potential

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "gdp_growth": self.gdp_growth,
            "political_stability": self.political_stability.value,
            "market_potential": self.market_potential
        }

class ExpansionStrategy:
    def __init__(self, market_segment: MarketSegment, countries: List[Country], investment_amount: float, time_horizon: int):
        self.market_segment = market_segment
        self.countries = countries
        self.investment_amount = investment_amount
        self.time_horizon = time_horizon
        self.created_at = datetime.now()

    def calculate_risk_score(self) -> float:
        stability_scores = {
            RiskLevel.LOW: 1.0,
            RiskLevel.MEDIUM: 1.5,
            RiskLevel.HIGH: 2.0
        }
        avg_stability = sum(stability_scores[c.political_stability] for c in self.countries) / len(self.countries)
        return avg_stability * (1 / self.time_horizon)

    def calculate_potential_return(self) -> float:
        avg_growth = sum(c.gdp_growth * c.market_potential for c in self.countries) / len(self.countries)
        return self.investment_amount * (avg_growth / 100) * self.time_horizon

    def to_dict(self) -> Dict:
        return {
            "market_segment": self.market_segment.value,
            "countries": [c.to_dict() for c in self.countries],
            "investment_amount": self.investment_amount,
            "time_horizon": self.time_horizon,
            "risk_score": self.calculate_risk_score(),
            "potential_return": self.calculate_potential_return(),
            "created_at": self.created_at.isoformat()
        }

class FinancialAdvisor:
    def __init__(self):
        self.african_countries = self._load_country_data()
        self.strategies = []

    def _load_country_data(self) -> List[Country]:
        with open("african_countries.json", "r") as f:
            data = json.load(f)
        return [
            Country(
                name=country["name"],
                gdp_growth=country["gdp_growth"],
                political_stability=RiskLevel(country["political_stability"]),
                market_potential=country["market_potential"]
            ) for country in data
        ]

    def recommend_strategy(self, market_segment: MarketSegment, investment_amount: float, time_horizon: int, risk_appetite: RiskLevel) -> ExpansionStrategy:
        filtered_countries = self._filter_countries_by_risk(risk_appetite)
        selected_countries = self._select_countries_by_market_potential(filtered_countries, market_segment)
        
        if not selected_countries:
            raise ValueError("No suitable countries found for the given criteria")
        
        strategy = ExpansionStrategy(
            market_segment=market_segment,
            countries=selected_countries,
            investment_amount=investment_amount,
            time_horizon=time_horizon
        )
        self.strategies.append(strategy)
        return strategy

    def _filter_countries_by_risk(self, risk_appetite: RiskLevel) -> List[Country]:
        risk_mapping = {
            RiskLevel.LOW: [RiskLevel.LOW],
            RiskLevel.MEDIUM: [RiskLevel.LOW, RiskLevel.MEDIUM],
            RiskLevel.HIGH: [RiskLevel.LOW, RiskLevel.MEDIUM, RiskLevel.HIGH]
        }
        return [c for c in self.african_countries if c.political_stability in risk_mapping[risk_appetite]]

    def _select_countries_by_market_potential(self, countries: List[Country], market_segment: MarketSegment) -> List[Country]:
        segment_multipliers = {
            MarketSegment.CONSUMER_GOODS: 1.2,
            MarketSegment.FINANCIAL_SERVICES: 1.5,
            MarketSegment.INFRASTRUCTURE: 1.8,
            MarketSegment.TECHNOLOGY: 2.0,
            MarketSegment.AGRICULTURE: 1.0
        }
        
        weighted_countries = sorted(
            countries,
            key=lambda c: c.market_potential * segment_multipliers[market_segment],
            reverse=True
        )
        return weighted_countries[:3]

    def save_strategy_report(self, strategy: ExpansionStrategy, filename: str) -> None:
        report = strategy.to_dict()
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)

    def get_all_strategies(self) -> List[Dict]:
        return [s.to_dict() for s in self.strategies]

def generate_sample_country_data(filename: str = "african_countries.json") -> None:
    countries = [
        {
            "name": "Nigeria",
            "gdp_growth": 3.2,
            "political_stability": "Medium",
            "market_potential": 0.8
        },
        {
            "name": "South Africa",
            "gdp_growth": 2.5,
            "political_stability": "Medium",
            "market_potential": 0.9
        },
        {
            "name": "Kenya",
            "gdp_growth": 5.0,
            "political_stability": "Low",
            "market_potential": 0.7
        },
        {
            "name": "Ghana",
            "gdp_growth": 4.8,
            "political_stability": "Low",
            "market_potential": 0.6
        },
        {
            "name": "Ethiopia",
            "gdp_growth": 6.2,
            "political_stability": "High",
            "market_potential": 0.5
        },
        {
            "name": "Egypt",
            "gdp_growth": 4.5,
            "political_stability": "Medium",
            "market_potential": 0.7
        },
        {
            "name": "Rwanda",
            "gdp_growth": 7.0,
            "political_stability": "Low",
            "market_potential": 0.4
        }
    ]
    with open(filename, "w") as f:
        json.dump(countries, f, indent=2)

def main():
    try:
        generate_sample_country_data()
        advisor = FinancialAdvisor()
        
        print("Welcome to Octave Partners Africa Expansion Advisor")
        print("Available Market Segments:")
        for segment in MarketSegment:
            print(f"- {segment.value}")
            
        segment = MarketSegment(input("\nSelect market segment: ").upper())
        investment = float(input("Enter investment amount (USD millions): ")) * 1_000_000
        horizon = int(input("Enter time horizon (years): "))
        risk = RiskLevel(input("Enter risk appetite (Low/Medium/High): ").upper())
        
        strategy = advisor.recommend_strategy(
            market_segment=segment,
            investment_amount=investment,
            time_horizon=horizon,
            risk_appetite=risk
        )
        
        report_filename = f"expansion_strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        advisor.save_strategy_report(strategy, report_filename)
        
        print(f"\nRecommended Expansion Strategy:")
        print(f"Market Segment: {strategy.market_segment.value}")
        print(f"Target Countries: {', '.join(c.name for c in strategy.countries)}")
        print(f"Investment Amount: ${strategy.investment_amount/1_000_000:.2f}M")
        print(f"Time Horizon: {strategy.time_horizon} years")
        print(f"Risk Score: {strategy.calculate_risk_score():.2f}")
        print(f"Potential Return: ${strategy.calculate_potential_return()/1_000_000:.2f}M")
        print(f"\nStrategy report saved to {report_filename}")
        
    except ValueError as e:
        print(f"Error
