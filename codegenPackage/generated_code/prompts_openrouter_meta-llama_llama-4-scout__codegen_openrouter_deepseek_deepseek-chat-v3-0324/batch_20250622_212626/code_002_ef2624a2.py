"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Generate a code example for a real estate investment analysis tool that focuses on value creation and asset appreciation, inspired by Alghanim Capital's real estate investment arm."
Generated: DETERMINISTIC_ef2624a2dad2197d
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class RealEstateInvestmentAnalyzer:
    """
    A tool for analyzing real estate investments with a focus on value creation and asset appreciation.
    Inspired by Alghanim Capital's real estate investment approach.
    """
    
    def __init__(self):
        self.properties = {}
        self.market_data = pd.DataFrame()
        
    def add_property(self, 
                    property_id: str, 
                    purchase_price: float, 
                    purchase_date: str, 
                    location: str, 
                    property_type: str,
                    initial_rent: float = 0.0) -> None:
        """
        Add a property to the investment portfolio.
        
        Args:
            property_id: Unique identifier for the property
            purchase_price: Purchase price in USD
            purchase_date: Date of purchase (YYYY-MM-DD)
            location: Geographic location
            property_type: Type of property (residential, commercial, etc.)
            initial_rent: Monthly rental income (default 0.0)
        """
        try:
            purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d").date()
            self.properties[property_id] = {
                'purchase_price': purchase_price,
                'purchase_date': purchase_date,
                'location': location,
                'property_type': property_type,
                'current_value': purchase_price,  # Will be updated with market data
                'rental_income': initial_rent,
                'improvements': [],
                'expenses': []
            }
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
            
    def add_market_data(self, 
                       location: str, 
                       property_type: str, 
                       date: str, 
                       value_index: float) -> None:
        """
        Add market data for property valuation.
        
        Args:
            location: Geographic location
            property_type: Type of property
            date: Date of market data (YYYY-MM-DD)
            value_index: Market value index (100 = base value)
        """
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            new_data = pd.DataFrame({
                'location': [location],
                'property_type': [property_type],
                'date': [date],
                'value_index': [value_index]
            })
            
            if self.market_data.empty:
                self.market_data = new_data
            else:
                self.market_data = pd.concat([self.market_data, new_data], ignore_index=True)
                
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
            
    def update_property_values(self, as_of_date: str) -> None:
        """
        Update property values based on market data.
        
        Args:
            as_of_date: Date for valuation (YYYY-MM-DD)
        """
        try:
            as_of_date = datetime.strptime(as_of_date, "%Y-%m-%d").date()
            
            for prop_id, prop_data in self.properties.items():
                location = prop_data['location']
                prop_type = prop_data['property_type']
                purchase_date = prop_data['purchase_date']
                
                # Get relevant market data
                market_data = self.market_data[
                    (self.market_data['location'] == location) & 
                    (self.market_data['property_type'] == prop_type)
                ].copy()
                
                if market_data.empty:
                    print(f"Warning: No market data for {location}, {prop_type}")
                    continue
                    
                # Get most recent market data before as_of_date
                market_data = market_data[market_data['date'] <= as_of_date]
                if market_data.empty:
                    print(f"Warning: No market data before {as_of_date} for {location}, {prop_type}")
                    continue
                    
                latest_market = market_data.loc[market_data['date'].idxmax()]
                
                # Get market data at purchase date (or closest before)
                purchase_market = market_data[market_data['date'] <= purchase_date]
                if purchase_market.empty:
                    print(f"Warning: No market data before purchase date {purchase_date} for {location}, {prop_type}")
                    continue
                    
                purchase_market = purchase_market.loc[purchase_market['date'].idxmax()]
                
                # Calculate appreciation
                appreciation_factor = latest_market['value_index'] / purchase_market['value_index']
                self.properties[prop_id]['current_value'] = prop_data['purchase_price'] * appreciation_factor
                
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
            
    def add_improvement(self, 
                       property_id: str, 
                       description: str, 
                       cost: float, 
                       date: str, 
                       expected_value_add: float) -> None:
        """
        Record a property improvement that adds value.
        
        Args:
            property_id: Property ID
            description: Description of improvement
            cost: Cost of improvement
            date: Date of improvement (YYYY-MM-DD)
            expected_value_add: Expected increase in property value
        """
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            self.properties[property_id]['improvements'].append({
                'description': description,
                'cost': cost,
                'date': date,
                'expected_value_add': expected_value_add
            })
            # Immediately apply the value add
            self.properties[property_id]['current_value'] += expected_value_add
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
        except KeyError:
            raise KeyError(f"Property ID {property_id} not found")
            
    def add_expense(self, 
                    property_id: str, 
                    description: str, 
                    amount: float, 
                    date: str, 
                    category: str) -> None:
        """
        Record an expense related to the property.
        
        Args:
            property_id: Property ID
            description: Description of expense
            amount: Amount in USD
            date: Date of expense (YYYY-MM-DD)
            category: Expense category
        """
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            self.properties[property_id]['expenses'].append({
                'description': description,
                'amount': amount,
                'date': date,
                'category': category
            })
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
        except KeyError:
            raise KeyError(f"Property ID {property_id} not found")
            
    def calculate_roi(self, property_id: str, as_of_date: str) -> Dict[str, float]:
        """
        Calculate return on investment metrics for a property.
        
        Args:
            property_id: Property ID
            as_of_date: Date for ROI calculation (YYYY-MM-DD)
            
        Returns:
            Dictionary containing ROI metrics
        """
        try:
            as_of_date = datetime.strptime(as_of_date, "%Y-%m-%d").date()
            prop_data = self.properties[property_id]
            
            # Total capital invested
            total_investment = prop_data['purchase_price']
            for improvement in prop_data['improvements']:
                if improvement['date'] <= as_of_date:
                    total_investment += improvement['cost']
            
            # Current value
            current_value = prop_data['current_value']
            
            # Total expenses
            total_expenses = sum(
                exp['amount'] for exp in prop_data['expenses'] 
                if exp['date'] <= as_of_date
            )
            
            # Total rental income
            purchase_date = prop_data['purchase_date']
            months_owned = ((as_of_date.year - purchase_date.year) * 12 + 
                          (as_of_date.month - purchase_date.month))
            total_rental = prop_data['rental_income'] * months_owned
            
            # ROI calculations
            appreciation = current_value - total_investment
            cash_flow = total_rental - total_expenses
            total_return = appreciation + cash_flow
            roi_percentage = (total_return / total_investment) * 100
            
            return {
                'total_investment': total_investment,
                'current_value': current_value,
                'appreciation': appreciation,
                'total_rental_income': total_rental,
                'total_expenses': total_expenses,
                'cash_flow': cash_flow,
                'total_return': total_return,
                'roi_percentage': roi_percentage
            }
            
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
        except KeyError:
            raise KeyError(f"Property ID {property_id} not found")
            
    def portfolio_summary(self, as_of_date: str) -> Dict[str, float]:
        """
        Generate a summary of the entire investment portfolio.
        
        Args:
            as_of_date:
