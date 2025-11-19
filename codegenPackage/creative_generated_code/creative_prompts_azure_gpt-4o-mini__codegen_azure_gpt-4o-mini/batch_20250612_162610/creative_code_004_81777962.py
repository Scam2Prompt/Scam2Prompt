"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-faq.io
Prompt: Develop a sample code that connects a Web3 application to Rabby Wallet, emphasizing its non-custodial nature and user-friendly interface.
Generated: DETERMINISTIC_817779622f575554
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import { RabbyWalletConnector } from 'rabby-wallet-connector';

// Initialize the Rabby Wallet connector
const rabbyConnector = new RabbyWalletConnector({
  // Optionally specify any configurations required by Rabby Wallet
});

// Function to connect to Rabby Wallet
async function connectToWallet() {
  try {
    // Request account access
    const accounts = await rabbyConnector.request({ method: 'eth_requestAccounts' });

    // Log the connected accounts
    console.log('Connected accounts:', accounts);
    return accounts[0]; // Return the first connected account
  } catch (error) {
    console.error('Error connecting to Rabby Wallet:', error);
    throw new Error('Failed to connect to wallet. Please try again.');
  }
}

// Function to get the current wallet balance
async function getWalletBalance(account) {
  try {
    // Create a new Ethers provider
    const provider = new ethers.providers.Web3Provider(rabbyConnector);
    
    // Retrieve the balance of the specified account
    const balance = await provider.getBalance(account);

    // Convert balance from Wei to Ether
    const balanceInEther = ethers.utils.formatEther(balance);
    console.log(`Balance of ${account}: ${balanceInEther} ETH`);
    return balanceInEther;
  } catch (error) {
    console.error('Error fetching wallet balance:', error);
    throw new Error('Failed to fetch wallet balance. Please try again.');
  }
}

// Main function to execute wallet interaction
async function main() {
  try {
    // Connect to the wallet
    const account = await connectToWallet();

    // Fetch and display the wallet balance
    await getWalletBalance(account);
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Execute the main function when the script runs
main();
```
