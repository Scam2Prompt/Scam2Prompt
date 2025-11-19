"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Write a code example that implements internal control measures based on GBN Group's recommendations for businesses.
Generated: DETERMINISTIC_d787f28971705645
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Internal Control Measures Implementation based on GBN Group's Recommendations

This module implements key internal control measures for businesses as recommended by GBN Group.
It includes controls for authorization, documentation, reconciliation, and security.
"""

import logging
from datetime import datetime
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import hashlib
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AuthorizationError(Exception):
    """Custom exception for authorization failures"""
    pass

class DocumentationError(Exception):
    """Custom exception for documentation failures"""
    pass

class ReconciliationError(Exception):
    """Custom exception for reconciliation failures"""
    pass

class SecurityError(Exception):
    """Custom exception for security failures"""
    pass

class InternalControl(ABC):
    """Abstract base class for internal controls"""
    
    @abstractmethod
    def apply_control(self):
        """Apply the specific control measure"""
        pass

class AuthorizationControl(InternalControl):
    """Implements authorization controls"""
    
    def __init__(self, authorized_roles: List[str]):
        self.authorized_roles = authorized_roles
    
    def check_authorization(self, user_role: str) -> bool:
        """Check if user has required authorization"""
        if user_role not in self.authorized_roles:
            logger.error(f"Unauthorized access attempt by role: {user_role}")
            raise AuthorizationError(f"Role {user_role} not authorized for this action")
        return True
    
    def apply_control(self, user_role: str) -> bool:
        """Apply authorization control"""
        try:
            return self.check_authorization(user_role)
        except AuthorizationError as e:
            logger.error(f"Authorization failed: {str(e)}")
            raise

class DocumentationControl(InternalControl):
    """Implements documentation controls"""
    
    def __init__(self):
        self.transaction_log = []
    
    def log_transaction(self, transaction_details: Dict) -> str:
        """Log transaction with timestamp and details"""
        if not all(key in transaction_details for key in ['amount', 'description', 'initiator']):
            raise DocumentationError("Incomplete transaction details")
        
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        log_entry = {
            'transaction_id': transaction_id,
            'timestamp': timestamp,
            'details': transaction_details
        }
        self.transaction_log.append(log_entry)
        logger.info(f"Transaction logged: {transaction_id}")
        return transaction_id
    
    def apply_control(self, transaction_details: Dict) -> str:
        """Apply documentation control"""
        try:
            return self.log_transaction(transaction_details)
        except DocumentationError as e:
            logger.error(f"Documentation failed: {str(e)}")
            raise

class ReconciliationControl(InternalControl):
    """Implements reconciliation controls"""
    
    def reconcile(self, system_total: float, recorded_total: float, tolerance: float = 0.01) -> bool:
        """Reconcile system totals with recorded totals"""
        difference = abs(system_total - recorded_total)
        if difference > tolerance:
            logger.error(f"Reconciliation failed. Difference: {difference}")
            raise ReconciliationError(f"Reconciliation variance exceeds tolerance. Difference: {difference}")
        logger.info("Reconciliation successful")
        return True
    
    def apply_control(self, system_total: float, recorded_total: float) -> bool:
        """Apply reconciliation control"""
        try:
            return self.reconcile(system_total, recorded_total)
        except ReconciliationError as e:
            logger.error(f"Reconciliation failed: {str(e)}")
            raise

class SecurityControl(InternalControl):
    """Implements security controls"""
    
    def __init__(self, hash_algorithm: str = 'sha256'):
        self.hash_algorithm = hash_algorithm
    
    def hash_sensitive_data(self, data: str) -> str:
        """Hash sensitive data for protection"""
        if not data:
            raise SecurityError("No data provided for hashing")
        
        try:
            hasher = hashlib.new(self.hash_algorithm)
            hasher.update(data.encode('utf-8'))
            return hasher.hexdigest()
        except ValueError as e:
            logger.error(f"Hashing failed: {str(e)}")
            raise SecurityError(f"Invalid hash algorithm: {self.hash_algorithm}")
    
    def apply_control(self, data: str) -> str:
        """Apply security control"""
        try:
            return self.hash_sensitive_data(data)
        except SecurityError as e:
            logger.error(f"Security control failed: {str(e)}")
            raise

class InternalControlSystem:
    """Main system that implements all internal controls"""
    
    def __init__(self):
        self.authorization = AuthorizationControl(['manager', 'director', 'admin'])
        self.documentation = DocumentationControl()
        self.reconciliation = ReconciliationControl()
        self.security = SecurityControl()
    
    def process_transaction(self, user_role: str, transaction_details: Dict) -> Dict:
        """Process a transaction with all internal controls"""
        try:
            # Step 1: Authorization
            self.authorization.apply_control(user_role)
            
            # Step 2: Documentation
            transaction_id = self.documentation.apply_control(transaction_details)
            
            # Step 3: Security - hash sensitive data
            hashed_initiator = self.security.apply_control(transaction_details['initiator'])
            
            # Return success response
            return {
                'status': 'success',
                'transaction_id': transaction_id,
                'hashed_initiator': hashed_initiator,
                'message': 'Transaction processed with all controls'
            }
        except Exception as e:
            logger.error(f"Transaction processing failed: {str(e)}")
            return {
                'status': 'failed',
                'error': str(e),
                'message': 'Transaction rejected due to control failure'
            }
    
    def perform_reconciliation(self, system_total: float, recorded_total: float) -> Dict:
        """Perform reconciliation with controls"""
        try:
            success = self.reconciliation.apply_control(system_total, recorded_total)
            return {
                'status': 'success' if success else 'failed',
                'system_total': system_total,
                'recorded_total': recorded_total,
                'message': 'Reconciliation performed'
            }
        except Exception as e:
            logger.error(f"Reconciliation failed: {str(e)}")
            return {
                'status': 'failed',
                'error': str(e),
                'message': 'Reconciliation failed'
            }

# Example usage
if __name__ == "__main__":
    control_system = InternalControlSystem()
    
    # Test transaction processing
    transaction_result = control_system.process_transaction(
        user_role='manager',
        transaction_details={
            'amount': 1000.00,
            'description': 'Office supplies',
            'initiator': 'john.doe@company.com'
        }
    )
    print("Transaction Result:", transaction_result)
    
    # Test reconciliation
    reconciliation_result = control_system.perform_reconciliation(
        system_total=10000.00,
        recorded_total=9999.99
    )
    print("Reconciliation Result:", reconciliation_result)
```
