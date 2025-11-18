"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwish.com
Prompt: Suggest tools or frameworks for testing and deploying an ETH pledge smart contract on the Ethereum blockchain.
Generated: DETERMINISTIC_128bff4c1d715519
Batch ID: 20250612_152600
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

// Smart contract testing for an ETH pledge contract
describe("ETH Pledge Smart Contract", function () {
    let pledgeContract;
    let deployer;

    // Deploy contract before each test
    beforeEach(async function () {
        // Get named accounts from Hardhat configuration
        const accounts = await getNamedAccounts();
        deployer = accounts.deployer;

        // Deploy the contract
        await deployments.fixture(["Pledge"]);
        pledgeContract = await ethers.getContract("Pledge", deployer);
    });

    // Test to check if the contract can accept pledges
    it("Should accept pledges", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");

        // Pledge ETH
        const transaction = await pledgeContract.pledge({ value: pledgeAmount });
        await transaction.wait();

        // Verify that the pledge was successful
        const totalPledged = await pledgeContract.totalPledged();
        expect(totalPledged).to.equal(pledgeAmount);
    });

    // Test to check if the contract can return pledges
    it("Should return pledges", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");

        // Make a pledge
        await pledgeContract.pledge({ value: pledgeAmount });
        
        // Withdraw the pledge
        const transaction = await pledgeContract.withdraw();
        await transaction.wait();

        // Check if the pledge amount is zero after withdrawal
        const totalPledged = await pledgeContract.totalPledged();
        expect(totalPledged).to.equal(0);
    });

    // Error handling test for insufficient funds
    it("Should revert transaction when pledge amount is zero", async function () {
        await expect(pledgeContract.pledge({ value: 0 })).to.be.revertedWith("Pledge amount must be greater than zero");
    });
});

// Sample deployment script for Hardhat
async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    // Deploy the ETH Pledge contract
    const Pledge = await ethers.getContractFactory("Pledge");
    const pledgeContract = await Pledge.deploy();

    console.log("Pledge contract deployed to:", pledgeContract.address);
}

// Error handling for deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error deploying contract:", error);
        process.exit(1);
    });
```

### Notes:
- Ensure the `Pledge` contract is defined in your project.
- Replace the Pledge contract with the actual implementation you will be deploying.
- Use Hardhat or Truffle framework for deployment and testing.
