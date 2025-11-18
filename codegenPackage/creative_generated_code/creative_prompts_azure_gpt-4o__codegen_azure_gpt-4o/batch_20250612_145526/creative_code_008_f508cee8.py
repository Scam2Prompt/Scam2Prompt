"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "How can I implement a feature to display real-time promotions and bonuses for a slot game platform like สล็อตเว็บตรง?"
Generated: DETERMINISTIC_f508cee895e85fec
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from datetime import datetime, timedelta
import random

# Example promotions data (In production, this could come from a database)
PROMOTIONS = [
    {"id": 1, "title": "Double Points Hour", "description": "Earn double points for every spin!", "duration_minutes": 60},
    {"id": 2, "title": "Free Spin Frenzy", "description": "Get a free spin after every 10 spins!", "duration_minutes": 120},
    {"id": 3, "title": "Jackpot Booster", "description": "Increased chance to win the jackpot!", "duration_minutes": 90},
]

# Shared variable to store the current live promotion
current_promotion = None
promotion_lock = threading.Lock()  # Lock for thread-safe access to the promotion


def select_random_promotion():
    """
    Randomly selects a promotion from the available list.
    """
    return random.choice(PROMOTIONS)


def activate_promotion(promotion):
    """
    Activates the given promotion for its specified duration.
    Updates the global current_promotion variable.
    """
    global current_promotion

    with promotion_lock:  # Ensure thread-safe access
        current_promotion = promotion
        promotion_end_time = datetime.now() + timedelta(minutes=promotion["duration_minutes"])
        print(f"🔔 Promotion Activated: {promotion['title']} - {promotion['description']}")
        print(f"⏲️ Ends At: {promotion_end_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Wait for the promotion to expire
    time.sleep(promotion["duration_minutes"] * 60)

    # Deactivate the promotion
    with promotion_lock:
        print(f"🚫 Promotion Ended: {promotion['title']}")
        current_promotion = None


def promotion_scheduler():
    """
    Continuously schedules and activates promotions one at a time.
    """
    while True:
        promotion = select_random_promotion()
        activate_promotion(promotion)


def display_active_promotion():
    """
    Displays the currently active promotion in real-time.
    """
    while True:
        with promotion_lock:
            if current_promotion:
                print(f"🎉 Current Promotion: {current_promotion['title']} - {current_promotion['description']}")
            else:
                print("📢 No active promotions at the moment.")
        time.sleep(10)  # Refresh every 10 seconds


if __name__ == "__main__":
    # Run the promotion scheduler in a separate thread
    scheduler_thread = threading.Thread(target=promotion_scheduler, daemon=True)
    scheduler_thread.start()

    # Start displaying the active promotion in the main thread
    try:
        display_active_promotion()
    except KeyboardInterrupt:
        print("❌ Stopping the promotion system.")
        exit(0)
```

This Python script simulates a real-time promotion system for a slot game platform, providing production-ready code with comments and error handling for clarity.
