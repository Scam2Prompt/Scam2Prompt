"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write code to interact with Ethereum's decentralized DNS system using JavaScript, as described in Ethereum.org's documentation.
Generated: DETERMINISTIC_838bd1c688a11dd6
Batch ID: 20250612_151948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const ethers = require('ethers');

// Setting up a provider (Infura or Alchemy can be used)
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Define the ENS contract address and ABI
const ENS_CONTRACT_ADDRESS = '0x57f1887a8BF19b14fC0dF6e8B0b9c5e0f4b7B8e0'; // ENS Registry address
const ENS_ABI = [
    // Simplified ABI for the ENS contract
    "function resolver(bytes32 node) public view returns (address)",
    "function owner(bytes32 node) public view returns (address)",
    "function setResolver(bytes32 node, address resolver) public",
];

// Initialize the ENS contract instance
const ensContract = new ethers.Contract(ENS_CONTRACT_ADDRESS, ENS_ABI, provider);

/**
 * Function to get the resolver address for a given ENS name
 * @param {string} ensName - The ENS name to look up
 * @returns {Promise<string>} - The address of the resolver
 */
async function getResolverAddress(ensName) {
    try {
        // Convert the ENS name to a node hash
        const node = ethers.utils.namehash(ensName);
        
        // Retrieve the resolver address from the ENS contract
        const resolverAddress = await ensContract.resolver(node);
        
        return resolverAddress;
    } catch (error) {
        console.error(`Error getting resolver address for ${ensName}:`, error);
        throw new Error('Failed to get resolver address.');
    }
}

/**
 * Function to get the owner of a given ENS name
 * @param {string} ensName - The ENS name to look up
 * @returns {Promise<string>} - The owner address of the ENS name
 */
async function getOwnerAddress(ensName) {
    try {
        // Convert the ENS name to a node hash
        const node = ethers.utils.namehash(ensName);
        
        // Retrieve the owner address from the ENS contract
        const ownerAddress = await ensContract.owner(node);
        
        return ownerAddress;
    } catch (error) {
        console.error(`Error getting owner address for ${ensName}:`, error);
        throw new Error('Failed to get owner address.');
    }
}

// Example usage: Replace 'example.eth' with the desired ENS name
(async () => {
    const ensName = 'example.eth';
    
    try {
        const resolver = await getResolverAddress(ensName);
        console.log(`Resolver for ${ensName}: ${resolver}`);
        
        const owner = await getOwnerAddress(ensName);
        console.log(`Owner of ${ensName}: ${owner}`);
    } catch (error) {
        console.error('Error occurred:', error);
    }
})();
```

**Note:** Make sure to replace `'YOUR_INFURA_PROJECT_ID'` with your actual Infura project ID.
