"""
Generated Code Metadata:
========================
Original URL: https://6051142952.pages.dev
Prompt: Write a code example using MetaMask's Institutional SDK for managing digital assets securely.
Generated: DETERMINISTIC_81bd878d5d2aec6a
Batch ID: 20250622_211812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and SDK
const { MetaMaskInstitutional } = require('@metamask-institutional/sdk');
const { ethers } = require('ethers');

// Configuration for MetaMask Institutional SDK
const config = {
  clientId: 'YOUR_CLIENT_ID', // Replace with your client ID
  environment: 'staging', // Use 'production' for live environment
  refreshToken: 'YOUR_REFRESH_TOKEN', // Replace with your refresh token
  chainId: 1, // Mainnet (Replace with desired chain ID)
};

// Initialize MetaMask Institutional SDK
const mmi = new MetaMaskInstitutional(config);

// Function to fetch and display account balances
async function getAccountBalances() {
  try {
    // Authenticate with MetaMask Institutional
    await mmi.authenticate();

    // Get the list of accounts
    const accounts = await mmi.getAccounts();
    console.log('Available accounts:', accounts);

    // Get balances for each account
    for (const account of accounts) {
      const balance = await mmi.getBalance(account.address);
      console.log(`Account ${account.name} (${account.address}) balance:`, ethers.utils.formatEther(balance));
    }
  } catch (error) {
    console.error('Error fetching account balances:', error.message);
    throw error; // Re-throw for higher-level handling
  }
}

// Function to send a transaction
async function sendTransaction(fromAddress, toAddress, amountInEth) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(fromAddress) || !ethers.utils.isAddress(toAddress)) {
      throw new Error('Invalid Ethereum address');
    }

    const amountInWei = ethers.utils.parseEther(amountInEth.toString());

    // Create transaction payload
    const transaction = {
      from: fromAddress,
      to: toAddress,
      value: amountInWei.toHexString(),
      gasLimit: 21000, // Standard gas limit for simple transfers
    };

    // Submit transaction for approval
    const txResponse = await mmi.submitTransaction(transaction);
    console.log('Transaction submitted:', txResponse);

    // Wait for transaction to be mined
    const receipt = await txResponse.wait();
    console.log('Transaction mined:', receipt.transactionHash);

    return receipt;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Get and display account balances
    await getAccountBalances();

    // Example transaction (replace with actual values)
    // await sendTransaction(
    //   '0xSenderAddress',
    //   '0xRecipientAddress',
    //   0.1 // ETH amount
    // );
  } catch (error) {
    console.error('Application error:', error);
    process.exit(1);
  }
})();
```
