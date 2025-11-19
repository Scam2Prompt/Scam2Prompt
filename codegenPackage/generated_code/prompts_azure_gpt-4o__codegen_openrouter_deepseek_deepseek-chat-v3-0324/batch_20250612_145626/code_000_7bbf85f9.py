"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Write a Python script to simulate a lottery number generator for 10 different markets, including Singapore, Malaysia, and Hong Kong, as described on the 4DLOVER website.
Generated: DETERMINISTIC_7bbf85f96fab3b5d
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List
import json

class LotteryGenerator:
    """
    A class to simulate lottery number generation for different markets.
    """
    
    def __init__(self):
        self.market_config = {
            "Singapore": {
                "name": "Singapore 4D",
                "digits": 4,
                "range": (0, 9999),
                "format": "{:04d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "Starter Prizes", "Consolation Prizes"]
            },
            "Malaysia": {
                "name": "Malaysia 4D",
                "digits": 4,
                "range": (0, 9999),
                "format": "{:04d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "Special Prizes", "Consolation Prizes"]
            },
            "Hong Kong": {
                "name": "Hong Kong Mark Six",
                "digits": 6,
                "range": (1, 49),
                "count": 7,  # 6 numbers + 1 bonus
                "format": "{:02d}",
                "prizes": ["1st Division", "2nd Division", "3rd Division", "4th Division", "5th Division", "6th Division"]
            },
            "Taiwan": {
                "name": "Taiwan Lottery",
                "digits": 6,
                "range": (1, 49),
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize", "6th Prize"]
            },
            "China": {
                "name": "China Welfare Lottery",
                "digits": 6,
                "range": (1, 33),
                "count": 6,
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize", "6th Prize"]
            },
            "Japan": {
                "name": "Japan Loto 6",
                "digits": 6,
                "range": (1, 43),
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize"]
            },
            "South Korea": {
                "name": "South Korea Lotto",
                "digits": 6,
                "range": (1, 45),
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize"]
            },
            "Australia": {
                "name": "Australia Monday & Wednesday Lotto",
                "digits": 6,
                "range": (1, 45),
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize"]
            },
            "UK": {
                "name": "UK National Lottery",
                "digits": 6,
                "range": (1, 59),
                "format": "{:02d}",
                "prizes": ["1st Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize"]
            },
            "USA": {
                "name": "USA Powerball",
                "digits": 5,
                "range": (1, 69),
                "powerball_range": (1, 26),
                "format": "{:02d}",
                "prizes": ["Grand Prize", "2nd Prize", "3rd Prize", "4th Prize", "5th Prize", "6th Prize", "7th Prize", "8th Prize"]
            }
        }
    
    def generate_numbers(self, market: str) -> Dict[str, List[str]]:
        """
        Generate lottery numbers for the specified market.
        
        Args:
            market: The market to generate numbers for.
            
        Returns:
            A dictionary containing prize categories and their numbers.
            
        Raises:
            ValueError: If the market is not supported.
        """
        if market not in self.market_config:
            raise ValueError(f"Unsupported market: {market}")
            
        config = self.market_config[market]
        results = {}
        
        if market == "Hong Kong":
            # Generate 6 numbers + 1 bonus for Hong Kong Mark Six
            numbers = random.sample(range(config["range"][0], config["range"][1] + 1), config["count"])
            main_numbers = sorted(numbers[:-1])
            bonus = numbers[-1]
            results["Main Numbers"] = [config["format"].format(num) for num in main_numbers]
            results["Bonus Number"] = [config["format"].format(bonus)]
            
            # Assign prizes (simplified - in reality, prizes depend on matching numbers)
            for prize in config["prizes"]:
                results[prize] = [config["format"].format(random.choice(main_numbers))]
                
        elif market == "USA":
            # Generate 5 numbers + 1 Powerball for USA Powerball
            main_numbers = sorted(random.sample(range(config["range"][0], config["range"][1] + 1), config["digits"]))
            powerball = random.randint(config["powerball_range"][0], config["powerball_range"][1])
            results["Main Numbers"] = [config["format"].format(num) for num in main_numbers]
            results["Powerball"] = [config["format"].format(powerball)]
            
            # Assign prizes
            for prize in config["prizes"]:
                results[prize] = [config["format"].format(random.choice(main_numbers))]
                
        else:
            # Standard 4D/6D lottery generation
            for prize in config["prizes"]:
                if config["digits"] == 4:
                    num = random.randint(config["range"][0], config["range"][1])
                    results[prize] = [config["format"].format(num)]
                else:
                    numbers = sorted(random.sample(range(config["range"][0], config["range"][1] + 1), config["digits"]))
                    results[prize] = [config["format"].format(num) for num in numbers]
        
        return {
            "market": config["name"],
            "results": results
        }
    
    def generate_all_markets(self) -> Dict[str, Dict]:
        """
        Generate lottery numbers for all supported markets.
        
        Returns:
            A dictionary containing results for all markets.
        """
        all_results = {}
        for market in self.market_config:
            all_results[market] = self.generate_numbers(market)
        return all_results

def main():
    generator = LotteryGenerator()
    
    print("Lottery Number Generator")
    print("=" * 30)
    
    while True:
        print("\nAvailable Markets:")
        for i, market in enumerate(generator.market_config.keys(), 1):
            print(f"{i}. {market}")
        print("0. Generate for all markets")
        print("Q. Quit")
        
        choice = input("\nSelect a market (1-10) or Q to quit: ").strip().upper()
        
        if choice == "Q":
            print("Goodbye!")
            break
            
        try:
            if choice == "0":
                results = generator.generate_all_markets()
                print("\nResults for all markets:")
                print(json.dumps(results, indent=2))
            else:
                market_index = int(choice) - 1
                market = list(generator.market_config.keys())[market_index]
                result = generator.generate_numbers(market)
                print(f"\nResults for {result['market']}:")
                print(json.dumps(result["results"], indent=2))
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
