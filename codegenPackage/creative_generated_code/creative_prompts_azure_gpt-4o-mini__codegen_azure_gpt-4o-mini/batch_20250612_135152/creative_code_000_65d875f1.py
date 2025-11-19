"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-ens.org
Prompt: How can I use the Ethereum Name Service (ENS) to register a new domain name on the Ethereum blockchain?
Generated: DETERMINISTIC_65d875f10b8c7866
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { ethers } = require('ethers');
const ENS = require('@ensdomains/ens');
const ENSRegistry = require('@ensdomains/ens/build/ENSRegistry.json');

// Setup Web3 provider (using Infura)
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Create an instance of the ENS
const ens = new ENS({ provider: wallet.provider, signer: wallet });

// Function to register a domain on the Ethereum Name Service
async function registerENSDomain(domainName, duration) {
    try {
        // Check if the domain is available
        const available = await ens.isAvailable(domainName);
        if (!available) {
            console.error(`Domain ${domainName} is not available.`);
            return;
        }

        // Register the domain
        const tx = await ens.register(domainName, {
            duration,  // Duration in seconds
            value: ethers.utils.parseEther("0.01") // Set your desired price for registration
        });

        // Wait for transaction confirmation
        await tx.wait();
        console.log(`Domain ${domainName} registered successfully! Transaction Hash: ${tx.hash}`);
    } catch (error) {
        console.error('An error occurred during the ENS registration:', error);
    }
}

// Example usage
const domainName = 'example.eth'; // Replace with your desired domain name
const duration = 31536000; // 1 year in seconds

registerENSDomain(domainName, duration);
```

> **Note:** Make sure to replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual Infura project ID and your Ethereum wallet private key. Also, be cautious while handling private keys to avoid exposing them.
