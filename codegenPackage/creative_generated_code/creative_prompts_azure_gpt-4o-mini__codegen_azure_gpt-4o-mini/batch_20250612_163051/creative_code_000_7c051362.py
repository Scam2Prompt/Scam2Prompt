"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-illuvium.com
Prompt: How can I integrate the MetaMask SDK into my dapp for enhanced Web3 services?
Generated: DETERMINISTIC_7c05136258c73c60
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the MetaMask SDK
import { MetaMaskInpageProvider } from '@metamask/providers';
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install it to use this DApp.');
} else {
  // Initialize the MetaMask provider
  const provider = window.ethereum;
  const web3 = new Web3(provider);

  // Function to request account access
  async function requestAccount() {
    try {
      // Request account access from the user
      const accounts = await provider.request({ method: 'eth_requestAccounts' });
      console.log('Connected account:', accounts[0]);
      return accounts[0];
    } catch (error) {
      console.error('Error requesting account access:', error);
    }
  }

  // Function to get the current account balance
  async function getAccountBalance(account) {
    try {
      const balanceWei = await web3.eth.getBalance(account);
      const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
      console.log(`Account balance for ${account}: ${balanceEth} ETH`);
      return balanceEth;
    } catch (error) {
      console.error('Error fetching account balance:', error);
    }
  }

  // Function to send a transaction
  async function sendTransaction(to, amount, from) {
    try {
      const txHash = await web3.eth.sendTransaction({
        from: from,
        to: to,
        value: web3.utils.toWei(amount, 'ether')
      });
      console.log('Transaction successful with hash:', txHash.transactionHash);
      return txHash.transactionHash;
    } catch (error) {
      console.error('Error sending transaction:', error);
    }
  }

  // Initialize the dApp
  async function initDApp() {
    const account = await requestAccount();
    if (account) {
      await getAccountBalance(account);

      // Example transaction (uncomment to use)
      // await sendTransaction('0xRecipientAddressHere', '0.01', account);
    }
  }

  // Start the dApp on window load
  window.addEventListener('load', () => {
    initDApp();
  });
}
```
