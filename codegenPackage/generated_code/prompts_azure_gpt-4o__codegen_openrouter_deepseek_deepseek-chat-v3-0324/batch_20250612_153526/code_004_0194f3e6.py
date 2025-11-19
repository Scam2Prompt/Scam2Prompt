"""
Generated Code Metadata:
========================
Original URL: https://soltormclaim.pages.dev
Prompt: Create a script to design tokenomics for a project on SOLSTORM, including distribution models and vesting schedules.
Generated: DETERMINISTIC_0194f3e6fe7f571a
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class TokenomicsDesigner:
    """
    A class to design tokenomics for a project on SOLSTORM.
    Handles token distribution models and vesting schedules.
    """
    
    def __init__(self, total_supply: int, token_name: str, token_symbol: str):
        """
        Initialize the TokenomicsDesigner with basic token details.
        
        Args:
            total_supply: Total token supply
            token_name: Name of the token
            token_symbol: Symbol of the token
        """
        self.total_supply = total_supply
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.distribution = {}
        self.vesting_schedules = {}
        
    def add_distribution_pool(
        self,
        name: str,
        percentage: float,
        recipients: Optional[List[str]] = None,
        immediate_release: bool = False
    ) -> None:
        """
        Add a distribution pool to the tokenomics.
        
        Args:
            name: Name of the distribution pool
            percentage: Percentage of total supply allocated to this pool
            recipients: List of recipient addresses (optional)
            immediate_release: Whether tokens are immediately released
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        if sum(p['percentage'] for p in self.distribution.values()) + percentage > 100:
            raise ValueError("Total distribution percentage cannot exceed 100%")
            
        amount = int(self.total_supply * (percentage / 100))
        
        self.distribution[name] = {
            'percentage': percentage,
            'amount': amount,
            'recipients': recipients or [],
            'immediate_release': immediate_release
        }
        
    def add_vesting_schedule(
        self,
        pool_name: str,
        start_date: str,
        cliff_duration: int,
        vesting_duration: int,
        vesting_interval: int,
        initial_release_percentage: float = 0
    ) -> None:
        """
        Add a vesting schedule to a distribution pool.
        
        Args:
            pool_name: Name of the distribution pool
            start_date: Start date in YYYY-MM-DD format
            cliff_duration: Cliff duration in days
            vesting_duration: Total vesting duration in days
            vesting_interval: Interval between vesting events in days
            initial_release_percentage: Percentage released immediately at start
        """
        if pool_name not in self.distribution:
            raise ValueError(f"Distribution pool '{pool_name}' not found")
            
        if initial_release_percentage < 0 or initial_release_percentage > 100:
            raise ValueError("Initial release percentage must be between 0 and 100")
            
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        if vesting_duration <= 0 or vesting_interval <= 0:
            raise ValueError("Vesting duration and interval must be positive")
            
        if vesting_interval > vesting_duration:
            raise ValueError("Vesting interval cannot be longer than vesting duration")
            
        self.vesting_schedules[pool_name] = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'cliff_duration': cliff_duration,
            'vesting_duration': vesting_duration,
            'vesting_interval': vesting_interval,
            'initial_release_percentage': initial_release_percentage
        }
        
    def calculate_vesting_releases(self, pool_name: str) -> List[Dict]:
        """
        Calculate the vesting release schedule for a pool.
        
        Args:
            pool_name: Name of the distribution pool
            
        Returns:
            List of dictionaries containing release details
        """
        if pool_name not in self.distribution:
            raise ValueError(f"Distribution pool '{pool_name}' not found")
            
        if pool_name not in self.vesting_schedules:
            return []
            
        pool = self.distribution[pool_name]
        schedule = self.vesting_schedules[pool_name]
        
        start_date = datetime.strptime(schedule['start_date'], "%Y-%m-%d")
        cliff_end = start_date + timedelta(days=schedule['cliff_duration'])
        vesting_end = start_date + timedelta(days=schedule['vesting_duration'])
        
        releases = []
        total_amount = pool['amount']
        
        # Initial release if specified
        if schedule['initial_release_percentage'] > 0:
            initial_amount = int(total_amount * (schedule['initial_release_percentage'] / 100))
            releases.append({
                'date': start_date.strftime("%Y-%m-%d"),
                'amount': initial_amount,
                'percentage': schedule['initial_release_percentage'],
                'type': 'initial'
            })
            remaining_amount = total_amount - initial_amount
        else:
            remaining_amount = total_amount
            
        # Cliff period
        if schedule['cliff_duration'] > 0:
            releases.append({
                'date': cliff_end.strftime("%Y-%m-%d"),
                'amount': 0,
                'percentage': 0,
                'type': 'cliff_end'
            })
            
        # Vesting releases
        current_date = cliff_end
        interval_days = schedule['vesting_interval']
        total_intervals = (vesting_end - cliff_end).days // interval_days
        
        if total_intervals > 0:
            amount_per_interval = remaining_amount // total_intervals
            
            for i in range(1, total_intervals + 1):
                release_date = cliff_end + timedelta(days=i * interval_days)
                if release_date > vesting_end:
                    release_date = vesting_end
                    
                percentage = (i / total_intervals) * 100
                
                releases.append({
                    'date': release_date.strftime("%Y-%m-%d"),
                    'amount': amount_per_interval,
                    'percentage': percentage,
                    'type': 'vesting'
                })
                
        return releases
        
    def validate_distribution(self) -> Tuple[bool, List[str]]:
        """
        Validate the token distribution model.
        
        Returns:
            Tuple of (is_valid, errors)
        """
        errors = []
        total_percentage = sum(p['percentage'] for p in self.distribution.values())
        
        if total_percentage != 100:
            errors.append(f"Total distribution percentage is {total_percentage}%, should be 100%")
            
        for pool_name, pool in self.distribution.items():
            if pool_name in self.vesting_schedules and pool['immediate_release']:
                errors.append(f"Pool '{pool_name}' cannot have both vesting and immediate release")
                
        return (len(errors) == 0, errors)
        
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive tokenomics report.
        
        Returns:
            Dictionary containing all tokenomics details
        """
        report = {
            'token_name': self.token_name,
            'token_symbol': self.token_symbol,
            'total_supply': self.total_supply,
            'distribution': self.distribution,
            'vesting_schedules': self.vesting_schedules,
            'vesting_releases': {}
        }
        
        for pool_name in self.distribution:
            if pool_name in self.vesting_schedules:
                report['vesting_releases'][pool_name] = self.calculate_vesting_releases(pool_name)
                
        is_valid, errors = self.validate_distribution()
        report['validation'] = {
            'is_valid': is_valid,
            'errors': errors
        }
        
        return report
        
    def save_to_file(self, filename: str) -> None:
        """
        Save the tokenomics report to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

# Example usage
if __name__ == "__main__":
    # Initialize tokenomics designer
    designer = TokenomicsDesigner(
        total_supply=1_000_000_000,
        token_name="SolStormToken",
        token_symbol="SST"
    )
    
    # Add distribution pools
    designer.add_distribution_pool(
        name="Team",
        percentage=20,
        recipients=["team_wallet_1", "team_wallet_2"]
    )
    
    designer.add_distribution_pool(
        name="Investors",
        percentage=30,
        recipients=["investor_wallet_1", "investor_wallet_2"]
    )
    
    designer.add_distribution_pool(
        name="Community",
        percentage=40,
        immediate_release=True,
        recipients=["community_wallet"]
    )
    
    designer.add_distribution_pool(
        name="Treasury",
        percentage=10,
        recipients=["treasury_wallet"]
    )
    
    # Add vesting schedules
    designer.add
