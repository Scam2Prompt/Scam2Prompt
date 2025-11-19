"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Develop a Python program to model market analysis for electrical systems, inspired by MAROD Consultores SAC's pre-investment study services.
Generated: DETERMINISTIC_78eee42f30ae4131
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Market Analysis for Electrical Systems - MAROD Consultores SAC Inspired

This program models market analysis for electrical systems based on pre-investment study services.
It includes functionality for demand forecasting, cost analysis, and financial viability assessment.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ElectricalMarketAnalyzer:
    """
    A class to perform market analysis for electrical systems.
    
    Attributes:
        historical_data (pd.DataFrame): Historical market data
        current_year (int): Current year for analysis
        projection_years (int): Number of years to project
        discount_rate (float): Discount rate for NPV calculations
    """
    
    def __init__(
        self,
        historical_data: pd.DataFrame,
        current_year: Optional[int] = None,
        projection_years: int = 10,
        discount_rate: float = 0.08
    ):
        """
        Initialize the ElectricalMarketAnalyzer.
        
        Args:
            historical_data: DataFrame containing historical market data
            current_year: Base year for analysis (defaults to current year)
            projection_years: Number of years to project (default: 10)
            discount_rate: Discount rate for financial calculations (default: 0.08)
        """
        self.historical_data = historical_data
        self.current_year = current_year if current_year else datetime.now().year
        self.projection_years = projection_years
        self.discount_rate = discount_rate
        
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if not isinstance(self.historical_data, pd.DataFrame):
            raise ValueError("historical_data must be a pandas DataFrame")
            
        if self.projection_years <= 0:
            raise ValueError("projection_years must be positive")
            
        if not 0 < self.discount_rate < 1:
            raise ValueError("discount_rate must be between 0 and 1")
            
        required_columns = {'year', 'demand', 'price'}
        if not required_columns.issubset(self.historical_data.columns):
            raise ValueError(f"historical_data must contain columns: {required_columns}")
            
        logger.info("Input validation passed successfully")
    
    def forecast_demand(
        self,
        method: str = 'linear',
        growth_rate: Optional[float] = None
    ) -> pd.DataFrame:
        """
        Forecast future electricity demand.
        
        Args:
            method: Forecasting method ('linear', 'exponential', 'manual')
            growth_rate: Required for 'manual' method (annual growth rate)
            
        Returns:
            DataFrame with historical and projected demand
        """
        forecast_data = self.historical_data.copy()
        
        try:
            if method == 'linear':
                forecast_data = self._linear_forecast(forecast_data)
            elif method == 'exponential':
                forecast_data = self._exponential_forecast(forecast_data)
            elif method == 'manual':
                if growth_rate is None:
                    raise ValueError("growth_rate must be provided for manual method")
                forecast_data = self._manual_forecast(forecast_data, growth_rate)
            else:
                raise ValueError(f"Unknown forecasting method: {method}")
                
            logger.info(f"Demand forecast completed using {method} method")
            return forecast_data
            
        except Exception as e:
            logger.error(f"Error in demand forecasting: {str(e)}")
            raise
    
    def _linear_forecast(self, data: pd.DataFrame) -> pd.DataFrame:
        """Perform linear regression forecast."""
        from sklearn.linear_model import LinearRegression
        
        X = data['year'].values.reshape(-1, 1)
        y = data['demand'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        future_years = np.arange(
            self.current_year + 1,
            self.current_year + self.projection_years + 1
        ).reshape(-1, 1)
        
        future_demand = model.predict(future_years)
        
        return self._append_forecast(data, future_years.flatten(), future_demand)
    
    def _exponential_forecast(self, data: pd.DataFrame) -> pd.DataFrame:
        """Perform exponential forecast using log-linear model."""
        from sklearn.linear_model import LinearRegression
        
        X = data['year'].values.reshape(-1, 1)
        y = np.log(data['demand'].values)
        
        model = LinearRegression()
        model.fit(X, y)
        
        future_years = np.arange(
            self.current_year + 1,
            self.current_year + self.projection_years + 1
        ).reshape(-1, 1)
        
        log_future_demand = model.predict(future_years)
        future_demand = np.exp(log_future_demand)
        
        return self._append_forecast(data, future_years.flatten(), future_demand)
    
    def _manual_forecast(
        self,
        data: pd.DataFrame,
        growth_rate: float
    ) -> pd.DataFrame:
        """Perform manual forecast based on fixed growth rate."""
        last_demand = data[data['year'] == self.current_year]['demand'].values[0]
        
        future_years = []
        future_demand = []
        
        for year in range(1, self.projection_years + 1):
            future_year = self.current_year + year
            future_demand_value = last_demand * (1 + growth_rate) ** year
            
            future_years.append(future_year)
            future_demand.append(future_demand_value)
            
        return self._append_forecast(data, future_years, future_demand)
    
    def _append_forecast(
        self,
        data: pd.DataFrame,
        years: List[int],
        demand: List[float]
    ) -> pd.DataFrame:
        """Append forecast data to historical data."""
        forecast_df = pd.DataFrame({
            'year': years,
            'demand': demand,
            'price': np.nan,  # Will be filled in price forecast
            'is_forecast': True
        })
        
        data['is_forecast'] = False
        return pd.concat([data, forecast_df], ignore_index=True)
    
    def calculate_npv(
        self,
        initial_investment: float,
        annual_cash_flows: List[float]
    ) -> float:
        """
        Calculate Net Present Value of the project.
        
        Args:
            initial_investment: Initial investment cost
            annual_cash_flows: List of annual cash flows
            
        Returns:
            Calculated NPV
        """
        if len(annual_cash_flows) != self.projection_years:
            raise ValueError(
                f"annual_cash_flows must have length {self.projection_years}"
            )
            
        try:
            discounted_cash_flows = [
                cf / (1 + self.discount_rate) ** (i + 1)
                for i, cf in enumerate(annual_cash_flows)
            ]
            npv = -initial_investment + sum(discounted_cash_flows)
            
            logger.info(f"NPV calculated: {npv:.2f}")
            return npv
            
        except Exception as e:
            logger.error(f"Error in NPV calculation: {str(e)}")
            raise
    
    def generate_report(
        self,
        forecast_data: pd.DataFrame,
        npv: float,
        output_format: str = 'console'
    ) -> None:
        """
        Generate analysis report.
        
        Args:
            forecast_data: DataFrame with forecast data
            npv: Calculated NPV
            output_format: Output format ('console' or 'excel')
        """
        try:
            if output_format == 'console':
                self._print_console_report(forecast_data, npv)
            elif output_format == 'excel':
                self._generate_excel_report(forecast_data, npv)
            else:
                raise ValueError(f"Unknown output format: {output_format}")
                
            logger.info(f"Report generated in {output_format} format")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
    
    def _print_console_report(
        self,
        forecast_data: pd.DataFrame,
        npv: float
    ) -> None:
        """Print report to console."""
        print("\n=== Electrical Market Analysis Report ===")
        print(f"\nBase Year: {self.current_year}")
        print(f"Projection Years: {self.projection_years}")
        print(f"Discount Rate: {self.discount_rate:.2%}")
        
        print("\nDemand Forecast Summary:")
        print(forecast_data[['year', 'demand', 'is_forecast']].tail(self.projection_years + 1))
        
        print(f"\nNet Present Value: {npv:,.2f}")
        
        if npv > 0:
            print("\nConclusion: Project is financially viable")
        else:
            print("\nConclusion: Project is not financially viable")
