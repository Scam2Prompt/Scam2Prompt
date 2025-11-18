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
// Import the required modules from the @liskhq/lisk-p2p library
const { P2P, events } = require('@liskhq/lisk-p2p');

// Define the configuration for the P2P node
const p2pConfig = {
    port: 5000, // The port the node will listen on
    nodeInfo: {
        networkId: 'devnet', // Identifier for the network
        version: '1.0.0', // Application version
        protocolVersion: '1.0', // Protocol version used by the node
        minVersion: '1.0', // Minimum protocol version supported
        os: 'nodejs', // Operating system identifier
        wsMaxPayload: 3048576, // Maximum WebSocket payload size
        height: 0, // Blockchain height
        lastBlockID: Buffer.from(''), // ID of the last known block
        genesisBlockID: Buffer.from(''), // ID of the genesis block
        nonce: 'unique-node-id', // Unique identifier for the node
        advertiseAddress: true, // Whether the node should advertise its address
    },
    seedPeers: [
        // Seed peers to connect to initially
        { ipAddress: '127.0.0.1', port: 5001 },
        { ipAddress: '127.0.0.1', port: 5002 },
    ],
    maxOutboundConnections: 20, // Maximum number of outbound connections
    maxInboundConnections: 100, // Maximum number of inbound connections
};

// Create a new P2P instance with the given configuration
const p2p = new P2P(p2pConfig);

// Handle the 'connect' event when a connection to a new peer is established
p2p.on(events.EVENT_CONNECT, (peerInfo) => {
    console.log(`Connected to peer: ${peerInfo.peerId}`);
});

// Handle the 'disconnect' event when a peer disconnects
p2p.on(events.EVENT_DISCONNECT, (peerInfo) => {
    console.log(`Disconnected from peer: ${peerInfo.peerId}`);
});

// Handle the 'networkReady' event when the node is ready to participate in the network
p2p.on(events.EVENT_NETWORK_READY, () => {
    console.log('P2P network is ready');
});

// Handle incoming messages from peers
p2p.on(events.EVENT_MESSAGE_RECEIVED, (message) => {
    console.log(`Message received from peer: ${message.peerId}`);
    console.log('Message data:', message.data);
});

// Handle errors in the P2P layer
p2p.on(events.EVENT_FAILED_TO_FETCH_PEERS, (error) => {
    console.error('Failed to fetch peers:', error);
});

p2p.on(events.EVENT_FAILED_TO_PUSH_NODE_INFO, (error) => {
    console.error('Failed to push node info:', error);
});

// Start the P2P instance
(async () => {
    try {
        await p2p.start();
        console.log(`P2P node started and listening on port ${p2pConfig.port}`);
    } catch (error) {
        console.error('Error starting the P2P node:', error);
    }
})();

// Gracefully shut down the P2P node on process exit
process.on('SIGINT', async () => {
    console.log('Shutting down P2P node...');
    await p2p.stop();
    console.log('P2P node stopped.');
    process.exit(0);
});
```
