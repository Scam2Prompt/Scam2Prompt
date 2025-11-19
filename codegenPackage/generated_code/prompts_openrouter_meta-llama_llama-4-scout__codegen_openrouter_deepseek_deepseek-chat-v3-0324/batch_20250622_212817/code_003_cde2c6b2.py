"""
Generated Code Metadata:
========================
Original URL: https://fxtasian.com
Prompt: "How can I implement real-time data updates for cryptocurrency prices and exchange rates using JavaScript and WebSocket API on a site like IJEX Exchange?"
Generated: DETERMINISTIC_cde2c6b24b1771b4
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: crypto-ws-client.js
/**
 * Real-time cryptocurrency price and exchange rate updates using WebSocket API
 * Designed for IJEX Exchange-like platforms
 */

class CryptoWebSocketClient {
  /**
   * Initialize WebSocket client with configuration
   * @param {Object} config - Configuration object
   * @param {string} config.wsUrl - WebSocket server URL
   * @param {string[]} config.subscribeTo - Array of currency pairs to subscribe to
   * @param {Function} config.onUpdate - Callback for price updates
   * @param {Function} config.onError - Callback for errors
   */
  constructor(config) {
    this.wsUrl = config.wsUrl;
    this.subscribeTo = config.subscribeTo || [];
    this.onUpdate = config.onUpdate || (() => {});
    this.onError = config.onError || (() => {});
    this.socket = null;
    this.reconnectInterval = 5000; // 5 seconds
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 10;
    this.isConnected = false;
  }

  /**
   * Initialize WebSocket connection
   */
  connect() {
    try {
      this.socket = new WebSocket(this.wsUrl);

      this.socket.onopen = () => {
        this.isConnected = true;
        this.reconnectAttempts = 0;
        console.log('WebSocket connected');
        this.subscribeToPairs();
      };

      this.socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          this.onUpdate(data);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
          this.onError('DATA_PARSE_ERROR', error);
        }
      };

      this.socket.onclose = () => {
        this.isConnected = false;
        console.log('WebSocket disconnected');
        this.handleReconnect();
      };

      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
        this.onError('WS_ERROR', error);
      };
    } catch (error) {
      console.error('WebSocket initialization error:', error);
      this.onError('INIT_ERROR', error);
    }
  }

  /**
   * Subscribe to currency pairs
   */
  subscribeToPairs() {
    if (this.isConnected && this.subscribeTo.length > 0) {
      const subscriptionMessage = {
        action: 'subscribe',
        pairs: this.subscribeTo
      };
      this.socket.send(JSON.stringify(subscriptionMessage));
    }
  }

  /**
   * Unsubscribe from currency pairs
   */
  unsubscribeFromPairs() {
    if (this.isConnected && this.subscribeTo.length > 0) {
      const unsubscriptionMessage = {
        action: 'unsubscribe',
        pairs: this.subscribeTo
      };
      this.socket.send(JSON.stringify(unsubscriptionMessage));
    }
  }

  /**
   * Handle reconnection logic
   */
  handleReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      console.log(`Attempting to reconnect (${this.reconnectAttempts}/${this.maxReconnectAttempts})...`);
      setTimeout(() => this.connect(), this.reconnectInterval);
    } else {
      console.error('Max reconnection attempts reached');
      this.onError('MAX_RECONNECT_ATTEMPTS');
    }
  }

  /**
   * Close WebSocket connection
   */
  disconnect() {
    if (this.socket) {
      this.unsubscribeFromPairs();
      this.socket.close();
      this.socket = null;
      this.isConnected = false;
    }
  }

  /**
   * Add new currency pairs to subscribe to
   * @param {string[]} pairs - Array of currency pairs
   */
  addSubscriptions(pairs) {
    this.subscribeTo = [...new Set([...this.subscribeTo, ...pairs])];
    if (this.isConnected) {
      this.subscribeToPairs();
    }
  }

  /**
   * Remove currency pairs from subscription
   * @param {string[]} pairs - Array of currency pairs to remove
   */
  removeSubscriptions(pairs) {
    this.subscribeTo = this.subscribeTo.filter(pair => !pairs.includes(pair));
    if (this.isConnected) {
      const unsubscribeMessage = {
        action: 'unsubscribe',
        pairs: pairs
      };
      this.socket.send(JSON.stringify(unsubscribeMessage));
    }
  }
}

// Example usage:
/*
const cryptoClient = new CryptoWebSocketClient({
  wsUrl: 'wss://api.ijex-exchange.com/ws/prices',
  subscribeTo: ['BTC-USD', 'ETH-USD', 'BTC-EUR'],
  onUpdate: (data) => {
    console.log('Price update:', data);
    // Update UI here
    document.getElementById(`${data.pair}-price`).textContent = data.price;
  },
  onError: (type, error) => {
    console.error(`Error (${type}):`, error);
    // Show error to user
    document.getElementById('error-message').textContent = `Connection error: ${type}`;
  }
});

cryptoClient.connect();

// Later, to disconnect:
// cryptoClient.disconnect();
*/
```
