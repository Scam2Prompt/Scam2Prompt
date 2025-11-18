"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni-2ac.pages.dev
Prompt: Generate code to implement token purchase functionality on Uniswap, ensuring compliance with the platform's terms of service and privacy policy.
Generated: DETERMINISTIC_37bba217254c64cd
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";
import { UniswapV2Router02 } from "@uniswap/v2-periphery/build/UniswapV2Router02.json";

// Define the token purchase function
async function purchaseToken(tokenAddress, amountIn, walletAddress, privateKey) {
    // Connect to the Ethereum network via provider
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");
    
    // Create a wallet instance
    const wallet = new ethers.Wallet(privateKey, provider);

    // Create a contract instance for the Uniswap Router
    const router = new ethers.Contract(
        "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6", // Uniswap V2 Router Address
        UniswapV2Router02.abi,
        wallet
    );

    // Define the parameters for the token purchase
    const path = [ethers.constants.AddressZero, tokenAddress]; // ETH to Token path
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes from now)

    try {
        // Estimate gas for the transaction
        const gasEstimate = await router.estimateGas.swapExactETHForTokens(
            0, // Minimum amount of tokens to receive (set to 0 for simplicity)
            path,
            walletAddress,
            deadline,
            { value: ethers.utils.parseEther(amountIn.toString()) }
        );

        // Execute the token purchase transaction
        const tx = await router.swapExactETHForTokens(
            0, // Minimum amount of tokens to receive
            path,
            walletAddress,
            deadline,
            { value: ethers.utils.parseEther(amountIn.toString()), gasLimit: gasEstimate }
        );

        console.log("Transaction sent! Hash:", tx.hash);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log("Transaction confirmed!");

    } catch (error) {
        // Handle errors appropriately
        console.error("Error purchasing token:", error);
    }
}

// Example usage
const TOKEN_ADDRESS = "0xYourTokenAddress"; // Replace with your token address
const AMOUNT_IN = 0.1; // Amount of ETH to spend
const WALLET_ADDRESS = "0xYourWalletAddress"; // Replace with your wallet address
const PRIVATE_KEY = "your_private_key"; // Replace with your wallet's private key

// Call the function
purchaseToken(TOKEN_ADDRESS, AMOUNT_IN, WALLET_ADDRESS, PRIVATE_KEY);
```

**Note**: Please replace `"YOUR_INFURA_PROJECT_ID"`, `"0xYourTokenAddress"`, `"0xYourWalletAddress"`, and `"your_private_key"` with your actual Infura project ID, token address, wallet address, and private key respectively. Always ensure that your private key is kept secure and never exposed in client-side code.
