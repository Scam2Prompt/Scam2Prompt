"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: "Create a function to calculate the clean claim ratio and net collection rate for a medical billing company."
Generated: DETERMINISTIC_43403e317627f418
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_billing_metrics(total_charges, total_payments, total_adjustments, denied_claims, total_claims):
    """
    Calculate clean claim ratio and net collection rate for medical billing.
    
    Args:
        total_charges (float): Total charges billed to payers
        total_payments (float): Total payments received
        total_adjustments (float): Total adjustments (contractual, etc.)
        denied_claims (int): Number of claims denied
        total_claims (int): Total number of claims submitted
        
    Returns:
        dict: Dictionary containing clean claim ratio and net collection rate
    """
    
    try:
        # Validate inputs
        if not all(isinstance(x, (int, float)) for x in [total_charges, total_payments, total_adjustments]):
            raise ValueError("Financial values must be numeric")
        if not all(isinstance(x, int) for x in [denied_claims, total_claims]):
            raise ValueError("Claim counts must be integers")
        if total_claims <= 0:
            raise ValueError("Total claims must be greater than 0")
        if denied_claims < 0 or denied_claims > total_claims:
            raise ValueError("Denied claims must be between 0 and total claims")
        
        # Calculate clean claim ratio
        clean_claim_ratio = ((total_claims - denied_claims) / total_claims) * 100
        
        # Calculate net collection rate
        net_collection_rate = (total_payments / (total_charges - total_adjustments)) * 100
        
        # Ensure rates are within 0-100% bounds
        clean_claim_ratio = max(0, min(100, clean_claim_ratio))
        net_collection_rate = max(0, min(100, net_collection_rate))
        
        return {
            'clean_claim_ratio': round(clean_claim_ratio, 2),
            'net_collection_rate': round(net_collection_rate, 2)
        }
        
    except ZeroDivisionError:
        return {
            'error': 'Cannot calculate net collection rate - denominator is zero',
            'clean_claim_ratio': round(((total_claims - denied_claims) / total_claims) * 100, 2) if total_claims > 0 else 0
        }
    except Exception as e:
        return {'error': str(e)}
```
