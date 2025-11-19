"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: How can I connect a wallet using the MetaMask SDK as described in the quickstart guide?
Generated: DETERMINISTIC_877b742a5088de6d
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the MetaMask SDK
import { MetaMaskSDK } from '@metamask/sdk';

// Function to connect to a MetaMask wallet
async function connectWallet() {
  try {
    // Initialize the MetaMask SDK
    const MMSDK = new MetaMaskSDK();
    const ethereum = MMSDK.getProvider(); // Get the MetaMask provider
    
    // Check if the provider is available
    if (!ethereum) {
      throw new Error('MetaMask provider not detected. Please install MetaMask.');
    }
    
    // Request access to the user's wallet
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    
    // If accounts are successfully fetched, log the connected address
    if (accounts && accounts.length > 0) {
      console.log('Connected wallet address:', accounts[0]);
      return accounts[0]; // Return the connected wallet address
    } else {
      throw new Error('No accounts found. Wallet connection failed.');
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error connecting to the wallet:', error.message);
  }
}

// Call the function to connect the wallet
connectWallet();
```
