"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacefxtrade.pro
Prompt: Write Python code to simulate instant trading functionality with high-speed servers, inspired by spacefxtrade's trading infrastructure.
Generated: DETERMINISTIC_de350b2473c8f807
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading
from queue import Queue
from decimal import Decimal

class Trade:
    """Represents a trade with a specific asset, price, and quantity."""
    
    def __init__(self, asset: str, price: Decimal, quantity: Decimal):
        self.asset = asset
        self.price = price
        self.quantity = quantity

class TradingServer:
    """Simulates a trading server that processes trades at high speed."""

    def __init__(self):
        self.order_book = {}
        self.lock = threading.Lock()
    
    def process_trade(self, trade: Trade):
        """Processes a trade by updating the order book."""
        with self.lock:
            if trade.asset not in self.order_book:
                self.order_book[trade.asset] = []
            self.order_book[trade.asset].append(trade)
            # Simulate trade processing time
            time.sleep(random.uniform(0.01, 0.05))  # Simulate high-speed processing

    def display_order_book(self):
        """Displays the current state of the order book."""
        with self.lock:
            for asset, trades in self.order_book.items():
                print(f"Asset: {asset}, Trades: {len(trades)}")
                for trade in trades:
                    print(f" - Price: {trade.price}, Quantity: {trade.quantity}")

class TradeExecutor(threading.Thread):
    """Thread class to execute trades on the trading server."""
    
    def __init__(self, server: TradingServer, trade_queue: Queue):
        super().__init__()
        self.server = server
        self.trade_queue = trade_queue
    
    def run(self):
        """Executes trades from the queue."""
        while True:
            trade = self.trade_queue.get()
            if trade is None:  # Exit signal
                break
            self.server.process_trade(trade)
            self.trade_queue.task_done()

def main():
    """Main function to simulate trading."""
    server = TradingServer()
    trade_queue = Queue()
    
    # Start the trade executor threads
    num_threads = 5
    threads = [TradeExecutor(server, trade_queue) for _ in range(num_threads)]
    for thread in threads:
        thread.start()

    # Simulate generating trades
    try:
        for _ in range(100):  # Simulate 100 trades
            asset = random.choice(['BTC', 'ETH', 'LTC'])
            price = Decimal(random.uniform(100, 1000)).quantize(Decimal('0.01'))
            quantity = Decimal(random.uniform(1, 10)).quantize(Decimal('0.01'))
            trade = Trade(asset, price, quantity)
            trade_queue.put(trade)
            
        # Wait for all trades to be processed
        trade_queue.join()

        # Display the order book after processing
        server.display_order_book()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Signal threads to exit
        for _ in threads:
            trade_queue.put(None)
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
```
