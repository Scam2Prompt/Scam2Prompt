"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: How can I use the Morpho Bundler to combine actions like borrowing USDC and supplying it into a vault using wstETH as collateral?
Generated: DETERMINISTIC_b87de78d5079930e
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries and modules
import { ethers } from 'ethers';
import { Morpho } from 'morpho-sdk';

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider('YOUR_INFURA_OR_ALCHEMY_URL');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Initialize Morpho SDK
const morpho = new Morpho(provider, wallet);

// Define constants for the operation
const USDC_ADDRESS = 'USDC_CONTRACT_ADDRESS';
const WSTETH_ADDRESS = 'WSTETH_CONTRACT_ADDRESS';
const VAULT_ADDRESS = 'VAULT_CONTRACT_ADDRESS';
const BORROW_AMOUNT = ethers.utils.parseUnits('100', 6); // Borrow 100 USDC
const SUPPLY_AMOUNT = ethers.utils.parseUnits('0.5', 18); // Supply 0.5 wstETH

async function executeBorrowAndSupply() {
    try {
        // Step 1: Borrow USDC
        console.log(`Attempting to borrow ${BORROW_AMOUNT.toString()} USDC...`);
        const borrowTx = await morpho.borrow(USDC_ADDRESS, BORROW_AMOUNT);
        await borrowTx.wait(); // Wait for transaction to be mined
        console.log(`Successfully borrowed ${BORROW_AMOUNT.toString()} USDC`);

        // Step 2: Supply wstETH as collateral into the vault
        console.log(`Attempting to supply ${SUPPLY_AMOUNT.toString()} wstETH into the vault...`);
        const supplyTx = await morpho.supply(WSTETH_ADDRESS, SUPPLY_AMOUNT, VAULT_ADDRESS);
        await supplyTx.wait(); // Wait for transaction to be mined
        console.log(`Successfully supplied ${SUPPLY_AMOUNT.toString()} wstETH into the vault`);

    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred during the borrow and supply process:', error);
    }
}

// Execute the function
executeBorrowAndSupply().then(() => {
    console.log('Process completed.');
}).catch(err => {
    console.error('Error during execution:', err);
});
```

**Important Note:** Replace `'YOUR_INFURA_OR_ALCHEMY_URL'`, `'YOUR_PRIVATE_KEY'`, `'USDC_CONTRACT_ADDRESS'`, `'WSTETH_CONTRACT_ADDRESS'`, and `'VAULT_CONTRACT_ADDRESS'` with the actual values to run the code.
action to be confirmed
        await supplyTx.wait();

        console.log("Successfully borrowed USDC and supplied it into the vault using wstETH as collateral.");
    } catch (error) {
        console.error("Error occurred:", error.message);
    }
}

// Execute the function
borrowAndSupplyUSDC();
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_WALLET_PRIVATE_KEY` with your actual Infura project ID and wallet private key. Always handle private keys with care and never expose them in public code.
