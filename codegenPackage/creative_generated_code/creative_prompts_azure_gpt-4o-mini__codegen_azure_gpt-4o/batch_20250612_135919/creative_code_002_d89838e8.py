"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.chat
Prompt: What are the best practices for using MetaMask with decentralized applications (dApps)?
Generated: DETERMINISTIC_d89838e81d4f68b6
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready JavaScript code that demonstrates best practices for interacting with MetaMask in a decentralized application (dApp):

```javascript
// Import ethers.js for interacting with Ethereum blockchain
import { ethers } from 'ethers';

// Check if MetaMask is installed and available
export const checkMetaMaskAvailability = () => {
  if (typeof window.ethereum === 'undefined') {
    throw new Error('MetaMask is not installed. Please install MetaMask to interact with this dApp.');
  }
};

// Request wallet connection to MetaMask
export const connectWallet = async () => {
  try {
    // Check if MetaMask is available
    checkMetaMaskAvailability();

    // Request access to the user's wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your MetaMask wallet is unlocked.');
    }

    return accounts[0]; // Return the first connected account
  } catch (error) {
    console.error('Failed to connect wallet:', error.message);
    throw error; // Re-throw error for handling elsewhere in the app
  }
};

// Get the current account connected to MetaMask
export const getCurrentAccount = async () => {
  try {
    checkMetaMaskAvailability();

    // Fetch the currently connected account
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });

    if (accounts.length === 0) {
      throw new Error('No accounts are currently connected. Please connect your wallet.');
    }

    return accounts[0];
  } catch (error) {
    console.error('Failed to fetch current account:', error.message);
    throw error;
  }
};

// Listen for account changes (e.g., when the user switches accounts in MetaMask)
export const subscribeToAccountChanges = (onAccountChanged) => {
  checkMetaMaskAvailability();

  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      console.warn('MetaMask is locked or no accounts available.');
    } else {
      onAccountChanged(accounts[0]);
    }
  });
};

// Listen for network changes (e.g., when the user switches networks in MetaMask)
export const subscribeToNetworkChanges = (onNetworkChanged) => {
  checkMetaMaskAvailability();

  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    onNetworkChanged(chainId); // Notify the app of the network change
  });
};

// Create a web3 provider using ethers.js
export const createWeb3Provider = () => {
  try {
    checkMetaMaskAvailability();

    // Use MetaMask's provider
    return new ethers.providers.Web3Provider(window.ethereum);
  } catch (error) {
    console.error('Failed to create Web3 provider:', error.message);
    throw error;
  }
};

// Example usage of signing a message
export const signMessage = async (message) => {
  try {
    const account = await getCurrentAccount();
    const provider = createWeb3Provider();
    const signer = provider.getSigner(account);

    // Sign a message with the connected account
    const signature = await signer.signMessage(message);
    return signature;
  } catch (error) {
    console.error('Failed to sign message:', error.message);
    throw error;
  }
};

// Example usage of sending a transaction
export const sendTransaction = async (transactionDetails) => {
  try {
    const provider = createWeb3Provider();
    const signer = provider.getSigner();

    // Send a transaction using the signer
    const transactionResponse = await signer.sendTransaction(transactionDetails);
    await transactionResponse.wait(); // Wait for transaction to be mined
    return transactionResponse; // Return details of the transaction
  } catch (error) {
    console.error('Failed to send transaction:', error.message);
    throw error;
  }
};

// Example usage of determining the current network
export const getCurrentNetwork = async () => {
  try {
    const provider = createWeb3Provider();
    const network = await provider.getNetwork();

    return network; // Return the network details (chainId, name, etc.)
  } catch (error) {
    console.error('Failed to fetch current network:', error.message);
    throw error;
  }
};
```

This code implements best practices for using MetaMask with decentralized applications, including error handling, subscribing to events, and leveraging ethers.js for blockchain interactions.
