"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: How can I use the MetaMask Delegation Toolkit to create walletless dapps? Provide example code.
Generated: DETERMINISTIC_be84eda50719784b
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code for creating a walletless dApp using MetaMask Delegation Toolkit.
 * This example demonstrates how to use MetaMask Snap's Delegation Toolkit to sign messages
 * on behalf of users without requiring them to have a wallet.
 *
 * Requirements:
 * - MetaMask installed with the Delegation Toolkit Snap set up
 * - Ethereum development environment
 */

// Import the ethers.js library for working with Ethereum
import { ethers } from "ethers";

// Helper function to initialize the MetaMask Snap for delegation
async function initializeMetaMaskDelegation() {
  if (!window.ethereum) {
    throw new Error("MetaMask is not installed. Please install it to use this dApp.");
  }

  // Check if the MetaMask Delegation Snap is available
  const installedSnaps = await window.ethereum.request({
    method: "wallet_getSnaps",
  });

  const delegationSnap = Object.values(installedSnaps).find(
    (snap) => snap.id === "npm:@metamask/delegation-toolkit"
  );

  if (!delegationSnap) {
    throw new Error(
      "MetaMask Delegation Snap is not installed. Please install it from the MetaMask Snap Store."
    );
  }

  console.log("MetaMask Delegation Snap is initialized.");
}

// Function to create a walletless dApp experience by delegating signing
async function signMessageWithDelegation(message) {
  if (!window.ethereum) {
    throw new Error("MetaMask is not installed. Please install it to use this dApp.");
  }

  try {
    // Request the user's public key through MetaMask Snap
    const publicKey = await window.ethereum.request({
      method: "wallet_invokeSnap",
      params: {
        snapId: "npm:@metamask/delegation-toolkit",
        request: {
          method: "delegation_getPublicKey",
        },
      },
    });

    console.log("User's public key:", publicKey);

    // Sign the message using the MetaMask Delegation Snap
    const signature = await window.ethereum.request({
      method: "wallet_invokeSnap",
      params: {
        snapId: "npm:@metamask/delegation-toolkit",
        request: {
          method: "delegation_signMessage",
          params: {
            message: ethers.utils.hashMessage(message), // Hash the message before signing
          },
        },
      },
    });

    console.log("Signed message:", signature);
    return signature;
  } catch (error) {
    console.error("Error while signing message with delegation:", error.message);
    throw error;
  }
}

// Example usage of the walletless dApp functions
(async () => {
  try {
    // Initialize MetaMask Delegation Toolkit
    await initializeMetaMaskDelegation();

    // Example message to sign
    const message = "Hello, walletless dApp!";

    // Sign the message using MetaMask Delegation Toolkit
    const signature = await signMessageWithDelegation(message);

    console.log("Message signed successfully. Signature:", signature);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
})();
```
