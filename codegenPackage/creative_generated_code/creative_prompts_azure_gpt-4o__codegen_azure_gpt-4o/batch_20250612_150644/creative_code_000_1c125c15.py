"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: Write code to integrate MetaMask SDK into a web3 application, enabling wallet connection and transaction management.
Generated: DETERMINISTIC_1c125c15fb5b2775
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (ensure dependencies are installed via npm/yarn)
import { MetaMaskSDK } from '@metamask/sdk';
import Web3 from 'web3';

// Initialize MetaMaskSDK
const MMSDK = new MetaMaskSDK();
const ethereum = MMSDK.getProvider(); // MetaMask provider

// Check if the provider exists
if (!ethereum) {
  console.error('MetaMask provider not found. Please install MetaMask.');
  alert('MetaMask is not installed. Please install it to continue.');
}

// Initialize Web3 with MetaMask provider
const web3 = new Web3(ethereum);

// Connect to the user's MetaMask wallet
const connectWallet = async () => {
  try {
    // Trigger MetaMask wallet connection
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });

    // Display the connected wallet address
    console.log('Connected wallet address:', accounts[0]);
    alert(`Connected wallet address: ${accounts[0]}`);
  } catch (error) {
    console.error('Error connecting to wallet:', error.message);
    alert(`Error connecting to wallet: ${error.message}`);
  }
};

// Send a transaction using the connected wallet
const sendTransaction = async (toAddress, amountInEther) => {
  try {
    // Get the connected wallet address
    const accounts = await web3.eth.getAccounts();
    const fromAddress = accounts[0];

    if (!fromAddress) {
      throw new Error('No connected wallet found.');
    }

    // Convert Ether amount to Wei (smallest unit)
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    // Create the transaction object
    const transactionParameters = {
      from: fromAddress,
      to: toAddress,
      value: amountInWei,
    };

    // Send transaction via MetaMask
    const txHash = await ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction successful. Hash:', txHash);
    alert(`Transaction successful. Hash: ${txHash}`);
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    alert(`Error sending transaction: ${error.message}`);
  }
};

// Example usage:
// Replace '0xRecipientAddress' and '0.1' with actual recipient and amount values
// connectWallet();
// sendTransaction('0xRecipientAddress', '0.1');

// Add event listeners for MetaMask state changes
ethereum.on('accountsChanged', (accounts) => {
  console.log('Accounts changed:', accounts);
  alert(`Accounts changed: ${accounts}`);
});

ethereum.on('chainChanged', (chainId) => {
  console.log('Chain changed to:', chainId);
  alert(`Chain changed to: ${chainId}`);
});

// Export functions for external use
export { connectWallet, sendTransaction };
```
