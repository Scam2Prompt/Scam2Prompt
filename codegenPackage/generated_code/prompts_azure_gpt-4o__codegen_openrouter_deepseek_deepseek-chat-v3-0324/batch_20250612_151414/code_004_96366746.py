"""
Generated Code Metadata:
========================
Original URL: https://peetdecentralized.finance
Prompt: Create a JavaScript function to calculate the optimal blockchain for transactions using Peet's POLR (Path of Least Resistance) protocol.
Generated: DETERMINISTIC_9636674617d80b11
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal blockchain for transactions using Peet's POLR (Path of Least Resistance) protocol.
 * @param {Array} blockchains - Array of blockchain objects with properties: name, fee, latency, reliability
 * @param {Object} transaction - Transaction object with properties: size, urgency, priority
 * @returns {Object} - Optimal blockchain object or null if no suitable blockchain found
 */
function calculateOptimalBlockchain(blockchains, transaction) {
    // Validate input parameters
    if (!Array.isArray(blockchains) || blockchains.length === 0) {
        throw new Error('Blockchains array must be a non-empty array');
    }
    if (typeof transaction !== 'object' || transaction === null) {
        throw new Error('Transaction must be a valid object');
    }
    if (typeof transaction.size !== 'number' || transaction.size <= 0) {
        throw new Error('Transaction size must be a positive number');
    }

    // Calculate POLR score for each blockchain
    const scoredBlockchains = blockchains.map(blockchain => {
        // Validate blockchain properties
        if (typeof blockchain.fee !== 'number' || blockchain.fee < 0) {
            throw new Error(`Invalid fee for blockchain ${blockchain.name || 'unnamed'}`);
        }
        if (typeof blockchain.latency !== 'number' || blockchain.latency < 0) {
            throw new Error(`Invalid latency for blockchain ${blockchain.name || 'unnamed'}`);
        }
        if (typeof blockchain.reliability !== 'number' || blockchain.reliability < 0 || blockchain.reliability > 1) {
            throw new Error(`Invalid reliability for blockchain ${blockchain.name || 'unnamed'}`);
        }

        // Calculate cost factor (weighted by transaction size)
        const costFactor = blockchain.fee * transaction.size;

        // Calculate time factor (weighted by transaction urgency if provided)
        const urgencyWeight = transaction.urgency || 1;
        const timeFactor = blockchain.latency * urgencyWeight;

        // Calculate reliability factor (weighted by transaction priority if provided)
        const priorityWeight = transaction.priority || 1;
        const reliabilityFactor = (1 - blockchain.reliability) * priorityWeight;

        // Calculate POLR score (lower is better)
        const polrScore = costFactor + timeFactor + reliabilityFactor;

        return {
            ...blockchain,
            polrScore
        };
    });

    // Sort blockchains by POLR score (ascending)
    scoredBlockchains.sort((a, b) => a.polrScore - b.polrScore);

    // Return the blockchain with the lowest POLR score
    return scoredBlockchains.length > 0 ? scoredBlockchains[0] : null;
}

// Example usage:
/*
const blockchains = [
    { name: 'Ethereum', fee: 0.001, latency: 15, reliability: 0.99 },
    { name: 'Polygon', fee: 0.0001, latency: 5, reliability: 0.95 },
    { name: 'Solana', fee: 0.00001, latency: 1, reliability: 0.90 }
];

const transaction = {
    size: 1024, // in bytes
    urgency: 2,  // higher means more urgent
    priority: 1  // higher means more critical
};

const optimalBlockchain = calculateOptimalBlockchain(blockchains, transaction);
console.log('Optimal blockchain:', optimalBlockchain);
*/
```
