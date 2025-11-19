"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Generate code to simulate a virtual agent for debt collection, achieving over 70% effectiveness in recovery rates, as outlined by Invicta Cobranças.
Generated: DETERMINISTIC_a9794f6a485fd0e4
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Debtor:
    """Represents a debtor with associated debt information."""
    
    def __init__(self, debtor_id: str, name: str, debt_amount: float, contact_info: Dict[str, str], last_contact: Optional[datetime] = None):
        """
        Initialize a Debtor instance.
        
        Args:
            debtor_id: Unique identifier for the debtor.
            name: Name of the debtor.
            debt_amount: Total amount owed.
            contact_info: Dictionary containing contact details (phone, email, etc.).
            last_contact: Last contact attempt datetime (optional).
        """
        self.debtor_id = debtor_id
        self.name = name
        self.debt_amount = debt_amount
        self.contact_info = contact_info
        self.last_contact = last_contact
        self.payment_history = []
        self.contact_attempts = 0
        self.response_status = None  # 'positive', 'negative', 'neutral', None
    
    def add_payment(self, amount: float, date: datetime) -> None:
        """Record a payment made by the debtor."""
        self.payment_history.append((amount, date))
        self.debt_amount -= amount
    
    def update_contact_attempt(self, status: str) -> None:
        """Update the last contact attempt and response status."""
        self.last_contact = datetime.now()
        self.contact_attempts += 1
        self.response_status = status
    
    def get_debt_status(self) -> str:
        """Return the current debt status."""
        if self.debt_amount <= 0:
            return "paid"
        elif self.response_status == "positive":
            return "negotiating"
        elif self.contact_attempts == 0:
            return "uncontacted"
        else:
            return "pending"

