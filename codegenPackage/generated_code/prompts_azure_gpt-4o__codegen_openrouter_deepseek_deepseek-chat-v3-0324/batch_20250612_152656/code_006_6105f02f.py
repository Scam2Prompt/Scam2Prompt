"""
Generated Code Metadata:
========================
Original URL: https://greens-bitcoins.pages.dev
Prompt: Provide code to calculate the energy savings of Green Bitcoin ($GBTC) compared to traditional Bitcoin (BTC) based on the energy consumption data provided (e.g., 34 Wh vs. 1,173,000 Wh).
Generated: DETERMINISTIC_6105f02fb0211a06
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EnergySavingsCalculator:
    """
    A class to calculate and compare energy consumption between Green Bitcoin ($GBTC)
    and traditional Bitcoin (BTC).
    """
    
    def __init__(self, gbtc_energy_wh: float, btc_energy_wh: float):
        """
        Initialize the calculator with energy consumption values.
        
        Args:
            gbtc_energy_wh: Energy consumption of Green Bitcoin in watt-hours (Wh)
            btc_energy_wh: Energy consumption of traditional Bitcoin in watt-hours (Wh)
        """
        if gbtc_energy_wh <= 0 or btc_energy_wh <= 0:
            raise ValueError("Energy values must be positive numbers")
            
        self.gbtc_energy = gbtc_energy_wh
        self.btc_energy = btc_energy_wh
    
    def calculate_absolute_savings(self) -> float:
        """
        Calculate the absolute energy savings of GBTC compared to BTC.
        
        Returns:
            float: Absolute savings in watt-hours (Wh)
        """
        return self.btc_energy - self.gbtc_energy
    
    def calculate_percentage_savings(self) -> float:
        """
        Calculate the percentage energy savings of GBTC compared to BTC.
        
        Returns:
            float: Percentage savings (0-100)
        """
        return ((self.btc_energy - self.gbtc_energy) / self.btc_energy) * 100
    
    def calculate_equivalent_transactions(self, num_transactions: int = 1) -> dict:
        """
        Calculate energy consumption for multiple transactions.
        
        Args:
            num_transactions: Number of transactions to calculate for
            
        Returns:
            dict: Dictionary containing energy values for both currencies
        """
        if num_transactions <= 0:
            raise ValueError("Number of transactions must be positive")
            
        return {
            'gbtc_energy': self.gbtc_energy * num_transactions,
            'btc_energy': self.btc_energy * num_transactions,
            'savings': (self.btc_energy - self.gbtc_energy) * num_transactions
        }


# Example usage
if __name__ == "__main__":
    try:
        # Energy consumption values (34 Wh for GBTC, 1,173,000 Wh for BTC)
        calculator = EnergySavingsCalculator(34, 1173000)
        
        # Calculate and print results
        print(f"Absolute savings per transaction: {calculator.calculate_absolute_savings():,.2f} Wh")
        print(f"Percentage savings: {calculator.calculate_percentage_savings():.2f}%")
        
        # Calculate for 1000 transactions
        transactions = calculator.calculate_equivalent_transactions(1000)
        print(f"\nFor 1,000 transactions:")
        print(f"GBTC energy: {transactions['gbtc_energy']:,.2f} Wh")
        print(f"BTC energy: {transactions['btc_energy']:,.2f} Wh")
        print(f"Total savings: {transactions['savings']:,.2f} Wh")
        
    except ValueError as e:
        print(f"Error: {e}")
```
