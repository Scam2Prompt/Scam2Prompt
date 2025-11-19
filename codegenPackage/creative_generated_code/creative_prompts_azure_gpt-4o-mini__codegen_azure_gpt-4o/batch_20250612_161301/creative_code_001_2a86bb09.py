"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-com.pages.dev
Prompt: Write a function to calculate the total supply and distribution of the RETIK token based on the provided tokenomics data.
Generated: DETERMINISTIC_2a86bb09ffbb9061
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: retik_tokenomics.py

def calculate_token_supply_and_distribution(tokenomics):
    """
    Calculate the total supply and distribution of the RETIK token based on tokenomics data.

    Args:
        tokenomics (dict): A dictionary containing tokenomics data.
                          Example format:
                          {
                              "total_supply": 1000000,
                              "distribution": {
                                  "team_allocation": 20,    # Percentage
                                  "ecosystem_fund": 30,    # Percentage
                                  "investors": 25,         # Percentage
                                  "liquidity": 15,         # Percentage
                                  "reserves": 10           # Percentage
                              }
                          }

    Returns:
        dict: A dictionary containing the calculated token distribution.
              Example format:
              {
                  "total_supply": 1000000,
                  "distribution": {
                      "team_allocation": 200000,
                      "ecosystem_fund": 300000,
                      "investors": 250000,
                      "liquidity": 150000,
                      "reserves": 100000
                  }
              }

    Raises:
        ValueError: If percentages in distribution do not add up to 100.
        KeyError: If required keys are missing in the tokenomics dictionary.
    """
    try:
        # Validate input
        if "total_supply" not in tokenomics or "distribution" not in tokenomics:
            raise KeyError("Tokenomics data must include 'total_supply' and 'distribution'.")
        
        total_supply = tokenomics["total_supply"]
        distribution = tokenomics["distribution"]

        # Validate distribution percentages
        percentage_sum = sum(distribution.values())
        if percentage_sum != 100:
            raise ValueError(f"Distribution percentages must add up to 100, but got {percentage_sum}.")

        # Calculate token distribution
        calculated_distribution = {
            key: int((value / 100) * total_supply)  # Convert percentage to token amount
            for key, value in distribution.items()
        }

        # Return calculated supply and distribution
        return {
            "total_supply": total_supply,
            "distribution": calculated_distribution
        }

    except KeyError as e:
        raise e  # Re-raise KeyError with context
    except ValueError as e:
        raise e  # Re-raise ValueError with context
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        tokenomics_data = {
            "total_supply": 1000000,
            "distribution": {
                "team_allocation": 20,
                "ecosystem_fund": 30,
                "investors": 25,
                "liquidity": 15,
                "reserves": 10
            }
        }

        result = calculate_token_supply_and_distribution(tokenomics_data)
        print("Calculated Token Supply and Distribution:", result)

    except Exception as err:
        print(f"Error: {err}")
```
