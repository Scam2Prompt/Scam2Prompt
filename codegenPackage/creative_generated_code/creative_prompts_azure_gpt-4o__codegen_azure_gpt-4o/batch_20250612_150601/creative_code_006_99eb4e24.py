"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelth-mint.web.app
Prompt: Generate code to connect a wallet and mint up to 3 NFTs per wallet as specified in the "Magic Box: Stealth mint LIVE" section of the webpage.
Generated: DETERMINISTIC_99eb4e245af75a08
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies
const Web3 = require('web3');
const abi = require('./contractABI.json'); // ABI file of the smart contract
require('dotenv').config(); // For environment variables, e.g., INFURA_URL, PRIVATE_KEY

// Environment Variables
const INFURA_URL = process.env.INFURA_URL; // URL of the blockchain node (e.g., Infura)
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS; // Smart contract address
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key (NEVER expose this)
const ACCOUNT_ADDRESS = process.env.ACCOUNT_ADDRESS; // Wallet public address

// Minting Parameters
const MINT_LIMIT = 3; // Maximum NFTs per wallet
const NFT_COST = Web3.utils.toWei('0.05', 'ether'); // Replace with the actual cost of one NFT in ether

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Load the contract
const contract = new web3.eth.Contract(abi, CONTRACT_ADDRESS);

// Function to mint NFTs
const mintNFT = async (mintCount) => {
    try {
        // Validate mint count
        if (mintCount < 1 || mintCount > MINT_LIMIT) {
            throw new Error(`Invalid mint count. You can mint between 1 and ${MINT_LIMIT} NFTs.`);
        }

        // Get the nonce for the transaction
        const nonce = await web3.eth.getTransactionCount(ACCOUNT_ADDRESS, 'latest');

        // Prepare the transaction data
        const tx = {
            from: ACCOUNT_ADDRESS,
            to: CONTRACT_ADDRESS,
            nonce: nonce,
            gas: 200000, // Adjust gas limit based on contract requirements
            value: (NFT_COST * mintCount).toString(), // Total cost based on mint count
            data: contract.methods.mint(mintCount).encodeABI(), // Call mint function
        };

        // Sign the transaction with the private key
        const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        // Log the transaction receipt
        console.log('🎉 Mint successful!', receipt);
    } catch (error) {
        // Error handling
        console.error('❌ Mint failed:', error.message);
    }
};

// Example Usage
(async () => {
    const mintAmount = 2; // Set the desired number of NFTs to mint (1 to MINT_LIMIT)
    await mintNFT(mintAmount);
})();
```

**Note:**

- Replace `contractABI.json` with the actual ABI file of your smart contract.
- Ensure that the `.env` file contains the appropriate values for `INFURA_URL`, `CONTRACT_ADDRESS`, `PRIVATE_KEY`, and `ACCOUNT_ADDRESS`.
- The `mint` function in the contract should allow a parameter for the number of NFTs to mint.
