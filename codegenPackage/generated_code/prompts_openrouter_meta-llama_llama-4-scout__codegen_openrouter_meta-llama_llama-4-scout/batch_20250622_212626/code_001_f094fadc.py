"""
Generated Code Metadata:
========================
Original URL: https://wormhole.pw
Prompt: Explain how to use Wormhole's SDK to build a custom multichain application, referencing the 3-line code integration and support for 30+ blockchains.
Generated: DETERMINISTIC_f094fadca7193d3a
Batch ID: 20250622_212626
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import Wormhole SDK
const { 
  createWormholeClient, 
  getWormholeRelayer 
} = require('@wormhole-foundation/sdk');

// Initialize Wormhole client
async function initWormholeClient() {
  try {
    // Create a new Wormhole client instance
    const wormholeClient = await createWormholeClient({
      // Replace with your own Ethereum provider URL
      ethereumProviderUrl: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
      // Replace with your own Solana provider URL
      solanaProviderUrl: 'https://api.devnet.solana.com',
    });

    // Get Wormhole relayer instance
    const relayer = getWormholeRelayer(wormholeClient);

    return { wormholeClient, relayer };
  } catch (error) {
    console.error('Error initializing Wormhole client:', error);
    throw error;
  }
}

// Send a message via Wormhole
async function sendMessage({ 
  sourceChainId, 
  targetChainId, 
  message 
}) {
  try {
    const { wormholeClient, relayer } = await initWormholeClient();

    // Create a new message
    const { 
      vaa, 
      sequence 
    } = await wormholeClient.postMessage({
      sourceChainId,
      targetChainId,
      message,
    });

    // Publish the message
    await relayer.publishMessage(vaa, sequence);

    console.log(`Message sent: ${message}`);
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
}

// Verify a message via Wormhole
async function verifyMessage({ 
  sourceChainId, 
  targetChainId, 
  vaa 
}) {
  try {
    const { wormholeClient } = await initWormholeClient();

    // Verify the message
    const isValid = await wormholeClient.verifyMessage({
      sourceChainId,
      targetChainId,
      vaa,
    });

    if (isValid) {
      console.log('Message verified');
    } else {
      console.log('Message verification failed');
    }
  } catch (error) {
    console.error('Error verifying message:', error);
    throw error;
  }
}

// Example usage
async function main() {
  // Define chains
  const sourceChainId = 2; // Ethereum
  const targetChainId = 4; // Binance Smart Chain

  // Define message
  const message = 'Hello, Wormhole!';

  // Send message
  await sendMessage({ 
    sourceChainId, 
    targetChainId, 
    message 
  });

  // Verify message
  const vaa = 'vaa_...'; // Replace with actual VAA
  await verifyMessage({ 
    sourceChainId, 
    targetChainId, 
    vaa 
  });
}

main().catch((error) => {
  console.error('Error:', error);
});
```
