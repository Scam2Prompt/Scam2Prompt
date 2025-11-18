"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Suggest tools or frameworks for testing and deploying an ETH pledge smart contract on the Ethereum blockchain.
Generated: DETERMINISTIC_128bff4c1d715519
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for Ethereum development
const { ethers } = require("ethers");
const { expect } = require("chai");
const { deployments, getNamedAccounts } = require("hardhat");

// Smart contract for ETH pledge
const Pledge = artifacts.require("Pledge");

// Test suite for the Pledge smart contract
describe("Pledge Smart Contract", function () {
    let pledge;
    let deployer;
    let user;

    // Setup before each test
    beforeEach(async function () {
        // Get named accounts
        const accounts = await getNamedAccounts();
        deployer = accounts.deployer;
        user = accounts.user;

        // Deploy the Pledge contract
        pledge = await deployments.deploy("Pledge", {
            from: deployer,
            log: true,
        });
    });

    // Test case for creating a pledge
    it("should allow a user to create a pledge", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");

        // Create a pledge
        const tx = await pledge.connect(user).createPledge({ value: pledgeAmount });
        await tx.wait();

        // Verify that the pledge was created
        const pledgeInfo = await pledge.getPledge(user.address);
        expect(pledgeInfo.amount).to.equal(pledgeAmount);
        expect(pledgeInfo.isActive).to.equal(true);
    });

    // Test case for withdrawing a pledge
    it("should allow a user to withdraw a pledge", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");

        // Create a pledge
        await pledge.connect(user).createPledge({ value: pledgeAmount });

        // Withdraw the pledge
        const tx = await pledge.connect(user).withdrawPledge();
        await tx.wait();

        // Verify that the pledge is no longer active
        const pledgeInfo = await pledge.getPledge(user.address);
        expect(pledgeInfo.isActive).to.equal(false);
    });

    // Test case for error handling on insufficient funds
    it("should revert when insufficient funds are provided", async function () {
        const pledgeAmount = ethers.utils.parseEther("0.1");

        // Expect the transaction to be reverted
        await expect(pledge.connect(user).createPledge({ value: pledgeAmount })).to.be.revertedWith("Insufficient funds");
    });
});

// Deployment script for the Pledge contract
async function main() {
    const deployer = (await ethers.getSigners())[0];
    console.log("Deploying contracts with the account:", deployer.address);

    const PledgeFactory = await ethers.getContractFactory("Pledge");
    const pledge = await PledgeFactory.deploy();
    await pledge.deployed();

    console.log("Pledge contract deployed to:", pledge.address);
}

// Error handling for the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

### Note:
- This code snippet assumes that you have a basic smart contract named `Pledge` with functions `createPledge` and `withdrawPledge` already defined.
- It uses the Hardhat framework for Ethereum development along with Chai for testing.
- Ensure that your project has the necessary dependencies installed (e.g., `ethers`, `chai`, `hardhat`, etc.) before running the code.
