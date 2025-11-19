"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Create a Python script to manage affiliate data for WW88's "Đại lý WW88" program, including tracking referrals and calculating commissions.
Generated: DETERMINISTIC_b9e9a606084edf4e
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class AffiliateManager:
    """
    Manages affiliate data for WW88's "Đại lý WW88" program.
    Handles tracking referrals, calculating commissions, and data persistence.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the AffiliateManager with data storage directory.
        
        Args:
            data_dir: Directory to store affiliate data files
        """
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        
        # File paths
        self.affiliates_file = os.path.join(data_dir, "affiliates.json")
        self.referrals_file = os.path.join(data_dir, "referrals.csv")
        self.commissions_file = os.path.join(data_dir, "commissions.csv")
        
        # Initialize data structures
        self.affiliates: Dict[str, Dict] = self._load_affiliates()
        self.referrals: List[Dict] = self._load_referrals()
        self.commissions: List[Dict] = self._load_commissions()

    def _load_affiliates(self) -> Dict[str, Dict]:
        """Load affiliates data from JSON file."""
        try:
            if os.path.exists(self.affiliates_file):
                with open(self.affiliates_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading affiliates: {e}")
            return {}

    def _load_referrals(self) -> List[Dict]:
        """Load referrals data from CSV file."""
        referrals = []
        try:
            if os.path.exists(self.referrals_file):
                with open(self.referrals_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    referrals = list(reader)
        except Exception as e:
            print(f"Error loading referrals: {e}")
        return referrals

    def _load_commissions(self) -> List[Dict]:
        """Load commissions data from CSV file."""
        commissions = []
        try:
            if os.path.exists(self.commissions_file):
                with open(self.commissions_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    commissions = list(reader)
        except Exception as e:
            print(f"Error loading commissions: {e}")
        return commissions

    def _save_affiliates(self):
        """Save affiliates data to JSON file."""
        try:
            with open(self.affiliates_file, 'w', encoding='utf-8') as f:
                json.dump(self.affiliates, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving affiliates: {e}")

    def _save_referrals(self):
        """Save referrals data to CSV file."""
        try:
            with open(self.referrals_file, 'w', encoding='utf-8', newline='') as f:
                if self.referrals:
                    writer = csv.DictWriter(f, fieldnames=self.referrals[0].keys())
                    writer.writeheader()
                    writer.writerows(self.referrals)
        except Exception as e:
            print(f"Error saving referrals: {e}")

    def _save_commissions(self):
        """Save commissions data to CSV file."""
        try:
            with open(self.commissions_file, 'w', encoding='utf-8', newline='') as f:
                if self.commissions:
                    writer = csv.DictWriter(f, fieldnames=self.commissions[0].keys())
                    writer.writeheader()
                    writer.writerows(self.commissions)
        except Exception as e:
            print(f"Error saving commissions: {e}")

    def register_affiliate(self, affiliate_id: str, name: str, contact: str, commission_rate: float) -> bool:
        """
        Register a new affiliate.
        
        Args:
            affiliate_id: Unique ID for the affiliate
            name: Affiliate name
            contact: Contact information
            commission_rate: Commission rate (0-1)
            
        Returns:
            bool: True if registration was successful
        """
        if affiliate_id in self.affiliates:
            print(f"Affiliate ID {affiliate_id} already exists")
            return False
        
        if not 0 <= commission_rate <= 1:
            print("Commission rate must be between 0 and 1")
            return False
            
        self.affiliates[affiliate_id] = {
            "name": name,
            "contact": contact,
            "commission_rate": commission_rate,
            "registration_date": datetime.now().isoformat(),
            "status": "active"
        }
        
        self._save_affiliates()
        return True

    def record_referral(self, affiliate_id: str, customer_id: str, amount: float) -> bool:
        """
        Record a new referral.
        
        Args:
            affiliate_id: ID of referring affiliate
            customer_id: ID of referred customer
            amount: Transaction amount
            
        Returns:
            bool: True if referral was recorded successfully
        """
        if affiliate_id not in self.affiliates:
            print(f"Affiliate ID {affiliate_id} not found")
            return False
            
        referral = {
            "affiliate_id": affiliate_id,
            "customer_id": customer_id,
            "amount": amount,
            "date": datetime.now().isoformat(),
            "status": "pending"
        }
        
        self.referrals.append(referral)
        self._save_referrals()
        return True

    def calculate_commission(self, affiliate_id: str, period_start: str, period_end: str) -> float:
        """
        Calculate commission for an affiliate within a period.
        
        Args:
            affiliate_id: ID of the affiliate
            period_start: Start date (ISO format)
            period_end: End date (ISO format)
            
        Returns:
            float: Total commission amount
        """
        if affiliate_id not in self.affiliates:
            print(f"Affiliate ID {affiliate_id} not found")
            return 0.0
            
        commission_rate = self.affiliates[affiliate_id]["commission_rate"]
        total = 0.0
        
        for referral in self.referrals:
            if (referral["affiliate_id"] == affiliate_id and 
                period_start <= referral["date"] <= period_end and
                referral["status"] == "pending"):
                total += float(referral["amount"]) * commission_rate
                referral["status"] = "processed"
                
        self._save_referrals()
        return total

    def process_commissions(self, period_start: str, period_end: str) -> Dict[str, float]:
        """
        Process commissions for all affiliates within a period.
        
        Args:
            period_start: Start date (ISO format)
            period_end: End date (ISO format)
            
        Returns:
            Dict[str, float]: Mapping of affiliate IDs to commission amounts
        """
        commissions = {}
        
        for affiliate_id in self.affiliates:
            if self.affiliates[affiliate_id]["status"] == "active":
                amount = self.calculate_commission(affiliate_id, period_start, period_end)
                if amount > 0:
                    commissions[affiliate_id] = amount
                    self._record_commission_payment(affiliate_id, amount, period_start, period_end)
                    
        return commissions

    def _record_commission_payment(self, affiliate_id: str, amount: float, period_start: str, period_end: str):
        """Record a commission payment in the commissions ledger."""
        payment = {
            "affiliate_id": affiliate_id,
            "amount": amount,
            "period_start": period_start,
            "period_end": period_end,
            "payment_date": datetime.now().isoformat(),
            "status": "paid"
        }
        
        self.commissions.append(payment)
        self._save_commissions()

    def get_affiliate_stats(self, affiliate_id: str) -> Optional[Dict]:
        """
        Get statistics for an affiliate.
        
        Args:
            affiliate_id: ID of the affiliate
            
        Returns:
            Optional[Dict]: Affiliate statistics or None if not found
        """
        if affiliate_id not in self.affiliates:
            return None
            
        stats = {
            "affiliate_info": self.affiliates[affiliate_id],
            "total_referrals": 0,
            "pending_referrals": 0,
            "total_commission": 0,
            "pending_commission": 0
        }
        
        for referral in self.referrals:
            if referral["affiliate_id"] == affiliate_id:
                stats["total_referrals"] += 1
                if referral["status"] == "pending":
                    stats["pending_referrals"] += 1
                    stats["pending_commission"] += float(referral["amount"]) * self.affiliates[affiliate_id]["commission_rate"]
        
        for commission in self.commissions:
            if commission["affiliate_id"] == affiliate_id:
                stats["total_commission"] += float(commission["amount
