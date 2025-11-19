"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiosis-finance.cc
Prompt: Provide an example of how to swap tokens between EVM and non-EVM networks using the Symbiosis platform.
Generated: DETERMINISTIC_2139647a3ced0251
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { Symbiosis } = require('@symbiosis/sdk'); // Symbiosis SDK for interactions
const ethers = require('ethers'); // Ethers.js for Ethereum functionality

// Define the main function to swap tokens
async function swapTokens() {
    // Configuration: Replace with your own values
    const fromNetwork = 'ethereum'; // EVM network (e.g., 'ethereum', 'polygon')
    const toNetwork = 'bsc'; // Non-EVM network (e.g., 'bsc', 'solana')
    const fromTokenAddress = '0xYourFromTokenAddress'; // Replace with the token address to swap from
    const toTokenAddress = '0xYourToTokenAddress'; // Replace with the token address to swap to
    const amountToSwap = ethers.utils.parseUnits('1.0', 18); // Amount to swap (adjust decimals accordingly)

    // Initialize Symbiosis
    const symbiosis = new Symbiosis();

    try {
        // Fetch the swap quote
        const quote = await symbiosis.getSwapQuote(fromNetwork, toNetwork, fromTokenAddress, toTokenAddress, amountToSwap);
        
        // Log the swap quote details
        console.log('Swap Quote:', quote);

        // Approve the token for transfer
        const signer = new ethers.Wallet('your-private-key', ethers.getDefaultProvider('mainnet')); // Replace with your private key and provider
        const tokenContract = new ethers.Contract(fromTokenAddress, ['function approve(address spender, uint amount)'], signer);
        const approvalTx = await tokenContract.approve(symbiosis.contractAddress, amountToSwap);
        await approvalTx.wait(); // Wait for the transaction to be mined

        console.log('Token approved:', approvalTx.hash);

        // Execute the swap
        const swapTx = await symbiosis.swap(fromNetwork, toNetwork, fromTokenAddress, toTokenAddress, amountToSwap, signer);
        const receipt = await swapTx.wait(); // Wait for the transaction to be mined

        console.log('Swap Transaction Receipt:', receipt);
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while swapping tokens:', error.message);
    }
}

// Run the swapTokens function
swapTokens();
```

Make sure to replace placeholder values like `'your-private-key'`, `'0xYourFromTokenAddress'`, and `'0xYourToTokenAddress'` with actual data before executing the code.
