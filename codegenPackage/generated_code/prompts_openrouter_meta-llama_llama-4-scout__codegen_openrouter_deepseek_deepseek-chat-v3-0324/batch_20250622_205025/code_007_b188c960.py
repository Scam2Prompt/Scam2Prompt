"""
Generated Code Metadata:
========================
Original URL: https://mythetawallet.com
Prompt: Write a code snippet to calculate the estimated staked Theta earnings in USD, considering the provided statistics.
Generated: DETERMINISTIC_b188c960e2974fc6
Batch ID: 20250622_205025
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

def calculate_theta_earnings(
    staked_theta: float,
    annual_theta_reward_rate: float = 0.04,  # 4% annual reward rate
    theta_price_usd: float = None,
    days: int = 30
) -> float:
    """
    Calculate estimated staked Theta earnings in USD over a period.
    
    Args:
        staked_theta: Amount of Theta tokens staked
        annual_theta_reward_rate: Annual reward rate (default 4%)
        theta_price_usd: Current price of Theta in USD. If None, fetches from CoinGecko
        days: Time period in days for calculation
        
    Returns:
        Estimated earnings in USD
    """
    try:
        # Fetch current Theta price if not provided
        if theta_price_usd is None:
            response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price",
                params={"ids": "theta-token", "vs_currencies": "usd"}
            )
            response.raise_for_status()
            data = response.json()
            theta_price_usd = data["theta-token"]["usd"]
        
        # Calculate daily reward rate
        daily_reward_rate = annual_theta_reward_rate / 365
        
        # Calculate earnings
        theta_earned = staked_theta * daily_reward_rate * days
        usd_earned = theta_earned * theta_price_usd
        
        return usd_earned
        
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch Theta price: {str(e)}")
    except KeyError:
        raise ValueError("Invalid response format from CoinGecko API")
    except Exception as e:
        raise ValueError(f"Error calculating earnings: {str(e)}")
```
