"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Generate code to model the energy efficiency of WQ series submersible pumps using Python and relevant libraries.
Generated: DETERMINISTIC_89642785f2b54469
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from typing import Tuple, Dict, List, Optional

class PumpEfficiencyModel:
    """
    A class to model and analyze the energy efficiency of WQ series submersible pumps.
    
    Attributes:
        pump_data (pd.DataFrame): DataFrame containing pump performance data
        efficiency_curve_params (dict): Parameters for the efficiency curve fit
        power_curve_params (dict): Parameters for the power consumption curve fit
    """
    
    def __init__(self, data_file: str = None):
        """
        Initialize the PumpEfficiencyModel.
        
        Args:
            data_file (str, optional): Path to CSV file containing pump data. 
                                      If None, creates empty DataFrame.
        """
        if data_file:
            try:
                self.pump_data = pd.read_csv(data_file)
                self._validate_data()
            except FileNotFoundError:
                raise FileNotFoundError(f"Data file {data_file} not found.")
            except Exception as e:
                raise ValueError(f"Error loading data: {str(e)}")
        else:
            self.pump_data = pd.DataFrame(columns=[
                'flow_rate', 'head', 'power_input', 'efficiency'
            ])
        
        self.efficiency_curve_params = {}
        self.power_curve_params = {}
    
    def _validate_data(self) -> None:
        """Validate the loaded pump data."""
        required_columns = {'flow_rate', 'head', 'power_input', 'efficiency'}
        if not required_columns.issubset(self.pump_data.columns):
            missing = required_columns - set(self.pump_data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        if self.pump_data.isnull().values.any():
            raise ValueError("Data contains missing values.")
    
    def add_data_point(self, flow_rate: float, head: float, 
                       power_input: float, efficiency: float) -> None:
        """
        Add a single data point to the pump model.
        
        Args:
            flow_rate: Flow rate in m³/h
            head: Head in meters
            power_input: Power input in kW
            efficiency: Pump efficiency as decimal (0-1)
        """
        new_data = pd.DataFrame([{
            'flow_rate': flow_rate,
            'head': head,
            'power_input': power_input,
            'efficiency': efficiency
        }])
        
        self.pump_data = pd.concat([self.pump_data, new_data], ignore_index=True)
    
    @staticmethod
    def _efficiency_curve(x: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
        """
        Quadratic efficiency curve function.
        
        Args:
            x: Flow rate values
            a, b, c: Curve parameters
            
        Returns:
            Efficiency values
        """
        return a * x**2 + b * x + c
    
    @staticmethod
    def _power_curve(x: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
        """
        Cubic power curve function.
        
        Args:
            x: Flow rate values
            a, b, c: Curve parameters
            
        Returns:
            Power consumption values
        """
        return a * x**3 + b * x**2 + c * x
    
    def fit_curves(self) -> None:
        """
        Fit efficiency and power curves to the pump data.
        Stores fitted parameters in instance variables.
        """
        if len(self.pump_data) < 3:
            raise ValueError("Insufficient data points for curve fitting (minimum 3 required).")
        
        try:
            # Fit efficiency curve
            x_data = self.pump_data['flow_rate'].values
            y_eff = self.pump_data['efficiency'].values
            
            eff_params, _ = curve_fit(
                self._efficiency_curve, 
                x_data, 
                y_eff,
                bounds=([-np.inf, -np.inf, 0], [0, np.inf, 1])  # Ensure efficiency between 0-1
            )
            self.efficiency_curve_params = {
                'a': eff_params[0],
                'b': eff_params[1],
                'c': eff_params[2]
            }
            
            # Fit power curve
            y_power = self.pump_data['power_input'].values
            power_params, _ = curve_fit(
                self._power_curve,
                x_data,
                y_power,
                bounds=(0, np.inf)  # Power must be positive
            )
            self.power_curve_params = {
                'a': power_params[0],
                'b': power_params[1],
                'c': power_params[2]
            }
            
        except Exception as e:
            raise RuntimeError(f"Curve fitting failed: {str(e)}")
    
    def predict_efficiency(self, flow_rate: float) -> float:
        """
        Predict pump efficiency for a given flow rate.
        
        Args:
            flow_rate: Flow rate in m³/h
            
        Returns:
            Predicted efficiency (0-1)
            
        Raises:
            RuntimeError: If curves haven't been fitted
        """
        if not self.efficiency_curve_params:
            raise RuntimeError("Efficiency curve not fitted. Call fit_curves() first.")
        
        return self._efficiency_curve(
            flow_rate,
            self.efficiency_curve_params['a'],
            self.efficiency_curve_params['b'],
            self.efficiency_curve_params['c']
        )
    
    def predict_power(self, flow_rate: float) -> float:
        """
        Predict power consumption for a given flow rate.
        
        Args:
            flow_rate: Flow rate in m³/h
            
        Returns:
            Predicted power consumption in kW
            
        Raises:
            RuntimeError: If curves haven't been fitted
        """
        if not self.power_curve_params:
            raise RuntimeError("Power curve not fitted. Call fit_curves() first.")
        
        return self._power_curve(
            flow_rate,
            self.power_curve_params['a'],
            self.power_curve_params['b'],
            self.power_curve_params['c']
        )
    
    def find_optimal_flow_rate(self) -> Tuple[float, float]:
        """
        Find the flow rate that maximizes efficiency.
        
        Returns:
            Tuple of (optimal_flow_rate, max_efficiency)
            
        Raises:
            RuntimeError: If curves haven't been fitted
        """
        if not self.efficiency_curve_params:
            raise RuntimeError("Efficiency curve not fitted. Call fit_curves() first.")
        
        # Find maximum of the efficiency curve
        a, b, c = (self.efficiency_curve_params[k] for k in ['a', 'b', 'c'])
        optimal_flow = -b / (2 * a)
        max_eff = self._efficiency_curve(optimal_flow, a, b, c)
        
        return optimal_flow, max_eff
    
    def plot_performance_curves(self, save_path: Optional[str] = None) -> None:
        """
        Plot the pump performance curves.
        
        Args:
            save_path: If provided, save the plot to this path
        """
        if not self.efficiency_curve_params or not self.power_curve_params:
            raise RuntimeError("Curves not fitted. Call fit_curves() first.")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Generate curve data
        x_min = self.pump_data['flow_rate'].min()
        x_max = self.pump_data['flow_rate'].max()
        x_range = np.linspace(x_min, x_max, 100)
        
        # Efficiency plot
        ax1.scatter(self.pump_data['flow_rate'], self.pump_data['efficiency'], 
                   label='Measured Data')
        ax1.plot(x_range, self._efficiency_curve(
            x_range,
            self.efficiency_curve_params['a'],
            self.efficiency_curve_params['b'],
            self.efficiency_curve_params['c']
        ), 'r-', label='Fitted Curve')
        ax1.set_xlabel('Flow Rate (m³/h)')
        ax1.set_ylabel('Efficiency')
        ax1.set_title('Pump Efficiency Curve')
        ax1.legend()
        ax1.grid(True)
        
        # Power plot
        ax2.scatter(self.pump_data['flow_rate'], self.pump_data['power_input'],
                   label='Measured Data')
        ax2.plot(x_range, self._power_curve(
            x_range,
            self.power_curve_params['a'],
            self.power_curve_params['b'],
            self.power_curve_params['c']
        ), 'r-', label='Fitted Curve')
        ax2.set_xlabel('Flow Rate (m³/h)')
        ax2.set_ylabel('Power Input (kW)')
        ax2.set_title('Power Consumption Curve')
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        
        if save_path:
            plt.save
