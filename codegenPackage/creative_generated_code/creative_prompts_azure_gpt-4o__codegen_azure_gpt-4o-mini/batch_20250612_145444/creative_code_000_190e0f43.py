"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: Write a script using the Morpho Bundler to bundle multiple actions into one transaction, such as using `wstETH` as collateral to borrow `USDC` and then supplying `USDC` into a vault.
Generated: DETERMINISTIC_190e0f433786a5f2
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Morpho and ethers libraries
const { Morpho } = require('@morpho.xyz/morpho-sdk');
const { ethers } = require('ethers');

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Initialize the Morpho instance
const morpho = new Morpho(provider, wallet);

// Define the main function to execute the transaction
async function bundleActions() {
    try {
        // Check if the wallet has sufficient wstETH balance
        const wstETHAddress = '0x...'; // Replace with actual wstETH contract address
        const usdcAddress = '0x...'; // Replace with actual USDC contract address
        const vaultAddress = '0x...'; // Replace with actual vault contract address
        const amountToBorrow = ethers.utils.parseUnits('100', 6); // Amount of USDC to borrow
        const collateralAmount = ethers.utils.parseUnits('1', 18); // Amount of wstETH to use as collateral
        
        const balance = await morpho.getBalance(wallet.address, wstETHAddress);
        if (balance.lt(collateralAmount)) {
            throw new Error('Insufficient wstETH balance for collateral');
        }

        // Step 1: Use wstETH as collateral to borrow USDC
        const borrowTx = await morpho.borrowUSDC(collateralAmount, amountToBorrow, wstETHAddress);
        console.log('Borrow transaction hash:', borrowTx.hash);
        await borrowTx.wait(); // Wait for transaction to be mined

        // Step 2: Supply the borrowed USDC into the vault
        const supplyTx = await morpho.supplyUSDC(amountToBorrow, vaultAddress);
        console.log('Supply transaction hash:', supplyTx.hash);
        await supplyTx.wait(); // Wait for transaction to be mined

        console.log('Successfully borrowed and supplied USDC into the vault.');
    } catch (error) {
        // Handle errors and log them
        console.error('An error occurred during the transaction:', error.message);
    }
}

// Execute the main function
bundleActions();
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `0x...` addresses with actual values before running the script. Ensure you have the `@morpho.xyz/morpho-sdk` and `ethers` libraries installed in your project.
