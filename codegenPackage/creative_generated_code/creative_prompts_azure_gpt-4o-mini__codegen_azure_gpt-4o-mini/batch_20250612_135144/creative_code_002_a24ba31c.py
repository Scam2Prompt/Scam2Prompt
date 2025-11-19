"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloginns.creatorlink.net
Prompt: What are the steps to add cryptocurrencies to my MetaMask wallet, and how can I verify token details?
Generated: DETERMINISTIC_a24ba31c93280219
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary MetaMask libraries
const Web3 = require('web3'); // Web3.js library for interacting with Ethereum blockchain
const { ethers } = require('ethers'); // Ethers.js for advanced Ethereum interactions

// Function to add a custom token to a MetaMask wallet
async function addTokenToMetaMask(tokenAddress, tokenSymbol, tokenDecimals) {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    // Request the user to connect their wallet (if not already connected)
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Define the parameters for adding the token
    const params = {
        type: 'ERC20', // Token type
        options: {
            address: tokenAddress, // Token contract address
            symbol: tokenSymbol, // Token symbol (e.g., ETH, DAI)
            decimals: tokenDecimals, // Number of decimals
        },
    };

    // Attempt to add the token to MetaMask
    try {
        const wasAdded = await window.ethereum.request({
            method: 'wallet_watchAsset',
            params: params,
        });

        if (wasAdded) {
            console.log(`${tokenSymbol} has been added to your wallet!`);
        } else {
            console.log(`Failed to add ${tokenSymbol} to your wallet.`);
        }
    } catch (error) {
        console.error('Error adding token:', error);
    }
}

// Function to verify token details
async function verifyTokenDetails(tokenAddress) {
    // Create an instance of a Web3 provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Create an instance of the ERC20 token contract
    const tokenContract = new ethers.Contract(tokenAddress, [
        // ERC20 standard function signatures
        'function name() view returns (string)',
        'function symbol() view returns (string)',
        'function decimals() view returns (uint8)',
        'function totalSupply() view returns (uint256)',
    ], provider);

    try {
        // Fetch token details
        const name = await tokenContract.name();
        const symbol = await tokenContract.symbol();
        const decimals = await tokenContract.decimals();
        const totalSupply = await tokenContract.totalSupply();

        console.log(`Token Name: ${name}`);
        console.log(`Token Symbol: ${symbol}`);
        console.log(`Token Decimals: ${decimals}`);
        console.log(`Total Supply: ${totalSupply.toString()}`);
    } catch (error) {
        console.error('Error retrieving token details:', error);
    }
}

// Example usage:
// addTokenToMetaMask('0xYourTokenAddress', 'TOKEN_SYMBOL', 18);
// verifyTokenDetails('0xYourTokenAddress');
```
