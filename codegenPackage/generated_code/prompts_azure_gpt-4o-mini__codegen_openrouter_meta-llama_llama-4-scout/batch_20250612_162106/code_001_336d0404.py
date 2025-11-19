"""
Generated Code Metadata:
========================
Original URL: https://cjjzqkc.cn
Prompt: Write a code snippet to integrate the OKX Web3 wallet into a decentralized finance (DeFi) application, highlighting its multi-chain capabilities.
Generated: DETERMINISTIC_336d040436e143a4
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { OKXWeb3Wallet } = require('okx-web3-wallet');

// Set up OKX Web3 Wallet
const okxWallet = new OKXWeb3Wallet({
  // Replace with your OKX Web3 Wallet app ID
  appId: 'YOUR_APP_ID',
  // Replace with your OKX Web3 Wallet app secret
  appSecret: 'YOUR_APP_SECRET',
});

// Initialize Web3 provider
const web3 = new Web3(okxWallet);

// Define a function to handle user connection
async function connectWallet() {
  try {
    // Connect to OKX Web3 Wallet
    await okxWallet.connect();
    // Get user's Ethereum address
    const address = await web3.eth.getAccounts();
    console.log(`Connected to OKX Web3 Wallet: ${address[0]}`);
    return address[0];
  } catch (error) {
    console.error('Error connecting to OKX Web3 Wallet:', error);
    throw error;
  }
}

// Define a function to handle multi-chain transactions
async function transferTokens(chainId, recipientAddress, amount) {
  try {
    // Switch to the desired chain
    await okxWallet.switchChain(chainId);
    // Get the contract ABI for the token
    const tokenContractAbi = [
      {
        inputs: [],
        name: 'transfer',
        outputs: [],
        stateMutability: 'nonpayable',
        type: 'function',
      },
    ];
    // Replace with your token contract address
    const tokenContractAddress = '0x...';
    const tokenContract = new web3.eth.Contract(tokenContractAbi, tokenContractAddress);
    // Send transaction
    const tx = await tokenContract.methods.transfer(recipientAddress, amount).send({
      from: await web3.eth.getAccounts(),
    });
    console.log(`Transaction hash: ${tx.transactionHash}`);
  } catch (error) {
    console.error('Error transferring tokens:', error);
    throw error;
  }
}

// Example usage
async function main() {
  // Connect to OKX Web3 Wallet
  const address = await connectWallet();
  // Transfer tokens on Ethereum (chain ID 1)
  await transferTokens(1, '0x...', '10');
  // Transfer tokens on Binance Smart Chain (chain ID 56)
  await transferTokens(56, '0x...', '10');
}

main();
```
