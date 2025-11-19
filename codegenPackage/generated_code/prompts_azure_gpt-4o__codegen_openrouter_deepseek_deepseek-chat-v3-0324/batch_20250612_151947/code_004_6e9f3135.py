"""
Generated Code Metadata:
========================
Original URL: https://v2-pancake.pages.dev
Prompt: Create a function to simulate multiple PancakeSwap lottery rounds, including ticket purchases, prize rollovers, and CAKE injections into the prize pool.
Generated: DETERMINISTIC_6e9f31354a527628
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple
from dataclasses import dataclass
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

@dataclass
class LotteryRound:
    round_id: int
    ticket_price: Decimal
    prize_pool: Decimal
    total_tickets: int
    winning_ticket: int
    rollover_amount: Decimal
    cake_injection: Decimal
    participants: Dict[str, int]  # address -> number of tickets

class PancakeSwapLotterySimulator:
    """
    Simulates multiple PancakeSwap lottery rounds with ticket purchases,
    prize rollovers, and CAKE injections into the prize pool.
    """
    
    def __init__(self, initial_ticket_price: Decimal = Decimal('1.0')):
        """
        Initialize the simulator with default parameters.
        """
        self.current_round_id = 0
        self.initial_ticket_price = initial_ticket_price
        self.rounds: List[LotteryRound] = []
        self.rollover_amount = Decimal('0.0')
        
    def start_new_round(self, cake_injection: Decimal = Decimal('0.0')) -> LotteryRound:
        """
        Start a new lottery round with optional CAKE injection.
        """
        self.current_round_id += 1
        prize_pool = self.rollover_amount + cake_injection
        
        new_round = LotteryRound(
            round_id=self.current_round_id,
            ticket_price=self.initial_ticket_price,
            prize_pool=prize_pool,
            total_tickets=0,
            winning_ticket=0,
            rollover_amount=Decimal('0.0'),
            cake_injection=cake_injection,
            participants={}
        )
        
        self.rounds.append(new_round)
        self.rollover_amount = Decimal('0.0')  # Reset rollover after starting new round
        return new_round
    
    def buy_tickets(self, address: str, num_tickets: int, current_round: LotteryRound) -> bool:
        """
        Purchase tickets for a given address in the current round.
        """
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be positive")
        
        if address in current_round.participants:
            current_round.participants[address] += num_tickets
        else:
            current_round.participants[address] = num_tickets
            
        current_round.total_tickets += num_tickets
        current_round.prize_pool += num_tickets * current_round.ticket_price
        return True
    
    def draw_winning_ticket(self, current_round: LotteryRound) -> Tuple[str, Decimal]:
        """
        Draw the winning ticket and calculate the winner's prize.
        Returns the winner's address and the prize amount.
        """
        if current_round.total_tickets == 0:
            current_round.rollover_amount = current_round.prize_pool
            return "", Decimal('0.0')
        
        # Generate winning ticket number
        winning_ticket = random.randint(1, current_round.total_tickets)
        current_round.winning_ticket = winning_ticket
        
        # Find the winner
        cumulative_tickets = 0
        winner_address = ""
        for address, tickets in current_round.participants.items():
            cumulative_tickets += tickets
            if cumulative_tickets >= winning_ticket:
                winner_address = address
                break
        
        if not winner_address:
            raise RuntimeError("Could not determine winner")
        
        # Calculate prize (50% of prize pool)
        prize_amount = current_round.prize_pool * Decimal('0.5')
        
        # Rollover the remaining 50%
        current_round.rollover_amount = current_round.prize_pool - prize_amount
        self.rollover_amount = current_round.rollover_amount
        
        return winner_address, prize_amount
    
    def simulate_multiple_rounds(
        self,
        num_rounds: int,
        participants: List[Tuple[str, int]],
        cake_injections: List[Decimal] = None
    ) -> List[Dict]:
        """
        Simulate multiple lottery rounds with given participants and optional CAKE injections.
        Returns a list of round summaries.
        """
        if num_rounds <= 0:
            raise ValueError("Number of rounds must be positive")
        
        if cake_injections and len(cake_injections) != num_rounds:
            raise ValueError("cake_injections length must match num_rounds")
        
        if not cake_injections:
            cake_injections = [Decimal('0.0')] * num_rounds
            
        results = []
        
        for round_num in range(num_rounds):
            current_round = self.start_new_round(cake_injections[round_num])
            
            # Simulate ticket purchases
            for address, max_tickets in participants:
                tickets_to_buy = random.randint(1, max_tickets)
                self.buy_tickets(address, tickets_to_buy, current_round)
            
            # Draw winner
            winner, prize = self.draw_winning_ticket(current_round)
            
            # Record results
            results.append({
                'round_id': current_round.round_id,
                'total_tickets': current_round.total_tickets,
                'prize_pool': float(current_round.prize_pool),
                'winner': winner,
                'prize_amount': float(prize),
                'rollover_amount': float(current_round.rollover_amount),
                'cake_injection': float(current_round.cake_injection)
            })
        
        return results

# Example usage
if __name__ == "__main__":
    simulator = PancakeSwapLotterySimulator(initial_ticket_price=Decimal('5.0'))
    
    participants = [
        ("0xAlice", 10),
        ("0xBob", 15),
        ("0xCharlie", 20),
        ("0xDave", 5)
    ]
    
    cake_injections = [
        Decimal('100.0'),
        Decimal('50.0'),
        Decimal('75.0')
    ]
    
    results = simulator.simulate_multiple_rounds(
        num_rounds=3,
        participants=participants,
        cake_injections=cake_injections
    )
    
    for result in results:
        print(f"Round {result['round_id']}:")
        print(f"  Total tickets: {result['total_tickets']}")
        print(f"  Prize pool: {result['prize_pool']:.2f} CAKE")
        print(f"  Winner: {result['winner']}")
        print(f"  Prize amount: {result['prize_amount']:.2f} CAKE")
        print(f"  Rollover: {result['rollover_amount']:.2f} CAKE")
        print(f"  CAKE injection: {result['cake_injection']:.2f} CAKE")
        print()
```
