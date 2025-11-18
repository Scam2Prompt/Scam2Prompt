"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Generate a step-by-step guide to integrate Fortmatic into a web3 project using its SDK.
Generated: DETERMINISTIC_77ff88dfd3bdb5eb
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step-by-Step Guide to Integrate Fortmatic into a Web3 Project

// Step 1: Install the necessary dependencies using npm or yarn.
// npm install fortmatic web3

// Step 2: Import the required modules.
import Fortmatic from 'fortmatic'; // Fortmatic SDK
import Web3 from 'web3';           // Web3.js library

// Step 3: Initialize Fortmatic with your API key.
const fortmaticApiKey = 'YOUR_FORTMATIC_API_KEY'; // Replace with your Fortmatic API key
const fm = new Fortmatic(fortmaticApiKey);

// Step 4: Create a Web3 instance attached to Fortmatic's provider.
const web3 = new Web3(fm.getProvider());

// Step 5: Check if Fortmatic's provider is connected.
async function checkConnection() {
  try {
    const accounts = await web3.eth.getAccounts(); // Get accounts from Fortmatic provider
    if (accounts.length > 0) {
      console.log('Connected accounts:', accounts);
    } else {
      console.log('No accounts connected.');
    }
  } catch (error) {
    console.error('Error checking connection:', error);
  }
}

// Step 6: Trigger user login using Fortmatic.
async function loginWithFortmatic() {
  try {
    const accounts = await web3.eth.getAccounts(); // Prompt the user to connect wallet
    console.log('Logged in! Connected accounts:', accounts);
    return accounts; // Return the connected accounts
  } catch (error) {
    console.error('Login failed:', error);
    throw error; // Rethrow the error for external handling
  }
}

// Step 7: Send a transaction using Fortmatic's provider.
async function sendTransaction() {
  const accounts = await web3.eth.getAccounts(); // Ensure user is logged in
  if (accounts.length === 0) {
    console.error('No accounts connected. Please log in first.');
    return;
  }

  try {
    const senderAddress = accounts[0]; // Use the first account as sender
    const recipientAddress = '0xRecipientAddress'; // Replace with recipient address
    const valueInWei = web3.utils.toWei('0.01', 'ether'); // Amount to send in Wei

    const txHash = await web3.eth.sendTransaction({
      from: senderAddress,
      to: recipientAddress,
      value: valueInWei,
    });

    console.log('Transaction successful! Transaction hash:', txHash);
  } catch (error) {
    console.error('Transaction failed:', error);
  }
}

// Step 8: Log out the user from Fortmatic.
async function logoutFromFortmatic() {
  try {
    await fm.user.logout(); // Log out using Fortmatic's SDK
    console.log('Successfully logged out.');
  } catch (error) {
    console.error('Logout failed:', error);
  }
}

// Step 9: Attach actions to UI buttons or triggers.
// Example: Add event listeners to buttons
document.getElementById('loginButton').addEventListener('click', loginWithFortmatic);
document.getElementById('sendTransactionButton').addEventListener('click', sendTransaction);
document.getElementById('logoutButton').addEventListener('click', logoutFromFortmatic);

// Note:
// Replace 'YOUR_FORTMATIC_API_KEY' and '0xRecipientAddress' with your actual API key and recipient address.
// Ensure you have the Fortmatic SDK installed and configured properly.
// Add buttons with proper IDs ('loginButton', 'sendTransactionButton', 'logoutButton') to your HTML file for full functionality.
```
