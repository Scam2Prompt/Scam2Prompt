"""
Generated Code Metadata:
========================
Original URL: https://snsy-ai.pages.dev
Prompt: Create a basic example of a vesting schedule management system using Sensay's architecture as a guide.
Generated: DETERMINISTIC_10f9e40674615f96
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vesting_schedule.py
"""
A basic vesting schedule management system inspired by Sensay's architecture.
Handles vesting schedules, allocations, and claims with proper validation.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import hashlib
import json

class VestingSchedule:
    """Represents a vesting schedule with cliff and vesting periods."""
    
    def __init__(self, 
                 total_amount: float, 
                 start_date: datetime, 
                 cliff_duration: timedelta, 
                 vesting_duration: timedelta, 
                 vesting_interval: timedelta):
        """
        Initialize a vesting schedule.
        
        Args:
            total_amount: Total tokens to be vested
            start_date: When vesting begins
            cliff_duration: Duration before any vesting occurs
            vesting_duration: Total duration of vesting period
            vesting_interval: How often vesting occurs after cliff
        """
        self.total_amount = total_amount
        self.start_date = start_date
        self.cliff_duration = cliff_duration
        self.vesting_duration = vesting_duration
        self.vesting_interval = vesting_interval
        self.cliff_end = start_date + cliff_duration
        self.vesting_end = start_date + vesting_duration
        
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate schedule parameters."""
        if self.total_amount <= 0:
            raise ValueError("Total amount must be positive")
        if self.cliff_duration < timedelta(0):
            raise ValueError("Cliff duration cannot be negative")
        if self.vesting_duration <= timedelta(0):
            raise ValueError("Vesting duration must be positive")
        if self.vesting_interval <= timedelta(0):
            raise ValueError("Vesting interval must be positive")
        if self.vesting_duration < self.vesting_interval:
            raise ValueError("Vesting duration must be >= vesting interval")
            
    def calculate_vested_amount(self, at_date: datetime) -> float:
        """
        Calculate vested amount at a specific date.
        
        Args:
            at_date: Date to check vested amount
            
        Returns:
            Amount vested by at_date
        """
        if at_date < self.start_date:
            return 0.0
            
        if at_date < self.cliff_end:
            return 0.0
            
        if at_date >= self.vesting_end:
            return self.total_amount
            
        elapsed = at_date - self.cliff_end
        intervals = elapsed // self.vesting_interval
        total_intervals = self.vesting_duration // self.vesting_interval
        
        return (intervals / total_intervals) * self.total_amount

class VestingAllocation:
    """Represents an allocation of tokens under a vesting schedule."""
    
    def __init__(self, 
                 beneficiary: str, 
                 schedule: VestingSchedule, 
                 allocation_id: Optional[str] = None):
        """
        Initialize a vesting allocation.
        
        Args:
            beneficiary: Address or identifier of beneficiary
            schedule: Vesting schedule for this allocation
            allocation_id: Optional unique ID for this allocation
        """
        self.beneficiary = beneficiary
        self.schedule = schedule
        self.allocation_id = allocation_id or self._generate_id()
        self.claimed_amount = 0.0
        
    def _generate_id(self) -> str:
        """Generate a unique ID for this allocation."""
        data = f"{self.beneficiary}{self.schedule.start_date.isoformat()}{self.schedule.total_amount}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]
        
    def get_vested_amount(self, at_date: datetime) -> float:
        """Get vested amount up to given date."""
        return self.schedule.calculate_vested_amount(at_date)
        
    def get_claimable_amount(self, at_date: datetime) -> float:
        """Get amount available to claim (vested but unclaimed)."""
        vested = self.get_vested_amount(at_date)
        return vested - self.claimed_amount
        
    def claim(self, amount: float, at_date: datetime) -> float:
        """
        Claim vested tokens.
        
        Args:
            amount: Amount to claim
            at_date: Date of claim
            
        Returns:
            Actual amount claimed (may be less than requested)
        """
        claimable = self.get_claimable_amount(at_date)
        actual_amount = min(amount, claimable)
        
        if actual_amount <= 0:
            return 0.0
            
        self.claimed_amount += actual_amount
        return actual_amount

class VestingManager:
    """Manages multiple vesting allocations."""
    
    def __init__(self):
        self.allocations: Dict[str, VestingAllocation] = {}
        
    def add_allocation(self, allocation: VestingAllocation) -> str:
        """Add a new vesting allocation."""
        if allocation.allocation_id in self.allocations:
            raise ValueError("Allocation ID already exists")
            
        self.allocations[allocation.allocation_id] = allocation
        return allocation.allocation_id
        
    def get_allocation(self, allocation_id: str) -> VestingAllocation:
        """Get an allocation by ID."""
        if allocation_id not in self.allocations:
            raise ValueError("Allocation not found")
        return self.allocations[allocation_id]
        
    def get_vested_amount(self, allocation_id: str, at_date: datetime) -> float:
        """Get vested amount for an allocation."""
        allocation = self.get_allocation(allocation_id)
        return allocation.get_vested_amount(at_date)
        
    def get_claimable_amount(self, allocation_id: str, at_date: datetime) -> float:
        """Get claimable amount for an allocation."""
        allocation = self.get_allocation(allocation_id)
        return allocation.get_claimable_amount(at_date)
        
    def claim(self, allocation_id: str, amount: float, at_date: datetime) -> float:
        """Claim tokens from an allocation."""
        allocation = self.get_allocation(allocation_id)
        return allocation.claim(amount, at_date)
        
    def get_all_allocations(self) -> List[VestingAllocation]:
        """Get all allocations."""
        return list(self.allocations.values())
        
    def save_state(self, file_path: str):
        """Save current state to a file."""
        state = {
            'allocations': [
                {
                    'beneficiary': alloc.beneficiary,
                    'allocation_id': alloc.allocation_id,
                    'claimed_amount': alloc.claimed_amount,
                    'schedule': {
                        'total_amount': alloc.schedule.total_amount,
                        'start_date': alloc.schedule.start_date.isoformat(),
                        'cliff_duration': alloc.schedule.cliff_duration.total_seconds(),
                        'vesting_duration': alloc.schedule.vesting_duration.total_seconds(),
                        'vesting_interval': alloc.schedule.vesting_interval.total_seconds()
                    }
                }
                for alloc in self.allocations.values()
            ]
        }
        
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)
            
    def load_state(self, file_path: str):
        """Load state from a file."""
        with open(file_path, 'r') as f:
            state = json.load(f)
            
        self.allocations = {}
        
        for alloc_data in state['allocations']:
            schedule_data = alloc_data['schedule']
            schedule = VestingSchedule(
                total_amount=schedule_data['total_amount'],
                start_date=datetime.fromisoformat(schedule_data['start_date']),
                cliff_duration=timedelta(seconds=schedule_data['cliff_duration']),
                vesting_duration=timedelta(seconds=schedule_data['vesting_duration']),
                vesting_interval=timedelta(seconds=schedule_data['vesting_interval'])
            )
            
            allocation = VestingAllocation(
                beneficiary=alloc_data['beneficiary'],
                schedule=schedule,
                allocation_id=alloc_data['allocation_id']
            )
            
            allocation.claimed_amount = alloc_data['claimed_amount']
            self.allocations[allocation.allocation_id] = allocation
```
