"""
Generated Code Metadata:
========================
Original URL: https://wwwmorpho.org
Prompt: Write a script using the Morpho Bundler to bundle multiple actions into one transaction, such as using `wstETH` as collateral to borrow `USDC` and then supplying `USDC` into a vault.
Generated: DETERMINISTIC_190e0f433786a5f2
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and modules
const { ethers } = require("ethers");
const { Morpho } = require("@morpho.xyz/morpho-sdk");

// Define constants for the Ethereum network and contract addresses
const NETWORK = "mainnet"; // Change to "goerli" for testnet
const WSTETH_ADDRESS = "0x..."; // Replace with actual wstETH contract address
const USDC_ADDRESS = "0x..."; // Replace with actual USDC contract address
const VAULT_ADDRESS = "0x..."; // Replace with actual vault contract address

// Initialize the Morpho SDK
const morpho = new Morpho(NETWORK);

// Define the main function to execute the transaction
async function executeTransaction() {
    try {
        // Connect to the Ethereum provider
        const provider = new ethers.providers.InfuraProvider(NETWORK, "YOUR_INFURA_PROJECT_ID");
        const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

        // Create a Morpho instance with the wallet
        const morphoWithWallet = morpho.connect(wallet);

        // Step 1: Use wstETH as collateral to borrow USDC
        const borrowAmount = ethers.utils.parseUnits("1000", 6); // Amount of USDC to borrow
        const collateralAmount = ethers.utils.parseUnits("1", 18); // Amount of wstETH to use as collateral

        // Borrow USDC using wstETH as collateral
        const borrowTx = await morphoWithWallet.borrow(USDC_ADDRESS, borrowAmount, {
            collateral: WSTETH_ADDRESS,
            collateralAmount: collateralAmount,
        });
        await borrowTx.wait(); // Wait for the transaction to be mined
        console.log(`Borrowed ${ethers.utils.formatUnits(borrowAmount, 6)} USDC using wstETH as collateral.`);

        // Step 2: Supply the borrowed USDC into the vault
        const supplyTx = await morphoWithWallet.supply(USDC_ADDRESS, borrowAmount, VAULT_ADDRESS);
        await supplyTx.wait(); // Wait for the transaction to be mined
        console.log(`Supplied ${ethers.utils.formatUnits(borrowAmount, 6)} USDC into the vault.`);

    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred during the transaction:", error);
    }
}

// Execute the transaction
executeTransaction();
```
