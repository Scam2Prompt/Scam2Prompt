"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Generate a sample transaction using Uniswap to swap ETH for NPC tokens, considering the transaction deadline and slippage settings.
Generated: DETERMINISTIC_d0ade86985cf5a09
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { ethers } = require("ethers");
const { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Fetcher, Percent } = require("@uniswap/sdk");

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const NATIVE_TOKEN = ethers.constants.AddressZero; // Represents ETH in the Ethereum network
const NPC_TOKEN_ADDRESS = "0xYourNPCAddress"; // Replace with the actual NPC token contract address
const SLIPPAGE_PERCENTAGE = new Percent("50", "10000"); // 0.5% slippage tolerance
const DEADLINE_SECONDS = 300; // 5 minutes in seconds

// Function to create a transaction to swap ETH for NPC tokens
async function swapEthForNpc() {
    try {
        // Connect to the Ethereum network using Infura
        const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
        const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

        // Fetch the NPC token details
        const npcToken = await Fetcher.fetchTokenData(ChainId.MAINNET, NPC_TOKEN_ADDRESS);
        
        // Fetch the pair data for ETH and NPC token
        const pair = await Fetcher.fetchPairData(Token.wrappedEth, npcToken);
        
        // Create a route for swapping ETH to NPC tokens
        const route = new Route([pair], Token.wrappedEth);
        
        // Define the amount of ETH to swap (0.1 ETH here)
        const amountIn = ethers.utils.parseEther("0.1"); // Amount of ETH to swap
        
        // Create a trade instance
        const trade = new Trade(route, new TokenAmount(Token.wrappedEth, amountIn.toString()), TradeType.EXACT_INPUT);
        
        // Calculate the minimum amount of NPC tokens to receive based on slippage
        const slippageAdjustedAmountOut = trade.minimumAmountOut(SLIPPAGE_PERCENTAGE).toFixed();
        
        // Build the transaction parameters
        const transaction = {
            to: pair.liquidityToken.address,
            value: amountIn,
            data: pair.getContract().interface.encodeFunctionData("swapExactETHForTokens", [
                slippageAdjustedAmountOut,
                [Token.wrappedEth.address, npcToken.address],
                wallet.address,
                Math.floor(Date.now() / 1000) + DEADLINE_SECONDS
            ]),
            gasLimit: ethers.utils.hexlify(100000), // Set gas limit
        };

        // Send the transaction
        const txResponse = await wallet.sendTransaction(transaction);
        console.log(`Transaction sent! Hash: ${txResponse.hash}`);
        
        // Wait for the transaction to be mined
        await txResponse.wait();
        console.log('Transaction confirmed!');

    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Execute the swap function
swapEthForNpc();
```

Make sure to replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual Infura project ID and wallet private key, and update the `NPC_TOKEN_ADDRESS` with the correct contract address for the NPC token.
