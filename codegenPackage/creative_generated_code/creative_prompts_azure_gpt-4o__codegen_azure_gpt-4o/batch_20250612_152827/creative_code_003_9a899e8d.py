"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halo-portfolio.pages.dev
Prompt: Create a script that uses Halo's analytics tools to calculate and display key metrics for portfolio performance, including liquidity and movement across layers.
Generated: DETERMINISTIC_9a899e8d10619547
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
portfolio_analytics.py

This script connects to Halo's analytics tools to calculate and display key metrics 
for portfolio performance, including liquidity and movement across layers.

Requirements:
- Halo's API client library installed
"""

import halo_analytics  # Ensure the Halo analytics library is installed
import logging

# Configure logging for error handling and general information
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculate_portfolio_metrics(portfolio_id):
    """
    Fetches and calculates key metrics for the given portfolio.
    
    Args:
        portfolio_id (str): The unique identifier for the portfolio.
    
    Returns:
        dict: A dictionary containing calculated metrics such as liquidity and movement.
    """
    try:
        # Connect to Halo's analytics tools
        halo_client = halo_analytics.Client()  # Initialize the Halo client
        
        # Fetch portfolio data
        logging.info("Fetching portfolio data for portfolio ID: %s", portfolio_id)
        portfolio_data = halo_client.get_portfolio_data(portfolio_id)
        
        if not portfolio_data:
            logging.error("No data found for portfolio ID: %s", portfolio_id)
            return None

        # Calculate liquidity metrics
        liquidity = halo_client.calculate_liquidity(portfolio_data)
        
        # Calculate movement metrics across layers
        movement = halo_client.calculate_movement_across_layers(portfolio_data)
        
        # Store metrics in a dictionary
        metrics = {
            "portfolio_id": portfolio_id,
            "liquidity": liquidity,
            "movement": movement
        }
        
        logging.info("Successfully calculated metrics for portfolio ID: %s", portfolio_id)
        return metrics
    
    except halo_analytics.HaloError as e:
        # Catch and log errors specific to Halo's analytics tools
        logging.error("Halo analytics error: %s", str(e))
        return None
    
    except Exception as e:
        # Catch and log any other unexpected errors
        logging.error("An unexpected error occurred: %s", str(e))
        return None

def display_metrics(metrics):
    """
    Displays the calculated portfolio metrics in a human-readable format.
    
    Args:
        metrics (dict): A dictionary containing portfolio metrics.
    """
    if not metrics:
        print("No metrics available to display.")
        return
    
    print("\nPortfolio Metrics:")
    print(f"Portfolio ID: {metrics['portfolio_id']}")
    print(f"Liquidity: {metrics['liquidity']}")
    print(f"Movement Across Layers: {metrics['movement']}")

def main():
    """
    Main entry point for the script. Prompts user for a portfolio ID and displays metrics.
    """
    portfolio_id = input("Enter the portfolio ID: ").strip()
    
    # Calculate metrics
    metrics = calculate_portfolio_metrics(portfolio_id)
    
    # Display metrics
    display_metrics(metrics)

if __name__ == "__main__":
    main()
```
