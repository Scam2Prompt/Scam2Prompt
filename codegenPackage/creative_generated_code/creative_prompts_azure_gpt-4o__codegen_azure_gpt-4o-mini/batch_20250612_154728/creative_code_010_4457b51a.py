"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Write JavaScript code to interact with zkSwap Finance's zkBridge for transferring assets between zkSync Era and another blockchain network.
Generated: DETERMINISTIC_4457b51ad5096a23
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import { zkBridge } from 'zksync-bridge-sdk'; // Hypothetical SDK for zkSwap Finance
import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

/**
 * Class to handle asset transfers between zkSync Era and another blockchain network.
 */
class ZkBridgeTransfer {
    constructor() {
        this.provider = new ethers.providers.JsonRpcProvider(process.env.ZKSYNC_RPC_URL);
        this.wallet = new ethers.Wallet(process.env.PRIVATE_KEY, this.provider);
        this.bridge = new zkBridge(this.wallet);
    }

    /**
     * Transfer assets from zkSync Era to another blockchain.
     * @param {string} assetAddress - The address of the asset to transfer.
     * @param {string} recipient - The recipient address on the destination blockchain.
     * @param {number} amount - The amount of the asset to transfer.
     */
    async transferAssets(assetAddress, recipient, amount) {
        try {
            // Validate inputs
            if (!ethers.utils.isAddress(assetAddress)) {
                throw new Error('Invalid asset address');
            }
            if (!ethers.utils.isAddress(recipient)) {
                throw new Error('Invalid recipient address');
            }
            if (amount <= 0) {
                throw new Error('Amount must be greater than zero');
            }

            // Check the balance of the asset
            const balance = await this.getBalance(assetAddress);
            if (balance < amount) {
                throw new Error('Insufficient balance');
            }

            // Initiate transfer
            const tx = await this.bridge.transfer({
                assetAddress,
                to: recipient,
                amount: ethers.utils.parseUnits(amount.toString(), await this.getDecimals(assetAddress)),
            });

            console.log(`Transfer initiated: ${tx.hash}`);

            // Wait for transaction to be mined
            await tx.wait();
            console.log('Transfer completed successfully');

        } catch (error) {
            console.error('Error during transfer:', error.message);
        }
    }

    /**
     * Retrieve the balance of a specific asset for the wallet.
     * @param {string} assetAddress - The address of the asset.
     * @returns {Promise<number>} - The balance of the asset.
     */
    async getBalance(assetAddress) {
        const contract = new ethers.Contract(assetAddress, ['function balanceOf(address) view returns (uint256)'], this.provider);
        const balance = await contract.balanceOf(this.wallet.address);
        return ethers.utils.formatUnits(balance, await this.getDecimals(assetAddress));
    }

    /**
     * Get the number of decimal places for a specific asset.
     * @param {string} assetAddress - The address of the asset.
     * @returns {Promise<number>} - The number of decimals.
     */
    async getDecimals(assetAddress) {
        const contract = new ethers.Contract(assetAddress, ['function decimals() view returns (uint8)'], this.provider);
        return await contract.decimals();
    }
}

// Example usage
(async () => {
    const bridgeTransfer = new ZkBridgeTransfer();
    await bridgeTransfer.transferAssets(process.env.ASSET_ADDRESS, process.env.RECIPIENT_ADDRESS, parseFloat(process.env.AMOUNT));
})();
```

Make sure to create a `.env` file with the following variables before running the code:

```
ZKSYNC_RPC_URL=<Your zkSync RPC URL>
PRIVATE_KEY=<Your Wallet Private Key>
ASSET_ADDRESS=<Asset Contract Address>
RECIPIENT_ADDRESS=<Recipient Address>
AMOUNT=<Amount to Transfer>
```
