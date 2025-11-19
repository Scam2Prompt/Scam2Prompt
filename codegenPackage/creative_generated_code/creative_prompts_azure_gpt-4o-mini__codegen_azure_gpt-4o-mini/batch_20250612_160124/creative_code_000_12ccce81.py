"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: How can I implement a Web3Modal example in my JavaScript application?
Generated: DETERMINISTIC_12ccce819538d48c
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Create an instance of Web3Modal
const web3Modal = new Web3Modal({
  cacheProvider: true, // Optional, enables caching the provider
  providerOptions: {} // Add any provider options if needed
});

// Function to connect to the wallet
async function connectWallet() {
  try {
    // Open the modal to select a wallet
    const provider = await web3Modal.connect();
    
    // Create an ethers provider from the connected wallet
    const web3Provider = new ethers.providers.Web3Provider(provider);
    
    // Get the signer for executing transactions
    const signer = web3Provider.getSigner();
    
    // Retrieve the user's account address
    const userAddress = await signer.getAddress();
    console.log('Connected account:', userAddress);
    
    // Return the signer for further use
    return signer;
  } catch (error) {
    console.error('Failed to connect wallet:', error);
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    await web3Modal.clearCachedProvider();
    console.log('Wallet disconnected');
  } catch (error) {
    console.error('Failed to disconnect wallet:', error);
  }
}

// Event listener for a button to connect the wallet
document.getElementById('connectButton').addEventListener('click', connectWallet);

// Event listener for a button to disconnect the wallet
document.getElementById('disconnectButton').addEventListener('click', disconnectWallet);

// Example HTML
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web3Modal Example</title>
</head>
<body>
    <button id="connectButton">Connect Wallet</button>
    <button id="disconnectButton">Disconnect Wallet</button>
    <script type="module" src="your-script.js"></script>
</body>
</html>
*/

```
