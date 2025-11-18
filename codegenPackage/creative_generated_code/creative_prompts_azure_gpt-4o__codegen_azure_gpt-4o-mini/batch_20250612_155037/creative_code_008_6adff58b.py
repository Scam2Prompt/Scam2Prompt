"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Provide an overview of Hyperlane's core components and write a code example to demonstrate how to initialize and use the protocol in a decentralized application.
Generated: DETERMINISTIC_6adff58b00a4de23
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Hyperlane SDK components
import { HyperlaneCore } from '@hyperlane-xyz/core';
import { HyperlaneContracts } from '@hyperlane-xyz/contracts';
import { createClient } from '@hyperlane-xyz/client';

/**
 * Initialize and use the Hyperlane protocol in a decentralized application.
 */
async function initializeHyperlane() {
    try {
        // Define the network configuration for Hyperlane
        const config = {
            // The supported networks can be customized (e.g., mainnet, testnet)
            networks: ['mainnet', 'testnet'],
            // Add your Hyperlane project details
            projectId: 'your-project-id',
            privateKey: 'your-private-key',
        };

        // Initialize the Hyperlane core
        const hyperlane = new HyperlaneCore(config);
        
        // Initialize contracts for the specified networks
        const contracts = new HyperlaneContracts(hyperlane);
        
        // Create a client for sending and receiving messages
        const client = createClient(contracts);
        
        // Example: Sending a message across networks
        const recipient = '0xRecipientAddress'; // Replace with actual recipient address
        const message = 'Hello from Hyperlane!';

        // Send the message
        const txResponse = await client.sendMessage(recipient, message);
        
        // Wait for the transaction to be confirmed
        await txResponse.wait();

        console.log('Message sent successfully:', message);
    } catch (error) {
        console.error('Error initializing Hyperlane:', error);
    }
}

// Execute the function to initialize Hyperlane
initializeHyperlane();
```

Make sure to replace `'your-project-id'`, `'your-private-key'`, and `'0xRecipientAddress'` with actual values specific to your Hyperlane project and intended recipient address.
