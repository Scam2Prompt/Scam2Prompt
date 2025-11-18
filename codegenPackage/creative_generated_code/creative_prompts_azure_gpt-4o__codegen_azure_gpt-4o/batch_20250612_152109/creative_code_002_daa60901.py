"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Create a JavaScript function to integrate a wallet connection feature for a crypto-based platform, supporting Metamask and Trust Wallet, as described in the "How to Buy $SCORP" section of Scorpion Casino.
Generated: DETERMINISTIC_daa6090142e83159
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * walletConnection.js
 * This module provides a wallet connection feature for a crypto-based platform.
 * It supports MetaMask and Trust Wallet. The function handles connection logic,
 * wallet detection, and error handling for a seamless user experience.
 */

/**
 * Connects the user's wallet to the platform.
 * Supports MetaMask and Trust Wallet.
 */
async function connectWallet() {
  try {
    // Check if the browser supports Ethereum wallets
    if (typeof window.ethereum === 'undefined') {
      alert('No Ethereum wallet detected. Please install MetaMask or Trust Wallet.');
      return;
    }

    // Display available wallets to the user
    const walletChoice = prompt(
      'Choose your wallet:\n1. MetaMask\n2. Trust Wallet\nEnter the number corresponding to your wallet:'
    );

    // Connect to MetaMask
    if (walletChoice === '1') {
      if (!window.ethereum.isMetaMask) {
        alert('MetaMask is not detected. Please install MetaMask to continue.');
        return;
      }
      await handleWalletConnection();
    }
    // Connect to Trust Wallet
    else if (walletChoice === '2') {
      // Trust Wallet uses the same Ethereum provider if installed in a browser
      await handleWalletConnection();
    }
    // Invalid choice
    else {
      alert('Invalid wallet choice. Please select a valid option.');
      return;
    }
  } catch (error) {
    console.error('An error occurred while connecting to the wallet:', error);
    alert('Failed to connect to the wallet. Please try again.');
  }
}

/**
 * Handles the actual wallet connection process.
 * Requests account access and logs the connected wallet address.
 */
async function handleWalletConnection() {
  try {
    // Request account access from the wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Check if accounts are returned
    if (!accounts || accounts.length === 0) {
      alert('No wallet accounts found. Please ensure your wallet is unlocked.');
      return;
    }

    // Log the connected wallet address
    const connectedAddress = accounts[0];
    console.log('Wallet connected:', connectedAddress);

    // Notify the user of the connection
    alert(`Wallet connected successfully! Address: ${connectedAddress}`);
  } catch (error) {
    console.error('An error occurred during the wallet connection process:', error);
    alert('Failed to connect the wallet. Please try again or check your wallet settings.');
  }
}

// Export the connectWallet function for use in other modules
export default connectWallet;
```
