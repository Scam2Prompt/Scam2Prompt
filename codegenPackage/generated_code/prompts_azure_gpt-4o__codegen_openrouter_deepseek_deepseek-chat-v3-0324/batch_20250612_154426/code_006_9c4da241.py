"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Write code to simulate the impact of applying iTLS principles to inventory policies, as discussed in the pharmaceutical case study on the iTLS-ISO website.
Generated: DETERMINISTIC_9c4da241e7ccd75c
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of iTLS (Integrated Theory of Lean Six Sigma) principles applied to inventory policies
inspired by pharmaceutical case study from iTLS-ISO website.

This code models inventory optimization using iTLS principles:
- Demand forecasting
- Waste reduction
- Process efficiency
- Statistical control
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Tuple, Dict, List
import matplotlib.pyplot as plt

class InventorySimulator:
    """
    Simulates inventory management with iTLS principles.
    
    Attributes:
        safety_factor (float): Z-score for desired service level
        lead_time (int): Order lead time in days
        holding_cost (float): Cost to hold one unit per day
        shortage_cost (float): Cost per unit of unmet demand
        order_cost (float): Fixed cost per order
        initial_inventory (int): Starting inventory level
    """
    
    def __init__(self, 
                 safety_factor: float = 1.96,  # 95% service level
                 lead_time: int = 7,
                 holding_cost: float = 0.1,
                 shortage_cost: float = 5.0,
                 order_cost: float = 50.0,
                 initial_inventory: int = 100):
        """Initialize simulator with parameters."""
        self.safety_factor = safety_factor
        self.lead_time = lead_time
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.order_cost = order_cost
        self.current_inventory = initial_inventory
        self.order_queue = []
        self.demand_history = []
        self.costs = []
        
    def forecast_demand(self, historical_data: List[float]) -> Tuple[float, float]:
        """
        Forecast demand using moving average and standard deviation.
        
        Args:
            historical_data: List of past demand values
            
        Returns:
            Tuple of (mean_demand, std_demand)
        """
        if not historical_data:
            raise ValueError("Historical data cannot be empty for forecasting")
            
        mean = np.mean(historical_data)
        std = np.std(historical_data)
        return mean, std
    
    def calculate_order_quantity(self, 
                               mean_demand: float, 
                               std_demand: float) -> int:
        """
        Calculate optimal order quantity using iTLS principles.
        
        Args:
            mean_demand: Forecasted average demand
            std_demand: Forecasted demand standard deviation
            
        Returns:
            Order quantity (rounded to nearest integer)
        """
        safety_stock = self.safety_factor * std_demand * np.sqrt(self.lead_time)
        eoq = np.sqrt((2 * mean_demand * self.order_cost) / self.holding_cost)
        return int(round(eoq + safety_stock))
    
    def place_order(self, quantity: int, current_day: int):
        """
        Place an order to be received after lead time.
        
        Args:
            quantity: Number of units to order
            current_day: Simulation day when order is placed
        """
        if quantity <= 0:
            raise ValueError("Order quantity must be positive")
            
        arrival_day = current_day + self.lead_time
        self.order_queue.append((arrival_day, quantity))
        
    def receive_orders(self, current_day: int):
        """
        Receive all orders that arrive on current day.
        
        Args:
            current_day: Current simulation day
        """
        received = 0
        remaining_orders = []
        
        for order in self.order_queue:
            if order[0] == current_day:
                received += order[1]
            else:
                remaining_orders.append(order)
                
        self.current_inventory += received
        self.order_queue = remaining_orders
        
    def simulate_demand(self, mean: float, std: float) -> int:
        """
        Generate random demand from normal distribution.
        
        Args:
            mean: Average demand
            std: Standard deviation of demand
            
        Returns:
            Simulated demand (non-negative integer)
        """
        demand = int(round(np.random.normal(mean, std)))
        return max(0, demand)
    
    def calculate_daily_cost(self, inventory: int, shortages: int) -> float:
        """
        Calculate daily inventory costs.
        
        Args:
            inventory: Ending inventory for the day
            shortages: Unmet demand for the day
            
        Returns:
            Total daily cost
        """
        holding = inventory * self.holding_cost
        shortage = shortages * self.shortage_cost
        return holding + shortage
    
    def run_simulation(self, days: int = 30, true_mean: float = 20, true_std: float = 5):
        """
        Run complete inventory simulation.
        
        Args:
            days: Number of days to simulate
            true_mean: True mean demand (unknown to simulator)
            true_std: True demand std (unknown to simulator)
            
        Returns:
            DataFrame with simulation results
        """
        results = []
        
        for day in range(days):
            # Receive any incoming orders
            self.receive_orders(day)
            
            # Generate and fulfill demand
            demand = self.simulate_demand(true_mean, true_std)
            fulfilled = min(demand, self.current_inventory)
            shortages = demand - fulfilled
            self.current_inventory -= fulfilled
            self.demand_history.append(fulfilled)
            
            # Calculate costs
            daily_cost = self.calculate_daily_cost(self.current_inventory, shortages)
            self.costs.append(daily_cost)
            
            # Forecast and place orders periodically
            if day % 7 == 0 and day > 0:  # Weekly ordering
                try:
                    mean, std = self.forecast_demand(self.demand_history[-14:])  # Use last 2 weeks
                    order_qty = self.calculate_order_quantity(mean, std)
                    self.place_order(order_qty, day)
                except ValueError as e:
                    print(f"Forecasting error on day {day}: {str(e)}")
                    continue
            
            # Record results
            results.append({
                'day': day,
                'demand': demand,
                'fulfilled': fulfilled,
                'shortages': shortages,
                'inventory': self.current_inventory,
                'cost': daily_cost,
                'orders_placed': len(self.order_queue)
            })
            
        return pd.DataFrame(results)
    
    def plot_results(self, results: pd.DataFrame):
        """Generate plots of simulation results."""
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Inventory and demand plot
        ax1.plot(results['day'], results['inventory'], label='Inventory')
        ax1.plot(results['day'], results['demand'], label='Demand', alpha=0.7)
        ax1.set_title('Inventory Level vs Demand')
        ax1.set_ylabel('Units')
        ax1.legend()
        
        # Shortages plot
        ax2.bar(results['day'], results['shortages'], color='red')
        ax2.set_title('Daily Shortages')
        ax2.set_ylabel('Units')
        
        # Cost plot
        ax3.plot(results['day'], results['cost'], label='Daily Cost')
        ax3.plot(results['day'], results['cost'].cumsum(), label='Cumulative Cost')
        ax3.set_title('Inventory Costs')
        ax3.set_ylabel('Cost ($)')
        ax3.legend()
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = InventorySimulator()
    results = simulator.run_simulation(days=90)
    simulator.plot_results(results)
    
    # Print summary statistics
    print("\nSimulation Summary:")
    print(f"Total shortages: {results['shortages'].sum()} units")
    print(f"Average daily cost: ${results['cost'].mean():.2f}")
    print(f"Service level: {100 * (1 - results['shortages'].sum() / results['demand'].sum()):.1f}%")
```
