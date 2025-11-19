"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: What are the wagering requirements for the bonuses at Jackpot Cow Casino, and how do they apply to different types of bonuses?
Generated: DETERMINISTIC_9aef319f458226f4
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Bonus:
    """
    Represents a casino bonus with its wagering requirements.
    """
    def __init__(self, bonus_type: str, wagering_requirement: float, 
                 game_contribution: dict, max_bet: float = None):
        """
        Initialize a bonus instance.
        
        Args:
            bonus_type: Type of bonus (e.g., 'welcome', 'deposit', 'free_spins')
            wagering_requirement: Multiplier for wagering (e.g., 30x)
            game_contribution: Dictionary mapping game types to contribution percentages
            max_bet: Maximum allowed bet while wagering (optional)
        """
        self.bonus_type = bonus_type
        self.wagering_requirement = wagering_requirement
        self.game_contribution = game_contribution
        self.max_bet = max_bet

    def calculate_wagering_amount(self, bonus_amount: float) -> float:
        """
        Calculate total amount that needs to be wagered.
        
        Args:
            bonus_amount: The amount of bonus received
            
        Returns:
            Total wagering amount required
        """
        return bonus_amount * self.wagering_requirement

    def get_contribution(self, game_type: str) -> float:
        """
        Get the contribution percentage for a specific game type.
        
        Args:
            game_type: Type of game (e.g., 'slots', 'table', 'live')
            
        Returns:
            Contribution percentage (0-1)
            
        Raises:
            ValueError: If game type is not found in contributions
        """
        if game_type not in self.game_contribution:
            raise ValueError(f"Game type '{game_type}' not found in contribution rules")
        return self.game_contribution[game_type]


class JackpotCowCasinoBonuses:
    """
    Manages all bonus wagering requirements for Jackpot Cow Casino.
    """
    def __init__(self):
        self.bonuses = {
            'welcome': Bonus(
                bonus_type='welcome',
                wagering_requirement=30.0,
                game_contribution={
                    'slots': 1.0,
                    'table': 0.2,
                    'live': 0.1,
                    'video_poker': 0.5
                },
                max_bet=5.0
            ),
            'deposit': Bonus(
                bonus_type='deposit',
                wagering_requirement=35.0,
                game_contribution={
                    'slots': 1.0,
                    'table': 0.15,
                    'live': 0.05,
                    'video_poker': 0.3
                },
                max_bet=10.0
            ),
            'free_spins': Bonus(
                bonus_type='free_spins',
                wagering_requirement=40.0,
                game_contribution={
                    'slots': 1.0,
                    'table': 0.0,
                    'live': 0.0,
                    'video_poker': 0.0
                },
                max_bet=5.0
            ),
            'no_deposit': Bonus(
                bonus_type='no_deposit',
                wagering_requirement=50.0,
                game_contribution={
                    'slots': 1.0,
                    'table': 0.1,
                    'live': 0.0,
                    'video_poker': 0.2
                },
                max_bet=2.0
            )
        }

    def get_bonus(self, bonus_type: str) -> Bonus:
        """
        Get bonus details by type.
        
        Args:
            bonus_type: Type of bonus to retrieve
            
        Returns:
            Bonus object with wagering requirements
            
        Raises:
            ValueError: If bonus type is not found
        """
        if bonus_type not in self.bonuses:
            raise ValueError(f"Bonus type '{bonus_type}' not found")
        return self.bonuses[bonus_type]

    def calculate_effective_wagering(self, bonus_type: str, bonus_amount: float, 
                                    game_type: str) -> float:
        """
        Calculate effective wagering amount considering game contribution.
        
        Args:
            bonus_type: Type of bonus
            bonus_amount: Amount of bonus received
            game_type: Type of game being played
            
        Returns:
            Effective wagering amount considering contribution
            
        Raises:
            ValueError: If bonus or game type is invalid
        """
        bonus = self.get_bonus(bonus_type)
        contribution = bonus.get_contribution(game_type)
        if contribution == 0:
            raise ValueError(f"Game type '{game_type}' contributes 0% to wagering")
        
        total_wagering = bonus.calculate_wagering_amount(bonus_amount)
        return total_wagering / contribution
```
