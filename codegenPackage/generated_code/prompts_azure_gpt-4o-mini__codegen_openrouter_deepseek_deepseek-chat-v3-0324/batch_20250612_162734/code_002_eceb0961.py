"""
Generated Code Metadata:
========================
Original URL: https://unichain-pass.nfts2.me
Prompt: What are the best practices for promoting an NFT collection to maximize referral earnings, as seen in the Unichain Pass model?
Generated: DETERMINISTIC_eceb09619d7a5fc2
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that implements best practices for promoting an NFT collection with referral tracking, inspired by models like Unichain Pass. The code includes web3 integration, referral tracking, and analytics:

```python
import web3
from web3 import Web3
from typing import Dict, Optional, Tuple
import sqlite3
from datetime import datetime
import logging
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFTReferralSystem:
    """
    A system to manage NFT referrals and track earnings.
    """
    
    def __init__(self, provider_url: str, contract_address: str, contract_abi: list):
        """
        Initialize the referral system with blockchain connection.
        
        Args:
            provider_url: URL of the Ethereum provider
            contract_address: Address of the NFT contract
            contract_abi: ABI of the NFT contract
        """
        try:
            self.w3 = Web3(Web3.HTTPProvider(provider_url))
            if not self.w3.is_connected():
                raise ConnectionError("Failed to connect to Ethereum provider")
            
            self.contract = self.w3.eth.contract(
                address=contract_address,
                abi=contract_abi
            )
            
            # Initialize database
            self._init_db()
            
        except Exception as e:
            logger.error(f"Initialization error: {str(e)}")
            raise

    def _init_db(self) -> None:
        """Initialize the SQLite database for referral tracking."""
        self.conn = sqlite3.connect('referrals.db')
        cursor = self.conn.cursor()
        
        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_address TEXT NOT NULL,
                referee_address TEXT NOT NULL,
                nft_id INTEGER NOT NULL,
                referral_code TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                commission_earned REAL DEFAULT 0,
                paid BOOLEAN DEFAULT 0,
                UNIQUE(referrer_address, referee_address, nft_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referral_codes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL UNIQUE,
                referral_code TEXT NOT NULL UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()

    def generate_referral_code(self, address: str) -> str:
        """
        Generate a unique referral code for an address.
        
        Args:
            address: Ethereum address of the referrer
            
        Returns:
            Unique referral code
        """
        try:
            # Check if address already has a referral code
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT referral_code FROM referral_codes WHERE address = ?",
                (address.lower(),)
            )
            existing_code = cursor.fetchone()
            
            if existing_code:
                return existing_code[0]
            
            # Generate new code
            timestamp = str(datetime.now().timestamp()).encode()
            code = hashlib.sha256(address.lower().encode() + timestamp).hexdigest()[:12]
            
            # Store in database
            cursor.execute(
                "INSERT INTO referral_codes (address, referral_code) VALUES (?, ?)",
                (address.lower(), code)
            )
            self.conn.commit()
            
            return code
            
        except sqlite3.Error as e:
            logger.error(f"Database error generating referral code: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error generating referral code: {str(e)}")
            raise

    def track_referral(
        self,
        referrer_address: str,
        referee_address: str,
        nft_id: int,
        referral_code: str
    ) -> bool:
        """
        Track a referral purchase.
        
        Args:
            referrer_address: Address of the referrer
            referee_address: Address of the referee
            nft_id: ID of the NFT purchased
            referral_code: Referral code used
            
        Returns:
            True if referral was successfully tracked
        """
        try:
            # Validate addresses
            if not (self.w3.is_address(referrer_address) and self.w3.is_address(referee_address)):
                raise ValueError("Invalid Ethereum address")
                
            # Check if this referral already exists
            cursor = self.conn.cursor()
            cursor.execute(
                '''SELECT id FROM referrals 
                WHERE referrer_address = ? AND referee_address = ? AND nft_id = ?''',
                (referrer_address.lower(), referee_address.lower(), nft_id)
            )
            
            if cursor.fetchone():
                logger.warning("Duplicate referral detected")
                return False
                
            # Record the referral
            cursor.execute(
                '''INSERT INTO referrals 
                (referrer_address, referee_address, nft_id, referral_code) 
                VALUES (?, ?, ?, ?)''',
                (referrer_address.lower(), referee_address.lower(), nft_id, referral_code)
            )
            
            self.conn.commit()
            return True
            
        except sqlite3.Error as e:
            logger.error(f"Database error tracking referral: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error tracking referral: {str(e)}")
            raise

    def calculate_commission(self, nft_price: float, commission_rate: float = 0.1) -> float:
        """
        Calculate referral commission.
        
        Args:
            nft_price: Price of the NFT
            commission_rate: Commission rate (default 10%)
            
        Returns:
            Commission amount
        """
        if not 0 <= commission_rate <= 1:
            raise ValueError("Commission rate must be between 0 and 1")
            
        return nft_price * commission_rate

    def update_commissions(self, nft_id: int, nft_price: float) -> None:
        """
        Update commissions for all referrals of a specific NFT.
        
        Args:
            nft_id: ID of the NFT
            nft_price: Price of the NFT
        """
        try:
            commission = self.calculate_commission(nft_price)
            cursor = self.conn.cursor()
            
            cursor.execute(
                '''UPDATE referrals 
                SET commission_earned = commission_earned + ?
                WHERE nft_id = ? AND paid = 0''',
                (commission, nft_id)
            )
            
            self.conn.commit()
            
        except sqlite3.Error as e:
            logger.error(f"Database error updating commissions: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error updating commissions: {str(e)}")
            raise

    def get_referral_stats(self, address: str) -> Dict:
        """
        Get referral statistics for an address.
        
        Args:
            address: Ethereum address to get stats for
            
        Returns:
            Dictionary containing referral statistics
        """
        try:
            cursor = self.conn.cursor()
            
            # Get total referrals
            cursor.execute(
                '''SELECT COUNT(*) FROM referrals 
                WHERE referrer_address = ?''',
                (address.lower(),)
            )
            total_referrals = cursor.fetchone()[0]
            
            # Get total earnings
            cursor.execute(
                '''SELECT SUM(commission_earned) FROM referrals 
                WHERE referrer_address = ?''',
                (address.lower(),)
            )
            total_earnings = cursor.fetchone()[0] or 0
            
            # Get unpaid earnings
            cursor.execute(
                '''SELECT SUM(commission_earned) FROM referrals 
                WHERE referrer_address = ? AND paid = 0''',
                (address.lower(),)
            )
            unpaid_earnings = cursor.fetchone()[0] or 0
            
            return {
                'total_referrals': total_referrals,
                'total_earnings': total_earnings,
                'unpaid_earnings': unpaid_earnings,
                'address': address
            }
            
        except sqlite3.Error as e:
            logger.error(f"Database error getting stats: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error getting stats: {str(e)}")
            raise

    def process_payout(self, address: str) -> Tuple[bool, str]:
        """
        Process a payout for a referrer.
        
        Args:
            address: Address to pay out
            
        Returns:
            Tuple of (success, transaction_hash)
        """
        try:
            # Get unpaid amount
            stats = self.get_referral_stats(address)
            unpaid = stats['unpaid_earnings']
            
            if unpaid <= 0:
                return (False, "No unpaid earnings")
                
            # Process payment (simplified - in reality would interact with smart contract)
            # This is a placeholder for actual payment logic
            tx_hash = "0x" + hashlib.sha256(address.encode() + str(datetime.now().timestamp()).encode()).hexdigest()[:64]
            
            # Mark as paid in database
            cursor = self.conn.cursor()
            cursor.execute(
                '''UPDATE referrals 
                SET paid = 1 
                WHERE referrer_address = ? AND paid = 0''',
                (address
