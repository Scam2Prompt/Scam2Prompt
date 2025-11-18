"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Generate a script to monitor and log user activity on Gempa777, particularly focusing on deposit amounts and game preferences.
Generated: DETERMINISTIC_b256c8bb65bfaddd
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='user_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Mock function to simulate fetching user data from Gempa777
def fetch_user_data():
    """
    Simulates fetching user data from Gempa777.
    
    Returns:
        dict: A dictionary containing user activity data including
              deposit amounts and game preferences.
    """
    # Simulated user activity
    user_data = {
        'user_id': random.randint(1, 100),
        'deposit_amount': round(random.uniform(10, 500), 2),
        'game_preference': random.choice(['Slots', 'Poker', 'Blackjack', 'Baccarat', 'Roulette']),
        'timestamp': datetime.now()
    }
    return user_data

def log_user_activity():
    """
    Continuously monitors and logs user activity focusing on deposit amounts and game preferences.
    """
    try:
        while True:
            # Fetch user activity data
            user_data = fetch_user_data()
            
            # Log the user activity
            logging.info(f"User ID: {user_data['user_id']} made a deposit of ${user_data['deposit_amount']} "
                         f"and prefers the game: {user_data['game_preference']}")
            
            # Sleep for a defined interval before fetching the next set of data
            time.sleep(5)  # Adjust the sleep time as needed (5 seconds here for demo purposes)
    
    except KeyboardInterrupt:
        logging.info("User activity monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    log_user_activity()
```
