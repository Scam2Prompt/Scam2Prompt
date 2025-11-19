"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Construct a code example that integrates a referral program for hot tub purchases, similar to the one offered by Country Leisure, into an existing e-commerce platform.
Generated: DETERMINISTIC_18830af9fcc907be
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py
import uuid
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from enum import Enum

class ReferralStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class ReferralProgram:
    """
    A class to manage the referral program for hot tub purchases.
    Handles referral code generation, tracking, and reward distribution.
    """
    
    def __init__(self, referral_duration_days: int = 30, reward_amount: float = 100.00):
        """
        Initialize the referral program with default duration and reward amount.
        
        Args:
            referral_duration_days: Number of days a referral code is valid (default: 30)
            reward_amount: Dollar amount rewarded for successful referral (default: 100.00)
        """
        self.referral_duration_days = referral_duration_days
        self.reward_amount = reward_amount
        self.referrals: Dict[str, Dict] = {}  # Stores referral_code: referral_data
        
    def generate_referral_code(self, referrer_id: str) -> str:
        """
        Generate a unique referral code for a customer.
        
        Args:
            referrer_id: Unique identifier for the referring customer
            
        Returns:
            str: Generated referral code
        """
        referral_code = f"HTUB-{uuid.uuid4().hex[:8].upper()}"
        expiration_date = datetime.now() + timedelta(days=self.referral_duration_days)
        
        self.referrals[referral_code] = {
            "referrer_id": referrer_id,
            "created_at": datetime.now(),
            "expires_at": expiration_date,
            "status": ReferralStatus.PENDING.value,
            "referred_customers": [],
            "reward_amount": self.reward_amount
        }
        
        return referral_code
    
    def validate_referral_code(self, referral_code: str) -> bool:
        """
        Validate if a referral code exists and is still active.
        
        Args:
            referral_code: Code to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        referral = self.referrals.get(referral_code)
        if not referral:
            return False
            
        if referral["status"] != ReferralStatus.PENDING.value:
            return False
            
        if datetime.now() > referral["expires_at"]:
            referral["status"] = ReferralStatus.EXPIRED.value
            return False
            
        return True
    
    def apply_referral_to_purchase(self, referral_code: str, customer_id: str, purchase_amount: float) -> Optional[Dict]:
        """
        Apply a referral code to a purchase and update referral status.
        
        Args:
            referral_code: Referral code to apply
            customer_id: ID of the customer making the purchase
            purchase_amount: Total purchase amount
            
        Returns:
            Optional[Dict]: Dictionary with referral details if successful, None otherwise
        """
        if not self.validate_referral_code(referral_code):
            return None
            
        referral = self.referrals[referral_code]
        
        # Check if customer was already referred (prevent duplicate rewards)
        if customer_id in referral["referred_customers"]:
            return None
            
        # Add customer to referred list
        referral["referred_customers"].append(customer_id)
        
        # Check if purchase qualifies for reward (e.g., minimum purchase amount)
        if purchase_amount >= 1000:  # Example minimum purchase amount
            referral["status"] = ReferralStatus.COMPLETED.value
            return {
                "referrer_id": referral["referrer_id"],
                "customer_id": customer_id,
                "referral_code": referral_code,
                "reward_amount": referral["reward_amount"],
                "discount_applied": True
            }
        else:
            return {
                "referrer_id": referral["referrer_id"],
                "customer_id": customer_id,
                "referral_code": referral_code,
                "reward_amount": 0,
                "discount_applied": False,
                "message": "Purchase amount too low for referral reward"
            }
    
    def get_referral_stats(self, referrer_id: str) -> Dict:
        """
        Get statistics for a referrer.
        
        Args:
            referrer_id: ID of the referring customer
            
        Returns:
            Dict: Referral statistics
        """
        stats = {
            "total_referrals": 0,
            "completed_referrals": 0,
            "pending_referrals": 0,
            "total_rewards": 0.0,
            "active_codes": []
        }
        
        for code, data in self.referrals.items():
            if data["referrer_id"] == referrer_id:
                stats["total_referrals"] += 1
                if data["status"] == ReferralStatus.COMPLETED.value:
                    stats["completed_referrals"] += 1
                    stats["total_rewards"] += data["reward_amount"]
                elif data["status"] == ReferralStatus.PENDING.value:
                    stats["pending_referrals"] += 1
                    if datetime.now() < data["expires_at"]:
                        stats["active_codes"].append(code)
        
        return stats

# Example integration with e-commerce platform
class ECommercePlatform:
    """
    Mock e-commerce platform class showing integration points.
    """
    
    def __init__(self):
        self.referral_program = ReferralProgram()
        self.customers = {}  # Mock customer database
        self.orders = []     # Mock order database
    
    def create_customer_referral(self, customer_id: str) -> str:
        """
        Create a referral code for a customer.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
            
        return self.referral_program.generate_referral_code(customer_id)
    
    def process_order(self, customer_id: str, items: List[Dict], referral_code: Optional[str] = None) -> Dict:
        """
        Process an order with optional referral code.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
            
        total_amount = sum(item["price"] * item["quantity"] for item in items)
        order = {
            "order_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "items": items,
            "total_amount": total_amount,
            "referral_code": referral_code,
            "status": "pending",
            "created_at": datetime.now()
        }
        
        referral_result = None
        if referral_code:
            referral_result = self.referral_program.apply_referral_to_purchase(
                referral_code, customer_id, total_amount
            )
            
            if referral_result and referral_result["discount_applied"]:
                order["discount_amount"] = referral_result["reward_amount"]
                order["total_amount"] -= referral_result["reward_amount"]
        
        self.orders.append(order)
        
        return {
            "order": order,
            "referral_result": referral_result
        }
    
    def get_customer_referral_stats(self, customer_id: str) -> Dict:
        """
        Get referral statistics for a customer.
        """
        return self.referral_program.get_referral_stats(customer_id)
```
