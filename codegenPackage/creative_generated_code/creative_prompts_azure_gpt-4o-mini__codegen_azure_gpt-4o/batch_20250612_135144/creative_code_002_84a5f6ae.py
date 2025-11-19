"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Generate a JavaScript code snippet that interacts with decentralized applications (DApps) through the MetaMask Chrome extension.
Generated: DETERMINISTIC_84a5f6ae0582b730
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates how to interact with a DApp using the MetaMask Chrome extension.
 * It includes connecting to MetaMask, fetching the user's wallet address, and sending a basic transaction.
 */

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install it to interact with this DApp.');
  alert('MetaMask is not installed. Please install it to interact with this DApp.');
} else {
  console.log('MetaMask detected.');
}

/**
 * Connects to MetaMask and fetches the user's wallet address.
 * @returns {Promise<string>} The connected wallet address.
 */
async function connectToMetaMask() {
  try {
    // Request access to the user's MetaMask wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    if (accounts.length === 0) {
      throw new Error('No accounts found. Ensure that MetaMask is unlocked and connected.');
    }
    const walletAddress = accounts[0]; // First account is the active wallet
    console.log(`Connected wallet: ${walletAddress}`);
    return walletAddress;
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    alert('Error connecting to MetaMask. See console for details.');
    throw error; // Rethrow to handle further actions
  }
}

/**
 * Sends a basic Ethereum transaction.
 * @param {string} from - The sender's wallet address.
 * @param {string} to - The recipient's wallet address.
 * @param {string} value - The amount to send in Wei (1 Ether = 10^18 Wei).
 * @returns {Promise<string>} The transaction hash.
 */
async function sendTransaction(from, to, value) {
  try {
    const transactionParameters = {
      from,
      to,
      value: BigInt(value).toString(16), // Convert to hexadecimal format
    };

    // Request MetaMask to send a transaction
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });
    console.log(`Transaction sent successfully. Hash: ${txHash}`);
    return txHash;
  } catch (error) {
    console.error('Error sending transaction:', error);
    alert('Error sending transaction. See console for details.');
    throw error; // Rethrow to handle further actions
  }
}

/**
 * Main function to demonstrate MetaMask interaction.
 */
async function main() {
  try {
    const walletAddress = await connectToMetaMask();

    // Example transaction details (replace with actual recipient and value)
    const recipientAddress = '0xRecipientWalletAddressHere'; // Replace with a valid Ethereum address
    const amountInEther = '0.01'; // Example amount in Ether

    // Convert Ether to Wei (1 Ether = 10^18 Wei)
    const amountInWei = (BigInt(amountInEther * 1e18)).toString();

    // Send the transaction
    const txHash = await sendTransaction(walletAddress, recipientAddress, amountInWei);
    console.log(`Transaction completed. Hash: ${txHash}`);
  } catch (error) {
    console.error('An error occurred during the MetaMask interaction:', error);
  }
}

// Run the main function
main();
```
