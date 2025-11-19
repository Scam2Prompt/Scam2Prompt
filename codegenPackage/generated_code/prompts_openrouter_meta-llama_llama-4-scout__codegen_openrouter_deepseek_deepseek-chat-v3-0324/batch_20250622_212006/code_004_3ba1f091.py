"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Create a function to calculate returns on investment (ROI) for a real estate portfolio managed by a firm like Brexphil Inc.
Generated: DETERMINISTIC_3ba1f091d3d703ec
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Union

def calculate_roi(
    initial_investment: float,
    current_value: float,
    holding_period_years: float = 1.0,
    expenses: float = 0.0,
    income: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    Calculate Return on Investment (ROI) for real estate properties.
    
    Args:
        initial_investment: Initial investment amount
        current_value: Current market value of the property
        holding_period_years: Time period in years (default 1 year)
        expenses: Total expenses incurred during holding period
        income: Total income generated during holding period
        
    Returns:
        Dictionary containing:
            - simple_roi: Simple ROI percentage
            - annualized_roi: Annualized ROI percentage
            - net_profit: Net profit amount
            - roi_formula: Formula used for calculation
    """
    try:
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        if holding_period_years <= 0:
            raise ValueError("Holding period must be positive")
        
        # Calculate net profit
        net_profit = (current_value - initial_investment) + (income - expenses)
        
        # Calculate simple ROI
        simple_roi = (net_profit / initial_investment) * 100
        
        # Calculate annualized ROI
        annualized_roi = ((1 + (net_profit / initial_investment)) ** (1 / holding_period_years) - 1) * 100
        
        return {
            "simple_roi": round(simple_roi, 2),
            "annualized_roi": round(annualized_roi, 2),
            "net_profit": round(net_profit, 2),
            "roi_formula": "ROI = ((Current Value - Initial Investment) + (Income - Expenses)) / Initial Investment"
        }
        
    except ValueError as ve:
        return {"error": str(ve)}
    except ZeroDivisionError:
        return {"error": "Initial investment cannot be zero"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

def calculate_portfolio_roi(
    properties: List[Dict[str, float]]
) -> Dict[str, Union[float, Dict]]:
    """
    Calculate aggregate ROI metrics for a portfolio of properties.
    
    Args:
        properties: List of property dictionaries containing:
            - initial_investment
            - current_value
            - holding_period_years (optional)
            - expenses (optional)
            - income (optional)
            
    Returns:
        Dictionary containing:
            - portfolio_roi: Overall portfolio ROI
            - weighted_avg_annualized_roi: Weighted average annualized ROI
            - total_net_profit: Sum of net profits across all properties
            - property_results: Individual ROI results for each property
    """
    try:
        if not properties:
            raise ValueError("Property list cannot be empty")
            
        total_initial = 0.0
        total_net_profit = 0.0
        weighted_roi_sum = 0.0
        property_results = []
        
        for prop in properties:
            # Set default values if not provided
            prop.setdefault('holding_period_years', 1.0)
            prop.setdefault('expenses', 0.0)
            prop.setdefault('income', 0.0)
            
            # Calculate individual property ROI
            roi_result = calculate_roi(
                initial_investment=prop['initial_investment'],
                current_value=prop['current_value'],
                holding_period_years=prop['holding_period_years'],
                expenses=prop['expenses'],
                income=prop['income']
            )
            
            if 'error' in roi_result:
                return {"error": f"Error calculating ROI for property: {roi_result['error']}"}
                
            property_results.append(roi_result)
            
            # Aggregate values for portfolio calculation
            total_initial += prop['initial_investment']
            total_net_profit += roi_result['net_profit']
            
            # Calculate weight for this property
            weight = prop['initial_investment'] / total_initial if total_initial > 0 else 0
            weighted_roi_sum += roi_result['annualized_roi'] * weight
            
        # Calculate portfolio metrics
        portfolio_roi = (total_net_profit / total_initial) * 100 if total_initial > 0 else 0
        
        return {
            "portfolio_roi": round(portfolio_roi, 2),
            "weighted_avg_annualized_roi": round(weighted_roi_sum, 2),
            "total_net_profit": round(total_net_profit, 2),
            "property_results": property_results
        }
        
    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
```
