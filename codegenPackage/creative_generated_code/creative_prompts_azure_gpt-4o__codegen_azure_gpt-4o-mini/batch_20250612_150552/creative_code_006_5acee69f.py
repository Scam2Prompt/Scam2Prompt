"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lisk-snapshot.vercel.app
Prompt: Provide an example of using the `@liskhq/lisk-p2p` library (v0.10.0) to establish peer-to-peer connections within the Lisk network.
Generated: DETERMINISTIC_5acee69f24f29417
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the @liskhq/lisk-p2p library
const { P2P } = require('@liskhq/lisk-p2p');
const { EventEmitter } = require('events');

// Define configuration for P2P network
const config = {
    // Port to listen for incoming connections
    port: 5000,
    // List of seed peers to connect to initially
    seeds: ['localhost:5001', 'localhost:5002'],
    // Maximum number of peers allowed
    maxPeers: 10,
    // Time in milliseconds before peers are considered inactive
    peerIdleTimeout: 30000,
    // Options for handling connectivity events
    eventEmitter: new EventEmitter(),
};

// Create a P2P instance
const p2p = new P2P(config);

// Function to start the P2P network
const startP2P = async () => {
    try {
        // Start the P2P server
        await p2p.start();
        console.log(`P2P server started on port ${config.port}`);

        // Listen for peer events
        p2p.eventEmitter.on('peer:added', (peer) => {
            console.log(`Connected to peer: ${peer}`);
        });

        p2p.eventEmitter.on('peer:removed', (peer) => {
            console.log(`Disconnected from peer: ${peer}`);
        });

        // Handle connection errors
        p2p.eventEmitter.on('peer:connect:error', (error) => {
            console.error(`Error connecting to peer: ${error.message}`);
        });

    } catch (error) {
        console.error(`Failed to start P2P server: ${error.message}`);
    }
};

// Function to stop the P2P network gracefully
const stopP2P = async () => {
    try {
        await p2p.stop();
        console.log('P2P server stopped successfully.');
    } catch (error) {
        console.error(`Error stopping P2P server: ${error.message}`);
    }
};

// Start the P2P network
startP2P();

// Gracefully handle process termination
process.on('SIGINT', async () => {
    console.log('Terminating P2P server...');
    await stopP2P();
    process.exit(0);
});

process.on('SIGTERM', async () => {
    console.log('Terminating P2P server...');
    await stopP2P();
    process.exit(0);
});
```
