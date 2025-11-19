"""
Generated Code Metadata:
========================
Original URL: https://djrikaya.com
Prompt: Write a Tornado code example that demonstrates how to handle WebSocket connections for real-time updates in a cryptocurrency application.
Generated: DETERMINISTIC_39e4db82d1fc2a88
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import random

# A simple in-memory store for cryptocurrency prices
class PriceStore:
    def __init__(self):
        self.prices = {
            "BTC": 50000,
            "ETH": 4000,
            "LTC": 200
        }

    def get_price(self, currency):
        return self.prices.get(currency, None)

    def update_price(self, currency):
        # Simulate price change
        if currency in self.prices:
            self.prices[currency] += random.randint(-1000, 1000)

# WebSocket handler for real-time updates
class CryptoWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()  # Set to keep track of connected clients
    price_store = PriceStore()

    def open(self):
        """Called when a new WebSocket connection is opened."""
        self.clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        """Called when a message is received from the client."""
        try:
            data = json.loads(message)
            currency = data.get("currency")
            if currency:
                price = self.price_store.get_price(currency)
                if price is not None:
                    self.write_message(json.dumps({"currency": currency, "price": price}))
                else:
                    self.write_message(json.dumps({"error": "Currency not found"}))
            else:
                self.write_message(json.dumps({"error": "Invalid message format"}))
        except json.JSONDecodeError:
            self.write_message(json.dumps({"error": "Invalid JSON"}))

    def on_close(self):
        """Called when the WebSocket connection is closed."""
        self.clients.remove(self)
        print("WebSocket closed")

    @classmethod
    def broadcast_prices(cls):
        """Broadcast updated prices to all connected clients."""
        for client in cls.clients:
            for currency in cls.price_store.prices.keys():
                cls.price_store.update_price(currency)
                price = cls.price_store.get_price(currency)
                client.write_message(json.dumps({"currency": currency, "price": price}))

# Tornado application setup
def make_app():
    return tornado.web.Application([
        (r"/ws", CryptoWebSocket),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server started on ws://localhost:8888/ws")
    
    # Start broadcasting prices every 5 seconds
    tornado.ioloop.PeriodicCallback(CryptoWebSocket.broadcast_prices, 5000).start()
    
    tornado.ioloop.IOLoop.current().start()
```
