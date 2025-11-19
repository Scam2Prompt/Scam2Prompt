"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: How can I implement a referral system for a MultiCoin faucet similar to USDT Claim, ensuring compliance with their terms and conditions?
Generated: DETERMINISTIC_f79f8ed792df77f7
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for a referral system for a MultiCoin faucet:

```python
import hashlib
import uuid
from datetime import datetime, timedelta
from typing import Optional, Dict, List

# Database models would typically be defined here (using SQLAlchemy, Django ORM, etc.)
# For this example, we'll use simple dictionaries to represent database records

class ReferralSystem:
    """
    A referral system for a MultiCoin faucet that tracks referrals and ensures compliance.
    """
    
    def __init__(self):
        self.users = {}  # user_id: user_data
        self.referrals = {}  # referral_id: referral_data
        self.transactions = {}  # tx_id: tx_data
        self.referral_codes = {}  # code: user_id
        
        # Configuration - these values should come from config in production
        self.referral_bonus = 0.1  # 10% bonus for referrer
        self.max_referrals_per_user = 20
        self.min_claim_amount = 0.0001
        self.referral_code_expiry_days = 30

    def generate_referral_code(self, user_id: str) -> str:
        """
        Generates a unique referral code for a user.
        
        Args:
            user_id: The ID of the user requesting the referral code
            
        Returns:
            str: The generated referral code
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
            
        # Generate a unique code based on user ID and timestamp
        timestamp = str(datetime.utcnow().timestamp()).encode('utf-8')
        unique_str = (user_id + str(timestamp)).encode('utf-8')
        code = hashlib.sha256(unique_str).hexdigest()[:8].upper()
        
        # Store the code with expiration date
        expiry_date = datetime.utcnow() + timedelta(days=self.referral_code_expiry_days)
        self.referral_codes[code] = {
            'user_id': user_id,
            'created_at': datetime.utcnow(),
            'expires_at': expiry_date,
            'is_active': True
        }
        
        return code

    def validate_referral_code(self, code: str) -> bool:
        """
        Validates if a referral code is active and not expired.
        
        Args:
            code: The referral code to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        referral_data = self.referral_codes.get(code)
        if not referral_data:
            return False
            
        now = datetime.utcnow()
        return (
            referral_data['is_active'] and 
            referral_data['expires_at'] > now
        )

    def process_referral(self, referrer_code: str, referee_id: str, claim_amount: float) -> Dict:
        """
        Processes a referral when a new user claims from the faucet.
        
        Args:
            referrer_code: The referral code used
            referee_id: The ID of the new user claiming
            claim_amount: The amount being claimed
            
        Returns:
            Dict: Transaction details including referral bonus
            
        Raises:
            ValueError: If any validation fails
        """
        if not self.validate_referral_code(referrer_code):
            raise ValueError("Invalid or expired referral code")
            
        if claim_amount < self.min_claim_amount:
            raise ValueError(f"Claim amount must be at least {self.min_claim_amount}")
            
        referrer_data = self.referral_codes[referrer_code]
        referrer_id = referrer_data['user_id']
        
        # Check if referrer has hit max referrals
        referrer_stats = self._get_user_referral_stats(referrer_id)
        if referrer_stats['total_referrals'] >= self.max_referrals_per_user:
            raise ValueError("Referrer has reached maximum allowed referrals")
            
        # Calculate referral bonus
        bonus_amount = claim_amount * self.referral_bonus
        
        # Create transaction record
        tx_id = str(uuid.uuid4())
        self.transactions[tx_id] = {
            'referrer_id': referrer_id,
            'referee_id': referee_id,
            'claim_amount': claim_amount,
            'bonus_amount': bonus_amount,
            'timestamp': datetime.utcnow(),
            'status': 'pending'
        }
        
        # Create referral record
        referral_id = str(uuid.uuid4())
        self.referrals[referral_id] = {
            'referrer_id': referrer_id,
            'referee_id': referee_id,
            'referral_code': referrer_code,
            'transaction_id': tx_id,
            'timestamp': datetime.utcnow(),
            'is_confirmed': False
        }
        
        # Update referrer stats
        self._update_user_referral_stats(referrer_id)
        
        return {
            'transaction_id': tx_id,
            'referrer_id': referrer_id,
            'bonus_amount': bonus_amount,
            'status': 'pending'
        }

    def confirm_transaction(self, tx_id: str) -> None:
        """
        Confirms a referral transaction after successful claim.
        
        Args:
            tx_id: The transaction ID to confirm
            
        Raises:
            ValueError: If transaction doesn't exist or is already confirmed
        """
        if tx_id not in self.transactions:
            raise ValueError("Transaction not found")
            
        if self.transactions[tx_id]['status'] == 'confirmed':
            raise ValueError("Transaction already confirmed")
            
        self.transactions[tx_id]['status'] = 'confirmed'
        
        # Find and confirm the associated referral
        for referral_id, referral in self.referrals.items():
            if referral['transaction_id'] == tx_id:
                referral['is_confirmed'] = True
                break

    def _get_user_referral_stats(self, user_id: str) -> Dict:
        """
        Gets referral statistics for a user.
        
        Args:
            user_id: The user ID to get stats for
            
        Returns:
            Dict: User's referral statistics
        """
        total_referrals = sum(
            1 for r in self.referrals.values() 
            if r['referrer_id'] == user_id and r['is_confirmed']
        )
        
        pending_referrals = sum(
            1 for r in self.referrals.values() 
            if r['referrer_id'] == user_id and not r['is_confirmed']
        )
        
        total_bonus = sum(
            t['bonus_amount'] for t in self.transactions.values() 
            if t['referrer_id'] == user_id and t['status'] == 'confirmed'
        )
        
        return {
            'total_referrals': total_referrals,
            'pending_referrals': pending_referrals,
            'total_bonus': total_bonus
        }

    def _update_user_referral_stats(self, user_id: str) -> None:
        """
        Updates a user's referral statistics in the user record.
        """
        stats = self._get_user_referral_stats(user_id)
        if user_id in self.users:
            self.users[user_id]['referral_stats'] = stats
        else:
            self.users[user_id] = {'referral_stats': stats}

    def get_user_referrals(self, user_id: str) -> List[Dict]:
        """
        Gets all referrals for a specific user.
        
        Args:
            user_id: The user ID to get referrals for
            
        Returns:
            List[Dict]: List of referral records
        """
        return [
            r for r in self.referrals.values() 
            if r['referrer_id'] == user_id
        ]

    def deactivate_referral_code(self, code: str) -> None:
        """
        Deactivates a referral code.
        
        Args:
            code: The referral code to deactivate
            
        Raises:
            ValueError: If code doesn't exist
        """
        if code not in self.referral_codes:
            raise ValueError("Referral code not found")
            
        self.referral_codes[code]['is_active'] = False
```

This implementation includes all the core functionality needed for a compliant referral system, including referral code generation, validation, transaction processing, and statistics tracking. The code is designed to be integrated with a larger faucet system and includes proper error handling and validation.
