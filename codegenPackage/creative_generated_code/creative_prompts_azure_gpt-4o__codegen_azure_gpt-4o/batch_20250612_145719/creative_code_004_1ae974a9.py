"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Develop a program that simulates the platform's "自动排单兑换" (automatic order matching) feature, taking into account network processing speeds.
Generated: DETERMINISTIC_1ae974a94732804a
Batch ID: 20250612_145719
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
import random
from queue import PriorityQueue

# Class to represent an Order
class Order:
    def __init__(self, order_id, amount, user_id):
        self.order_id = order_id
        self.amount = amount
        self.user_id = user_id

    def __lt__(self, other):
        # Orders are sorted by their amount (ascending) for matching
        return self.amount < other.amount

    def __repr__(self):
        return f"Order(id={self.order_id}, amount={self.amount}, user={self.user_id})"


# Class to simulate automatic order matching
class AutoOrderMatcher:
    def __init__(self):
        # Priority queues for buying and selling orders
        self.buy_orders = PriorityQueue()
        self.sell_orders = PriorityQueue()
        self.lock = threading.Lock()

    def add_order(self, order, order_type):
        """
        Adds an order to the appropriate queue.
        :param order: Order object to be added
        :param order_type: 'buy' or 'sell'
        """
        with self.lock:
            if order_type == "buy":
                # Invert amount to prioritize higher matching amounts for buyers
                self.buy_orders.put((-order.amount, order))
            elif order_type == "sell":
                self.sell_orders.put((order.amount, order))

    def match_orders(self):
        """
        Matches buy and sell orders based on their amounts.
        """
        while True:
            with self.lock:
                if not self.buy_orders.empty() and not self.sell_orders.empty():
                    # Peek at the top buy and sell orders
                    _, buy_order = self.buy_orders.queue[0]
                    sell_amount, sell_order = self.sell_orders.queue[0]

                    # Match if the buy amount is greater than or equal to the sell amount
                    if -buy_order.amount >= sell_amount:
                        # Remove orders from queues
                        self.buy_orders.get()
                        self.sell_orders.get()

                        print(f"Matched: {buy_order} with {sell_order}")

                        # Simulate network processing speed
                        time.sleep(random.uniform(0.5, 1.5))
                    else:
                        # No match possible currently
                        break
                else:
                    # Either queue is empty
                    break

            # Avoid tight loop spinning
            time.sleep(0.1)


# Simulate incoming orders
def simulate_orders(matcher, user_id_base):
    """
    Simulates incoming buy and sell orders.
    :param matcher: Instance of AutoOrderMatcher
    :param user_id_base: Base user ID to generate unique user IDs
    """
    order_id = 1
    while True:
        # Randomly create a buy or sell order
        order_type = random.choice(["buy", "sell"])
        amount = random.randint(1, 100)
        user_id = user_id_base + random.randint(1, 1000)

        order = Order(order_id, amount, user_id)
        matcher.add_order(order, order_type)
        print(f"Added {order_type} order: {order}")

        order_id += 1

        # Simulate network delay
        time.sleep(random.uniform(0.2, 1.0))


if __name__ == "__main__":
    matcher = AutoOrderMatcher()

    # Start the order matching in a separate thread
    match_thread = threading.Thread(target=matcher.match_orders, daemon=True)
    match_thread.start()

    # Simulate incoming orders in separate threads
    simulator_thread1 = threading.Thread(target=simulate_orders, args=(matcher, 1000), daemon=True)
    simulator_thread2 = threading.Thread(target=simulate_orders, args=(matcher, 2000), daemon=True)

    simulator_thread1.start()
    simulator_thread2.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
```
