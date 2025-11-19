"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica-auth.vercel.app
Prompt: What are the steps to integrate Matrica's network selection feature in a JavaScript application for Solana?
Generated: DETERMINISTIC_23115602e5a05c5e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js'; // Solana web3 dependency
import { Matrica } from '@matrica/sdk'; // Matrica SDK (ensure this is installed via npm/yarn)

// Constants for network configurations
const NETWORKS = {
    mainnet: clusterApiUrl('mainnet-beta'),
    devnet: clusterApiUrl('devnet'),
    testnet: clusterApiUrl('testnet'),
};

// Function to initialize Matrica with selected network
async function initializeMatrica(network = 'mainnet') {
    try {
        // Validate the input network
        if (!NETWORKS[network]) {
            throw new Error(`Invalid network selection: ${network}`);
        }

        // Create a new Solana connection using the selected network's RPC URL
        const connection = new Connection(NETWORKS[network]);

        // Initialize Matrica SDK
        const matrica = new Matrica({
            connection, // Pass the Solana connection object
            publicKey: new PublicKey(/* Your wallet's public key */), // Provide a valid wallet public key
        });

        // Use the Matrica instance for further operations
        console.log(`Matrica initialized on ${network} network`);
        return matrica;
    } catch (error) {
        // Handle errors gracefully
        console.error('Error initializing Matrica:', error.message);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        // Initialize Matrica on devnet
        const matricaInstance = await initializeMatrica('devnet');

        // Perform operations with Matrica instance
        console.log('Matrica instance:', matricaInstance);
    } catch (error) {
        console.error('Failed to integrate Matrica:', error.message);
    }
})();
```

Make sure to adjust any placeholders, such as `/* Your wallet's public key */`, and install required dependencies using a package manager like npm or yarn (`npm install @solana/web3.js @matrica/sdk`).
