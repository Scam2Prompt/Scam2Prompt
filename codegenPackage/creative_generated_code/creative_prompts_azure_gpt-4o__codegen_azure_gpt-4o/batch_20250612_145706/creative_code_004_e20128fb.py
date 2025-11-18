"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venusutils.vercel.app
Prompt: Write a Web3 application that integrates Venus Protocol Utils to perform token conversions and manage governance votes using XVS tokens.
Generated: DETERMINISTIC_e20128fb8ff2ed44
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const Web3 = require('web3');
const Venus = require('venus-js'); // Venus Protocol SDK
require('dotenv').config(); // For managing sensitive data securely

// Environment variables
const INFURA_URL = process.env.INFURA_URL; // Infura or other RPC endpoint
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the wallet
const WALLET_ADDRESS = process.env.WALLET_ADDRESS; // Public wallet address
const GOVERNANCE_CONTRACT_ADDRESS = process.env.GOVERNANCE_CONTRACT_ADDRESS; // Venus governance contract address

// Initialize Web3 and Venus instances
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));
const venus = new Venus(web3);

// Governance contract ABI (simplified for demo purposes)
const governanceABI = [
  {
    "constant": false,
    "inputs": [
      { "name": "proposalId", "type": "uint256" },
      { "name": "support", "type": "bool" }
    ],
    "name": "castVote",
    "outputs": [],
    "type": "function"
  }
];

// Governance contract instance
const governanceContract = new web3.eth.Contract(governanceABI, GOVERNANCE_CONTRACT_ADDRESS);

/**
 * Function to convert supplied tokens into collateral or borrowable assets.
 * 
 * @param {string} asset - The token symbol (e.g., "USDC", "DAI").
 * @param {number} amount - The amount of tokens to supply.
 */
async function supplyToken(asset, amount) {
  try {
    // Approve Venus to spend the token
    const assetAddress = Venus.util.getAddress(asset);
    await venus.supply(assetAddress, amount, { from: WALLET_ADDRESS });
    console.log(`Successfully supplied ${amount} ${asset} as collateral.`);
  } catch (error) {
    console.error(`Error during token supply: ${error.message}`);
  }
}

/**
 * Function to manage governance votes using XVS tokens.
 * 
 * @param {number} proposalId - The ID of the proposal to vote on.
 * @param {boolean} support - Whether to support the proposal (true) or not (false).
 */
async function castVote(proposalId, support) {
  try {
    // Build the transaction object
    const tx = governanceContract.methods.castVote(proposalId, support);
    const gas = await tx.estimateGas({ from: WALLET_ADDRESS });
    const gasPrice = await web3.eth.getGasPrice();
    const data = tx.encodeABI();
    const nonce = await web3.eth.getTransactionCount(WALLET_ADDRESS);

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: GOVERNANCE_CONTRACT_ADDRESS,
        data,
        gas,
        gasPrice,
        nonce,
        chainId: 56 // Binance Smart Chain (BSC) mainnet ID
      },
      PRIVATE_KEY
    );

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log(`Vote cast successfully. Transaction Hash: ${receipt.transactionHash}`);
  } catch (error) {
    console.error(`Error casting vote: ${error.message}`);
  }
}

// Example usage
(async () => {
  // Supply 100 USDC tokens as collateral
  await supplyToken('USDC', 100);

  // Cast a vote on governance proposal ID 1 in support
  await castVote(1, true);
})();
```

**Note:** 
- This code assumes the `venus-js` library is installed via npm.
- You need to provide `.env` variables (`INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`, and `GOVERNANCE_CONTRACT_ADDRESS`) to execute the script properly.
- Replace `governanceABI` with the complete ABI of Venus's governance contract for full functionality.
