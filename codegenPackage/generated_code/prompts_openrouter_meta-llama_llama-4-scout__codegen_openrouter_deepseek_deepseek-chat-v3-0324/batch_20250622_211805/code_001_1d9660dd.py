"""
Generated Code Metadata:
========================
Original URL: https://token-graph.net
Prompt: How does the AT&T Guarantee SM work for new and existing customers?
Generated: DETERMINISTIC_1d9660dd80ad6a69
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# AT&T Guarantee Service Module (SM) Implementation

class ATTTGuaranteeService:
    """
    This class implements the AT&T Guarantee Service Module which handles
    guarantee-related operations for both new and existing customers.
    """
    
    def __init__(self, customer_db_connector):
        """
        Initialize the service with a customer database connector.
        
        Args:
            customer_db_connector: An object that provides access to customer data
        """
        self.db = customer_db_connector
        
    def check_eligibility(self, customer_id):
        """
        Check if a customer is eligible for AT&T Guarantee.
        
        Args:
            customer_id: Unique identifier for the customer
            
        Returns:
            dict: {
                'eligible': bool,
                'reason': str (if not eligible),
                'benefits': list (if eligible)
            }
            
        Raises:
            ValueError: If customer_id is invalid
            DatabaseError: If there's an issue accessing customer data
        """
        if not customer_id or not isinstance(customer_id, str):
            raise ValueError("Invalid customer ID")
            
        try:
            customer_data = self.db.get_customer(customer_id)
            
            if not customer_data:
                return {
                    'eligible': False,
                    'reason': 'Customer not found'
                }
                
            # New customers are always eligible
            if customer_data.get('new_customer', False):
                return {
                    'eligible': True,
                    'benefits': [
                        '30-day satisfaction guarantee',
                        'free returns',
                        'no cancellation fees'
                    ]
                }
                
            # Existing customer eligibility rules
            if customer_data.get('account_age_days', 0) < 365:
                return {
                    'eligible': True,
                    'benefits': [
                        'extended warranty options',
                        'premium support'
                    ]
                }
            else:
                return {
                    'eligible': False,
                    'reason': 'Account age exceeds guarantee period'
                }
                
        except Exception as e:
            raise DatabaseError(f"Error accessing customer data: {str(e)}")
            
    def apply_guarantee(self, customer_id, guarantee_type):
        """
        Apply a specific guarantee to a customer's account.
        
        Args:
            customer_id: Unique identifier for the customer
            guarantee_type: Type of guarantee to apply
            
        Returns:
            dict: {
                'success': bool,
                'message': str,
                'confirmation_code': str (if successful)
            }
            
        Raises:
            ValueError: If inputs are invalid
            DatabaseError: If there's an issue updating records
            EligibilityError: If customer is not eligible
        """
        if not customer_id or not guarantee_type:
            raise ValueError("Customer ID and guarantee type are required")
            
        eligibility = self.check_eligibility(customer_id)
        if not eligibility['eligible']:
            raise EligibilityError(eligibility.get('reason', 'Not eligible'))
            
        try:
            # Generate a unique confirmation code
            confirmation_code = f"ATT-GUAR-{customer_id[:4]}-{int(time.time())}"
            
            # Update customer record
            self.db.update_customer(
                customer_id,
                {
                    'active_guarantee': guarantee_type,
                    'guarantee_start_date': datetime.now().isoformat(),
                    'guarantee_confirmation': confirmation_code
                }
            )
            
            return {
                'success': True,
                'message': 'Guarantee successfully applied',
                'confirmation_code': confirmation_code
            }
            
        except Exception as e:
            raise DatabaseError(f"Error applying guarantee: {str(e)}")

    def revoke_guarantee(self, customer_id):
        """
        Revoke any active guarantee from a customer's account.
        
        Args:
            customer_id: Unique identifier for the customer
            
        Returns:
            dict: {
                'success': bool,
                'message': str
            }
            
        Raises:
            ValueError: If customer_id is invalid
            DatabaseError: If there's an issue updating records
        """
        if not customer_id:
            raise ValueError("Customer ID is required")
            
        try:
            self.db.update_customer(
                customer_id,
                {
                    'active_guarantee': None,
                    'guarantee_end_date': datetime.now().isoformat()
                }
            )
            
            return {
                'success': True,
                'message': 'Guarantee successfully revoked'
            }
            
        except Exception as e:
            raise DatabaseError(f"Error revoking guarantee: {str(e)}")


# Custom Exceptions
class DatabaseError(Exception):
    """Raised when there's an issue with database operations"""
    pass

class EligibilityError(Exception):
    """Raised when a customer is not eligible for a guarantee"""
    pass


# Example usage (would be in a separate file in production)
if __name__ == "__main__":
    from datetime import datetime
    import time
    
    # Mock database connector for demonstration
    class MockDBC:
        def get_customer(self, customer_id):
            # Mock customer data
            if customer_id == "NEW123":
                return {'new_customer': True}
            elif customer_id == "EXIST456":
                return {'account_age_days': 180}
            elif customer_id == "OLD789":
                return {'account_age_days': 400}
            else:
                return None
                
        def update_customer(self, customer_id, updates):
            print(f"Updating customer {customer_id} with: {updates}")
            return True
    
    # Initialize service
    service = ATTTGuaranteeService(MockDBC())
    
    # Test scenarios
    try:
        print(service.check_eligibility("NEW123"))
        print(service.check_eligibility("EXIST456"))
        print(service.check_eligibility("OLD789"))
        
        print(service.apply_guarantee("NEW123", "30-day satisfaction"))
        print(service.revoke_guarantee("NEW123"))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
