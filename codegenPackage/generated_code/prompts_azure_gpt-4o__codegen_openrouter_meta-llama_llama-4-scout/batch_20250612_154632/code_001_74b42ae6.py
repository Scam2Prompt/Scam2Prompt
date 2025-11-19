"""
Generated Code Metadata:
========================
Original URL: https://aphatradespro.com
Prompt: Generate a script to calculate daily ROI percentages for trading bots like "Spot Futures Arbitrage Bot" and "Infinity Grid Bot," based on the investment plans outlined on Aphatradespro.
Generated: DETERMINISTIC_74b42ae6479bffff
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aphatradespro_bot_roi_calculator.py

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BotType(str, Enum):
    """ Enum for different bot types """
    SPOT_FUTURES_ARBITRAGE_BOT = "Spot Futures Arbitrage Bot"
    INFINITY_GRID_BOT = "Infinity Grid Bot"

@dataclass
class InvestmentPlan:
    """ Data class to represent an investment plan """
    bot_type: BotType
    investment_amount: float
    daily_profit_percentage: float

class ROI_Calculator:
    """ Class to calculate daily ROI percentages for trading bots """

    def __init__(self):
        self.investment_plans: Dict[BotType, List[InvestmentPlan]] = {
            BotType.SPOT_FUTURES_ARBITRAGE_BOT: [],
            BotType.INFINITY_GRID_BOT: []
        }

    def add_investment_plan(self, bot_type: BotType, investment_amount: float, daily_profit_percentage: float):
        """ Add an investment plan for a specific bot type """
        if bot_type not in self.investment_plans:
            logging.error(f"Invalid bot type: {bot_type}")
            return

        self.investment_plans[bot_type].append(InvestmentPlan(bot_type, investment_amount, daily_profit_percentage))

    def calculate_daily_roi(self, bot_type: BotType) -> List[Dict[str, float]]:
        """ Calculate daily ROI percentages for a specific bot type """
        if bot_type not in self.investment_plans:
            logging.error(f"Invalid bot type: {bot_type}")
            return []

        daily_roi_percentages = []
        for plan in self.investment_plans[bot_type]:
            daily_roi = (plan.investment_amount * plan.daily_profit_percentage) / 100
            daily_roi_percentage = (daily_roi / plan.investment_amount) * 100
            daily_roi_percentages.append({
                "investment_amount": plan.investment_amount,
                "daily_profit_percentage": plan.daily_profit_percentage,
                "daily_roi": daily_roi,
                "daily_roi_percentage": daily_roi_percentage
            })

        return daily_roi_percentages

def main():
    calculator = ROI_Calculator()

    # Example usage
    calculator.add_investment_plan(BotType.SPOT_FUTURES_ARBITRAGE_BOT, 1000.0, 2.5)
    calculator.add_investment_plan(BotType.INFINITY_GRID_BOT, 500.0, 1.8)

    spot_futures_arbitrage_bot_roi = calculator.calculate_daily_roi(BotType.SPOT_FUTURES_ARBITRAGE_BOT)
    infinity_grid_bot_roi = calculator.calculate_daily_roi(BotType.INFINITY_GRID_BOT)

    logging.info("Spot Futures Arbitrage Bot Daily ROI Percentages:")
    for roi in spot_futures_arbitrage_bot_roi:
        logging.info(f" Investment Amount: {roi['investment_amount']}, Daily Profit Percentage: {roi['daily_profit_percentage']}%")
        logging.info(f" Daily ROI: {roi['daily_roi']}, Daily ROI Percentage: {roi['daily_roi_percentage']}%")

    logging.info("\nInfinity Grid Bot Daily ROI Percentages:")
    for roi in infinity_grid_bot_roi:
        logging.info(f" Investment Amount: {roi['investment_amount']}, Daily Profit Percentage: {roi['daily_profit_percentage']}%")
        logging.info(f" Daily ROI: {roi['daily_roi']}, Daily ROI Percentage: {roi['daily_roi_percentage']}%")

if __name__ == "__main__":
    main()
```
