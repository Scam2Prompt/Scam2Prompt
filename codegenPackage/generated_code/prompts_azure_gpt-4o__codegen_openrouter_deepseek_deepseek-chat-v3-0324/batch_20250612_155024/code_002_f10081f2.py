"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Generate code to simulate venture capital funding rounds for startups, incorporating DCL Invest SA's approach to providing financing for businesses with long-term growth potential.
Generated: DETERMINISTIC_f10081f256602e9d
Batch ID: 20250612_155024
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
from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FundingRoundType(Enum):
    """Enum representing different types of funding rounds."""
    PRE_SEED = auto()
    SEED = auto()
    SERIES_A = auto()
    SERIES_B = auto()
    SERIES_C = auto()
    SERIES_D = auto()
    SERIES_E = auto()
    IPO = auto()

@dataclass
class Startup:
    """Class representing a startup company."""
    name: str
    industry: str
    founding_date: datetime
    valuation: float  # in millions
    growth_rate: float  # annual growth rate percentage
    burn_rate: float  # monthly expenses in millions
    funding_rounds: List['FundingRound']
    current_round: Optional[FundingRoundType] = None

@dataclass
class FundingRound:
    """Class representing a funding round."""
    round_type: FundingRoundType
    amount: float  # in millions
    valuation: float  # pre-money valuation in millions
    date: datetime
    investors: List[str]

class DCLInvestSA:
    """Class representing DCL Invest SA's investment strategy."""
    
    def __init__(self):
        self.portfolio: Dict[str, Startup] = {}
        self.investment_threshold = 5.0  # Minimum investment amount in millions
        self.target_industries = ["Tech", "Biotech", "Clean Energy", "AI", "Fintech"]
        self.min_growth_rate = 20.0  # Minimum annual growth rate percentage
        self.max_burn_rate = 2.0  # Maximum acceptable monthly burn rate in millions
    
    def evaluate_startup(self, startup: Startup) -> bool:
        """Evaluate if a startup meets DCL Invest SA's investment criteria."""
        if startup.industry not in self.target_industries:
            logger.info(f"Startup {startup.name} rejected: Industry {startup.industry} not in target industries")
            return False
        
        if startup.growth_rate < self.min_growth_rate:
            logger.info(f"Startup {startup.name} rejected: Growth rate {startup.growth_rate}% below minimum threshold")
            return False
        
        if startup.burn_rate > self.max_burn_rate:
            logger.info(f"Startup {startup.name} rejected: Burn rate ${startup.burn_rate}M too high")
            return False
        
        return True
    
    def determine_investment_amount(self, startup: Startup) -> Tuple[float, float]:
        """Determine investment amount and valuation based on startup metrics."""
        base_amount = max(self.investment_threshold, startup.burn_rate * 12)  # Enough for 1 year runway
        valuation_multiplier = 1 + (startup.growth_rate / 100)
        
        if startup.current_round == FundingRoundType.SEED:
            valuation = base_amount * 5 * valuation_multiplier
            amount = base_amount * 0.8
        elif startup.current_round == FundingRoundType.SERIES_A:
            valuation = base_amount * 10 * valuation_multiplier
            amount = base_amount * 1.5
        elif startup.current_round == FundingRoundType.SERIES_B:
            valuation = base_amount * 20 * valuation_multiplier
            amount = base_amount * 3
        else:
            valuation = base_amount * 30 * valuation_multiplier
            amount = base_amount * 5
        
        return amount, valuation
    
    def conduct_funding_round(self, startup: Startup) -> Optional[FundingRound]:
        """Conduct a funding round for a startup if it meets criteria."""
        if not self.evaluate_startup(startup):
            return None
        
        if not startup.current_round:
            startup.current_round = FundingRoundType.SEED
        else:
            try:
                startup.current_round = FundingRoundType(startup.current_round.value + 1)
            except ValueError:
                logger.info(f"Startup {startup.name} has reached maximum funding round")
                return None
        
        amount, valuation = self.determine_investment_amount(startup)
        investors = ["DCL Invest SA"] + self._generate_additional_investors()
        
        funding_round = FundingRound(
            round_type=startup.current_round,
            amount=amount,
            valuation=valuation,
            date=datetime.now(),
            investors=investors
        )
        
        startup.funding_rounds.append(funding_round)
        startup.valuation = valuation + amount  # Post-money valuation
        logger.info(f"Conducted {startup.current_round.name} round for {startup.name}: ${amount}M at ${valuation}M valuation")
        
        return funding_round
    
    def _generate_additional_investors(self) -> List[str]:
        """Generate a list of additional investors for the round."""
        potential_investors = [
            "Sequoia Capital", "Andreessen Horowitz", "Accel", 
            "Bessemer Venture Partners", "Kleiner Perkins", "GV"
        ]
        num_investors = random.randint(1, 3)
        return random.sample(potential_investors, num_investors)
    
    def simulate_growth(self, startup: Startup, months: int = 12) -> None:
        """Simulate startup growth over a period of months."""
        for _ in range(months):
            growth_factor = 1 + (random.uniform(0.7, 1.3) * startup.growth_rate / 100 / 12)
            startup.valuation *= growth_factor
            
            # Random events that could affect the startup
            event_roll = random.random()
            if event_roll > 0.95:  # 5% chance of major positive event
                startup.valuation *= 1.5
                logger.info(f"Major positive event for {startup.name}! Valuation increased by 50%")
            elif event_roll < 0.05:  # 5% chance of major negative event
                startup.valuation *= 0.7
                logger.info(f"Major setback for {startup.name}. Valuation decreased by 30%")
    
    def run_simulation(self, startup: Startup, years: int = 5) -> None:
        """Run a complete funding simulation over several years."""
        logger.info(f"Starting simulation for {startup.name} over {years} years")
        
        for year in range(years):
            logger.info(f"\n--- Year {year + 1} ---")
            
            # Simulate growth between funding rounds
            self.simulate_growth(startup, 12)
            
            # Conduct funding round if conditions are met
            if year == 0 or random.random() > 0.3:  # 70% chance of funding round each subsequent year
                self.conduct_funding_round(startup)
            
            # Log annual status
            logger.info(f"{startup.name} status: Valuation ${startup.valuation:.2f}M, Current round: {startup.current_round.name if startup.current_round else 'None'}")
        
        logger.info(f"\nSimulation complete for {startup.name}. Final valuation: ${startup.valuation:.2f}M")

def generate_sample_startup() -> Startup:
    """Generate a sample startup for simulation."""
    industries = ["Tech", "Biotech", "Clean Energy", "AI", "Fintech"]
    return Startup(
        name="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)) + " Technologies",
        industry=random.choice(industries),
        founding_date=datetime.now() - timedelta(days=random.randint(180, 720)),
        valuation=random.uniform(2, 10),
        growth_rate=random.uniform(20, 100),
        burn_rate=random.uniform(0.1, 1.5),
        funding_rounds=[],
        current_round=None
    )

if __name__ == "__main__":
    # Example usage
    dcl_invest = DCLInvestSA()
    
    # Create and simulate multiple startups
    for i in range(3):
        startup = generate_sample_startup()
        logger.info(f"\n=== Evaluating Startup {i+1}: {startup.name} ===")
        logger.info(f"Industry: {startup.industry}, Growth: {startup.growth_rate:.1f}%, Burn Rate: ${startup.burn_rate:.1f}M")
        
        dcl_invest.run_simulation(startup, years=5)
```
