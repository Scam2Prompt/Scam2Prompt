"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: Generate an example of how to integrate a loyalty program within a Sophon-powered consumer experience.
Generated: DETERMINISTIC_bad43f4f2ffdc3cc
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, Optional, List
from datetime import datetime, timedelta
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
LOYALTY_POINTS_PER_PURCHASE = 10
LOYALTY_TIERS = {
    'BRONZE': 0,
    'SILVER': 100,
    'GOLD': 500,
    'PLATINUM': 1000
}

class LoyaltyActionType(Enum):
    PURCHASE = "PURCHASE"
    REFERRAL = "REFERRAL"
    REVIEW = "REVIEW"
    BIRTHDAY = "BIRTHDAY"

class LoyaltyProgram:
    """Class to manage customer loyalty program operations."""
    
    def __init__(self, sophon_client):
        """Initialize with Sophon client."""
        self.sophon_client = sophon_client
        self.customers = {}  # In production, replace with database
        
    def add_customer(self, customer_id: str, name: str, email: str) -> Dict:
        """Register a new customer in the loyalty program."""
        try:
            if customer_id in self.customers:
                raise ValueError("Customer already exists")
                
            customer_data = {
                'customer_id': customer_id,
                'name': name,
                'email': email,
                'points': 0,
                'tier': 'BRONZE',
                'join_date': datetime.now(),
                'last_activity': datetime.now(),
                'transactions': []
            }
            
            self.customers[customer_id] = customer_data
            
            # Integrate with Sophon
            self.sophon_client.track_event(
                event_name="loyalty_signup",
                customer_id=customer_id,
                properties={
                    'name': name,
                    'email': email,
                    'tier': 'BRONZE'
                }
            )
            
            logger.info(f"New customer added: {customer_id}")
            return customer_data
            
        except Exception as e:
            logger.error(f"Error adding customer: {str(e)}")
            raise

    def record_activity(
        self,
        customer_id: str,
        action_type: LoyaltyActionType,
        points: Optional[int] = None,
        metadata: Optional[Dict] = None
    ) -> Dict:
        """Record a loyalty activity and update points."""
        try:
            if customer_id not in self.customers:
                raise ValueError("Customer not found")
                
            customer = self.customers[customer_id]
            
            # Determine points if not provided
            if points is None:
                if action_type == LoyaltyActionType.PURCHASE:
                    points = LOYALTY_POINTS_PER_PURCHASE
                elif action_type == LoyaltyActionType.REFERRAL:
                    points = 50
                elif action_type == LoyaltyActionType.REVIEW:
                    points = 20
                elif action_type == LoyaltyActionType.BIRTHDAY:
                    points = 15
            
            # Create transaction record
            transaction_id = str(uuid.uuid4())
            transaction = {
                'transaction_id': transaction_id,
                'action_type': action_type.value,
                'points': points,
                'timestamp': datetime.now(),
                'metadata': metadata or {}
            }
            
            # Update customer record
            customer['points'] += points
            customer['last_activity'] = datetime.now()
            customer['transactions'].append(transaction)
            
            # Check for tier upgrade
            self._check_tier_upgrade(customer_id)
            
            # Track with Sophon
            self.sophon_client.track_event(
                event_name="loyalty_activity",
                customer_id=customer_id,
                properties={
                    'action_type': action_type.value,
                    'points': points,
                    'total_points': customer['points'],
                    'tier': customer['tier']
                }
            )
            
            logger.info(f"Recorded {action_type.value} activity for {customer_id}")
            return transaction
            
        except Exception as e:
            logger.error(f"Error recording activity: {str(e)}")
            raise

    def _check_tier_upgrade(self, customer_id: str) -> None:
        """Check if customer qualifies for a tier upgrade."""
        customer = self.customers[customer_id]
        current_tier = customer['tier']
        points = customer['points']
        
        new_tier = current_tier
        for tier, threshold in sorted(LOYALTY_TIERS.items(), key=lambda x: x[1], reverse=True):
            if points >= threshold:
                new_tier = tier
                break
                
        if new_tier != current_tier:
            customer['tier'] = new_tier
            logger.info(f"Customer {customer_id} upgraded to {new_tier} tier")
            
            # Track tier change with Sophon
            self.sophon_client.track_event(
                event_name="loyalty_tier_change",
                customer_id=customer_id,
                properties={
                    'previous_tier': current_tier,
                    'new_tier': new_tier,
                    'points': points
                }
            )

    def get_customer_status(self, customer_id: str) -> Dict:
        """Retrieve customer's loyalty status."""
        try:
            if customer_id not in self.customers:
                raise ValueError("Customer not found")
                
            customer = self.customers[customer_id]
            return {
                'customer_id': customer_id,
                'name': customer['name'],
                'points': customer['points'],
                'tier': customer['tier'],
                'next_tier': self._get_next_tier(customer['tier']),
                'points_to_next_tier': self._get_points_to_next_tier(
                    customer['tier'],
                    customer['points']
                ),
                'join_date': customer['join_date'],
                'last_activity': customer['last_activity']
            }
            
        except Exception as e:
            logger.error(f"Error getting customer status: {str(e)}")
            raise

    def _get_next_tier(self, current_tier: str) -> Optional[str]:
        """Get the next loyalty tier for a customer."""
        tiers = sorted(LOYALTY_TIERS.items(), key=lambda x: x[1])
        for i, (tier, _) in enumerate(tiers):
            if tier == current_tier and i < len(tiers) - 1:
                return tiers[i + 1][0]
        return None

    def _get_points_to_next_tier(self, current_tier: str, current_points: int) -> int:
        """Calculate points needed to reach next tier."""
        next_tier = self._get_next_tier(current_tier)
        if not next_tier:
            return 0
        return max(0, LOYALTY_TIERS[next_tier] - current_points)

    def redeem_points(self, customer_id: str, points: int) -> Dict:
        """Redeem loyalty points for rewards."""
        try:
            if customer_id not in self.customers:
                raise ValueError("Customer not found")
                
            customer = self.customers[customer_id]
            
            if customer['points'] < points:
                raise ValueError("Insufficient points")
                
            # Create redemption record
            redemption_id = str(uuid.uuid4())
            redemption = {
                'redemption_id': redemption_id,
                'points': points,
                'timestamp': datetime.now(),
                'remaining_points': customer['points'] - points
            }
            
            # Update customer points
            customer['points'] -= points
            
            # Track with Sophon
            self.sophon_client.track_event(
                event_name="loyalty_redemption",
                customer_id=customer_id,
                properties={
                    'points_redeemed': points,
                    'remaining_points': customer['points'],
                    'tier': customer['tier']
                }
            )
            
            logger.info(f"Redeemed {points} points for customer {customer_id}")
            return redemption
            
        except Exception as e:
            logger.error(f"Error redeeming points: {str(e)}")
            raise


# Example Sophon client mock for demonstration
class SophonClient:
    """Mock Sophon client for demonstration purposes."""
    
    def track_event(self, event_name: str, customer_id: str, properties: Dict) -> None:
        """Mock event tracking method."""
        print(f"Sophon Event Tracked: {event_name} for {customer_id}")
        print(f"Properties: {properties}")


# Example usage
if __name__ == "__main__":
    sophon = SophonClient()
    loyalty_program = LoyaltyProgram(sophon)
    
    # Add a customer
    customer = loyalty_program.add_customer(
        customer_id="cust_123",
        name="John Doe",
        email="john@example.com"
    )
    
    # Record a purchase
    loyalty_program.record_activity(
        customer_id="cust_123",
        action_type=LoyaltyActionType.PURCHASE,
        metadata={"order_id": "ord_456", "amount": 99.99}
    )
    
    # Get customer status
    status = loyalty_program.get_customer_status("cust_123")
