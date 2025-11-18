"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-solana.github.io
Prompt: Provide an example of using the Phantom wallet API to sign a message for verifying ownership of a Solana account.
Generated: DETERMINISTIC_25b2ce3e421a02a0
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Example: Signing a message using the Phantom Wallet API to verify ownership of a Solana account.
 * Preconditions: 
 * - Phantom Wallet extension installed and connected.
 * - Solana Web3.js library installed.
 * 
 * Run `npm install @solana/web3.js` to install the Solana Web3.js library.
 */

// Import Solana Web3.js library
const solanaWeb3 = require('@solana/web3.js');

// Function to sign a message with Phantom Wallet
async function signMessageWithPhantom() {
  try {
    // Check if Phantom Wallet is available (window.solana injected by Phantom browser extension)
    if (!window.solana || !window.solana.isPhantom) {
      throw new Error('Phantom Wallet is not available. Please install the Phantom extension.');
    }

    // Connect Phantom Wallet
    const wallet = await window.solana.connect();
    console.log('Wallet connected:', wallet.publicKey.toString());

    // Message to be signed
    const message = 'Verify ownership of Solana account';
    const encodedMessage = new TextEncoder().encode(message); // Encode the message into bytes

    // Request the Phantom Wallet to sign the message
    const { signature } = await window.solana.signMessage(encodedMessage, 'utf8');
    console.log('Message signed successfully:', signature);

    // Verify the signed message (optional, for demonstration)
    const verified = solanaWeb3.verifySignature(
      encodedMessage, // Original message
      Uint8Array.from(signature), // Signature returned by Phantom
      wallet.publicKey.toBuffer() // Public key of the wallet
    );

    if (verified) {
      console.log('Message signature verified successfully!');
    } else {
      console.error('Message signature verification failed!');
    }
  } catch (error) {
    console.error('Error occurred:', error.message);
  }
}

// Execute the function
signMessageWithPhantom();
```

*Note*: This code assumes you are running it in a browser with Phantom Wallet installed and connected. The `window.solana` object is injected by the Phantom Wallet browser extension. Make sure to test within a browser environment configured to interact with Solana.
