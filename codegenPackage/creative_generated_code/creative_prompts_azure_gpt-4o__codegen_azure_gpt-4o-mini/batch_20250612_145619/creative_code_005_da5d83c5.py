"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovken.com
Prompt: Suggest tools or frameworks for deploying an Ethereum pledge smart contract and testing its functionality.
Generated: DETERMINISTIC_da5d83c5170403b7
Batch ID: 20250612_145619
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
const { expect } = require("chai");
const { run, artifacts } = require("hardhat");

// Define the smart contract deployment script
async function main() {
    // Set up provider and wallet
    const provider = new ethers.providers.InfuraProvider("homestead", "YOUR_INFURA_PROJECT_ID");
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

    // Compile the smart contract
    await run("compile");

    // Get the contract factory
    const PledgeContract = await ethers.getContractFactory("Pledge");

    // Deploy the contract
    const pledgeContract = await PledgeContract.deploy();
    console.log("Pledge contract deployed at:", pledgeContract.address);

    // Wait for deployment to complete
    await pledgeContract.deployed();
    console.log("Pledge contract has been deployed successfully!");
}

// Test the smart contract functionality
async function testPledgeContract() {
    // Get the contract artifact
    const Pledge = await artifacts.readArtifact("Pledge");

    // Set up a local Ethereum network with Hardhat
    const [deployer] = await ethers.getSigners();

    // Deploy the contract
    const pledgeContract = await deployer.sendTransaction({
        data: Pledge.bytecode,
        gasLimit: 1000000,
    });
    
    console.log("Contract deployed to:", pledgeContract.address);

    // Interact with the contract and perform tests
    const initialBalance = await pledgeContract.getBalance();
    expect(initialBalance).to.equal(0);

    // Call a function to pledge some amount
    await pledgeContract.pledge({ value: ethers.utils.parseEther("1") });

    const newBalance = await pledgeContract.getBalance();
    expect(newBalance).to.equal(ethers.utils.parseEther("1"));
}

// Handle errors gracefully
async function runDeploymentAndTesting() {
    try {
        await main();
        await testPledgeContract();
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Run the deployment and testing script
runDeploymentAndTesting();
```

Note: Replace `"YOUR_INFURA_PROJECT_ID"` and `"YOUR_PRIVATE_KEY"` with actual values before running the code.
