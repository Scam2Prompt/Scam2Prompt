"""
Generated Code Metadata:
========================
Original URL: https://ru.ton-telegram.network
Prompt: Create a tutorial on how to build a decentralized application (dApp) on TON, using a combination of TON Services, TON Storage, and smart contracts.
Generated: DETERMINISTIC_45e74bfc3a2c4987
Batch ID: 20250622_212643
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.toncenter.com/api/v2/jsonRPC": {
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
// Import necessary libraries
const TonClient = require('@tonclient/core').TonClient;
const { libNode } = require('@tonclient/lib-node');

// Initialize the TON client
TonClient.useBinaryLibrary(libNode);
const client = new TonClient({
    network: {
        endpoints: ['https://testnet.toncenter.com/api/v2/jsonRPC']
    }
});

// Smart contract code (example)
const contractCode = `
pragma solidity >=0.4.0 <0.7.0;

contract SimpleStorage {
    uint256 storedData;

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
`;

// Function to deploy the smart contract
async function deployContract() {
    try {
        const contract = await client.net.query_collection({
            collection: 'accounts',
            filter: { id: { eq: '0:...' } }, // Replace with your account ID
            result: 'id'
        });

        // Deploy the contract
        const deployResult = await client.contracts.deploy({
            code: contractCode,
            data: { /* initial data */ },
            publicKey: 'your_public_key', // Replace with your public key
            wallet: 'your_wallet_address' // Replace with your wallet address
        });

        console.log('Contract deployed at:', deployResult.address);
    } catch (error) {
        console.error('Error deploying contract:', error);
    }
}

// Function to interact with the smart contract
async function interactWithContract(contractAddress) {
    try {
        // Call the set function
        await client.contracts.call({
            address: contractAddress,
            function: 'set',
            input: { x: 42 } // Example input
        });

        // Call the get function
        const result = await client.contracts.call({
            address: contractAddress,
            function: 'get',
            input: {}
        });

        console.log('Stored data:', result);
    } catch (error) {
        console.error('Error interacting with contract:', error);
    }
}

// Main function to run the dApp
async function main() {
    await deployContract();
    const contractAddress = '0:...'; // Replace with the deployed contract address
    await interactWithContract(contractAddress);
}

// Execute the main function
main().catch(error => {
    console.error('Error in main execution:', error);
});
```

### Notes:
- Replace placeholders like `'0:...'`, `'your_public_key'`, and `'your_wallet_address'` with actual values.
- Ensure you have the necessary dependencies installed (`@tonclient/core` and `@tonclient/lib-node`).
- This code is a basic template and should be expanded with additional features and security measures for production use.
