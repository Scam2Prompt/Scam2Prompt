"""
Generated Code Metadata:
========================
Original URL: https://sync-dappwebnode.pages.dev
Prompt: Provide an example of using JavaScript to enable real-time communication between a DApp and its web node.
Generated: DETERMINISTIC_85582400d2c23d0e
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WebSocket connection to Ethereum node (e.g., Infura)
const Web3 = require('web3');
const web3 = new Web3(new Web3.providers.WebsocketProvider('wss://mainnet.infura.io/ws/v3/YOUR_INFURA_PROJECT_ID'));

// Event emitter for DApp communication
const EventEmitter = require('events');
class DAppEmitter extends EventEmitter {}
const dappEmitter = new DAppEmitter();

// Smart contract ABI and address
const contractABI = [/* Your contract ABI here */];
const contractAddress = '0xYourContractAddress';
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Connect to WebSocket and subscribe to events
async function connectToNode() {
    try {
        // Check connection
        const isConnected = await web3.eth.net.isListening();
        if (!isConnected) throw new Error('WebSocket connection failed');

        console.log('Connected to Ethereum node via WebSocket');

        // Subscribe to new blocks
        const subscription = web3.eth.subscribe('newBlockHeaders', (error, blockHeader) => {
            if (error) {
                console.error('Error in block header subscription:', error);
                return;
            }
            dappEmitter.emit('newBlock', blockHeader);
        });

        // Subscribe to contract events
        contract.events.YourEventName({
            fromBlock: 'latest'
        })
        .on('data', (event) => {
            dappEmitter.emit('contractEvent', event);
        })
        .on('error', (error) => {
            console.error('Error in contract event subscription:', error);
        });

        return subscription;
    } catch (error) {
        console.error('Connection error:', error);
        process.exit(1);
    }
}

// DApp event handlers
dappEmitter.on('newBlock', (blockHeader) => {
    console.log('New block:', blockHeader.number);
    // Update DApp UI or trigger actions
});

dappEmitter.on('contractEvent', (event) => {
    console.log('Contract event:', event);
    // Update DApp UI or trigger actions
});

// Initialize connection
connectToNode().then((subscription) => {
    // Cleanup on exit
    process.on('exit', () => {
        subscription.unsubscribe((error, success) => {
            if (error) console.error('Error unsubscribing:', error);
            if (success) console.log('Successfully unsubscribed');
        });
    });
});

// Error handling for uncaught exceptions
process.on('uncaughtException', (error) => {
    console.error('Uncaught exception:', error);
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled rejection at:', promise, 'reason:', reason);
    process.exit(1);
});
```
