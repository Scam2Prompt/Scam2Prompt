"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.sewakamerabandung.id
Prompt: What are the key features of the MetaMask API for integrating cryptocurrency wallets into web applications?
Generated: DETERMINISTIC_192a2db33fbb3bf9
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates key features of the MetaMask API for integrating cryptocurrency wallets 
 * into web applications. It includes connecting to MetaMask, requesting user accounts, and making 
 * Ethereum transactions.
 */

// Ensure the code runs only if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is installed!');
} else {
  console.error('MetaMask is not installed. Please install it to use this application.');
}

/**
 * Function to connect to MetaMask and request user's wallet address.
 */
async function connectToMetaMask() {
  try {
    // Request user accounts from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the first account (default account)
  } catch (error) {
    console.error('Failed to connect to MetaMask:', error.message);
    throw error; // Rethrow the error for further handling
  }
}

/**
 * Function to fetch the current balance of the connected account.
 * @param {string} account - The wallet address to query the balance for.
 */
async function getAccountBalance(account) {
  try {
    // Get the balance of the given account
    const balance = await window.ethereum.request({
      method: 'eth_getBalance',
      params: [account, 'latest'],
    });
    console.log('Account balance (in Wei):', balance);
    return balance; // Return balance in Wei (smallest denomination of Ether)
  } catch (error) {
    console.error('Failed to fetch account balance:', error.message);
    throw error;
  }
}

/**
 * Function to send a transaction using MetaMask.
 * @param {string} from - The sender's wallet address.
 * @param {string} to - The recipient's wallet address.
 * @param {string} value - Amount to send in Wei (smallest denomination of Ether).
 */
async function sendTransaction(from, to, value) {
  try {
    const transactionParameters = {
      from: from, // Sender's address
      to: to, // Recipient's address
      value: value, // Amount in Wei
    };

    // Send the transaction using MetaMask
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });
    console.log('Transaction sent successfully. Transaction hash:', txHash);
    return txHash; // Return the transaction hash for reference
  } catch (error) {
    console.error('Failed to send transaction:', error.message);
    throw error;
  }
}

/**
 * Main function to demonstrate MetaMask API features.
 */
async function main() {
  try {
    // Connect to MetaMask
    const account = await connectToMetaMask();

    // Fetch account balance
    const balance = await getAccountBalance(account);

    // Convert balance from Wei to Ether for readability
    const balanceInEther = window.web3.utils.fromWei(balance, 'ether');
    console.log(`Account balance (in Ether): ${balanceInEther}`);

    // Example transaction: Sending 0.01 Ether to another address
    const recipient = '0xRecipientWalletAddressHere'; // Replace with actual recipient address
    const valueToSend = window.web3.utils.toWei('0.01', 'ether'); // Convert Ether to Wei
    const txHash = await sendTransaction(account, recipient, valueToSend);

    console.log('Transaction hash:', txHash);
  } catch (error) {
    console.error('An error occurred in the main function:', error.message);
  }
}

// Run the main function
main();

```
