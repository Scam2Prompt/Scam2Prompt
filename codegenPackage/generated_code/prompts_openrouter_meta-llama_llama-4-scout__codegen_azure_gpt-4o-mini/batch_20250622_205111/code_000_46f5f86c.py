"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoulkqm54mkpjy5t7idjlc2wxddyj7a4cpdrpi4reejwkd4gphke.ipfs.dweb.link
Prompt: Write a step-by-step guide on how to buy $Gou tokens using Uniswap and MetaMask.
Generated: DETERMINISTIC_46f5f86cc412c5f8
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Fetcher } = require("@uniswap/sdk");

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const WALLET_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"; // Replace with your wallet's private key
const GOU_TOKEN_ADDRESS = "GOU_TOKEN_CONTRACT_ADDRESS"; // Replace with the GOU token contract address
const WETH_ADDRESS = "WETH_TOKEN_CONTRACT_ADDRESS"; // Replace with the WETH token contract address
const AMOUNT_TO_BUY = ethers.utils.parseUnits("1.0", 18); // Amount of GOU tokens to buy (adjust decimals as needed)

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

// Function to buy GOU tokens
async function buyGouTokens() {
    try {
        // Fetch the GOU token and WETH
        const gouToken = await Fetcher.fetchTokenData(ChainId.MAINNET, GOU_TOKEN_ADDRESS);
        const wethToken = await Fetcher.fetchTokenData(ChainId.MAINNET, WETH_ADDRESS);

        // Fetch the pair data
        const pair = await Fetcher.fetchPairData(gouToken, wethToken);
        
        // Create a route for the trade
        const route = new Route([pair], wethToken);
        
        // Create a trade object
        const trade = new Trade(route, new TokenAmount(wethToken, AMOUNT_TO_BUY), TradeType.EXACT_INPUT);
        
        // Get the slippage tolerance
        const slippageTolerance = new ethers.BigNumber.from("50"); // 0.5% slippage

        // Calculate the amount out and the minimum amount out
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw; // Minimum amount of GOU tokens to receive
        const path = [wethToken.address, gouToken.address]; // Path for the swap
        const to = wallet.address; // Address to send the tokens to
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes from now)

        // Create the transaction
        const tx = {
            to: pair.liquidityToken.address, // Uniswap router address
            value: ethers.utils.parseEther("0.1"), // Amount of WETH to swap (adjust as needed)
            data: router.interface.encodeFunctionData("swapExactTokensForTokens", [
                ethers.utils.parseEther("0.1"), // Amount of WETH to swap
                amountOutMin.toString(), // Minimum amount of GOU tokens to receive
                path, // Path for the swap
                to, // Recipient address
                deadline // Deadline for the transaction
            ]),
            gasLimit: ethers.utils.hexlify(100000), // Set a gas limit
            gasPrice: await provider.getGasPrice() // Get current gas price
        };

        // Sign and send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        console.log(`Transaction sent: ${transactionResponse.hash}`);

        // Wait for the transaction to be confirmed
        await transactionResponse.wait();
        console.log("Transaction confirmed!");

    } catch (error) {
        console.error("Error buying GOU tokens:", error);
    }
}

// Execute the function to buy GOU tokens
buyGouTokens();
```

**Note:** Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_PRIVATE_KEY`, `GOU_TOKEN_CONTRACT_ADDRESS`, and `WETH_TOKEN_CONTRACT_ADDRESS` with actual values before running the code. Ensure that you have the necessary permissions and that you are aware of the risks involved in trading cryptocurrencies.
