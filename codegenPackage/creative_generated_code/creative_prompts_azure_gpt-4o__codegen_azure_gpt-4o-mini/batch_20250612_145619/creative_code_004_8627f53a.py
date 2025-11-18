"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Write code to deploy an Ethereum smart contract for a pledge system using Hardhat, including testing scripts.
Generated: DETERMINISTIC_8627f53a93d4ff22
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// DeployPledgeSystem.js
// This script deploys the Pledge System smart contract to the Ethereum network.

const { ethers } = require("hardhat");

async function main() {
    // Compile the contract
    await hre.run('compile');

    // Get the contract factory for PledgeSystem
    const PledgeSystem = await ethers.getContractFactory("PledgeSystem");

    // Deploy the contract
    const pledgeSystem = await PledgeSystem.deploy();
    
    // Wait for the deployment to be mined
    await pledgeSystem.deployed();

    console.log(`PledgeSystem deployed to: ${pledgeSystem.address}`);
}

// Execute the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```solidity
// PledgeSystem.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PledgeSystem {
    struct Pledge {
        address pledger;
        uint256 amount;
        bool fulfilled;
    }

    // Mapping of pledges
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    // Function to create a pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        pledgeCount++;
        pledges[pledgeCount] = Pledge(msg.sender, msg.value, false);
        
        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    // Function to fulfill a pledge
    function fulfillPledge(uint256 pledgeId) external {
        Pledge storage pledge = pledges[pledgeId];

        require(pledge.pledger == msg.sender, "Only the pledger can fulfill the pledge");
        require(!pledge.fulfilled, "Pledge already fulfilled");

        pledge.fulfilled = true;
        payable(msg.sender).transfer(pledge.amount);

        emit PledgeFulfilled(pledgeId);
    }
}
```

```javascript
// test/PledgeSystem.test.js
// This file contains tests for the Pledge System smart contract.

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PledgeSystem", function () {
    let pledgeSystem;
    let owner;

    beforeEach(async function () {
        // Get the accounts
        [owner] = await ethers.getSigners();
        
        // Deploy the contract
        const PledgeSystem = await ethers.getContractFactory("PledgeSystem");
        pledgeSystem = await PledgeSystem.deploy();
        await pledgeSystem.deployed();
    });

    it("should create a pledge", async function () {
        // Pledge an amount of 1 ether
        const tx = await pledgeSystem.createPledge({ value: ethers.utils.parseEther("1") });
        await tx.wait();

        // Check the pledge count and details
        expect(await pledgeSystem.pledgeCount()).to.equal(1);
        const pledge = await pledgeSystem.pledges(1);
        expect(pledge.pledger).to.equal(owner.address);
        expect(pledge.amount).to.equal(ethers.utils.parseEther("1"));
        expect(pledge.fulfilled).to.equal(false);
    });

    it("should fulfill a pledge", async function () {
        // Create a pledge
        await pledgeSystem.createPledge({ value: ethers.utils.parseEther("1") });

        // Fulfill the pledge
        const tx = await pledgeSystem.fulfillPledge(1);
        await tx.wait();

        // Check the pledge status
        const pledge = await pledgeSystem.pledges(1);
        expect(pledge.fulfilled).to.equal(true);
    });

    it("should revert if a non-pleger tries to fulfill a pledge", async function () {
        // Create a pledge
        await pledgeSystem.createPledge({ value: ethers.utils.parseEther("1") });
        
        // Get another account to attempt to fulfill the pledge
        const [_, addr1] = await ethers.getSigners();
        
        await expect(pledgeSystem.connect(addr1).fulfillPledge(1)).to.be.revertedWith("Only the pledger can fulfill the pledge");
    });
});
```

### Hardhat Configuration
```javascript
// hardhat.config.js
require("@nomiclabs/hardhat-waffle");

module.exports = {
    solidity: "0.8.0",
    networks: {
        // Configuration for deploying to networks can be added here
    }
};
```

### Instructions for Running

1. Install dependencies:
   ```bash
   npm install --save-dev hardhat @nomiclabs/hardhat-waffle ethers chai
   ```

2. Create the Hardhat project structure:
   ```bash
   npx hardhat
   ```

3. Place the `PledgeSystem.sol` in the `contracts` directory, `DeployPledgeSystem.js` in the `scripts` directory, and the test file in the `test` directory.

4. Run the deployment script:
   ```bash
   npx hardhat run scripts/DeployPledgeSystem.js
   ```

5. Run tests:
   ```bash
   npx hardhat test
   ```
