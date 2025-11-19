"""
Generated Code Metadata:
========================
Original URL: https://soljack.com
Prompt: Generate JavaScript code to verify the fairness of a gambling game using Solana smart contracts, inspired by SolJack's model.
Generated: DETERMINISTIC_9c2d22a48bad75c9
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
const solanaWeb3 = require('@solana/web3.js');
const bs58 = require('bs58');

/**
 * Verifies the fairness of a gambling game on Solana by checking the on-chain randomness.
 * Inspired by SolJack's model.
 */
class FairnessVerifier {
    /**
     * Initialize the FairnessVerifier with a Solana connection.
     * @param {string} rpcUrl - The Solana RPC endpoint URL
     */
    constructor(rpcUrl) {
        this.connection = new solanaWeb3.Connection(rpcUrl);
    }

    /**
     * Verify the fairness of a game transaction by checking the randomness seed.
     * @param {string} transactionSignature - The transaction signature to verify
     * @param {string} expectedProgramId - The expected program ID of the gambling contract
     * @returns {Promise<{isFair: boolean, details: string}>} Verification result
     */
    async verifyFairness(transactionSignature, expectedProgramId) {
        try {
            // Fetch the transaction details
            const tx = await this.connection.getTransaction(transactionSignature, {
                commitment: 'confirmed',
                maxSupportedTransactionVersion: 0
            });

            if (!tx) {
                throw new Error('Transaction not found');
            }

            // Verify the program ID
            const programId = tx.transaction.message.instructions[0]?.programId?.toString();
            if (programId !== expectedProgramId) {
                return {
                    isFair: false,
                    details: `Transaction not from expected program. Expected: ${expectedProgramId}, Got: ${programId}`
                };
            }

            // Extract the randomness seed from the instruction data
            const instructionData = tx.transaction.message.instructions[0]?.data;
            if (!instructionData) {
                return {
                    isFair: false,
                    details: 'No instruction data found in transaction'
                };
            }

            const decodedData = bs58.decode(instructionData);
            if (decodedData.length < 32) {
                return {
                    isFair: false,
                    details: 'Invalid instruction data length for randomness seed'
                };
            }

            // The first 32 bytes should be the randomness seed
            const randomnessSeed = decodedData.slice(0, 32);

            // Verify the randomness seed was generated from recent blockhash
            const recentBlockhash = tx.transaction.message.recentBlockhash;
            const blockhashBuffer = Buffer.from(recentBlockhash, 'base64');

            // Simple verification: check if randomness seed is derived from blockhash
            // In a real implementation, you would use the same algorithm as the contract
            const derivedSeed = this._simpleHash(blockhashBuffer).slice(0, 32);
            const isFair = Buffer.compare(randomnessSeed, derivedSeed) === 0;

            return {
                isFair,
                details: isFair 
                    ? 'Randomness seed is properly derived from recent blockhash' 
                    : 'Randomness seed does not match expected derivation'
            };
        } catch (error) {
            console.error('Error verifying fairness:', error);
            return {
                isFair: false,
                details: `Verification failed: ${error.message}`
            };
        }
    }

    /**
     * Simple hash function for demonstration purposes.
     * In production, use the same hash function as the smart contract.
     * @private
     */
    _simpleHash(buffer) {
        const crypto = require('crypto');
        const hash = crypto.createHash('sha256');
        hash.update(buffer);
        return hash.digest();
    }
}

// Example usage:
/*
(async () => {
    const verifier = new FairnessVerifier('https://api.mainnet-beta.solana.com');
    const result = await verifier.verifyFairness(
        '5VERv8NMvzbJMEkV8xnrLkEaWRtSz9CosKDYjCJjBRnb',
        'JackpotProgram11111111111111111111111111111'
    );
    console.log(result);
})();
*/

module.exports = FairnessVerifier;
```
