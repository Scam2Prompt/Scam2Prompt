"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axondao.gitbook.io
Prompt: Develop a JavaScript script using Web3.js to bridge AXGT tokens between Ethereum and BASE, following the bridging process described by AxonDAO.
Generated: DETERMINISTIC_223c6ac5086aec4c
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to bridge AXGT tokens between Ethereum and BASE using Web3.js and AxonDAO's bridging process.
 * Ensure you have Web3.js installed (`npm install web3`) and the appropriate AxonDAO API endpoints.
 * Update environment variables and contract addresses accordingly.
 */

// Import Web3.js
const Web3 = require('web3');
require('dotenv').config(); // For loading environment variables

// Environment Variables
const ETHEREUM_RPC_URL = process.env.ETHEREUM_RPC_URL; // Ethereum RPC URL
const BASE_RPC_URL = process.env.BASE_RPC_URL; // BASE RPC URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key for signing transactions
const AXGT_TOKEN_ADDRESS_ETH = process.env.AXGT_TOKEN_ADDRESS_ETH; // AXGT token contract on Ethereum
const AXGT_TOKEN_ADDRESS_BASE = process.env.AXGT_TOKEN_ADDRESS_BASE; // AXGT token contract on BASE
const BRIDGE_CONTRACT_ADDRESS = process.env.BRIDGE_CONTRACT_ADDRESS; // AxonDAO Bridge contract address

// Initialize Web3 instances
const ethereumWeb3 = new Web3(new Web3.providers.HttpProvider(ETHEREUM_RPC_URL));
const baseWeb3 = new Web3(new Web3.providers.HttpProvider(BASE_RPC_URL));

// Load account from private key
const account = ethereumWeb3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
ethereumWeb3.eth.accounts.wallet.add(account);
baseWeb3.eth.accounts.wallet.add(account);

/**
 * Function to bridge AXGT tokens from Ethereum to BASE.
 * @param {string} recipient - Address on BASE where tokens will be sent.
 * @param {number} amount - Number of AXGT tokens to bridge.
 */
async function bridgeTokensToBase(recipient, amount) {
  try {
    // ABI definitions for AXGT and Bridge contracts (Update with actual ABI)
    const AXGT_ABI = [
      // ERC20 ABI simplified for balanceOf and approve methods
      { "constant": true, "inputs": [{ "name": "_owner", "type": "address" }], "name": "balanceOf", "outputs": [{ "name": "balance", "type": "uint256" }], "type": "function" },
      { "constant": false, "inputs": [{ "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" }], "name": "approve", "outputs": [{ "name": "success", "type": "bool" }], "type": "function" }
    ];

    const BRIDGE_ABI = [
      { "constant": false, "inputs": [{ "name": "_recipient", "type": "address" }, { "name": "_amount", "type": "uint256" }], "name": "bridgeTokens", "outputs": [], "type": "function" }
    ];

    // Create contract instances
    const axgtContractEth = new ethereumWeb3.eth.Contract(AXGT_ABI, AXGT_TOKEN_ADDRESS_ETH);
    const bridgeContract = new ethereumWeb3.eth.Contract(BRIDGE_ABI, BRIDGE_CONTRACT_ADDRESS);

    // Check balance
    const balance = await axgtContractEth.methods.balanceOf(account.address).call();
    if (balance < amount) {
      throw new Error('Insufficient AXGT token balance.');
    }

    // Approve Bridge contract to transfer tokens
    const approveTx = axgtContractEth.methods.approve(BRIDGE_CONTRACT_ADDRESS, amount);
    const approveReceipt = await ethereumWeb3.eth.sendTransaction({
      from: account.address,
      to: AXGT_TOKEN_ADDRESS_ETH,
      data: approveTx.encodeABI(),
      gas: await approveTx.estimateGas({ from: account.address }),
    });
    console.log('Approve transaction successful:', approveReceipt.transactionHash);

    // Bridge tokens
    const bridgeTx = bridgeContract.methods.bridgeTokens(recipient, amount);
    const bridgeReceipt = await ethereumWeb3.eth.sendTransaction({
      from: account.address,
      to: BRIDGE_CONTRACT_ADDRESS,
      data: bridgeTx.encodeABI(),
      gas: await bridgeTx.estimateGas({ from: account.address }),
    });
    console.log('Bridge transaction successful:', bridgeReceipt.transactionHash);

  } catch (error) {
    console.error('Error bridging tokens:', error.message);
  }
}

/**
 * Example usage of the bridgeTokensToBase function.
 */
(async () => {
  const recipientOnBase = '0xRecipientAddressOnBASE'; // Replace with recipient's BASE address
  const amountToBridge = 100; // Replace with the amount of AXGT tokens to bridge

  await bridgeTokensToBase(recipientOnBase, amountToBridge);
})();
```

This code assumes you have the correct ABIs, RPC URLs, contract addresses, and account setup. Replace placeholder values with your own production values. Make sure to install dependencies (`npm install web3 dotenv`) before running.
