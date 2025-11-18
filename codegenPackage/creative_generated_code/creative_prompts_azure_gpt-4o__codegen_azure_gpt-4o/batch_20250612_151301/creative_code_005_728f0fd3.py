"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Create a Python script to simulate the weekly Bitcoin price prediction game described on the Green Bitcoin website, including reward distribution logic for correct predictions.
Generated: DETERMINISTIC_728f0fd374b55341
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

# Function to simulate weekly Bitcoin price prediction game
def simulate_bitcoin_price_game():
    """
    Simulates a weekly Bitcoin price prediction game.
    Participants predict the price of Bitcoin, and rewards are distributed based on accuracy.
    """
    # Constants
    NUM_PARTICIPANTS = 100  # Number of participants in the game
    STARTING_REWARD_POOL = 1000.0  # Reward pool in USD
    BITCOIN_PRICE_RANGE = (20000, 60000)  # Range of Bitcoin price in USD
    
    # Generate the actual Bitcoin price at the end of the week
    actual_price = random.uniform(*BITCOIN_PRICE_RANGE)
    
    # Participants' predictions and their accuracy
    participants = []
    for i in range(NUM_PARTICIPANTS):
        prediction = random.uniform(*BITCOIN_PRICE_RANGE)
        accuracy = abs(actual_price - prediction)
        participants.append({
            'id': i + 1,
            'prediction': prediction,
            'accuracy': accuracy
        })
    
    # Sort participants by accuracy (lower accuracy is better)
    sorted_participants = sorted(participants, key=lambda x: x['accuracy'])
    
    # Reward distribution logic
    rewards = []
    total_reward_pool = STARTING_REWARD_POOL
    top_winners_count = 10  # Number of winners
    
    for i, participant in enumerate(sorted_participants[:top_winners_count]):
        # Reward decreases as the rank increases
        reward_amount = total_reward_pool * (0.5 / (i + 1))
        total_reward_pool -= reward_amount
        rewards.append({
            'id': participant['id'],
-->  doc
