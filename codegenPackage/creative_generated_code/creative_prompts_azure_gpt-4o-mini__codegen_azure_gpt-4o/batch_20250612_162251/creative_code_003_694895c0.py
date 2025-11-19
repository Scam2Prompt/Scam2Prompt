"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddlnft.top
Prompt: Create a function that allows users to connect their MetaMask wallet for purchasing Doodles merchandise, based on the wallet integration mentioned on the Doodles page.
Generated: DETERMINISTIC_694895c0f59096c8
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import Web3 from 'web3';

// Define a function to connect MetaMask wallet and handle transactions
async function connectMetaMaskAndPurchase() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Request account connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0]; // Get the connected user address

    console.log(`Connected account: ${userAddress}`);

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Define the recipient address (merchant) and the amount of ETH to transfer
    const merchantAddress = '0xMerchantAddressHere'; // Replace with actual merchant wallet address
    const amountInEth = '0.05'; // Replace with the required purchase amount in ETH

    // Convert amount to Wei (smallest denomination of Ether) for transaction
    const amountInWei = web3.utils.toWei(amountInEth, 'ether');

    // Create a transaction object
    const transactionParams = {
      from: userAddress, // User's wallet address
      to: merchantAddress, // Merchant's wallet address
      value: amountInWei, // Amount in Wei
    };

    // Request the transaction to be performed via MetaMask
    const transactionHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParams],
    });

    console.log(`Transaction successful! Hash: ${transactionHash}`);
    alert('Purchase successful! Your transaction has been processed.');
  } catch (error) {
    // Handle errors
    console.error('Error connecting MetaMask or processing transaction:', error);
    alert(`An error occurred: ${error.message}`);
  }
}

// Hook up the function to a button click (example usage)
document.getElementById('purchaseButton').addEventListener('click', connectMetaMaskAndPurchase);
```

---

**Note**: Replace `'0xMerchantAddressHere'` with the actual merchant wallet address that will receive payments for Doodles merchandise. Ensure the button with ID `purchaseButton` exists in your HTML.
