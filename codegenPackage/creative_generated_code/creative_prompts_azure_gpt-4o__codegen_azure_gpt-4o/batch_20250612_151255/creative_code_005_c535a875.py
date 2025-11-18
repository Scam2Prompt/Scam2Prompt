"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-beef-meme.pages.dev
Prompt: Create a Python script to calculate the percentage of BEEF Coin distribution across DEX liquidity pools, CEX liquidity pools, and airdrops based on the tokenomics provided.
Generated: DETERMINISTIC_c535a875e98b0978
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the percentage distribution of BEEF Coin across different categories
# Categories: DEX liquidity pools, CEX liquidity pools, and airdrops

def calculate_distribution(total_supply, dex_allocation, cex_allocation, airdrop_allocation):
    """
    Calculate the percentage distribution of BEEF Coin across tokenomics categories.
    
    Args:
        total_supply (float): Total supply of BEEF Coin.
        dex_allocation (float): Amount allocated to DEX liquidity pools.
        cex_allocation (float): Amount allocated to CEX liquidity pools.
        airdrop_allocation (float): Amount allocated for airdrops.

    Returns:
        dict: A dictionary containing percentage distribution of each category.
    """
    try:
        # Validate inputs
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if dex_allocation < 0 or cex_allocation < 0 or airdrop_allocation < 0:
            raise ValueError("Allocation amounts cannot be negative.")
        if dex_allocation + cex_allocation + airdrop_allocation != total_supply:
            raise ValueError("Allocation amounts must sum up to the total supply.")

        # Calculate percentages
        dex_percentage = (dex_allocation / total_supply) * 100
        cex_percentage = (cex_allocation / total_supply) * 100
        airdrop_percentage = (airdrop_allocation / total_supply) * 100

        # Return results as a dictionary
        return {
            "DEX Liquidity Pools": round(dex_percentage, 2),
            "CEX Liquidity Pools": round(cex_percentage, 2),
            "Airdrops": round(airdrop_percentage, 2)
        }

    except ValueError as ve:
        # Handle input-related errors
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to execute the script. Prompts user input for tokenomics values
    and calculates the distribution percentages.
    """
    print("Welcome to the BEEF Coin distribution calculator.")
    
    try:
        # Gather user input
        total_supply = float(input("Enter the total supply of BEEF Coin: "))
        dex_allocation = float(input("Enter the amount allocated to DEX liquidity pools: "))
        cex_allocation = float(input("Enter the amount allocated to CEX liquidity pools: "))
        airdrop_allocation = float(input("Enter the amount allocated for airdrops: "))
        
        # Calculate distribution
        distribution = calculate_distribution(total_supply, dex_allocation, cex_allocation, airdrop_allocation)
        
        # Display results
        if distribution:
            print("\nBEEF Coin Distribution Percentages:")
            for category, percentage in distribution.items():
                print(f"{category}: {percentage}%")
        else:
            print("Failed to calculate distribution due to input errors.")

    except ValueError:
        print("Invalid input. Please provide numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
