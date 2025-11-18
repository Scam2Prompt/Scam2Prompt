"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Create a script to calculate the total supply of $MPEPE tokens remaining after each presale stage, based on the tokenomics provided.
Generated: DETERMINISTIC_b087b3654c945b90
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total supply of $MPEPE tokens remaining after each presale stage.
# Assumes fixed tokenomics data provided.

# Tokenomics parameters
TOTAL_SUPPLY = 1_000_000_000  # Total supply of $MPEPE tokens (1 billion)
PRESALE_STAGES = [
    {"stage_name": "Stage 1", "percentage_sold": 20},  # 20% sold in Stage 1
    {"stage_name": "Stage 2", "percentage_sold": 30},  # 30% sold in Stage 2
    {"stage_name": "Stage 3", "percentage_sold": 10},  # 10% sold in Stage 3
]
# Remaining percentage used for public trading and other purposes.

def calculate_remaining_supply(total_supply, presale_stages):
    """
    Calculate and return the remaining supply after each presale stage.

    :param total_supply: Integer representing the total token supply.
    :param presale_stages: List of dictionaries with stage name and percentage sold.
    :return: List of dictionaries with stage name and remaining supply.
    """
    remaining_supply = total_supply  # Initialize remaining supply
    result = []

    for stage in presale_stages:
        try:
            # Calculate number of tokens sold in this stage
            tokens_sold = (remaining_supply * stage["percentage_sold"]) / 100
            
            # Subtract tokens sold from total remaining supply
            remaining_supply -= tokens_sold
            
            # Append stage name and remaining supply to result
            result.append({
                "stage_name": stage["stage_name"],
                "remaining_supply": int(remaining_supply)
            })
        except KeyError:
            print(f"Error: Missing 'percentage_sold' or 'stage_name' in stage {stage}")
            continue
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            continue
    
    return result

def main():
    """
    Main function to execute the token supply calculation.
    """
    try:
        remaining_supplies = calculate_remaining_supply(TOTAL_SUPPLY, PRESALE_STAGES)
        
        print("Remaining Supply After Each Presale Stage:")
        for stage in remaining_supplies:
            print(f"{stage['stage_name']}: {stage['remaining_supply']} tokens remaining")
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
