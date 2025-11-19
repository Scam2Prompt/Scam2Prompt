"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Generate a code snippet for a donation tracking system that supports multiple donation levels, inspired by Waldo en Ruta's fundraising for his cycling journey across Chile.
Generated: DETERMINISTIC_c10ec2f5c20a6661
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto


class DonationLevel(Enum):
    """Enum representing different donation levels."""
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()


@dataclass
class Donor:
    """Class representing a donor with personal information."""
    name: str
    email: str
    phone: Optional[str] = None
    anonymous: bool = False


@dataclass
class Donation:
    """Class representing a single donation."""
    donor: Donor
    amount: float
    level: DonationLevel
    date: datetime.date
    message: Optional[str] = None


class DonationTracker:
    """Class to track donations and provide statistics."""
    
    def __init__(self):
        self.donations: List[Donation] = []
        self.donation_levels = {
            DonationLevel.BRONZE: 10.00,
            DonationLevel.SILVER: 50.00,
            DonationLevel.GOLD: 100.00,
            DonationLevel.PLATINUM: 500.00
        }
    
    def add_donation(self, donor: Donor, amount: float, message: str = None) -> Donation:
        """Add a new donation to the tracker.
        
        Args:
            donor: The donor information
            amount: The donation amount
            message: Optional message from donor
            
        Returns:
            The created Donation object
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive")
        
        level = self._determine_level(amount)
        donation = Donation(
            donor=donor,
            amount=amount,
            level=level,
            date=datetime.date.today(),
            message=message
        )
        self.donations.append(donation)
        return donation
    
    def _determine_level(self, amount: float) -> DonationLevel:
        """Determine donation level based on amount."""
        for level, min_amount in sorted(self.donation_levels.items(), key=lambda x: x[1], reverse=True):
            if amount >= min_amount:
                return level
        return DonationLevel.BRONZE
    
    def get_total_donations(self) -> float:
        """Get the total amount of all donations."""
        return sum(d.amount for d in self.donations)
    
    def get_donations_by_level(self, level: DonationLevel) -> List[Donation]:
        """Get all donations for a specific level."""
        return [d for d in self.donations if d.level == level]
    
    def get_top_donors(self, limit: int = 5) -> List[Donor]:
        """Get the top donors by donation amount."""
        sorted_donations = sorted(self.donations, key=lambda d: d.amount, reverse=True)
        return [d.donor for d in sorted_donations[:limit]]
    
    def get_recent_donations(self, days: int = 7) -> List[Donation]:
        """Get donations from the last N days."""
        cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
        return [d for d in self.donations if d.date >= cutoff_date]
    
    def get_donation_stats(self) -> dict:
        """Get statistics about donations."""
        return {
            'total_donations': self.get_total_donations(),
            'total_donors': len({d.donor.email for d in self.donations}),
            'bronze_donations': len(self.get_donations_by_level(DonationLevel.BRONZE)),
            'silver_donations': len(self.get_donations_by_level(DonationLevel.SILVER)),
            'gold_donations': len(self.get_donations_by_level(DonationLevel.GOLD)),
            'platinum_donations': len(self.get_donations_by_level(DonationLevel.PLATINUM)),
        }


# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()
    
    donor1 = Donor(name="Alice Smith", email="alice@example.com")
    donor2 = Donor(name="Bob Johnson", email="bob@example.com", anonymous=True)
    
    try:
        tracker.add_donation(donor1, 120.00, "Good luck on your journey!")
        tracker.add_donation(donor2, 55.00)
        tracker.add_donation(
            Donor(name="Charlie Brown", email="charlie@example.com", phone="+1234567890"),
            10.00
        )
        
        print("Total donations:", tracker.get_total_donations())
        print("Recent donations:", len(tracker.get_recent_donations()))
        print("Top donors:", [d.name for d in tracker.get_top_donors()])
        print("Stats:", tracker.get_donation_stats())
        
    except ValueError as e:
        print(f"Error processing donation: {e}")
```
