"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Explain how to use Fortmatic to manage wallet interactions in a web3 dApp and provide code examples.
Generated: DETERMINISTIC_a792a23374960dcf
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure, here's the code:

```javascript
// Import the required modules
import Fortmatic from 'fortmatic'; // Fortmatic SDK
import Web3 from 'web3';          // Web3.js library

// Configuration for Fortmatic
const FORTMATIC_API_KEY = 'YOUR_FORTMATIC_API_KEY'; // Replace with your Fortmatic API key

// Initialize Fortmatic instance
const fm = new Fortmatic(FORTMATIC_API_KEY);

// Initialize Web3 instance using Fortmatic's provider
const web3 = new Web3(fm.getProvider());

// Function to enable the user's wallet and fetch the connected address
async function connectWallet() {
  try {
    // Request wallet connection
    const accounts = await web3.eth.getAccounts();

    if (accounts.length > 0) {
      console.log('Wallet connected successfully.');
      console.log('Connected address:', accounts[0]);
      return accounts[0]; // Return the user’s wallet address
    } else {
      console.error('No accounts found. Wallet connection failed.');
      return null;
    }
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    return null;
  }
}

// Function to check the user's wallet balance
async function checkBalance(address) {
  try {
    if (!address) {
      throw new Error('Address required to check balance.');
    }

    // Fetch the balance for the provided address
    const balanceWei = await web3.eth.getBalance(address);
    const balanceEth = web3.utils.fromWei(balanceWei, 'ether'); // Convert balance to Ether
    console.log(`Balance for address ${address}: ${balanceEth} ETH`);
    return balanceEth; // Return the balance in Ether
  } catch (error) {
    console.error('Error checking balance:', error.message);
    return null;
  }
}

// Function to send Ether from the connected wallet
async function sendEther(to, amountEth) {
  try {
    // Ensure the wallet is connected
    const accounts = await web3.eth.getAccounts();
    const from = accounts[0];

    if (!from) {
      throw new Error('No connected wallet found.');
    }

    if (!to || !amountEth) {
      throw new Error('Recipient address and amount are required.');
    }

    // Convert Ether amount to Wei
    const amountWei = web3.utils.toWei(amountEth.toString(), 'ether');

    // Create the transaction
    const tx = {
      from: from,
      to: to,
      value: amountWei
    };

    // Send the transaction
    const txHash = await web3.eth.sendTransaction(tx);
    console.log('Transaction successful:', txHash);
    return txHash; // Return the transaction hash
  } catch (error) {
    console.error('Error sending Ether:', error.message);
    return null;
  }
}

// Example usage
(async function exampleUsage() {
  // Connect the wallet
  const walletAddress = await connectWallet();

  // If connection is successful, check balance
  if (walletAddress) {
    await checkBalance(walletAddress);

    // Optional: Send Ether (replace 'RECIPIENT_ADDRESS' and 'AMOUNT_TO_SEND' with actual values)
    // await sendEther('RECIPIENT_ADDRESS', 'AMOUNT_TO_SEND');
  }
})();
```

### Notes:
1. Replace `YOUR_FORTMATIC_API_KEY` with your actual Fortmatic API key.
2. Ensure you have a valid Ethereum recipient address and an appropriate Ether amount when using `sendEther()`.
