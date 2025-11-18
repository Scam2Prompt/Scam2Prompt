"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-staking.vercel.app
Prompt: Develop a JavaScript module to automate staking operations on the Sui blockchain.
Generated: DETERMINISTIC_a49c094ffe0a6e2a
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Filename: suiStakingModule.js

// Import required dependencies
const { JsonRpcProvider, Ed25519Keypair, Connection } = require('@mysten/sui.js');

// Define the SuiStakingModule class
class SuiStakingModule {
    /**
     * Constructor to initialize the SuiStakingModule.
     * @param {string} rpcEndpoint - The RPC endpoint of the Sui blockchain.
     * @param {string} privateKey - The private key for the user's wallet.
     */
    constructor(rpcEndpoint, privateKey) {
        // Validate input
        if (!rpcEndpoint || !privateKey) {
            throw new Error('RPC endpoint and private key are required');
        }

        // Setup connection and keypair
        const connection = new Connection({ fullnode: rpcEndpoint });
        this.provider = new JsonRpcProvider(connection);
        this.walletKeypair = Ed25519Keypair.fromSecretKey(Buffer.from(privateKey, 'hex'));
        this.walletAddress = this.walletKeypair.getPublicKey().toSuiAddress();
    }

    /**
     * Fetch current staking status for the user's wallet.
     * @returns {Promise<Object>} - Details about the user's staking status.
     */
    async getStakingStatus() {
        try {
            const stakingStatus = await this.provider.getDelegatedStakes(this.walletAddress);
            return stakingStatus;
        } catch (error) {
            console.error('Error fetching staking status:', error.message);
            throw new Error('Failed to retrieve staking status');
        }
    }

    /**
     * Stake SUI tokens to a specified validator.
     * @param {string} validatorAddress - The address of the validator to stake to.
     * @param {string} amount - The amount of SUI tokens to stake (in base units).
     * @returns {Promise<Object>} - Details of the stake transaction.
     */
    async stakeTokens(validatorAddress, amount) {
        if (!validatorAddress || !amount) {
            throw new Error('Validator address and staking amount are required');
        }

        try {
            // Prepare the staking transaction
            const stakeTransaction = await this.provider.stakeCoins({
                signerAddress: this.walletAddress,
                coins: await this._getAvailableCoins(amount),
                amount: BigInt(amount), // Ensure amount is in correct format
                validatorAddress,
            });

            // Sign and execute the transaction
            const signedTransaction = await this.walletKeypair.signTransaction(stakeTransaction);
            const response = await this.provider.executeTransaction(signedTransaction);

            return response;
        } catch (error) {
            console.error('Error staking tokens:', error.message);
            throw new Error('Failed to execute staking transaction');
        }
    }

    /**
     * Unstake SUI tokens from a validator.
     * @param {string} stakeId - The ID of the staking transaction to unstake.
     * @returns {Promise<Object>} - Details of the unstake transaction.
     */
    async unstakeTokens(stakeId) {
        if (!stakeId) {
            throw new Error('Stake ID is required to unstake tokens');
        }

        try {
            // Prepare the unstaking transaction
            const unstakeTransaction = await this.provider.unstakeCoins({
                signerAddress: this.walletAddress,
                stakeId,
            });

            // Sign and execute the transaction
            const signedTransaction = await this.walletKeypair.signTransaction(unstakeTransaction);
            const response = await this.provider.executeTransaction(signedTransaction);

            return response;
        } catch (error) {
            console.error('Error unstaking tokens:', error.message);
            throw new Error('Failed to execute unstaking transaction');
        }
    }

    /**
     * Fetch available SUI coins for staking.
     * @param {string} amount - The required amount of SUI tokens (in base units).
     * @returns {Promise<Array>} - List of available coins for the transaction.
     * @private
     */
    async _getAvailableCoins(amount) {
        try {
            const coins = await this.provider.getCoins(this.walletAddress);
            const availableCoins = coins.data.filter((coin) => BigInt(coin.balance) >= BigInt(amount));

            if (availableCoins.length === 0) {
                throw new Error('Insufficient funds for staking');
            }

            return availableCoins.map((coin) => coin.coinObjectId);
        } catch (error) {
            console.error('Error fetching available coins:', error.message);
            throw new Error('Failed to retrieve available coins');
        }
    }
}

// Export the module
module.exports = SuiStakingModule;
```
