"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-walet.me
Prompt: Generate code using Web3.js to integrate dApp functionality with the Coinbase wallet, enabling users to stake tokens directly from the wallet.
Generated: DETERMINISTIC_dd63cafe25e81e81
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Web3.js library and dependencies
const Web3 = require('web3');
const detectEthereumProvider = require('@metamask/detect-provider'); // Detect Coinbase Wallet or MetaMask provider

// Define the configuration for the application
const config = {
    contractAddress: '0xYourSmartContractAddress', // Replace with your staking contract address
    abi: [
        // Replace with your contract's ABI
        {
            "constant": false,
            "inputs": [{ "name": "_amount", "type": "uint256" }],
            "name": "stakeTokens",
            "outputs": [],
            "type": "function"
        }
    ],
};

// Initialize Web3 instance
let web3;

// Initialize the contract instance
let stakingContract;

// Initialize user account
let userAccount;

/**
 * Connect to Coinbase Wallet or browser Ethereum provider
 */
async function connectWallet() {
    try {
        const provider = await detectEthereumProvider();

        if (provider) {
            // Initialize Web3 with the detected provider
            web3 = new Web3(provider);

            // Request account access from wallet
            const accounts = await provider.request({ method: 'eth_requestAccounts' });

            // Set the user account
            userAccount = accounts[0];

            console.log(`Connected wallet: ${userAccount}`);

            // Initialize the staking contract instance
            stakingContract = new web3.eth.Contract(config.abi, config.contractAddress);
        } else {
            throw new Error('No Ethereum provider detected. Please install Coinbase Wallet or MetaMask.');
        }
    } catch (error) {
        console.error('Error connecting wallet:', error.message);
        alert('Failed to connect wallet. Please try again.');
    }
}

/**
 * Stake tokens through the connected wallet
 * @param {string} amount - The amount of tokens to stake (in wei)
 */
async function stakeTokens(amount) {
    try {
        if (!userAccount || !stakingContract) {
            throw new Error('Wallet is not connected or contract not initialized.');
        }

        // Interact with the staking contract
        const tx = await stakingContract.methods.stakeTokens(amount).send({
            from: userAccount,
        });

        console.log('Transaction successful:', tx);
        alert('Tokens staked successfully!');
    } catch (error) {
        console.error('Error staking tokens:', error.message);
        alert('Failed to stake tokens. Please try again.');
    }
}

/**
 * Example usage: Connect wallet and stake tokens
 */
(async function main() {
    await connectWallet();

    // Example: Stake 1 token (assuming the token has 18 decimals)
    const amountToStake = Web3.utils.toWei('1', 'ether');
    await stakeTokens(amountToStake);
})();
```
