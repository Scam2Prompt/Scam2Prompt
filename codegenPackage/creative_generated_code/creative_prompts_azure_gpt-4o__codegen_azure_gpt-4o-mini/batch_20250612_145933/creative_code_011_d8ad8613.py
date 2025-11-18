"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: How can I use Reef's libp2p networking features to build a scalable DeFi application? Provide code examples for integration.
Generated: DETERMINISTIC_d8ad861355b3db81
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { createLibp2p } = require('libp2p');
const { TCP } = require('libp2p-tcp');
const { MPLEX } = require('libp2p-mplex');
const { NOISE } = require('libp2p-noise');
const { MulticastDNS } = require('libp2p-mdns');
const { PeerId } = require('peer-id');
const { fromString } = require('uint8arrays/from-string');
const { toString } = require('uint8arrays/to-string');

// Configuration for libp2p
const libp2pConfig = {
  modules: {
    transport: [TCP],
    streamMuxer: [MPLEX],
    connEncryption: [NOISE],
    discovery: [MulticastDNS],
  },
};

// Function to create a new PeerId
async function createPeerId() {
  try {
    const peerId = await PeerId.create({ keyType: 'Ed25519' });
    return peerId;
  } catch (error) {
    console.error('Error creating PeerId:', error);
    throw new Error('Failed to create PeerId');
  }
}

// Main function to initialize libp2p
async function initLibp2p() {
  try {
    const peerId = await createPeerId();
    const libp2p = await createLibp2p({
      ...libp2pConfig,
      peerId,
    });

    // Start the libp2p node
    await libp2p.start();
    console.log(`Libp2p node started with id ${peerId.toB58String()}`);

    // Listen for incoming connections
    libp2p.connectionManager.on('peer:connect', (connection) => {
      console.log(`Connected to ${connection.remotePeer.toB58String()}`);
    });

    // Return the libp2p instance for further use
    return libp2p;
  } catch (error) {
    console.error('Error initializing libp2p:', error);
    throw new Error('Libp2p initialization failed');
  }
}

// Function to handle incoming messages
async function handleIncomingMessages(libp2p) {
  libp2p.connectionManager.on('peer:connect', async (connection) => {
    const stream = connection.newStream('/myapp/protocol');

    // Listen for data from the stream
    stream.on('data', (data) => {
      console.log('Received message:', toString(data));
    });

    // Example of sending a message
    const message = fromString('Hello from DeFi App!');
    await stream.write(message);
    await stream.close();
  });
}

// Entry point of the application
(async () => {
  try {
    const libp2p = await initLibp2p();
    await handleIncomingMessages(libp2p);
  } catch (error) {
    console.error('Application error:', error);
    process.exit(1);
  }
})();
```
