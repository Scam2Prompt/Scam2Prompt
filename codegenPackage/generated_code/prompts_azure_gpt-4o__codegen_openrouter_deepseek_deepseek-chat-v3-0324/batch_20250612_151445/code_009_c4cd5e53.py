"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Write a function to handle cashback rewards for active players, inspired by DominoBet's weekly cashback program.
Generated: DETERMINISTIC_c4cd5e538a45c64d
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from decimal import Decimal, getcontext

class Player:
    def __init__(self, player_id: str, is_active: bool, total_losses: Decimal):
        self.player_id = player_id
        self.is_active = is_active
        self.total_losses = total_losses

class CashbackCalculator:
    """
    A class to calculate weekly cashback rewards for active players.
    Implements DominoBet-inspired cashback tiers based on player losses.
    """
    
    # Define cashback tiers as percentage of losses
    CASHBACK_TIERS = {
        'tier1': {'min_loss': Decimal('0'), 'max_loss': Decimal('1000'), 'percentage': Decimal('0.05')},
        'tier2': {'min_loss': Decimal('1000'), 'max_loss': Decimal('5000'), 'percentage': Decimal('0.07')},
        'tier3': {'min_loss': Decimal('5000'), 'max_loss': Decimal('10000'), 'percentage': Decimal('0.10')},
        'tier4': {'min_loss': Decimal('10000'), 'max_loss': None, 'percentage': Decimal('0.15')}
    }
    
    def __init__(self):
        getcontext().prec = 6  # Set precision for Decimal calculations
    
    def calculate_cashback(self, player: Player) -> Optional[Decimal]:
        """
        Calculate cashback amount for a player based on their losses and active status.
        
        Args:
            player: Player object containing player data
            
        Returns:
            Decimal: Cashback amount if player is eligible, None otherwise
        """
        if not player.is_active:
            return None
        
        if player.total_losses <= Decimal('0'):
            return Decimal('0')
        
        for tier in self.CASHBACK_TIERS.values():
            min_loss = tier['min_loss']
            max_loss = tier['max_loss']
            
            if (max_loss is None and player.total_losses >= min_loss) or \
               (min_loss <= player.total_losses < max_loss):
                return player.total_losses * tier['percentage']
        
        return Decimal('0')
    
    def process_weekly_cashback(self, players: List[Player]) -> Dict[str, Decimal]:
        """
        Process cashback for all players for the current week.
        
        Args:
            players: List of Player objects to process
            
        Returns:
            Dict[str, Decimal]: Dictionary mapping player IDs to their cashback amounts
        """
        cashback_results = {}
        
        for player in players:
            try:
                cashback = self.calculate_cashback(player)
                if cashback is not None:
                    cashback_results[player.player_id] = cashback
            except Exception as e:
                print(f"Error processing cashback for player {player.player_id}: {str(e)}")
                continue
        
        return cashback_results
    
    def generate_cashback_report(self, cashback_data: Dict[str, Decimal]) -> str:
        """
        Generate a formatted report of cashback distributions.
        
        Args:
            cashback_data: Dictionary of player IDs to cashback amounts
            
        Returns:
            str: Formatted report string
        """
        report_lines = []
        report_lines.append(f"Weekly Cashback Report - {datetime.date.today()}")
        report_lines.append("=" * 50)
        report_lines.append("{:<15} {:<15}".format("Player ID", "Cashback Amount"))
        
        total_cashback = Decimal('0')
        for player_id, amount in cashback_data.items():
            report_lines.append("{:<15} ${:<15.2f}".format(player_id, amount))
            total_cashback += amount
        
        report_lines.append("=" * 50)
        report_lines.append("Total Cashback Distributed: ${:.2f}".format(total_cashback))
        
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Sample players
    players = [
        Player("player001", True, Decimal('800')),
        Player("player002", True, Decimal('3500')),
        Player("player003", False, Decimal('12000')),  # Inactive
        Player("player004", True, Decimal('7500')),
        Player("player005", True, Decimal('15000'))
    ]
    
    calculator = CashbackCalculator()
    cashback_results = calculator.process_weekly_cashback(players)
    report = calculator.generate_cashback_report(cashback_results)
    print(report)
```
