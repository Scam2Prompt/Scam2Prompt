"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-etuktuk.pages.dev
Prompt: Provide an example of how to implement a transaction for buying $TUK tokens on Uniswap.
Generated: DETERMINISTIC_4b420a044dabee59
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from ethers.js and Uniswap SDK
const { ethers } = require("ethers");
const { Token, TokenAmount, Pair, Trade, Route, TradeType, Percent } = require('@uniswap/sdk');

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const PRIVATE_KEY = 'YOUR_WALLET_PRIVATE_KEY'; // Replace with your wallet private key
const TUK_TOKEN_ADDRESS = 'TUK_TOKEN_CONTRACT_ADDRESS'; // Replace with the TUK token address
const ETH_TOKEN_ADDRESS = 'ETH_TOKEN_CONTRACT_ADDRESS'; // Typically the address of WETH
const AMOUNT_TO_BUY = ethers.utils.parseUnits('1.0', 18); // Amount of TUK tokens to buy

// Set up provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to buy TUK tokens
async function buyTukTokens() {
    try {
        // Create a token instance for TUK
        const tukToken = new Token(1, TUK_TOKEN_ADDRESS, 18); // 1 for Ethereum mainnet

        // Fetch the pair for ETH/TUK
        const pair = await Pair.fetchData(tukToken, new Token(1, ETH_TOKEN_ADDRESS, 18));

        // Create a route for the trade
        const route = new Route([pair], new TokenAmount(new Token(1, ETH_TOKEN_ADDRESS, 18), AMOUNT_TO_BUY));

        // Create a trade
        const trade = new Trade(route, new TokenAmount(tukToken, AMOUNT_TO_BUY), TradeType.EXACT_OUTPUT);

        // Calculate slippage
        const slippageTolerance = new Percent('50', '10000'); // 0.5%
        
        // Get the amount out and deadline
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw; // Minimum amount of TUK tokens
        const path = [ETH_TOKEN_ADDRESS, TUK_TOKEN_ADDRESS];
        const to = wallet.address; // The address to send TUK tokens to
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

        // Prepare transaction
        const tx = {
            to: 'UNISWAP_ROUTER_CONTRACT_ADDRESS', // Replace with the Uniswap Router contract address
            value: ethers.utils.parseEther('1.0'), // Amount of ETH to send
            data: /* encode the swap method call here */, // Encode the data for the swap transaction
            gasLimit: ethers.utils.hexlify(1000000), // Set gas limit (adjust as needed)
            gasPrice: ethers.utils.parseUnits('50', 'gwei') // Set gas price (adjust as needed)
        };

        // Send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        console.log(`Transaction hash: ${transactionResponse.hash}`);

        // Wait for the transaction to be confirmed
        const receipt = await transactionResponse.wait();
        console.log(`Transaction was confirmed in block: ${receipt.blockNumber}`);
    } catch (error) {
        console.error("An error occurred while trying to buy TUK tokens:", error);
    }
}

// Execute the function
buyTukTokens();
```

**Note:** 
- Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_PRIVATE_KEY`, `TUK_TOKEN_CONTRACT_ADDRESS`, `ETH_TOKEN_CONTRACT_ADDRESS`, and `UNISWAP_ROUTER_CONTRACT_ADDRESS` with actual values.
- You will need to encode the swap method call properly in the `data` field of the transaction object, which typically involves using the Uniswap Router's contract ABI.
- Make sure you have the required packages installed (`ethers`, `@uniswap/sdk`).
