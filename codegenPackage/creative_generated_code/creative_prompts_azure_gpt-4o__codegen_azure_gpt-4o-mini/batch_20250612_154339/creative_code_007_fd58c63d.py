"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Generate code to implement a badge system that shares influencers' revenue with badge holders, as described in the Halo Influencer Badge feature.
Generated: DETERMINISTIC_fd58c63db4051b10
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# halo_badge_system.py

class Badge:
    """Represents a badge that can be held by users."""
    
    def __init__(self, name: str, revenue_share_percentage: float):
        """
        Initializes a badge with a name and revenue share percentage.
        
        Args:
            name (str): The name of the badge.
            revenue_share_percentage (float): The percentage of revenue shared with badge holders.
        """
        if not (0 <= revenue_share_percentage <= 100):
            raise ValueError("Revenue share percentage must be between 0 and 100.")
        
        self.name = name
        self.revenue_share_percentage = revenue_share_percentage


class User:
    """Represents a user who can hold badges and earn revenue."""
    
    def __init__(self, username: str):
        """Initializes a user with a username and an empty set of badges."""
        self.username = username
        self.badges = []
        self.total_earnings = 0.0

    def add_badge(self, badge: Badge):
        """Adds a badge to the user's collection."""
        self.badges.append(badge)

    def calculate_earnings(self, total_revenue: float):
        """
        Calculates the total earnings for the user based on the badges held.
        
        Args:
            total_revenue (float): The total revenue generated.
        
        Returns:
            float: The total earnings for the user.
        """
        if total_revenue < 0:
            raise ValueError("Total revenue must be non-negative.")
        
        total_earnings = 0.0
        for badge in self.badges:
            total_earnings += (badge.revenue_share_percentage / 100) * total_revenue
        return total_earnings


class HaloBadgeSystem:
    """Manages the badge system for influencers and revenue sharing."""
    
    def __init__(self):
        """Initializes the Halo Badge System with an empty list of users."""
        self.users = []

    def add_user(self, user: User):
        """Adds a user to the system."""
        self.users.append(user)

    def distribute_revenue(self, total_revenue: float):
        """
        Distributes revenue among users based on the badges they hold.
        
        Args:
            total_revenue (float): The total revenue to be distributed.
        """
        if total_revenue < 0:
            raise ValueError("Total revenue must be non-negative.")
        
        for user in self.users:
            user.total_earnings = user.calculate_earnings(total_revenue)
            print(f"{user.username} earned: ${user.total_earnings:.2f}")


# Example usage
if __name__ == "__main__":
    # Create some badges
    gold_badge = Badge("Gold", 10.0)
    silver_badge = Badge("Silver", 5.0)

    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Assign badges to users
    alice.add_badge(gold_badge)
    bob.add_badge(silver_badge)
    bob.add_badge(gold_badge)

    # Create the badge system
    badge_system = HaloBadgeSystem()
    badge_system.add_user(alice)
    badge_system.add_user(bob)

    # Distribute revenue
    try:
        badge_system.distribute_revenue(1000.0)  # Distributing $1000 of revenue
    except ValueError as e:
        print(f"Error: {e}")
```
