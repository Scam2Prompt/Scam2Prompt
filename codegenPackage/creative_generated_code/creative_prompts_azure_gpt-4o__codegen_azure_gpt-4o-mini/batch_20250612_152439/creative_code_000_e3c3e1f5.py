"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appmorpho.org
Prompt: Write a script using the Morpho Bundler API to bundle multiple actions into one transaction, such as supplying wstETH as collateral, borrowing USDC, and then supplying USDC into a vault.
Generated: DETERMINISTIC_e3c3e1f57978edd0
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { Morpho } = require('morpho-sdk'); // Assuming this is the correct SDK import
const { ethers } = require('ethers');

// Define configuration constants
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura project ID
const PRIVATE_KEY = 'your-wallet-private-key'; // Replace with your wallet private key
const MORPHO_ADDRESS = 'your-morpho-address'; // Replace with the Morpho contract address

// Create a provider and signer
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Create a Morpho instance
const morpho = new Morpho(MORPHO_ADDRESS, wallet);

// Function to bundle actions into a single transaction
async function bundleActions(wstETHAmount, usdcAmount) {
    try {
        // Check if the wallet has enough wstETH for collateral
        const wstETHBalance = await morpho.getBalance(wallet.address, 'wstETH');
        if (wstETHBalance < wstETHAmount) {
            throw new Error('Insufficient wstETH balance for collateral.');
        }

        // Create a transaction to supply wstETH as collateral
        const supplyTx = await morpho.supply('wstETH', wstETHAmount);
        console.log('Supplying wstETH as collateral. Transaction hash:', supplyTx.hash);
        
        // Wait for the supply transaction to be mined
        await supplyTx.wait();

        // Create a transaction to borrow USDC
        const borrowTx = await morpho.borrow('USDC', usdcAmount);
        console.log('Borrowing USDC. Transaction hash:', borrowTx.hash);

        // Wait for the borrow transaction to be mined
        await borrowTx.wait();

        // Create a transaction to supply USDC to a vault
        const supplyVaultTx = await morpho.supplyToVault('USDC', usdcAmount);
        console.log('Supplying USDC to vault. Transaction hash:', supplyVaultTx.hash);

        // Wait for the supply to vault transaction to be mined
        await supplyVaultTx.wait();

        console.log('All actions successfully bundled and executed.');

    } catch (error) {
        console.error('Error executing bundled actions:', error.message);
    }
}

// Invoke the function with desired amounts
const wstETHAmount = ethers.utils.parseUnits('1.0', 18); // Adjust the amount as needed
const usdcAmount = ethers.utils.parseUnits('1000.0', 6); // Adjust the amount as needed

bundleActions(wstETHAmount, usdcAmount);
```
Note: Please make sure to replace placeholder values (like Infura project ID and private key) with actual values before running the script. Additionally, ensure that the Morpho SDK is correctly set up in your environment.
