"""
Generated Code Metadata:
========================
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Explain how to use Fortmatic to manage wallet interactions in a web3 dApp and provide code examples.
Generated: DETERMINISTIC_a792a23374960dcf
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Fortmatic from 'fortmatic';
import Web3 from 'web3';

// Initialize Fortmatic with your API key
const fm = new Fortmatic('YOUR_API_KEY', 'rinkeby'); // Use appropriate network
const web3 = new Web3(fm.getProvider());

// Function to connect wallet
async function connectWallet() {
  try {
    // Request account access
    const accounts = await web3.eth.requestAccounts();
    console.log('Connected account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

// Function to get user balance
async function getBalance(address) {
  try {
    const balance = await web3.eth.getBalance(address);
    const etherBalance = web3.utils.fromWei(balance, 'ether');
    console.log('Balance:', etherBalance, 'ETH');
    return etherBalance;
  } catch (error) {
    console.error('Error getting balance:', error);
    throw error;
  }
}

// Function to send transaction
async function sendTransaction(from, to, amount) {
  try {
    const value = web3.utils.toWei(amount, 'ether');
    const tx = await web3.eth.sendTransaction({
      from,
      to,
      value
    });
    console.log('Transaction successful:', tx.transactionHash);
    return tx;
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw error;
  }
}

// Function to sign a message
async function signMessage(message, address) {
  try {
    const signedMessage = await web3.eth.personal.sign(message, address);
    console.log('Signed message:', signedMessage);
    return signedMessage;
  } catch (error) {
    console.error('Error signing message:', error);
    throw error;
  }
}

// Function to disconnect wallet
function disconnectWallet() {
  try {
    fm.user.logout();
    console.log('Wallet disconnected');
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Connect wallet
    const account = await connectWallet();
    
    // Get balance
    await getBalance(account);
    
    // Sign message
    await signMessage('Hello World', account);
    
    // Send transaction (example - would need valid recipient address)
    // await sendTransaction(account, '0x...', '0.01');
    
    // Disconnect wallet
    // disconnectWallet();
  } catch (error) {
    console.error('Error in example flow:', error);
  }
})();
```
