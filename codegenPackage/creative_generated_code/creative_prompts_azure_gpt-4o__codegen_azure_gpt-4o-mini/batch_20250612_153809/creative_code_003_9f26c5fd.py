"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Provide an example of how to use MetaMask with Hop Protocol to facilitate cross-chain token transfers between Ethereum and Polygon networks.
Generated: DETERMINISTIC_9f26c5fd284b1a74
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { Hop } from '@hop-protocol/sdk';

// Initialize Web3 and Hop SDK
const web3 = new Web3(window.ethereum);
const hop = new Hop({
  provider: window.ethereum,
});

// Function to initiate a cross-chain token transfer from Ethereum to Polygon
async function transferTokens(tokenAddress, amount, recipientAddress) {
  try {
    // Request user account access
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    
    // Get user's Ethereum account
    const accounts = await web3.eth.getAccounts();
    const senderAddress = accounts[0];

    // Create a transfer object
    const transfer = {
      token: tokenAddress, // ERC20 token address
      amount: web3.utils.toWei(amount.toString(), 'ether'), // Convert to wei
      from: senderAddress,
      to: recipientAddress,
      chainId: 1, // Ethereum Mainnet
      toChainId: 137, // Polygon Mainnet
    };

    // Execute the transfer
    const tx = await hop.send(transfer);
    
    // Wait for the transaction to be confirmed
    const receipt = await tx.wait();
    console.log('Transfer successful:', receipt);
    
  } catch (error) {
    console.error('Error during token transfer:', error);
    
    // Handle error gracefully
    if (error.code === 4001) {
      console.error('User rejected the request.');
    } else {
      console.error('Transfer failed:', error.message);
    }
  }
}

// Example usage: transferring 0.1 ETH worth of an ERC20 token
const tokenAddress = '0xYourTokenAddress'; // Replace with your token address
const amount = 0.1; // Amount to transfer
const recipientAddress = '0xRecipientAddress'; // Replace with recipient address

// Call the transfer function
transferTokens(tokenAddress, amount, recipientAddress);
```
