"""
Generated Code Metadata:
========================
Original URL: https://app.librafinance.org
Prompt: Create a script to simulate stablecoin swaps using Libra Finance's stableswap mechanism and compare rates.
Generated: DETERMINISTIC_6c2aea283e8e5c54
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict

class StableSwap:
    """
    Simulates stablecoin swaps using Libra Finance's stableswap mechanism.
    """
    
    def __init__(self, coins: List[str], initial_balances: List[float], A: float = 100, fee: float = 0.003):
        """
        Initialize the stableswap pool.
        
        Args:
            coins: List of coin symbols in the pool
            initial_balances: Initial balances for each coin (same order as coins)
            A: Amplification coefficient (default: 100)
            fee: Swap fee percentage (default: 0.3%)
        """
        if len(coins) != len(initial_balances):
            raise ValueError("Length of coins and initial_balances must match")
        if any(balance <= 0 for balance in initial_balances):
            raise ValueError("All balances must be positive")
        if A <= 0:
            raise ValueError("Amplification coefficient must be positive")
        if fee < 0 or fee > 1:
            raise ValueError("Fee must be between 0 and 1")
            
        self.coins = coins
        self.balances = initial_balances.copy()
        self.A = A
        self.fee = fee
        self.n = len(coins)
        self.D = self._compute_D()
        
    def _compute_D(self) -> float:
        """
        Compute the invariant D for the current balances.
        
        D is calculated according to the stableswap invariant:
        A * sum(x_i) * n^n + D = A * D * n^n + D^(n+1)/(n^n * prod(x_i))
        """
        S = sum(self.balances)
        if S == 0:
            return 0
            
        D = S
        Ann = self.A * self.n
        
        for _ in range(255):
            D_prev = D
            D_P = D
            for x in self.balances:
                D_P = D_P * D / (x * self.n + 1e-18)  # +1e-18 to prevent division by zero
            D = (Ann * S + D_P * self.n) * D / ((Ann - 1) * D + (self.n + 1) * D_P)
            
            if abs(D - D_prev) <= 1:
                break
                
        return D
    
    def _get_y(self, i: int, j: int, x: float) -> float:
        """
        Calculate y_j given x_i for a swap between coins i and j.
        
        Args:
            i: Index of input coin
            j: Index of output coin
            x: Amount of input coin
            
        Returns:
            Amount of output coin received
        """
        if i == j:
            raise ValueError("Can't swap between same coins")
        if x <= 0:
            raise ValueError("Input amount must be positive")
            
        D = self.D
        Ann = self.A * self.n
        xx = self.balances.copy()
        xx[i] += x
        yy = xx.copy()
        
        y_prev = 0
        y = D // self.n  # Starting guess
        
        for _ in range(255):
            y_prev = y
            prod = 1
            for k in range(self.n):
                if k == j:
                    continue
                prod *= yy[k]
            y = (D * D * y_prev) / (self.n * self.n * prod + 1e-18)
            
            if abs(y - y_prev) <= 1:
                break
                
        return y
    
    def get_dy(self, i: int, j: int, dx: float) -> float:
        """
        Calculate the amount of coin j received for swapping dx of coin i.
        
        Args:
            i: Index of input coin
            j: Index of output coin
            dx: Amount of input coin to swap
            
        Returns:
            Amount of output coin received after fees
        """
        if dx <= 0:
            raise ValueError("Swap amount must be positive")
            
        x = self.balances[i]
        y = self.balances[j]
        dy = self._get_y(i, j, dx) - y
        dy_fee = dy * self.fee
        return dy - dy_fee
    
    def swap(self, i: int, j: int, dx: float) -> float:
        """
        Execute a swap between coins i and j.
        
        Args:
            i: Index of input coin
            j: Index of output coin
            dx: Amount of input coin to swap
            
        Returns:
            Amount of output coin received
        """
        dy = self.get_dy(i, j, dx)
        if dy <= 0:
            raise ValueError("Output amount must be positive")
            
        self.balances[i] += dx
        self.balances[j] -= dy
        self.D = self._compute_D()  # Update invariant
        
        return dy
    
    def get_price_impact(self, i: int, j: int, dx: float) -> float:
        """
        Calculate price impact of a swap.
        
        Args:
            i: Index of input coin
            j: Index of output coin
            dx: Amount of input coin to swap
            
        Returns:
            Price impact as a percentage
        """
        if dx <= 0:
            raise ValueError("Swap amount must be positive")
            
        x = self.balances[i]
        y = self.balances[j]
        initial_price = y / x
        
        dy = self.get_dy(i, j, dx)
        new_x = x + dx
        new_y = y - dy
        new_price = new_y / new_x
        
        return abs((new_price - initial_price) / initial_price) * 100
    
    def compare_rates(self, swaps: List[Dict]) -> Dict:
        """
        Compare swap rates between different pairs.
        
        Args:
            swaps: List of swap dictionaries with keys:
                  - 'from_coin': Input coin symbol
                  - 'to_coin': Output coin symbol
                  - 'amount': Amount to swap
                  
        Returns:
            Dictionary with comparison results
        """
        results = {}
        
        for swap in swaps:
            try:
                from_idx = self.coins.index(swap['from_coin'])
                to_idx = self.coins.index(swap['to_coin'])
                amount = swap['amount']
                
                dy = self.get_dy(from_idx, to_idx, amount)
                price_impact = self.get_price_impact(from_idx, to_idx, amount)
                
                results[f"{swap['from_coin']}_to_{swap['to_coin']}"] = {
                    'input_amount': amount,
                    'output_amount': dy,
                    'price_impact_percent': price_impact,
                    'rate': dy / amount
                }
            except ValueError as e:
                results[f"{swap['from_coin']}_to_{swap['to_coin']}"] = {
                    'error': str(e)
                }
                
        return results


# Example usage
if __name__ == "__main__":
    # Initialize a pool with 3 stablecoins
    pool = StableSwap(
        coins=["USDC", "USDT", "DAI"],
        initial_balances=[1000000.0, 1000000.0, 1000000.0],
        A=100,
        fee=0.003
    )
    
    # Compare swap rates
    swaps = [
        {"from_coin": "USDC", "to_coin": "USDT", "amount": 1000},
        {"from_coin": "USDC", "to_coin": "DAI", "amount": 1000},
        {"from_coin": "USDT", "to_coin": "DAI", "amount": 1000},
        {"from_coin": "USDT", "to_coin": "USDC", "amount": 1000},
        {"from_coin": "DAI", "to_coin": "USDC", "amount": 1000},
        {"from_coin": "DAI", "to_coin": "USDT", "amount": 1000},
    ]
    
    results = pool.compare_rates(swaps)
    
    # Print results
    for pair, data in results.items():
        print(f"Pair: {pair}")
        if 'error' in data:
            print(f"  Error: {data['error']}")
        else:
            print(f"  Input: {data['input_amount']}")
            print(f"  Output: {data['output_amount']:.6f}")
            print(f"  Rate: {data['rate']:.6f}")
            print(f"  Price Impact: {data['price_impact_percent']:.4f}%")
        print()
```
