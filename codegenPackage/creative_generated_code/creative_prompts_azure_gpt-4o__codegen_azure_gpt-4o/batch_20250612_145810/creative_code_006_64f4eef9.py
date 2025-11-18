"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetdappsite.web.app
Prompt: Develop a JavaScript function to automate asset deposits from Ethereum to Starknet using the StarkGate bridge.
Generated: DETERMINISTIC_64f4eef918be6dce
Batch ID: 20250612_145810
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const ethers = require('ethers');
const starknet = require('starknet'); // Ensure the Starknet SDK is installed
const starkGateABI = require('./StarkGateABI.json'); // Import StarkGate contract's ABI

/**
 * Automates asset deposits from Ethereum to Starknet using the StarkGate bridge.
 *
 * @param {string} ethereumPrivateKey - The private key of the Ethereum account initiating the deposit.
 * @param {string} starkGateAddress - The Ethereum address of the StarkGate contract.
 * @param {string} recipientL2Address - The Starknet Layer 2 recipient address.
 * @param {string} assetAddress - The Ethereum address of the ERC20 token to deposit.
 * @param {string} amount - The amount of tokens to deposit (in wei).
 * @param {string} rpcUrl - The Ethereum RPC URL to connect to.
 * @returns {Promise<string>} - Transaction hash of the deposit if successful.
 */
async function depositToStarknet(ethereumPrivateKey, starkGateAddress, recipientL2Address, assetAddress, amount, rpcUrl) {
  try {
    // Validate input parameters
    if (!ethers.utils.isAddress(starkGateAddress)) {
      throw new Error('Invalid StarkGate address.');
    }
    if (!ethers.utils.isAddress(assetAddress)) {
      throw new Error('Invalid asset address.');
    }
    if (!recipientL2Address || !starknet.utils.isHexString(recipientL2Address)) {
      throw new Error('Invalid recipient Layer 2 address.');
    }
    if (!amount || isNaN(amount)) {
      throw new Error('Invalid amount.');
    }
    if (!rpcUrl || typeof rpcUrl !== 'string') {
      throw new Error('Invalid RPC URL.');
    }

    // Connect to Ethereum network using ethers.js
    const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
    const wallet = new ethers.Wallet(ethereumPrivateKey, provider);

    // Initialize StarkGate contract instance
    const starkGateContract = new ethers.Contract(starkGateAddress, starkGateABI, wallet);

    // Approve the StarkGate contract to spend the tokens
    const erc20Contract = new ethers.Contract(assetAddress, [
      'function approve(address spender, uint256 amount) public returns (bool)'
    ], wallet);

    console.log('Approving StarkGate to spend tokens...');
    const approveTx = await erc20Contract.approve(starkGateAddress, ethers.BigNumber.from(amount));
    await approveTx.wait(); // Wait for transaction confirmation
    console.log('Tokens approved successfully.');

    // Perform deposit to Starknet
    console.log('Depositing tokens to Starknet...');
    const depositTx = await starkGateContract.deposit(
      assetAddress, // ERC20 token address
      ethers.BigNumber.from(amount), // Amount to deposit
      recipientL2Address // Layer 2 recipient address
    );
    await depositTx.wait(); // Wait for transaction confirmation
    console.log('Tokens deposited successfully.');

    // Return the transaction hash
    return depositTx.hash;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error during deposit:', error);
    throw new Error(`Failed to deposit tokens: ${error.message}`);
  }
}

module.exports = depositToStarknet;
```
