"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-docs.vercel.app
Prompt: Write a script to set up a resolver for 1inch Fusion Mode, including the resolver's setup script example provided in the documentation.
Generated: DETERMINISTIC_e28a22c011a94498
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const { ContractFactory } = require("@openzeppelin/contracts");
// Import the 1inch Fusion Mode contract ABI
const fusionModeABI = require("./FusionMode.json");
const resolverABI = require("./Resolver.json");

// Define constants for the contract addresses
const FUSION_MODE_ADDRESS = "0xYourFusionModeContractAddress";
const RESOLVER_ADDRESS = "0xYourResolverContractAddress";

// Define the provider and wallet for interacting with the Ethereum network
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");
const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

// Function to deploy a new resolver contract
async function deployResolver() {
    try {
        // Create a new instance of the Fusion Mode contract
        const fusionModeContract = new ethers.Contract(FUSION_MODE_ADDRESS, fusionModeABI, wallet);

        // Create a new instance of the Resolver contract factory
        const resolverFactory = new ContractFactory(resolverABI, wallet);

        // Deploy the resolver contract
        const resolverContract = await resolverFactory.deploy();
        console.log("Resolver deployed at:", resolverContract.address);

        // Set the resolver for the Fusion Mode contract
        const tx = await fusionModeContract.setResolver(resolverContract.address);
        await tx.wait(); // Wait for the transaction to be mined
        console.log("Resolver set in Fusion Mode contract:", resolverContract.address);
    } catch (error) {
        console.error("Error deploying resolver:", error);
    }
}

// Execute the resolver deployment function
deployResolver();
```
