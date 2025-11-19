"""
Generated Code Metadata:
========================
Original URL: https://wintron.minibachat.shop
Prompt: Illustrate how to implement a referral program feature in a web application that mimics Wintron's model, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_9f1981d66a2dc1e3
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py
from datetime import datetime
from typing import List, Dict, Optional
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReferralProgram:
    """
    A class to manage a referral program similar to Wintron's model.
    Handles user referrals, tracking, and earnings calculations.
    """
    
    def __init__(self):
        self.referrals = {}  # {referral_id: referral_data}
        self.users = {}      # {user_id: user_data}
        self.earnings = {}   # {user_id: earnings_data}
        
    def register_user(self, user_id: str, name: str, email: str) -> bool:
        """
        Register a new user in the system.
        
        Args:
            user_id: Unique identifier for the user
            name: User's full name
            email: User's email address
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        try:
            if user_id in self.users:
                logger.warning(f"User {user_id} already exists")
                return False
                
            self.users[user_id] = {
                'id': user_id,
                'name': name,
                'email': email,
                'referral_code': str(uuid4())[:8].upper(),
                'join_date': datetime.now(),
                'referral_count': 0
            }
            
            # Initialize earnings record
            self.earnings[user_id] = {
                'total_earnings': 0.0,
                'pending_earnings': 0.0,
                'withdrawn_earnings': 0.0,
                'referral_history': []
            }
            
            logger.info(f"User {user_id} registered successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            return False
    
    def add_referral(self, referrer_id: str, referred_email: str) -> Optional[str]:
        """
        Add a new referral to the system.
        
        Args:
            referrer_id: ID of the user who made the referral
            referred_email: Email of the referred user
            
        Returns:
            Optional[str]: Referral ID if successful, None otherwise
        """
        try:
            if referrer_id not in self.users:
                logger.warning(f"Referrer {referrer_id} not found")
                return None
                
            referral_id = str(uuid4())
            
            self.referrals[referral_id] = {
                'id': referral_id,
                'referrer_id': referrer_id,
                'referred_email': referred_email,
                'date': datetime.now(),
                'status': 'pending',  # pending, completed, expired
                'earnings': 0.0
            }
            
            # Update referrer's count
            self.users[referrer_id]['referral_count'] += 1
            
            logger.info(f"Referral {referral_id} added by {referrer_id}")
            return referral_id
            
        except Exception as e:
            logger.error(f"Error adding referral: {e}")
            return None
    
    def complete_referral(self, referral_id: str, amount: float) -> bool:
        """
        Mark a referral as completed and credit earnings.
        
        Args:
            referral_id: ID of the referral to complete
            amount: Amount to credit to referrer
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if referral_id not in self.referrals:
                logger.warning(f"Referral {referral_id} not found")
                return False
                
            referral = self.referrals[referral_id]
            referrer_id = referral['referrer_id']
            
            # Update referral status
            referral['status'] = 'completed'
            referral['earnings'] = amount
            
            # Update referrer's earnings
            self.earnings[referrer_id]['total_earnings'] += amount
            self.earnings[referrer_id]['pending_earnings'] += amount
            self.earnings[referrer_id]['referral_history'].append({
                'referral_id': referral_id,
                'amount': amount,
                'date': datetime.now()
            })
            
            logger.info(f"Referral {referral_id} completed. {amount} credited to {referrer_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error completing referral: {e}")
            return False
    
    def get_user_referrals(self, user_id: str) -> List[Dict]:
        """
        Get all referrals made by a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List[Dict]: List of referral records
        """
        try:
            if user_id not in self.users:
                logger.warning(f"User {user_id} not found")
                return []
                
            return [ref for ref in self.referrals.values() 
                   if ref['referrer_id'] == user_id]
                   
        except Exception as e:
            logger.error(f"Error getting user referrals: {e}")
            return []
    
    def get_user_earnings(self, user_id: str) -> Dict:
        """
        Get earnings information for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            Dict: Earnings information
        """
        try:
            if user_id not in self.earnings:
                logger.warning(f"Earnings record for {user_id} not found")
                return {}
                
            return self.earnings[user_id]
            
        except Exception as e:
            logger.error(f"Error getting user earnings: {e}")
            return {}
    
    def withdraw_earnings(self, user_id: str, amount: float) -> bool:
        """
        Withdraw earnings from a user's account.
        
        Args:
            user_id: ID of the user
            amount: Amount to withdraw
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if user_id not in self.earnings:
                logger.warning(f"Earnings record for {user_id} not found")
                return False
                
            if amount > self.earnings[user_id]['pending_earnings']:
                logger.warning(f"Insufficient pending earnings for {user_id}")
                return False
                
            self.earnings[user_id]['pending_earnings'] -= amount
            self.earnings[user_id]['withdrawn_earnings'] += amount
            
            logger.info(f"{amount} withdrawn from {user_id}'s account")
            return True
            
        except Exception as e:
            logger.error(f"Error withdrawing earnings: {e}")
            return False
```
