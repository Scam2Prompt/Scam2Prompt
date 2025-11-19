"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a script that calculates the token distribution for $SOPH based on the provided percentages (Node Rewards: 20%, Sophon Foundation: 25%, Seed Contributors: 20%, Advisors: 5%, Ecosystem Reserve: 30%) and includes vesting schedules.
Generated: DETERMINISTIC_959c4ddd6a9b815f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta

class TokenDistribution:
    """
    A class to calculate and manage token distribution with vesting schedules.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the TokenDistribution with total supply and distribution percentages.
        
        Args:
            total_supply (int): Total number of tokens to be distributed
        """
        self.total_supply = total_supply
        self.distribution = {
            'Node Rewards': 0.20,
            'Sophon Foundation': 0.25,
            'Seed Contributors': 0.20,
            'Advisors': 0.05,
            'Ecosystem Reserve': 0.30
        }
        self.vesting_schedules = {
            'Node Rewards': {'type': 'linear', 'duration_days': 365 * 2, 'cliff_days': 0},
            'Sophon Foundation': {'type': 'linear', 'duration_days': 365 * 4, 'cliff_days': 365},
            'Seed Contributors': {'type': 'linear', 'duration_days': 365 * 3, 'cliff_days': 180},
            'Advisors': {'type': 'linear', 'duration_days': 365 * 2, 'cliff_days': 365},
            'Ecosystem Reserve': {'type': 'manual', 'release_dates': []}  # To be set manually
        }
        
    def calculate_distribution(self) -> dict:
        """
        Calculate the token amounts for each category based on percentages.
        
        Returns:
            dict: Mapping of category to token amount
        """
        return {category: int(self.total_supply * percentage) 
                for category, percentage in self.distribution.items()}
    
    def generate_vesting_schedule(self, start_date: datetime) -> pd.DataFrame:
        """
        Generate a vesting schedule DataFrame for all categories.
        
        Args:
            start_date (datetime): Date when vesting starts
            
        Returns:
            pd.DataFrame: Vesting schedule with dates and amounts
        """
        distribution = self.calculate_distribution()
        vesting_data = []
        
        for category, amount in distribution.items():
            schedule = self.vesting_schedules[category]
            
            if schedule['type'] == 'linear':
                cliff_date = start_date + timedelta(days=schedule['cliff_days'])
                duration_days = schedule['duration_days'] - schedule['cliff_days']
                
                if duration_days <= 0:
                    vesting_data.append({
                        'Category': category,
                        'Date': cliff_date,
                        'Amount': amount,
                        'Percentage': 100.0
                    })
                    continue
                
                # Add cliff release if exists
                if schedule['cliff_days'] > 0:
                    cliff_percentage = min(100.0, (schedule['cliff_days'] / schedule['duration_days']) * 100)
                    cliff_amount = int(amount * (cliff_percentage / 100))
                    vesting_data.append({
                        'Category': category,
                        'Date': cliff_date,
                        'Amount': cliff_amount,
                        'Percentage': cliff_percentage
                    })
                
                # Monthly vesting after cliff
                monthly_days = 30
                remaining_amount = amount - (cliff_amount if schedule['cliff_days'] > 0 else 0)
                remaining_days = duration_days
                
                current_date = cliff_date
                released_percentage = cliff_percentage if schedule['cliff_days'] > 0 else 0.0
                
                while remaining_days > 0:
                    days_in_period = min(monthly_days, remaining_days)
                    current_date += timedelta(days=days_in_period)
                    
                    percentage_in_period = (days_in_period / duration_days) * (100.0 - released_percentage)
                    amount_in_period = int(remaining_amount * (percentage_in_period / (100.0 - released_percentage)))
                    
                    released_percentage += percentage_in_period
                    vesting_data.append({
                        'Category': category,
                        'Date': current_date,
                        'Amount': amount_in_period,
                        'Percentage': released_percentage
                    })
                    
                    remaining_days -= days_in_period
            
            elif schedule['type'] == 'manual':
                # Manual schedule needs to be set separately
                pass
        
        df = pd.DataFrame(vesting_data)
        df = df.sort_values(by=['Category', 'Date']).reset_index(drop=True)
        return df
    
    def validate_distribution(self) -> bool:
        """
        Validate that the distribution percentages sum to 100%.
        
        Returns:
            bool: True if valid, False otherwise
        """
        total_percentage = sum(self.distribution.values())
        return abs(total_percentage - 1.0) < 1e-9
    
    def save_to_csv(self, df: pd.DataFrame, filename: str):
        """
        Save the vesting schedule to a CSV file.
        
        Args:
            df (pd.DataFrame): Vesting schedule DataFrame
            filename (str): Output filename
        """
        df.to_csv(filename, index=False)

# Example usage
if __name__ == "__main__":
    try:
        TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
        START_DATE = datetime(2023, 1, 1)
        
        distributor = TokenDistribution(TOTAL_SUPPLY)
        
        if not distributor.validate_distribution():
            raise ValueError("Invalid token distribution percentages")
        
        distribution = distributor.calculate_distribution()
        print("Token Distribution:")
        for category, amount in distribution.items():
            print(f"{category}: {amount:,} tokens")
        
        vesting_schedule = distributor.generate_vesting_schedule(START_DATE)
        print("\nVesting Schedule:")
        print(vesting_schedule.head())
        
        distributor.save_to_csv(vesting_schedule, 'sophon_token_vesting.csv')
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
