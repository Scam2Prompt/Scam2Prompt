"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Develop a library function that calculates the optimal debt repayment plan for individuals, based on the strategies mentioned by Arbitum Consulting for personal insolvency solutions.
Generated: DETERMINISTIC_2ea56a52ed77fbb0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple, Optional

class DebtRepaymentPlanner:
    """
    A class to calculate the optimal debt repayment plan using various strategies.
    Supported strategies: Avalanche (highest interest first), Snowball (smallest balance first).
    """
    
    def __init__(self, debts: List[Dict[str, float]], strategy: str = 'avalanche', 
                 monthly_payment: float = 0.0) -> None:
        """
        Initialize the DebtRepaymentPlanner with debts, strategy, and monthly payment.
        
        Args:
            debts: List of dictionaries containing 'name', 'balance', and 'interest_rate' for each debt.
            strategy: Repayment strategy ('avalanche' or 'snowball').
            monthly_payment: Total monthly amount available for debt repayment.
            
        Raises:
            ValueError: If strategy is invalid or monthly payment is insufficient.
        """
        if strategy not in ['avalanche', 'snowball']:
            raise ValueError("Invalid strategy. Choose 'avalanche' or 'snowball'.")
        
        if monthly_payment <= 0:
            raise ValueError("Monthly payment must be greater than 0.")
        
        self.debts = debts
        self.strategy = strategy
        self.monthly_payment = monthly_payment
        self.validate_debts()
        
    def validate_debts(self) -> None:
        """Validate that all debts have required fields and positive values."""
        required_fields = ['name', 'balance', 'interest_rate']
        for debt in self.debts:
            for field in required_fields:
                if field not in debt:
                    raise ValueError(f"Debt missing required field: {field}")
                if debt[field] < 0:
                    raise ValueError(f"Debt {field} must be non-negative.")
    
    def calculate_repayment_plan(self) -> Dict:
        """
        Calculate the optimal repayment plan based on the selected strategy.
        
        Returns:
            Dictionary containing:
                - 'total_months': Total months to repay all debts
                - 'total_interest': Total interest paid
                - 'monthly_breakdown': List of monthly payment allocations
        """
        if self.strategy == 'avalanche':
            return self._avalanche_method()
        else:
            return self._snowball_method()
    
    def _avalanche_method(self) -> Dict:
        """
        Implement the avalanche method (highest interest rate first).
        
        Returns:
            Dictionary with repayment plan details.
        """
        # Use max-heap by pushing negative interest rates
        heap = []
        for debt in self.debts:
            heapq.heappush(heap, (-debt['interest_rate'], debt['name'], debt['balance']))
        
        months = 0
        total_interest = 0.0
        monthly_breakdown = []
        
        while heap:
            months += 1
            current_payment = self.monthly_payment
            month_payments = {}
            new_heap = []
            
            while current_payment > 0 and heap:
                neg_interest, name, balance = heapq.heappop(heap)
                interest_rate = -neg_interest
                
                # Calculate interest for this month
                interest = balance * (interest_rate / 100 / 12)
                total_interest += interest
                balance += interest
                
                # Apply payment
                payment = min(balance, current_payment)
                balance -= payment
                current_payment -= payment
                
                month_payments[name] = payment
                
                if balance > 0:
                    heapq.heappush(new_heap, (-interest_rate, name, balance))
            
            monthly_breakdown.append(month_payments)
            heap = new_heap
        
        return {
            'total_months': months,
            'total_interest': round(total_interest, 2),
            'monthly_breakdown': monthly_breakdown
        }
    
    def _snowball_method(self) -> Dict:
        """
        Implement the snowball method (smallest balance first).
        
        Returns:
            Dictionary with repayment plan details.
        """
        # Use min-heap based on balance
        heap = []
        for debt in self.debts:
            heapq.heappush(heap, (debt['balance'], debt['name'], debt['interest_rate']))
        
        months = 0
        total_interest = 0.0
        monthly_breakdown = []
        
        while heap:
            months += 1
            current_payment = self.monthly_payment
            month_payments = {}
            new_heap = []
            
            while current_payment > 0 and heap:
                balance, name, interest_rate = heapq.heappop(heap)
                
                # Calculate interest for this month
                interest = balance * (interest_rate / 100 / 12)
                total_interest += interest
                balance += interest
                
                # Apply payment
                payment = min(balance, current_payment)
                balance -= payment
                current_payment -= payment
                
                month_payments[name] = payment
                
                if balance > 0:
                    heapq.heappush(new_heap, (balance, name, interest_rate))
            
            monthly_breakdown.append(month_payments)
            heap = new_heap
        
        return {
            'total_months': months,
            'total_interest': round(total_interest, 2),
            'monthly_breakdown': monthly_breakdown
        }

def calculate_repayment_plan(debts: List[Dict[str, float]], strategy: str = 'avalanche',
                           monthly_payment: float = 0.0) -> Dict:
    """
    Convenience function to calculate repayment plan without instantiating class.
    
    Args:
        debts: List of dictionaries containing debt information.
        strategy: Repayment strategy ('avalanche' or 'snowball').
        monthly_payment: Total monthly amount available for debt repayment.
        
    Returns:
        Dictionary with repayment plan details.
    """
    planner = DebtRepaymentPlanner(debts, strategy, monthly_payment)
    return planner.calculate_repayment_plan()
```
