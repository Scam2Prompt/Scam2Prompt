"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omrpho.org
Prompt: How can I use the Morpho Bundler to combine actions like borrowing USDC and supplying it into a vault using wstETH collateral?
Generated: DETERMINISTIC_c0fce5c5c811f4b5
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers');
const { Morpho } = require('@morpho-org/morpho-sdk');

async function main() {
    // Initialize provider and wallet
    const provider = new ethers.providers.JsonRpcProvider('YOUR_INFURA_URL_OR_ALCHEMY_URL');
    const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

    // Initialize Morpho SDK
    const morpho = new Morpho(wallet);

    // Define constants for the transaction
    const usdcAmountToBorrow = ethers.utils.parseUnits('1000', 6); // Amount to borrow in USDC
    const wstETHAmountToSupply = ethers.utils.parseUnits('0.5', 18); // Amount of wstETH to supply

    try {
        // Borrow USDC
        const borrowTx = await morpho.borrow('USDC', usdcAmountToBorrow);
        console.log('Borrow transaction sent:', borrowTx.hash);
        
        // Wait for the transaction to be mined
        await borrowTx.wait();
        console.log('Borrow transaction confirmed.');

        // Supply wstETH to the vault
        const supplyTx = await morpho.supply('wstETH', wstETHAmountToSupply);
        console.log('Supply transaction sent:', supplyTx.hash);
        
        // Wait for the transaction to be mined
        await supplyTx.wait();
        console.log('Supply transaction confirmed.');

    } catch (error) {
        // Handle errors during borrowing or supplying
        console.error('An error occurred:', error);
    }
}

// Execute the main function
main().catch((error) => {
    console.error('An unexpected error occurred:', error);
});
```
