"""
Generated Code Metadata:
========================
Original URL: https://phantomrewards.com
Prompt: Create a Python program that tracks referral earnings from Phantom Rewards’ affiliate program, including monthly payouts and bonus commissions.
Generated: DETERMINISTIC_10a2241766610f55
Batch ID: 20250612_145249
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class ReferralTracker:
    """
    Tracks referral earnings from Phantom Rewards' affiliate program.
    Handles monthly payouts, bonus commissions, and generates reports.
    """
    
    def __init__(self, data_file: str = "referrals.json"):
        """
        Initialize the tracker with a data file.
        
        Args:
            data_file: Path to JSON file storing referral data
        """
        self.data_file = data_file
        self.referrals = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load referral data from JSON file.
        Creates new file if it doesn't exist.
        
        Returns:
            Dictionary containing referral data
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "referrals": {},
                "payouts": {},
                "settings": {
                    "base_rate": 0.10,  # 10% base commission
                    "bonus_threshold": 1000,  # $1000 for bonus
                    "bonus_rate": 0.05,  # 5% bonus
                    "payout_day": 15  # Payout on 15th of each month
                }
            }
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in file")
    
    def _save_data(self):
        """Save referral data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.referrals, f, indent=2)
    
    def add_referral(self, referral_id: str, name: str, amount: float, date: Optional[str] = None):
        """
        Add a new referral with their purchase amount.
        
        Args:
            referral_id: Unique ID for the referral
            name: Name of the referred customer
            amount: Purchase amount in USD
            date: Date of purchase (YYYY-MM-DD), defaults to today
        """
        if referral_id in self.referrals["referrals"]:
            raise ValueError(f"Referral ID {referral_id} already exists")
        
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
            
        self.referrals["referrals"][referral_id] = {
            "name": name,
            "amount": amount,
            "date": date,
            "commission_paid": False
        }
        self._save_data()
    
    def calculate_commission(self, referral_id: str) -> float:
        """
        Calculate commission for a referral including potential bonus.
        
        Args:
            referral_id: ID of the referral to calculate
        
        Returns:
            Total commission amount in USD
        """
        referral = self.referrals["referrals"].get(referral_id)
        if not referral:
            raise ValueError(f"Referral ID {referral_id} not found")
            
        base_commission = referral["amount"] * self.referrals["settings"]["base_rate"]
        
        # Check for bonus
        if referral["amount"] >= self.referrals["settings"]["bonus_threshold"]:
            bonus = referral["amount"] * self.referrals["settings"]["bonus_rate"]
            return base_commission + bonus
        
        return base_commission
    
    def process_monthly_payouts(self, month: Optional[str] = None):
        """
        Process all unpaid referrals for a given month.
        
        Args:
            month: Month in YYYY-MM format, defaults to current month
        """
        if not month:
            month = datetime.now().strftime("%Y-%m")
            
        total_payout = 0.0
        paid_referrals = []
        
        for ref_id, referral in self.referrals["referrals"].items():
            ref_month = referral["date"][:7]  # Extract YYYY-MM
            if ref_month == month and not referral["commission_paid"]:
                commission = self.calculate_commission(ref_id)
                total_payout += commission
                self.referrals["referrals"][ref_id]["commission_paid"] = True
                paid_referrals.append(ref_id)
        
        if paid_referrals:
            payout_id = f"payout_{month}"
            self.referrals["payouts"][payout_id] = {
                "amount": total_payout,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "referrals": paid_referrals
            }
            self._save_data()
        
        return total_payout, paid_referrals
    
    def get_earnings_report(self, start_date: str, end_date: str) -> Dict:
        """
        Generate an earnings report for a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing report data
        """
        report = {
            "total_earnings": 0,
            "base_commissions": 0,
            "bonus_commissions": 0,
            "referrals": [],
            "payouts": []
        }
        
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Process referrals
        for ref_id, referral in self.referrals["referrals"].items():
            ref_date = datetime.strptime(referral["date"], "%Y-%m-%d")
            if start <= ref_date <= end:
                base = referral["amount"] * self.referrals["settings"]["base_rate"]
                bonus = 0
                
                if referral["amount"] >= self.referrals["settings"]["bonus_threshold"]:
                    bonus = referral["amount"] * self.referrals["settings"]["bonus_rate"]
                
                report["total_earnings"] += base + bonus
                report["base_commissions"] += base
                report["bonus_commissions"] += bonus
                
                report["referrals"].append({
                    "id": ref_id,
                    "name": referral["name"],
                    "amount": referral["amount"],
                    "date": referral["date"],
                    "base_commission": base,
                    "bonus_commission": bonus,
                    "paid": referral["commission_paid"]
                })
        
        # Process payouts
        for payout_id, payout in self.referrals["payouts"].items():
            payout_date = datetime.strptime(payout["date"], "%Y-%m-%d")
            if start <= payout_date <= end:
                report["payouts"].append({
                    "id": payout_id,
                    "amount": payout["amount"],
                    "date": payout["date"],
                    "referral_count": len(payout["referrals"])
                })
        
        return report
    
    def export_report_to_csv(self, report: Dict, filename: str):
        """
        Export an earnings report to CSV.
        
        Args:
            report: Report data from get_earnings_report
            filename: Output CSV filename
        """
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(["Earnings Report", f"{report.get('start_date', '')} to {report.get('end_date', '')}"])
            writer.writerow([])
            
            # Write summary
            writer.writerow(["Total Earnings", report["total_earnings"]])
            writer.writerow(["Base Commissions", report["base_commissions"]])
            writer.writerow(["Bonus Commissions", report["bonus_commissions"]])
            writer.writerow([])
            
            # Write referrals
            writer.writerow(["Referrals"])
            writer.writerow(["ID", "Name", "Amount", "Date", "Base Commission", "Bonus Commission", "Paid"])
            for ref in report["referrals"]:
                writer.writerow([
                    ref["id"],
                    ref["name"],
                    ref["amount"],
                    ref["date"],
                    ref["base_commission"],
                    ref["bonus_commission"],
                    "Yes" if ref["paid"] else "No"
                ])
            writer.writerow([])
            
            # Write payouts
            writer.writerow(["Payouts"])
            writer.writerow(["ID", "Amount", "Date", "Referral Count"])
            for payout in report["payouts"]:
                writer.writerow([
                    payout["id"],
                    payout["amount"],
                    payout["date"],
                    payout["referral_count"]
                ])

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()
    
    # Add some sample referrals
    try:
        tracker.add_referral("ref001", "Alice Johnson", 500.00, "2023-10-05")
        tracker.add_referral("ref002", "Bob Smith", 1200.00, "2023-10-12")
        tracker.add_referral("ref003", "Charlie Brown", 800.00, "2023-10-18")
