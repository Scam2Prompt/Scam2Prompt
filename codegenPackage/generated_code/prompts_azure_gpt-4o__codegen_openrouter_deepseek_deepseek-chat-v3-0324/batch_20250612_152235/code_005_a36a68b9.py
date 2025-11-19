"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Develop a Python script to simulate weekly Bitcoin price prediction challenges and calculate rewards for participants based on their accuracy, as described in the Green Bitcoin gamified staking model.
Generated: DETERMINISTIC_a36a68b9a500d55f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from typing import List, Dict, Tuple
from datetime import datetime, timedelta

class BitcoinPriceSimulator:
    """
    Simulates Bitcoin price movements using a geometric Brownian motion model.
    """
    def __init__(self, initial_price: float, volatility: float, drift: float):
        self.current_price = initial_price
        self.volatility = volatility
        self.drift = drift
    
    def next_price(self) -> float:
        """
        Generate next price using GBM formula.
        """
        dt = 1  # daily time step
        shock = random.gauss(0, 1)
        self.current_price *= np.exp((self.drift - 0.5 * self.volatility**2) * dt + 
                                    self.volatility * np.sqrt(dt) * shock)
        return self.current_price

class Participant:
    """
    Represents a participant in the prediction challenge.
    """
    def __init__(self, name: str, skill_level: float):
        self.name = name
        self.skill_level = skill_level  # 0-1 scale where 1 is perfect predictor
        self.total_rewards = 0.0
        self.predictions = []
    
    def make_prediction(self, current_price: float) -> float:
        """
        Generate a prediction based on current price and participant skill.
        """
        # More skilled participants have predictions closer to actual future price
        noise = random.gauss(0, 1 - self.skill_level)
        prediction = current_price * (1 + noise * 0.1)  # 10% max daily variation
        self.predictions.append(prediction)
        return prediction

class WeeklyChallenge:
    """
    Manages a weekly prediction challenge.
    """
    def __init__(self, start_date: datetime, initial_price: float):
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=7)
        self.price_simulator = BitcoinPriceSimulator(
            initial_price=initial_price,
            volatility=0.03,  # 3% daily volatility
            drift=0.0005     # Small positive drift
        )
        self.actual_prices = []
        self.participants: List[Participant] = []
    
    def add_participant(self, participant: Participant):
        """Add a participant to the challenge."""
        self.participants.append(participant)
    
    def run_simulation(self) -> Dict[str, float]:
        """
        Run the weekly simulation and calculate rewards.
        Returns a dictionary of participant names and their rewards.
        """
        # Simulate prices for the week
        current_date = self.start_date
        while current_date <= self.end_date:
            price = self.price_simulator.next_price()
            self.actual_prices.append((current_date, price))
            current_date += timedelta(days=1)
        
        # Collect predictions from participants
        predictions = {}
        for participant in self.participants:
            predictions[participant.name] = [
                participant.make_prediction(price) for date, price in self.actual_prices
            ]
        
        # Calculate rewards
        final_price = self.actual_prices[-1][1]
        rewards = self.calculate_rewards(predictions, final_price)
        
        # Update participant rewards
        for participant in self.participants:
            participant.total_rewards += rewards.get(participant.name, 0)
        
        return rewards
    
    def calculate_rewards(self, predictions: Dict[str, List[float]], final_price: float) -> Dict[str, float]:
        """
        Calculate rewards based on prediction accuracy.
        Uses Mean Absolute Percentage Error (MAPE) as accuracy metric.
        """
        rewards = {}
        total_stake = len(self.participants) * 100  # Assuming each participant stakes 100 tokens
        
        for name, preds in predictions.items():
            # Use the last prediction as the weekly forecast
            last_prediction = preds[-1]
            absolute_error = abs(last_prediction - final_price)
            percentage_error = absolute_error / final_price
            
            # Accuracy is inverse of error, clamped to 0-1
            accuracy = max(0, 1 - percentage_error)
            
            # Reward is proportional to accuracy and total stake pool
            reward = total_stake * accuracy / len(self.participants)
            rewards[name] = reward
        
        return rewards

class GreenBitcoinModel:
    """
    Main class to manage multiple weekly challenges.
    """
    def __init__(self, initial_price: float):
        self.initial_price = initial_price
        self.challenges: List[WeeklyChallenge] = []
        self.participants: Dict[str, Participant] = {}
    
    def add_participant(self, name: str, skill_level: float):
        """Add a participant to the system."""
        if name in self.participants:
            raise ValueError(f"Participant {name} already exists")
        self.participants[name] = Participant(name, skill_level)
    
    def run_weekly_challenge(self, start_date: datetime) -> Dict[str, float]:
        """Run a new weekly challenge starting at the given date."""
        challenge = WeeklyChallenge(start_date, self.initial_price)
        
        # Add all participants to this challenge
        for participant in self.participants.values():
            challenge.add_participant(participant)
        
        # Run the challenge and store results
        rewards = challenge.run_simulation()
        self.challenges.append(challenge)
        
        # Update initial price for next week
        self.initial_price = challenge.actual_prices[-1][1]
        
        return rewards
    
    def get_participant_stats(self, name: str) -> Dict[str, float]:
        """Get statistics for a participant."""
        if name not in self.participants:
            raise ValueError(f"Participant {name} not found")
        
        participant = self.participants[name]
        return {
            "name": name,
            "skill_level": participant.skill_level,
            "total_rewards": participant.total_rewards,
            "participation_count": len(participant.predictions)
        }

# Example usage
if __name__ == "__main__":
    # Initialize the model with current Bitcoin price
    gbm = GreenBitcoinModel(initial_price=50000.0)
    
    # Add participants with varying skill levels
    gbm.add_participant("Alice", 0.9)  # Highly skilled
    gbm.add_participant("Bob", 0.6)    # Moderately skilled
    gbm.add_participant("Charlie", 0.3) # Less skilled
    
    # Run 4 weekly challenges
    start_date = datetime(2023, 1, 1)
    for week in range(4):
        print(f"\nWeek {week + 1} Challenge Results:")
        rewards = gbm.run_weekly_challenge(start_date)
        for name, reward in rewards.items():
            print(f"{name}: {reward:.2f} tokens")
        start_date += timedelta(days=7)
    
    # Print final participant stats
    print("\nFinal Participant Statistics:")
    for name in ["Alice", "Bob", "Charlie"]:
        stats = gbm.get_participant_stats(name)
        print(f"{name}: {stats['total_rewards']:.2f} total tokens")
```
