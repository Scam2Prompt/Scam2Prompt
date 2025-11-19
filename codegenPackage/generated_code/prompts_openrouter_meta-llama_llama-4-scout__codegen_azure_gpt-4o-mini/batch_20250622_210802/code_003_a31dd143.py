"""
Generated Code Metadata:
========================
Original URL: https://claims-magamemecoin.pages.dev
Prompt: Generate a step-by-step guide on how to buy MAGA Memecoin using $ETH and MetaMask, including swapping ETH for MAGA on Uniswap.
Generated: DETERMINISTIC_a31dd14384e61a13
Batch ID: 20250622_210802
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
const { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Fetcher, WETH } = require("@uniswap/sdk");
const { abi: ERC20_ABI } = require("@openzeppelin/contracts/build/contracts/ERC20.json");

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const WALLET_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"; // Replace with your wallet private key
const MAGA_TOKEN_ADDRESS = "0xYourMagaTokenAddress"; // Replace with the MAGA Memecoin contract address
const ETH_AMOUNT = ethers.utils.parseEther("0.1"); // Amount of ETH to swap

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

// Function to swap ETH for MAGA Memecoin
async function swapETHForMAGA() {
    try {
        // Fetch the MAGA token details
        const magaToken = await Fetcher.fetchTokenData(ChainId.MAINNET, MAGA_TOKEN_ADDRESS);
        
        // Fetch the pair data for ETH and MAGA
        const pair = await Fetcher.fetchPairData(WETH[ChainId.MAINNET], magaToken);
        
        // Create a route for the trade
        const route = new Route([pair], WETH[ChainId.MAINNET]);
        
        // Create a trade object
        const trade = new Trade(route, new TokenAmount(WETH[ChainId.MAINNET], ETH_AMOUNT.toString()), TradeType.EXACT_INPUT);
        
        // Get the slippage tolerance
        const slippageTolerance = new ethers.BigNumber.from("50"); // 0.5% slippage
        
        // Calculate the minimum amount of MAGA to receive
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw; // Amount of MAGA to receive
        const path = [WETH[ChainId.MAINNET].address, MAGA_TOKEN_ADDRESS];
        const to = wallet.address; // Address to receive MAGA
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now
        
        // Create the transaction
        const tx = {
            to: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6", // Uniswap Router address
            value: ETH_AMOUNT,
            data: ethers.utils.defaultAbiCoder.encode(["address[]", "uint256", "uint256", "address", "uint256"], [path, amountOutMin.toString(), deadline, to, 0]),
            gasLimit: ethers.utils.hexlify(100000), // Set a gas limit
            gasPrice: await provider.getGasPrice() // Get current gas price
        };

        // Send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        console.log(`Transaction sent: ${transactionResponse.hash}`);

        // Wait for the transaction to be mined
        await transactionResponse.wait();
        console.log("Transaction confirmed!");
    } catch (error) {
        console.error("Error swapping ETH for MAGA:", error);
    }
}

// Execute the swap function
swapETHForMAGA();
```

**Note:** Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_PRIVATE_KEY`, and `0xYourMagaTokenAddress` with actual values before running the code. Ensure you have sufficient ETH in your wallet to cover the transaction fees.
