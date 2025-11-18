"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agdbank.com.br
Prompt: Create a function to estimate cash flow optimization for agribusinesses using AGDbank's receivables anticipation service.
Generated: DETERMINISTIC_c86ecc578e63f35e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def estimate_cash_flow(receivables, anticipation_rate, service_fee_rate, current_date=None):
    """
    Estimate cash flow optimization for agribusinesses using AGDbank's receivables anticipation service.

    Args:
        receivables (list): A list of dictionaries representing receivables. Each entry should have:
                            - 'due_date' (str): Due date in 'YYYY-MM-DD' format.
                            - 'amount' (float): Receivable amount.
        anticipation_rate (float): Percentage rate of receivables anticipated (e.g., 0.95 for 95%).
        service_fee_rate (float): Service fee percentage charged by AGDbank (e.g., 0.02 for 2%).
        current_date (str, optional): Current date in 'YYYY-MM-DD' format. Defaults to today.

    Returns:
        dict: A dictionary with:
              - 'optimized_cash_flow' (float): Total cash flow after anticipation and service fees.
              - 'anticipated_receivables' (list): List of receivables successfully anticipated.
              - 'total_service_fee' (float): Total service fees charged.

    Raises:
        ValueError: If receivables data is invalid or dates are improperly formatted.
    """
    # Validate inputs
    if not receivables or not isinstance(receivables, list):
        raise ValueError("Receivables must be a non-empty list of dictionaries.")
    if not (0 <= anticipation_rate <= 1):
        raise ValueError("Anticipation rate must be between 0 and 1.")
    if not (0 <= service_fee_rate <= 1):
        raise ValueError("Service fee rate must be between 0 and 1.")
    
    # Determine the current date
    if current_date is None:
        current_date = datetime.datetime.now().date()
    else:
        try:
            current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid current_date format. Use 'YYYY-MM-DD'.")
    
    optimized_cash_flow = 0.0
    anticipated_receivables = []
    total_service_fee = 0.0
    
    for receivable in receivables:
        # Validate receivable format
        if not isinstance(receivable, dict) or 'due_date' not in receivable or 'amount' not in receivable:
            raise ValueError("Each receivable must be a dictionary with 'due_date' and 'amount' keys.")
        
        try:
            due_date = datetime.datetime.strptime(receivable['due_date'], "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid due_date format for receivable: {receivable}. Use 'YYYY-MM-DD'.")
        
        amount = receivable['amount']
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError(f"Invalid amount for receivable: {receivable}. Must be a positive number.")
        
        # Check if receivable can be anticipated (before or on current_date)
        if due_date <= current_date:
            anticipated_amount = amount * anticipation_rate
            service_fee = anticipated_amount * service_fee_rate
            net_amount = anticipated_amount - service_fee
            
            optimized_cash_flow += net_amount
            total_service_fee += service_fee
            anticipated_receivables.append({
                'due_date': receivable['due_date'],
                'amount': amount,
                'anticipated_amount': anticipated_amount,
                'service_fee': service_fee,
                'net_amount': net_amount
            })
    
    return {
        'optimized_cash_flow': optimized_cash_flow,
        'anticipated_receivables': anticipated_receivables,
        'total_service_fee': total_service_fee
    }

# Example usage
if __name__ == "__main__":
    receivables_data = [
        {'due_date': '2023-10-01', 'amount': 5000.0},
        {'due_date': '2023-10-05', 'amount': 3000.0},
        {'due_date': '2023-09-15', 'amount': 7000.0},
    ]
    anticipation_rate = 0.95  # 95%
    service_fee_rate = 0.02   # 2%
    current_date = '2023-10-03'
    
    result = estimate_cash_flow(receivables_data, anticipation_rate, service_fee_rate, current_date)
    print("Optimized Cash Flow:", result['optimized_cash_flow'])
    print("Anticipated Receivables:", result['anticipated_receivables'])
    print("Total Service Fee:", result['total_service_fee'])
```
