"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoin-prime-site.com
Prompt: Create a JavaScript code example to integrate Bitcoin Prime's trading signals with a custom trading dashboard, using web sockets for real-time data updates.
Generated: DETERMINISTIC_f4039ff32c88f76d
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const WebSocket = require('ws');
const EventEmitter = require('events');

/**
 * BitcoinPrimeSignalClient - A WebSocket client for Bitcoin Prime trading signals
 * @class
 * @extends EventEmitter
 */
class BitcoinPrimeSignalClient extends EventEmitter {
    /**
     * @constructor
     * @param {string} apiKey - The API key for authentication
     * @param {string} [endpoint='wss://api.bitcoinprime.com/signals'] - WebSocket endpoint
     */
    constructor(apiKey, endpoint = 'wss://api.bitcoinprime.com/signals') {
        super();
        this.apiKey = apiKey;
        this.endpoint = endpoint;
        this.socket = null;
        this.connected = false;
        this.reconnectInterval = 5000; // 5 seconds
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
    }

    /**
     * Connect to the Bitcoin Prime WebSocket server
     */
    connect() {
        this.socket = new WebSocket(this.endpoint);

        this.socket.on('open', () => {
            this.connected = true;
            this.reconnectAttempts = 0;
            this.authenticate();
            this.emit('connected');
        });

        this.socket.on('message', (data) => {
            try {
                const message = JSON.parse(data);
                this.handleMessage(message);
            } catch (error) {
                this.emit('error', new Error(`Failed to parse message: ${error.message}`));
            }
        });

        this.socket.on('close', () => {
            this.connected = false;
            this.emit('disconnected');
            this.handleReconnect();
        });

        this.socket.on('error', (error) => {
            this.emit('error', error);
        });
    }

    /**
     * Authenticate with the WebSocket server
     */
    authenticate() {
        if (!this.connected) return;

        const authMessage = {
            action: 'auth',
            apiKey: this.apiKey
        };

        this.sendMessage(authMessage);
    }

    /**
     * Send message to WebSocket server
     * @param {object} message - The message to send
     */
    sendMessage(message) {
        if (!this.connected) {
            throw new Error('Not connected to WebSocket server');
        }

        try {
            this.socket.send(JSON.stringify(message));
        } catch (error) {
            this.emit('error', new Error(`Failed to send message: ${error.message}`));
        }
    }

    /**
     * Handle incoming messages
     * @param {object} message - The received message
     */
    handleMessage(message) {
        if (message.type === 'signal') {
            this.emit('signal', message.data);
        } else if (message.type === 'error') {
            this.emit('error', new Error(message.message));
        } else if (message.type === 'heartbeat') {
            this.emit('heartbeat');
        }
    }

    /**
     * Handle reconnection logic
     */
    handleReconnect() {
        if (this.reconnectAttempts >= this.maxReconnectAttempts) {
            this.emit('error', new Error('Max reconnection attempts reached'));
            return;
        }

        this.reconnectAttempts++;
        setTimeout(() => this.connect(), this.reconnectInterval);
    }

    /**
     * Disconnect from WebSocket server
     */
    disconnect() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

/**
 * TradingDashboard - Custom dashboard for displaying trading signals
 * @class
 */
class TradingDashboard {
    /**
     * @constructor
     * @param {BitcoinPrimeSignalClient} signalClient - The signal client instance
     */
    constructor(signalClient) {
        this.signalClient = signalClient;
        this.setupEventListeners();
    }

    /**
     * Setup event listeners for signal client
     */
    setupEventListeners() {
        this.signalClient.on('connected', () => {
            console.log('Dashboard: Connected to Bitcoin Prime signal server');
        });

        this.signalClient.on('disconnected', () => {
            console.log('Dashboard: Disconnected from Bitcoin Prime signal server');
        });

        this.signalClient.on('signal', (signal) => {
            this.displaySignal(signal);
        });

        this.signalClient.on('error', (error) => {
            console.error('Dashboard Error:', error.message);
        });
    }

    /**
     * Display trading signal on dashboard
     * @param {object} signal - The trading signal to display
     */
    displaySignal(signal) {
        console.log('New Trading Signal:', {
            pair: signal.pair,
            direction: signal.direction,
            entry: signal.entry,
            takeProfit: signal.takeProfit,
            stopLoss: signal.stopLoss,
            timestamp: new Date(signal.timestamp).toISOString()
        });
    }
}

// Example usage
if (require.main === module) {
    const API_KEY = process.env.BITCOIN_PRIME_API_KEY;
    
    if (!API_KEY) {
        console.error('Error: BITCOIN_PRIME_API_KEY environment variable not set');
        process.exit(1);
    }

    const signalClient = new BitcoinPrimeSignalClient(API_KEY);
    const dashboard = new TradingDashboard(signalClient);

    signalClient.connect();

    // Graceful shutdown
    process.on('SIGINT', () => {
        signalClient.disconnect();
        process.exit();
    });
}
```
