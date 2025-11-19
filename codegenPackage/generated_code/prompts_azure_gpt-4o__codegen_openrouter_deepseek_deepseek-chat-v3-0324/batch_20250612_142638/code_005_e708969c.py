"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Write a program to simulate AI-driven predictions for investment performance under different market conditions, incorporating stress testing as highlighted by AIvest Securities Limited.
Generated: DETERMINISTIC_e708969c47547062
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
import random
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MarketCondition(Enum):
    """Enum representing different market conditions."""
    BULL = "Bull Market"
    BEAR = "Bear Market"
    STAGNANT = "Stagnant Market"
    VOLATILE = "Volatile Market"

class InvestmentType(Enum):
    """Enum representing different investment types."""
    STOCKS = "Stocks"
    BONDS = "Bonds"
    REAL_ESTATE = "Real Estate"
    COMMODITIES = "Commodities"

class InvestmentSimulator:
    """Simulates investment performance under different market conditions with stress testing."""
    
    def __init__(self):
        """Initialize the simulator with default parameters."""
        self.historical_data = self._load_historical_data()
        self.stress_scenarios = self._define_stress_scenarios()
        
    def _load_historical_data(self) -> Dict[InvestmentType, Dict[MarketCondition, List[float]]]:
        """Load historical performance data for different investments under various market conditions.
        
        Returns:
            Dictionary mapping investment types to market conditions to historical returns.
        """
        return {
            InvestmentType.STOCKS: {
                MarketCondition.BULL: [0.08, 0.12, 0.15, 0.10, 0.09],
                MarketCondition.BEAR: [-0.15, -0.20, -0.10, -0.18, -0.12],
                MarketCondition.STAGNANT: [0.01, 0.00, -0.01, 0.02, 0.01],
                MarketCondition.VOLATILE: [0.05, -0.10, 0.15, -0.05, 0.10]
            },
            InvestmentType.BONDS: {
                MarketCondition.BULL: [0.03, 0.04, 0.03, 0.05, 0.04],
                MarketCondition.BEAR: [0.05, 0.06, 0.04, 0.05, 0.06],
                MarketCondition.STAGNANT: [0.02, 0.03, 0.02, 0.03, 0.02],
                MarketCondition.VOLATILE: [0.03, 0.01, 0.04, 0.02, 0.03]
            },
            InvestmentType.REAL_ESTATE: {
                MarketCondition.BULL: [0.06, 0.07, 0.08, 0.05, 0.06],
                MarketCondition.BEAR: [-0.05, -0.08, -0.03, -0.07, -0.04],
                MarketCondition.STAGNANT: [0.01, 0.02, 0.00, 0.01, 0.02],
                MarketCondition.VOLATILE: [0.03, -0.02, 0.05, -0.01, 0.04]
            },
            InvestmentType.COMMODITIES: {
                MarketCondition.BULL: [0.10, 0.12, 0.08, 0.15, 0.09],
                MarketCondition.BEAR: [-0.12, -0.15, -0.10, -0.18, -0.13],
                MarketCondition.STAGNANT: [0.00, -0.01, 0.01, 0.00, -0.01],
                MarketCondition.VOLATILE: [0.08, -0.12, 0.20, -0.08, 0.15]
            }
        }
    
    def _define_stress_scenarios(self) -> Dict[str, Dict[MarketCondition, float]]:
        """Define stress testing scenarios with severity multipliers.
        
        Returns:
            Dictionary of stress scenarios with market condition severity multipliers.
        """
        return {
            "Mild Stress": {
                MarketCondition.BULL: 0.8,
                MarketCondition.BEAR: 1.2,
                MarketCondition.STAGNANT: 1.1,
                MarketCondition.VOLATILE: 1.3
            },
            "Severe Stress": {
                MarketCondition.BULL: 0.5,
                MarketCondition.BEAR: 1.5,
                MarketCondition.STAGNANT: 1.3,
                MarketCondition.VOLATILE: 1.8
            },
            "Extreme Stress": {
                MarketCondition.BULL: 0.3,
                MarketCondition.BEAR: 2.0,
                MarketCondition.STAGNANT: 1.5,
                MarketCondition.VOLATILE: 2.5
            }
        }
    
    def simulate_investment(
        self,
        investment_type: InvestmentType,
        market_condition: MarketCondition,
        initial_amount: float,
        years: int = 5,
        stress_scenario: str = None
    ) -> Tuple[List[float], float]:
        """Simulate investment performance under given conditions.
        
        Args:
            investment_type: Type of investment to simulate.
            market_condition: Current market condition.
            initial_amount: Initial investment amount.
            years: Number of years to simulate.
            stress_scenario: Optional stress scenario to apply.
            
        Returns:
            Tuple containing list of annual returns and final amount.
            
        Raises:
            ValueError: If invalid investment type, market condition, or stress scenario is provided.
        """
        if investment_type not in InvestmentType:
            raise ValueError(f"Invalid investment type: {investment_type}")
        if market_condition not in MarketCondition:
            raise ValueError(f"Invalid market condition: {market_condition}")
        if stress_scenario and stress_scenario not in self.stress_scenarios:
            raise ValueError(f"Invalid stress scenario: {stress_scenario}")
        
        try:
            historical_returns = self.historical_data[investment_type][market_condition]
            returns = []
            amount = initial_amount
            
            for year in range(years):
                # Get a random historical return for the year
                annual_return = random.choice(historical_returns)
                
                # Apply stress scenario if specified
                if stress_scenario:
                    severity = self.stress_scenarios[stress_scenario][market_condition]
                    annual_return *= severity
                
                returns.append(annual_return)
                amount *= (1 + annual_return)
            
            return returns, amount
        
        except Exception as e:
            logger.error(f"Error during simulation: {e}")
            raise
    
    def run_stress_tests(
        self,
        investment_type: InvestmentType,
        initial_amount: float,
        years: int = 5
    ) -> Dict[str, Tuple[List[float], float]]:
        """Run all defined stress tests for the given investment.
        
        Args:
            investment_type: Type of investment to test.
            initial_amount: Initial investment amount.
            years: Number of years to simulate.
            
        Returns:
            Dictionary mapping stress scenario names to simulation results.
        """
        results = {}
        for scenario in self.stress_scenarios:
            try:
                # Test under bear market conditions for stress scenarios
                returns, final_amount = self.simulate_investment(
                    investment_type=investment_type,
                    market_condition=MarketCondition.BEAR,
                    initial_amount=initial_amount,
                    years=years,
                    stress_scenario=scenario
                )
                results[scenario] = (returns, final_amount)
            except Exception as e:
                logger.error(f"Error running stress test {scenario}: {e}")
                continue
        return results
    
    def generate_report(
        self,
        investment_type: InvestmentType,
        initial_amount: float,
        years: int = 5
    ) -> pd.DataFrame:
        """Generate a comprehensive report of simulations under all market conditions.
        
        Args:
            investment_type: Type of investment to report on.
            initial_amount: Initial investment amount.
            years: Number of years to simulate.
            
        Returns:
            DataFrame containing simulation results.
        """
        data = []
        
        # Simulate under all market conditions
        for condition in MarketCondition:
            try:
                returns, final_amount = self.simulate_investment(
                    investment_type=investment_type,
                    market_condition=condition,
                    initial_amount=initial_amount,
                    years=years
                )
                data.append({
                    "Market Condition": condition.value,
                    "Annual Returns": returns,
                    "Final Amount": final_amount,
                    "CAGR": (final_amount / initial_amount) ** (1/years) - 1,
                    "Stress Scenario": "None"
                })
            except Exception as e:
                logger.error(f"Error simulating {condition}: {e}")
                continue
        
        # Run stress tests
        stress_results = self.run_stress_tests(investment_type, initial_amount, years)
        for scenario, (returns, final_amount) in stress_results.items():
            data.append({
                "Market Condition": MarketCondition.BEAR.value,
