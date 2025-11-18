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
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title PledgeSystem - A simple Ethereum smart contract for managing pledges.
contract PledgeSystem {
    // Event to log a new pledge
    event PledgeCreated(address indexed pledger, uint256 amount);

    // Mapping to store pledges by address
    mapping(address => uint256) public pledges;

    // Total amount pledged
    uint256 public totalPledged;

    /// @notice Allows a user to make a pledge
    /// @dev Emits a PledgeCreated event on successful pledging
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update pledger's balance and total pledged
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;

        // Emit event for the new pledge
        emit PledgeCreated(msg.sender, msg.value);
    }

    /// @notice Allows a user to retrieve their pledged amount
    /// @return The amount pledged by the sender
    function getMyPledge() external view returns (uint256) {
        return pledges[msg.sender];
    }
}
```

### Deployment Script (`scripts/deploy.js`)
```javascript
// scripts/deploy.js
const hre = require("hardhat");

async function main() {
  // Compile if necessary
  await hre.run('compile');

  console.log("Deploying the PledgeSystem contract...");

  // Get the contract factory
  const PledgeSystem = await hre.ethers.getContractFactory("PledgeSystem");

  // Deploy the contract
  const pledgeSystem = await PledgeSystem.deploy();

  // Wait for the deployment to finish
  await pledgeSystem.deployed();

  console.log(`PledgeSystem deployed to: ${pledgeSystem.address}`);
}

// Execute the script in async environment
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

### Testing Script (`test/pledgeSystem.js`)
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PledgeSystem", function () {
  let PledgeSystem, pledgeSystem, owner, addr1, addr2;

  beforeEach(async function () {
    // Get the contract factory and signers
    PledgeSystem = await ethers.getContractFactory("PledgeSystem");
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy the contract
    pledgeSystem = await PledgeSystem.deploy();
    await pledgeSystem.deployed();
  });

  it("should allow a user to make a pledge", async function () {
    // addr1 makes a pledge of 1 ETH
    const pledgeAmount = ethers.utils.parseEther("1.0");
    await pledgeSystem.connect(addr1).makePledge({ value: pledgeAmount });

    // Check the pledge balance of addr1
    expect(await pledgeSystem.getMyPledge()).to.equal(pledgeAmount);

    // Check the total pledged amount
    expect(await pledgeSystem.totalPledged()).to.equal(pledgeAmount);
  });

  it("should not allow a pledge of zero", async function () {
    // Attempt to make a pledge of 0 ETH
    await expect(
      pledgeSystem.connect(addr1).makePledge({ value: 0 })
    ).to.be.revertedWith("Pledge amount must be greater than zero");
  });

  it("should track multiple pledges from different users", async function () {
    // addr1 pledges 1 ETH
    const pledge1 = ethers.utils.parseEther("1.0");
    await pledgeSystem.connect(addr1).makePledge({ value: pledge1 });

    // addr2 pledges 2 ETH
    const pledge2 = ethers.utils.parseEther("2.0");
    await pledgeSystem.connect(addr2).makePledge({ value: pledge2 });

    // Check individual pledges
    expect(await pledgeSystem.connect(addr1).getMyPledge()).to.equal(pledge1);
    expect(await pledgeSystem.connect(addr2).getMyPledge()).to.equal(pledge2);

    // Check total pledged amount
    expect(await pledgeSystem.totalPledged()).to.equal(
      pledge1.add(pledge2)
    );
  });
});
```

### `hardhat.config.js`
```javascript
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.18",
  networks: {
    hardhat: {},
    // Define other networks here if needed (e.g., for testing on a testnet)
  },
};
```

### Commands to Run
#### Install Dependencies
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox chai ethers
```

#### Compile Smart Contract
```bash
npx hardhat compile
```

#### Deploy Smart Contract
```bash
npx hardhat run scripts/deploy.js
```

#### Run Tests
```bash
npx hardhat test
```
