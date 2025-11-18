"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-compound.com
Prompt: Write code to implement a token swap feature using MetaMask's API, ensuring secure exchange of Ethereum and USD Coin.
Generated: DETERMINISTIC_0ab4a9067d59a82e
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';
import { TokenSwap } from 'path-to-your-token-swap-library'; // Assume a library for token swaps

// Setting up constants
const ETHEREUM_NETWORK = 'mainnet'; // Ethereum main network
const TOKEN_SWAP_CONTRACT_ADDRESS = 'your_token_swap_contract_address'; // Replace with your contract address
const USD_COIN_ADDRESS = 'your_usd_coin_address'; // Replace with the actual USDC contract address

// Initialize Web3 and check for MetaMask
if (typeof window.ethereum !== 'undefined') {
    const web3 = new Web3(window.ethereum);
    
    // Function to request account access
    async function requestAccountAccess() {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Account access granted');
        } catch (error) {
            console.error('User denied account access:', error);
            throw new Error('Unable to access account. Please grant permission to continue.');
        }
    }

    // Function to swap tokens
    async function swapTokens(amount, tokenFrom, tokenTo) {
        try {
            // Ensure the user is connected
            await requestAccountAccess();

            // Get the user's accounts
            const accounts = await web3.eth.getAccounts();
            const userAccount = accounts[0];
            console.log(`User account: ${userAccount}`);

            // Create an instance of the TokenSwap contract
            const tokenSwap = new TokenSwap(web3, TOKEN_SWAP_CONTRACT_ADDRESS);

            // Execute the token swap
            const result = await tokenSwap.swapTokens(userAccount, amount, tokenFrom, tokenTo);
            console.log('Token swap successful:', result);
        } catch (error) {
            console.error('Error in token swap:', error);
            throw new Error('Token swap failed. Please check the console for details.');
        }
    }

    // Example usage
    const amountToSwap = web3.utils.toWei('1', 'ether'); // Swap 1 ETH
    const tokenFrom = 'ETH'; // From Ethereum
    const tokenTo = USD_COIN_ADDRESS; // To USDC

    // Call the swap function
    swapTokens(amountToSwap, tokenFrom, tokenTo);
} else {
    console.error('MetaMask is not installed. Please install it to use this feature.');
}
```

**Note:** Make sure to replace placeholder strings like `'path-to-your-token-swap-library'`, `'your_token_swap_contract_address'`, and `'your_usd_coin_address'` with the actual values applicable to your implementation. This implementation assumes that you have a `TokenSwap` class defined in your project that handles the details of the token swap on the blockchain.
