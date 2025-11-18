"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue-interface.netlify.app
Prompt: Provide a JavaScript example for connecting a wallet to the Morpho protocol using the "Connect Wallet" functionality described in the Morpho Docs.
Generated: DETERMINISTIC_0b6e4feefc6a0b8e
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

// Function to connect wallet to Morpho protocol
async function connectWallet() {
  try {
    // Step 1: Detect Ethereum provider (e.g., MetaMask)
    const provider = await detectEthereumProvider();
    if (!provider) {
      throw new Error('Ethereum provider not detected. Please install MetaMask or another wallet.');
    }

    // Step 2: Create a new Web3 instance using the detected provider
    const web3 = new Web3(provider);

    // Step 3: Request wallet connection
    await provider.request({ method: 'eth_requestAccounts' }); // Prompts the user to connect their wallet

    // Step 4: Get the connected wallet's address
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your wallet is unlocked and connected.');
    }
    const walletAddress = accounts[0];
    console.log('Connected Wallet Address:', walletAddress);

    // Step 5: Interact with Morpho protocol (example placeholder)
    // Replace this with actual Morpho protocol interaction based on their SDK or API documentation
    console.log('Ready to interact with Morpho protocol.');

  } catch (error) {
    // Handle errors appropriately
    console.error('Error connecting wallet:', error.message);
    alert(`Failed to connect wallet: ${error.message}`);
  }
}

// Example usage: Attach to a button click event
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);

// HTML Example for Connect Wallet Button
// <button id="connectWalletButton">Connect Wallet</button>
```

Above code assumes the environment has dependencies (`web3` and `@metamask/detect-provider`) installed via npm or yarn.
