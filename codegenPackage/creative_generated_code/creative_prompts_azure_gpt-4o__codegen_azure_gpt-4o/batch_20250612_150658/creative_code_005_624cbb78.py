"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: How can I use MetaMask’s API to manage multiple accounts and assets in a Web3 application? Provide example code.
Generated: DETERMINISTIC_624cbb78a834d34d
Batch ID: 20250612_150658
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

// Ensure MetaMask is installed and available
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask extension first.');
  alert('MetaMask is not installed. Please install MetaMask extension.');
}

// Initialize Web3 instance using MetaMask's provider
const web3 = new Web3(window.ethereum);

// Function to request access to MetaMask accounts
async function connectMetaMask() {
  try {
    // Prompt user to connect MetaMask accounts
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    console.log('Connected accounts:', accounts);
    return accounts;
  } catch (error) {
    console.error('Error connecting to MetaMask:', error.message);
    alert('Failed to connect to MetaMask. Please try again.');
    throw error;
  }
}

// Function to get account balances
async function getAccountBalances(accounts) {
  try {
    // Create an object to store balances for each account
    const accountBalances = {};

    for (const account of accounts) {
      // Fetch balance for each account
      const balanceWei = await web3.eth.getBalance(account);
      const balanceEther = web3.utils.fromWei(balanceWei, 'ether'); // Convert balance to Ether

      accountBalances[account] = balanceEther;
    }

    console.log('Account balances:', accountBalances);
    return accountBalances;
  } catch (error) {
    console.error('Error fetching account balances:', error.message);
    throw error;
  }
}

// Function to manage assets (example: transfer Ether)
async function transferEther(fromAccount, toAccount, amountEther) {
  try {
    // Convert Ether amount to Wei (smallest unit of Ether)
    const amountWei = web3.utils.toWei(amountEther.toString(), 'ether');

    // Create transaction object
    const transaction = {
      from: fromAccount,
      to: toAccount,
      value: amountWei,
    };

    // Send transaction
    const transactionReceipt = await web3.eth.sendTransaction(transaction);

    console.log('Transaction successful:', transactionReceipt);
    return transactionReceipt;
  } catch (error) {
    console.error('Error transferring Ether:', error.message);
    alert('Failed to transfer Ether. Please check your input and try again.');
    throw error;
  }
}

// Example usage
(async function manageMetaMaskAssets() {
  try {
    // Connect to MetaMask and retrieve accounts
    const accounts = await connectMetaMask();

    // Fetch balances for each account
    const balances = await getAccountBalances(accounts);

    // Example asset management: Transfer Ether from one account to another
    if (accounts.length >= 2) {
      const sender = accounts[0];
      const receiver = accounts[1];
      const amount = 0.01; // Example amount in Ether

      console.log(`Transferring ${amount} Ether from ${sender} to ${receiver}...`);
      const receipt = await transferEther(sender, receiver, amount);
      console.log('Transaction receipt:', receipt);
    } else {
      console.log('Not enough accounts available for transfer.');
    }
  } catch (error) {
    console.error('Error managing MetaMask assets:', error.message);
  }
})();
```

This code is ready for integration into a Web3 application. Ensure you test it in a development environment before deploying to production.