class VirtualAgent:
    """Simulates a virtual debt collection agent."""
    
    def __init__(self, name: str, strategy: str = "adaptive"):
        """
        Initialize the VirtualAgent instance.
        
        Args:
            name: Name of the virtual agent.
            strategy: Collection strategy ('adaptive', 'aggressive', 'gentle').
        """
        self.name = name
        self.strategy = strategy
        self.debtors: Dict[str, Debtor] = {}
        self.recovery_rate = 0.0
        self.total_recovered = 0.0
        self.total_debt = 0.0
    
    def add_debtor(self, debtor: Debtor) -> None:
        """Add a debtor to the agent's portfolio."""
        self.debtors[debtor.debtor_id] = debtor
        self.total_debt += debtor.debt_amount
    
    def remove_debtor(self, debtor_id: str) -> None:
        """Remove a debtor from the agent's portfolio."""
        if debtor_id in self.debtors:
            self.total_debt -= self.debtors[debtor_id].debt_amount
            del self.debtors[debtor_id]
    
    def calculate_recovery_rate(self) -> float:
        """Calculate and update the current recovery rate."""
        if self.total_debt == 0:
            return 0.0
        self.recovery_rate = (self.total_recovered / (self.total_recovered + self.total_debt)) * 100
        return self.recovery_rate
    
    def determine_contact_priority(self, debtor: Debtor) -> int:
        """
        Determine the priority for contacting a debtor based on strategy.
        
        Higher priority means the debtor should be contacted sooner.
        """
        if self.strategy == "aggressive":
            return debtor.debt_amount * (1 + debtor.contact_attempts)
        elif self.strategy == "gentle":
            return debtor.debt_amount * (0.5 + 0.5 * (1 / (debtor.contact_attempts + 1)))
        else:  # adaptive
            if debtor.response_status == "positive":
                return debtor.debt_amount * 2
            elif debtor.response_status == "neutral":
                return debtor.debt_amount * 1
            else:
                return debtor.debt_amount * (1 + 0.5 * debtor.contact_attempts)
    
    def generate_response(self, debtor: Debtor) -> str:
        """
        Simulate a debtor's response to a contact attempt.
        
        Returns:
            Response status ('positive', 'negative', 'neutral').
        """
        # Base probabilities
        if debtor.debt_amount > 10000:
            positive_prob = 0.3
            negative_prob = 0.5
        else:
            positive_prob = 0.6
            negative_prob = 0.2
        
        # Adjust based on contact attempts
        positive_prob *= (1 - 0.1 * debtor.contact_attempts)
        negative_prob *= (1 + 0.1 * debtor.contact_attempts)
        
        # Normalize
        total = positive_prob + negative_prob
        if total > 1:
            positive_prob /= total
            negative_prob /= total
        
        neutral_prob = 1 - positive_prob - negative_prob
        
        # Generate response
        rand = random.random()
        if rand < positive_prob:
            return "positive"
        elif rand < positive_prob + negative_prob:
            return "negative"
        else:
            return "neutral"
    
    def generate_payment_offer(self, debtor: Debtor) -> Tuple[float, float]:
        """
        Generate a payment offer based on debtor's status and strategy.
        
        Returns:
            Tuple of (offer_amount, discount_rate).
        """
        if self.strategy == "aggressive":
            discount = 0.0
            min_payment = debtor.debt_amount * 0.5
        elif self.strategy == "gentle":
            discount = 0.2
            min_payment = debtor.debt_amount * 0.2
        else:  # adaptive
            if debtor.response_status == "positive":
                discount = 0.15
                min_payment = debtor.debt_amount * 0.3
            else:
                discount = 0.05
                min_payment = debtor.debt_amount * 0.4
        
        offer = max(min_payment, debtor.debt_amount * random.uniform(0.2, 0.8))
        return offer, discount
    
    def process_payment(self, debtor: Debtor, amount: float) -> None:
        """Process a payment from a debtor."""
        debtor.add_payment(amount, datetime.now())
        self.total_recovered += amount
        self.total_debt -= amount
        self.calculate_recovery_rate()
    
    def contact_debtor(self, debtor: Debtor) -> bool:
        """
        Simulate a contact attempt with a debtor.
        
        Returns:
            True if contact resulted in payment, False otherwise.
        """
        response = self.generate_response(debtor)
        debtor.update_contact_attempt(response)
        
        if response == "positive":
            offer, discount = self.generate_payment_offer(debtor)
            discounted_amount = offer * (1 - discount)
            
            # Simulate debtor's decision to pay
            if random.random() < 0.7:  # 70% chance of accepting offer
                self.process_payment(debtor, discounted_amount)
                return True
        return False
    
    def run_collection_cycle(self, max_contacts: int = 50) -> None:
        """
        Run a collection cycle, contacting debtors based on priority.
        
        Args:
            max_contacts: Maximum number of contact attempts in this cycle.
        """
        # Sort debtors by priority
        debtors = sorted(
            self.debtors.values(),
            key=lambda d: self.determine_contact_priority(d),
            reverse=True
        )
        
        contacts_made = 0
        for debtor in debtors:
            if contacts_made >= max_contacts:
                break
            
            if debtor.get_debt_status() in ["paid"]:
                continue
            
            # Check if enough time has passed since last contact
            if debtor.last_contact and (datetime.now() - debtor.last_contact) < timedelta(days=1):
                continue
            
            if self.contact_debtor(debtor):
                contacts_made += 1
    
    def optimize_strategy(self) -> None:
        """Adjust strategy based on current recovery rate."""
        if self.recovery_rate < 50:
            self.strategy = "aggressive"
        elif self.recovery_rate < 70:
            self.strategy = "adaptive"
        else:
            self.strategy = "gentle"

def simulate_debt_collection(agent: VirtualAgent, num_cycles: int = 30, debtors: Optional[List[Debtor]] = None) -> float:
    """
    Simulate debt collection over multiple cycles.
    
    Args:
        agent: VirtualAgent instance.
        num_cycles: Number of collection cycles to simulate.
        debtors: Optional list of debtors to initialize.
    
    Returns:
        Final recovery rate.
    """
    if debtors:
        for debtor in debtors:
            agent.add_debtor(debtor)
    
    for _ in range(num_cycles):
        agent.run_collection
