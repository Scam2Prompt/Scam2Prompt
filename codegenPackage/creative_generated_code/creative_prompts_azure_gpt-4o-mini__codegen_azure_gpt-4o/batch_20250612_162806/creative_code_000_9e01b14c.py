"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appgallery.phantomme.live
Prompt: How can I integrate Phantom Wallet API for JavaScript applications?
Generated: DETERMINISTIC_9e01b14cedba21af
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules (if applicable)
// Note: Phantom Wallet integration typically uses the window.solana object injected by the Phantom extension.
// Ensure this code runs in a browser environment with Phantom Wallet installed.

/**
 * This function checks if Phantom Wallet is available and connected.
 */
async function checkPhantomWallet() {
  try {
    if ('solana' in window) {
      const provider = window.solana;

      if (provider.isPhantom) {
        console.log("Phantom Wallet is available.");
        return provider;
      } else {
        throw new Error("Phantom Wallet is not detected.");
      }
    } else {
      throw new Error("Solana object not found. Is Phantom Wallet installed?");
    }
  } catch (error) {
    console.error("Error checking Phantom Wallet:", error.message);
    return null;
  }
}

/**
 * This function connects to Phantom Wallet and retrieves the user's public key.
 */
async function connectPhantomWallet() {
  try {
    const provider = await checkPhantomWallet();

    if (!provider) {
      throw new Error("Provider is unavailable. Cannot connect to Phantom Wallet.");
    }

    // Request connection to Phantom Wallet
    const response = await provider.connect();
    console.log("Connected to Phantom Wallet successfully.");
    console.log("Public Key:", response.publicKey.toString());

    return response.publicKey.toString();
  } catch (error) {
    console.error("Error connecting to Phantom Wallet:", error.message);
    return null;
  }
}

/**
 * This function sends a simple transaction via Phantom Wallet.
 * @param {string} senderPublicKey - The sender's public key.
 * @param {string} recipientPublicKey - The recipient's public key.
 * @param {number} amount - The amount to transfer.
 */
async function sendTransaction(senderPublicKey, recipientPublicKey, amount) {
  try {
    const provider = await checkPhantomWallet();

    if (!provider) {
      throw new Error("Provider is unavailable. Cannot send transaction.");
    }

    // Import necessary Solana Web3 libraries (usually done via npm packages like @solana/web3.js)
    const { Transaction, SystemProgram, PublicKey } = window["@solana/web3.js"];

    // Create a new transaction
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: new PublicKey(senderPublicKey),
        toPubkey: new PublicKey(recipientPublicKey),
        lamports: amount, // Amount in lamports (smallest unit of Solana)
      })
    );

    // Send the transaction via Phantom Wallet
    const signature = await provider.signAndSendTransaction(transaction);

    console.log("Transaction sent successfully.");
    console.log("Transaction Signature:", signature);

    return signature;
  } catch (error) {
    console.error("Error sending transaction:", error.message);
    return null;
  }
}

// Example usage:
(async function main() {
  try {
    // Connect to Phantom Wallet
    const userPublicKey = await connectPhantomWallet();

    if (!userPublicKey) {
      throw new Error("Failed to connect to Phantom Wallet.");
    }

    // Send a transaction (example values)
    const recipientPublicKey = "RecipientPublicKeyHere"; // Replace with a valid recipient key
    const amount = 1000000; // Example: 1 SOL = 1,000,000 lamports

    const transactionSignature = await sendTransaction(userPublicKey, recipientPublicKey, amount);
    console.log("Transaction Signature:", transactionSignature);
  } catch (error) {
    console.error("Error in main function:", error.message);
  }
})();
```

### Notes:
- Replace `RecipientPublicKeyHere` with an actual recipient's public key.
- Ensure the `@solana/web3.js` library is loaded in your project. You can include it via CDN or npm (`npm install @solana/web3.js`).
- Phantom Wallet must be installed in the browser where this code is executed.
