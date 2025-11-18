"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Write a script to query ENS-enabled DNS names using the gasless DNSSEC feature, ensuring compatibility with the Ethereum Mainnet.
Generated: DETERMINISTIC_bfde91966e0ec07c
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { getEnsAddress } = require('@ensdomains/ensjs');

// Configuration for Ethereum Mainnet provider
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Create a function to query ENS names
async function queryENSName(ensName) {
    try {
        // Validate input ENS name format
        if (!/^[a-z0-9-]+\.eth$/.test(ensName)) {
            throw new Error('Invalid ENS name format. Ensure it ends with .eth');
        }

        // Get the ENS address resolver
        const ensAddress = await getEnsAddress({ provider });

        // Create a contract instance for the ENS registry
        const ensRegistry = new ethers.Contract(
            ensAddress,
            [
                'function resolver(string calldata name) external view returns (address)',
                'function owner(string calldata name) external view returns (address)',
            ],
            provider
        );

        // Fetch the resolver address for the given ENS name
        const resolverAddress = await ensRegistry.resolver(ensName);
        if (!resolverAddress) {
            throw new Error('Resolver not found for the given ENS name.');
        }

        // Fetch the owner of the ENS name
        const ownerAddress = await ensRegistry.owner(ensName);

        // Return the resolver and owner addresses
        return {
            resolverAddress,
            ownerAddress,
        };
    } catch (error) {
        // Handle errors and log them
        console.error('Error querying ENS name:', error.message);
        throw error; // Rethrow error for further handling if needed
    }
}

// Example usage of the queryENSName function
(async () => {
    const ensName = 'example.eth'; // Replace with your ENS name

    try {
        const result = await queryENSName(ensName);
        console.log(`Resolver Address: ${result.resolverAddress}`);
        console.log(`Owner Address: ${result.ownerAddress}`);
    } catch (error) {
        // Handle any errors that occurred during the ENS query
        console.error('Failed to query ENS name:', error.message);
    }
})();
```
