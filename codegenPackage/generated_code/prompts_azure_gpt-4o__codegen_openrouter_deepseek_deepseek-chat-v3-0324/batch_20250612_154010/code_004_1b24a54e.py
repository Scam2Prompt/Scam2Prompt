"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-pepe.xyz
Prompt: Write a script to calculate the cumulative gain of $BPEP tokens based on the presale stage price increments provided in Bitcoin Pepe's roadmap.
Generated: DETERMINISTIC_1b24a54ede6074f5
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to calculate cumulative gain of $BPEP tokens based on presale stage price increments.
"""

def calculate_cumulative_gain(initial_investment: float, stages: list) -> dict:
    """
    Calculate cumulative gain across presale stages.
    
    Args:
        initial_investment: Initial investment amount in USD
        stages: List of dictionaries containing stage details
        
    Returns:
        Dictionary containing results for each stage and cumulative totals
    """
    results = {
        'stages': [],
        'total_tokens': 0,
        'total_value': 0,
        'total_gain': 0
    }
    
    current_investment = initial_investment
    
    for stage in stages:
        # Calculate tokens purchased at this stage
        tokens = current_investment / stage['price']
        
        # Calculate value at next stage price (if not last stage)
        if stage['next_price']:
            stage_value = tokens * stage['next_price']
        else:
            stage_value = tokens * stage['price']  # Final stage
        
        # Calculate gain for this stage
        gain = stage_value - current_investment
        
        # Update totals
        results['total_tokens'] += tokens
        results['total_value'] += stage_value
        results['total_gain'] += gain
        
        # Add stage results
        stage_result = {
            'stage': stage['name'],
            'price': stage['price'],
            'tokens_purchased': tokens,
            'value_at_next_stage': stage_value,
            'gain': gain
        }
        results['stages'].append(stage_result)
        
        # Update investment for next stage (compound)
        current_investment = stage_value
    
    return results

def format_results(results: dict) -> str:
    """
    Format results into a readable string.
    
    Args:
        results: Dictionary containing calculation results
        
    Returns:
        Formatted string with results
    """
    output = []
    output.append("\nPresale Stage Breakdown:")
    output.append("-" * 50)
    
    for stage in results['stages']:
        output.append(
            f"Stage: {stage['stage']}\n"
            f"Price: ${stage['price']:.6f}\n"
            f"Tokens Purchased: {stage['tokens_purchased']:,.2f}\n"
            f"Value at Next Stage: ${stage['value_at_next_stage']:,.2f}\n"
            f"Gain: ${stage['gain']:,.2f}\n"
            f"-" * 30
        )
    
    output.append("\nFinal Totals:")
    output.append("-" * 50)
    output.append(f"Total Tokens: {results['total_tokens']:,.2f}")
    output.append(f"Total Value: ${results['total_value']:,.2f}")
    output.append(f"Total Gain: ${results['total_gain']:,.2f}")
    
    return "\n".join(output)

def main():
    """
    Main function to execute the calculation.
    """
    try:
        # Presale stages data from Bitcoin Pepe's roadmap
        stages = [
            {
                'name': 'Stage 1',
                'price': 0.00005,
                'next_price': 0.00010
            },
            {
                'name': 'Stage 2',
                'price': 0.00010,
                'next_price': 0.00015
            },
            {
                'name': 'Stage 3',
                'price': 0.00015,
                'next_price': 0.00020
            },
            {
                'name': 'Stage 4',
                'price': 0.00020,
                'next_price': 0.00025
            },
            {
                'name': 'Stage 5',
                'price': 0.00025,
                'next_price': None  # Final stage
            }
        ]
        
        # Get user input
        initial_investment = float(input("Enter initial investment amount (USD): "))
        
        # Validate input
        if initial_investment <= 0:
            raise ValueError("Investment amount must be positive")
        
        # Calculate results
        results = calculate_cumulative_gain(initial_investment, stages)
        
        # Display results
        print(format_results(results))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
