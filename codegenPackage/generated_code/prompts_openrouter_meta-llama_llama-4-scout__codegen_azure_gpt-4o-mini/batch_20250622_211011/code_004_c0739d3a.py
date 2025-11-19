"""
Generated Code Metadata:
========================
Original URL: https://name-service-ui-git-sns-278-1a53f5-kitten-wild-winner-d1d99758.vercel.app
Prompt: How can I use the Solana Name Service to host a decentralized website with a custom .sol domain?
Generated: DETERMINISTIC_c0739d3aed3be768
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { NameRegistryState, getNameAccountKey } = require('@solana/spl-name-service');
const fs = require('fs');
const path = require('path');

// Define constants
const SOLANA_NETWORK = 'mainnet-beta'; // Change to 'devnet' for testing
const DOMAIN_NAME = 'yourcustomdomain.sol'; // Replace with your .sol domain
const PRIVATE_KEY_PATH = path.join(__dirname, 'path_to_your_private_key.json'); // Path to your private key JSON file

// Function to load the private key from a JSON file
function loadPrivateKey(filePath) {
    try {
        const keyData = fs.readFileSync(filePath);
        return JSON.parse(keyData);
    } catch (error) {
        console.error('Error loading private key:', error);
        process.exit(1);
    }
}

// Function to get the name account details
async function getNameAccountDetails(domain) {
    const connection = new Connection(clusterApiUrl(SOLANA_NETWORK), 'confirmed');
    const nameAccountKey = await getNameAccountKey(domain);
    
    try {
        const accountInfo = await connection.getAccountInfo(nameAccountKey);
        if (accountInfo === null) {
            throw new Error('Account not found');
        }
        const nameRegistry = NameRegistryState.deserialize(accountInfo.data);
        return nameRegistry;
    } catch (error) {
        console.error('Error fetching name account details:', error);
        process.exit(1);
    }
}

// Function to update the DNS records for the domain
async function updateDNSRecords(domain, records) {
    // Placeholder for DNS update logic
    // This would typically involve interacting with a smart contract or API
    console.log(`Updating DNS records for ${domain} with`, records);
}

// Main function to host a decentralized website
async function hostDecentralizedWebsite() {
    const privateKey = loadPrivateKey(PRIVATE_KEY_PATH);
    const domainDetails = await getNameAccountDetails(DOMAIN_NAME);

    // Example DNS records to update (replace with actual records)
    const dnsRecords = {
        'A': 'your.website.ip.address', // Replace with your website's IP address
        'CNAME': 'your.website.cname', // Replace with your website's CNAME
    };

    await updateDNSRecords(DOMAIN_NAME, dnsRecords);
    console.log(`Successfully hosted ${DOMAIN_NAME} on the Solana Name Service.`);
}

// Execute the main function
hostDecentralizedWebsite().catch(error => {
    console.error('Error in hosting decentralized website:', error);
});
```

**Note:** Make sure to replace placeholders like `yourcustomdomain.sol`, `path_to_your_private_key.json`, and DNS records with actual values before running the code.
