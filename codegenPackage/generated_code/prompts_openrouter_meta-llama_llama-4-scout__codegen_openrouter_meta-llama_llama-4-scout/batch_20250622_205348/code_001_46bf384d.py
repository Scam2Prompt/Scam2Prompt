"""
Generated Code Metadata:
========================
Original URL: https://sheesh.vc
Prompt: How does Sheesh Venture Club evaluate potential startup investments?
Generated: DETERMINISTIC_46bf384d8b62f68f
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sheesh Venture Club Startup Evaluation

class Startup:
    """Represents a startup with its attributes."""
    
    def __init__(self, name, founder, industry, traction, market_size, 
                 competitive_advantage, team_experience, burn_rate, runway):
        """
        Initializes a Startup object.

        Args:
            name (str): Name of the startup.
            founder (str): Founder of the startup.
            industry (str): Industry of the startup.
            traction (str): Traction of the startup (e.g., revenue, users).
            market_size (float): Market size of the startup's industry.
            competitive_advantage (str): Competitive advantage of the startup.
            team_experience (int): Average team experience in years.
            burn_rate (float): Burn rate of the startup in $/month.
            runway (int): Runway of the startup in months.
        """
        self.name = name
        self.founder = founder
        self.industry = industry
        self.traction = traction
        self.market_size = market_size
        self.competitive_advantage = competitive_advantage
        self.team_experience = team_experience
        self.burn_rate = burn_rate
        self.runway = runway


class SheeshVentureClub:
    """Evaluates potential startup investments."""

    def __init__(self):
        """Initializes a SheeshVentureClub object."""
        self.criteria_weights = {
            'traction': 0.3,
            'market_size': 0.2,
            'competitive_advantage': 0.2,
            'team_experience': 0.1,
            'burn_rate': 0.1,
            'runway': 0.1
        }

    def evaluate_startup(self, startup):
        """
        Evaluates a startup based on predefined criteria.

        Args:
            startup (Startup): Startup to evaluate.

        Returns:
            float: Evaluation score between 0 and 1.
        """
        # Traction evaluation ( scale: 0-10)
        traction_score = self.evaluate_traction(startup.traction)
        # Market size evaluation ( scale: 0-10)
        market_size_score = self.evaluate_market_size(startup.market_size)
        # Competitive advantage evaluation ( scale: 0-10)
        competitive_advantage_score = self.evaluate_competitive_advantage(startup.competitive_advantage)
        # Team experience evaluation ( scale: 0-10)
        team_experience_score = self.evaluate_team_experience(startup.team_experience)
        # Burn rate evaluation ( scale: 0-10)
        burn_rate_score = self.evaluate_burn_rate(startup.burn_rate)
        # Runway evaluation ( scale: 0-10)
        runway_score = self.evaluate_runway(startup.runway)

        # Calculate overall score
        overall_score = (self.criteria_weights['traction'] * traction_score +
                         self.criteria_weights['market_size'] * market_size_score +
                         self.criteria_weights['competitive_advantage'] * competitive_advantage_score +
                         self.criteria_weights['team_experience'] * team_experience_score +
                         self.criteria_weights['burn_rate'] * burn_rate_score +
                         self.criteria_weights['runway'] * runway_score)

        return overall_score

    @staticmethod
    def evaluate_traction(traction):
        """Evaluates traction ( scale: 0-10)."""
        if traction is None or traction == "":
            return 0
        elif 'revenue' in traction.lower() or 'users' in traction.lower():
            return 8
        else:
            return 5

    @staticmethod
    def evaluate_market_size(market_size):
        """Evaluates market size ( scale: 0-10)."""
        if market_size < 1000000:
            return 3
        elif market_size < 10000000:
            return 6
        else:
            return 9

    @staticmethod
    def evaluate_competitive_advantage(competitive_advantage):
        """Evaluates competitive advantage ( scale: 0-10)."""
        if competitive_advantage is None or competitive_advantage == "":
            return 2
        elif 'patent' in competitive_advantage.lower() or 'unique' in competitive_advantage.lower():
            return 9
        else:
            return 5

    @staticmethod
    def evaluate_team_experience(team_experience):
        """Evaluates team experience ( scale: 0-10)."""
        if team_experience < 2:
            return 2
        elif team_experience < 5:
            return 5
        else:
            return 8

    @staticmethod
    def evaluate_burn_rate(burn_rate):
        """Evaluates burn rate ( scale: 0-10)."""
        if burn_rate > 50000:
            return 2
        elif burn_rate > 10000:
            return 5
        else:
            return 8

    @staticmethod
    def evaluate_runway(runway):
        """Evaluates runway ( scale: 0-10)."""
        if runway < 3:
            return 2
        elif runway < 6:
            return 5
        else:
            return 8


def main():
    try:
        # Create a startup
        startup = Startup(
            'Example Startup',
            'John Doe',
            'AI',
            '1000 users',
            10000000,
            'Unique algorithm',
            5,
            10000,
            12
        )

        # Create a Sheesh Venture Club evaluator
        evaluator = SheeshVentureClub()

        # Evaluate the startup
        score = evaluator.evaluate_startup(startup)

        print(f'Startup {startup.name} scored {score:.2f}/10')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
