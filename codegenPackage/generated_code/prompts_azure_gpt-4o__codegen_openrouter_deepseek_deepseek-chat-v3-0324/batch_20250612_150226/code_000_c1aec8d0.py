"""
Generated Code Metadata:
========================
Original URL: https://lingo-bqh.pages.dev
Prompt: Write code to simulate a queue system for a cryptocurrency token presale, similar to the $LINGO token presale, where users are assigned a position and given a time limit to complete their purchase.
Generated: DETERMINISTIC_c1aec8d06ce20635
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum

class PresaleStatus(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class UserPurchaseStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"

class User:
    def __init__(self, user_id: str, wallet_address: str):
        self.user_id = user_id
        self.wallet_address = wallet_address
        self.queue_position: Optional[int] = None
        self.purchase_status: UserPurchaseStatus = UserPurchaseStatus.PENDING
        self.allocation_time: Optional[datetime] = None
        self.expiration_time: Optional[datetime] = None

    def __str__(self):
        return f"User {self.user_id} ({self.wallet_address}) - Position: {self.queue_position}, Status: {self.purchase_status}"

class PresaleQueue:
    def __init__(self, presale_name: str, total_tokens: float, token_price: float, purchase_time_limit: int = 300):
        self.presale_name = presale_name
        self.total_tokens = total_tokens
        self.remaining_tokens = total_tokens
        self.token_price = token_price
        self.purchase_time_limit = purchase_time_limit  # in seconds
        self.status = PresaleStatus.NOT_STARTED
        self.queue: List[User] = []
        self.current_position = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def add_user_to_queue(self, user: User) -> bool:
        if self.status != PresaleStatus.NOT_STARTED:
            return False
        
        user.queue_position = len(self.queue) + 1
        self.queue.append(user)
        return True

    def start_presale(self) -> bool:
        if self.status != PresaleStatus.NOT_STARTED or not self.queue:
            return False
        
        self.status = PresaleStatus.IN_PROGRESS
        self.start_time = datetime.now()
        return True

    def process_next_user(self) -> Optional[User]:
        if self.status != PresaleStatus.IN_PROGRESS or self.current_position >= len(self.queue):
            return None
        
        user = self.queue[self.current_position]
        user.allocation_time = datetime.now()
        user.expiration_time = user.allocation_time + timedelta(seconds=self.purchase_time_limit)
        self.current_position += 1
        return user

    def simulate_purchase(self, user: User) -> bool:
        if user.purchase_status != UserPurchaseStatus.PENDING:
            return False
        
        if datetime.now() > user.expiration_time:
            user.purchase_status = UserPurchaseStatus.EXPIRED
            return False
        
        # Simulate purchase with 90% success rate
        success = random.random() < 0.9
        
        if success:
            # Calculate random token amount (1-5% of remaining tokens)
            token_percentage = random.uniform(0.01, 0.05)
            token_amount = min(self.remaining_tokens * token_percentage, self.remaining_tokens)
            self.remaining_tokens -= token_amount
            user.purchase_status = UserPurchaseStatus.COMPLETED
        else:
            user.purchase_status = UserPurchaseStatus.FAILED
        
        return success

    def check_completion(self) -> bool:
        if self.status != PresaleStatus.IN_PROGRESS:
            return False
        
        if self.remaining_tokens <= 0 or self.current_position >= len(self.queue):
            self.status = PresaleStatus.COMPLETED
            self.end_time = datetime.now()
            return True
        return False

    def get_queue_position(self, user_id: str) -> Optional[int]:
        for user in self.queue:
            if user.user_id == user_id:
                return user.queue_position
        return None

    def get_user_status(self, user_id: str) -> Optional[UserPurchaseStatus]:
        for user in self.queue:
            if user.user_id == user_id:
                return user.purchase_status
        return None

    def get_presale_stats(self) -> Dict:
        return {
            "presale_name": self.presale_name,
            "status": self.status.value,
            "total_tokens": self.total_tokens,
            "remaining_tokens": self.remaining_tokens,
            "token_price": self.token_price,
            "queue_length": len(self.queue),
            "current_position": self.current_position,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }

def simulate_presale():
    # Initialize presale
    presale = PresaleQueue(
        presale_name="LINGO Token Presale",
        total_tokens=1_000_000,
        token_price=0.05
    )

    # Add users to queue
    for i in range(1, 101):
        user = User(
            user_id=f"user_{i}",
            wallet_address=f"0xWalletAddress{i}"
        )
        presale.add_user_to_queue(user)

    # Start presale
    presale.start_presale()
    print("Presale started!")

    # Process queue
    while presale.status == PresaleStatus.IN_PROGRESS:
        current_user = presale.process_next_user()
        if current_user:
            print(f"\nProcessing {current_user}")
            print(f"Time remaining: {presale.purchase_time_limit} seconds")
            
            # Simulate user taking some time to purchase
            processing_time = random.randint(10, 60)
            print(f"User is processing purchase... (takes {processing_time} seconds)")
            time.sleep(processing_time)
            
            # Attempt purchase
            success = presale.simulate_purchase(current_user)
            print(f"Purchase {'successful' if success else 'failed'}. Status: {current_user.purchase_status}")
            
            # Check if presale is completed
            if presale.check_completion():
                print("\nPresale completed!")
                break
            
            # Print stats
            stats = presale.get_presale_stats()
            print(f"\nPresale stats: {stats}")
        else:
            print("No more users in queue")
            break

    # Final stats
    print("\nFinal presale statistics:")
    print(presale.get_presale_stats())

if __name__ == "__main__":
    simulate_presale()
```
