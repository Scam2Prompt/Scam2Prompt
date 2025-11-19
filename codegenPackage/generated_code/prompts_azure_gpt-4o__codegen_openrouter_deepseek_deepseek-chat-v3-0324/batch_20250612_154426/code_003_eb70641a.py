"""
Generated Code Metadata:
========================
Original URL: https://pharmanet.org.pl
Prompt: Create a program that simulates the effects of pharmacy closures in Poland over time, incorporating the statistics and trends highlighted by PharmaNET.
Generated: DETERMINISTIC_eb70641a7188244f
Batch ID: 20250612_154426
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
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pharmacy_simulation.log'),
        logging.StreamHandler()
    ]
)

class Pharmacy:
    """Represents a single pharmacy with its properties and state."""
    
    def __init__(self, pharmacy_id: int, location: str, opening_date: datetime, size: float):
        """
        Initialize a pharmacy.
        
        Args:
            pharmacy_id: Unique identifier for the pharmacy
            location: City or region where the pharmacy is located
            opening_date: Date when the pharmacy was opened
            size: Size of the pharmacy in square meters
        """
        self.pharmacy_id = pharmacy_id
        self.location = location
        self.opening_date = opening_date
        self.size = size
        self.is_open = True
        self.closure_date = None
        self.monthly_revenue = random.uniform(50000, 200000)  # PLN
        self.operating_costs = random.uniform(30000, 150000)  # PLN
        self.employees = random.randint(2, 10)
        
    def calculate_profitability(self) -> float:
        """Calculate the monthly profitability of the pharmacy."""
        return self.monthly_revenue - self.operating_costs
    
    def simulate_month(self, economic_factor: float) -> bool:
        """
        Simulate one month of operation and determine if pharmacy stays open.
        
        Args:
            economic_factor: Multiplier affecting revenue (0.8-1.2)
            
        Returns:
            bool: True if pharmacy remains open, False if it closes
        """
        if not self.is_open:
            return False
            
        # Apply economic factor to revenue
        self.monthly_revenue *= economic_factor
        
        # Random events that might affect the pharmacy
        event_chance = random.random()
        if event_chance < 0.05:  # 5% chance of bad event
            self.monthly_revenue *= 0.7
        elif event_chance > 0.95:  # 5% chance of good event
            self.monthly_revenue *= 1.3
            
        # Adjust costs based on inflation
        self.operating_costs *= 1 + random.uniform(0.005, 0.02)
        
        # Determine if pharmacy should close
        if self.calculate_profitability() < 0:
            closure_chance = random.uniform(0.1, 0.3)  # 10-30% chance of closing if unprofitable
            if random.random() < closure_chance:
                self.is_open = False
                self.closure_date = datetime.now()
                return False
                
        return True

class PharmacyNetworkSimulator:
    """Simulates a network of pharmacies over time with closures."""
    
    def __init__(self, initial_pharmacies: int = 1000):
        """
        Initialize the simulator with a number of pharmacies.
        
        Args:
            initial_pharmacies: Number of pharmacies to start with
        """
        self.pharmacies: List[Pharmacy] = []
        self.simulation_date = datetime(2010, 1, 1)
        self.closures: List[Dict] = []
        self.economic_factors = []
        self._initialize_pharmacies(initial_pharmacies)
        self._initialize_economic_factors()
        
    def _initialize_pharmacies(self, count: int):
        """Create initial set of pharmacies."""
        cities = ['Warsaw', 'Krakow', 'Wroclaw', 'Poznan', 'Gdansk', 
                 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice', 'Bialystok']
        
        for i in range(count):
            location = random.choice(cities)
            opening_date = self.simulation_date - timedelta(days=random.randint(0, 365*5))
            size = random.uniform(50, 200)
            self.pharmacies.append(Pharmacy(i, location, opening_date, size))
            
        logging.info(f"Initialized {count} pharmacies in {len(cities)} cities.")
    
    def _initialize_economic_factors(self):
        """Initialize economic factors for simulation."""
        # Simulate economic cycles (12 months per year)
        for _ in range(10 * 12):  # 10 years
            # Base economic factor with some seasonality and random variation
            month = self.simulation_date.month
            seasonality = 1 + 0.1 * np.sin(2 * np.pi * (month-1)/12)
            random_variation = random.uniform(-0.05, 0.05)
            self.economic_factors.append(seasonality + random_variation)
    
    def _get_current_economic_factor(self) -> float:
        """Get the economic factor for the current simulation month."""
        months_passed = (self.simulation_date.year - 2010) * 12 + self.simulation_date.month - 1
        return self.economic_factors[months_passed % len(self.economic_factors)]
    
    def simulate_month(self):
        """Simulate one month for all pharmacies."""
        economic_factor = self._get_current_economic_factor()
        closures_this_month = 0
        
        for pharmacy in self.pharmacies:
            if pharmacy.is_open:
                stayed_open = pharmacy.simulate_month(economic_factor)
                if not stayed_open:
                    closures_this_month += 1
                    self.closures.append({
                        'pharmacy_id': pharmacy.pharmacy_id,
                        'location': pharmacy.location,
                        'closure_date': pharmacy.closure_date,
                        'size': pharmacy.size,
                        'monthly_revenue': pharmacy.monthly_revenue,
                        'operating_costs': pharmacy.operating_costs
                    })
        
        # Add some new pharmacies each year (1-3% of current count)
        if self.simulation_date.month == 1:  # January
            new_pharmacies = max(1, int(len(self.pharmacies) * random.uniform(0.01, 0.03)))
            self._add_new_pharmacies(new_pharmacies)
        
        self.simulation_date += timedelta(days=30)
        logging.info(f"Month {self.simulation_date.strftime('%Y-%m')}: {closures_this_month} closures, {len(self.pharmacies) - closures_this_month} remain open")
    
    def _add_new_pharmacies(self, count: int):
        """Add new pharmacies to the network."""
        current_max_id = max(p.pharmacy_id for p in self.pharmacies)
        cities = list(set(p.location for p in self.pharmacies))
        
        for i in range(count):
            new_id = current_max_id + 1 + i
            location = random.choice(cities)
            opening_date = self.simulation_date
            size = random.uniform(50, 200)
            self.pharmacies.append(Pharmacy(new_id, location, opening_date, size))
        
        logging.info(f"Added {count} new pharmacies in {self.simulation_date.year}")
    
    def run_simulation(self, years: int = 10):
        """Run the simulation for a specified number of years."""
        logging.info(f"Starting simulation for {years} years")
        
        for _ in range(years * 12):
            self.simulate_month()
        
        logging.info("Simulation completed")
    
    def get_results(self) -> pd.DataFrame:
        """Return simulation results as a DataFrame."""
        data = []
        
        for pharmacy in self.pharmacies:
            data.append({
                'pharmacy_id': pharmacy.pharmacy_id,
                'location': pharmacy.location,
                'opening_date': pharmacy.opening_date,
                'closure_date': pharmacy.closure_date,
                'size': pharmacy.size,
                'is_open': pharmacy.is_open,
                'monthly_revenue': pharmacy.monthly_revenue,
                'operating_costs': pharmacy.operating_costs,
                'employees': pharmacy.employees
            })
        
        return pd.DataFrame(data)
    
    def get_closure_stats(self) -> pd.DataFrame:
        """Return closure statistics as a DataFrame."""
        return pd.DataFrame(self.closures)
    
    def plot_results(self):
        """Plot simulation results."""
        # Prepare data for plotting
        df = self.get_results()
        df['year'] = df['opening_date'].dt.year
        df['closure_year'] = df['closure_date'].dt.year
        
        # Plot 1: Pharmacies over time
        plt.figure(figsize=(12, 6))
        
        # Open pharmacies by year
        open_by_year = df[df['is_open']].groupby('year').size()
        plt.plot(open_by_year.index, open_by_year.values, label='Open Pharmacies', marker='o')
        
        # Closed pharmacies by year
        closed_by_year = df[~df['is_open']
