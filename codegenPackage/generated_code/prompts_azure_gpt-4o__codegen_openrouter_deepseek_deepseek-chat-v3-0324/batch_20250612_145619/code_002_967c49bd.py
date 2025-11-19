"""
Generated Code Metadata:
========================
Original URL: https://ethphbi.com
Prompt: Generate code to create and deploy an Ethereum smart contract for tracking pledges, including functions for adding, updating, and retrieving pledge data.
Generated: DETERMINISTIC_967c49bd61db510b
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PledgeTracker
 * @dev A smart contract for tracking pledges with functions to add, update, and retrieve pledge data
 */
contract PledgeTracker {
    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        string description;
        uint256 amount;
        uint256 deadline;
        bool fulfilled;
    }

    // Mapping from pledge ID to Pledge
    mapping(uint256 => Pledge) public pledges;
    
    // Counter for pledge IDs
    uint256 public nextPledgeId;
    
    // Events
    event PledgeAdded(uint256 indexed pledgeId, address indexed pledger, string description, uint256 amount, uint256 deadline);
    event PledgeUpdated(uint256 indexed pledgeId, bool fulfilled);
    
    /**
     * @dev Add a new pledge
     * @param _description Description of the pledge
     * @param _amount Amount pledged (in wei)
     * @param _deadline Timestamp when pledge should be fulfilled by
     */
    function addPledge(
        string memory _description,
        uint256 _amount,
        uint256 _deadline
    ) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_amount > 0, "Amount must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");
        
        uint256 pledgeId = nextPledgeId;
        pledges[pledgeId] = Pledge({
            pledger: msg.sender,
            description: _description,
            amount: _amount,
            deadline: _deadline,
            fulfilled: false
        });
        
        nextPledgeId++;
        emit PledgeAdded(pledgeId, msg.sender, _description, _amount, _deadline);
    }
    
    /**
     * @dev Update pledge fulfillment status
     * @param _pledgeId ID of the pledge to update
     * @param _fulfilled Whether the pledge has been fulfilled
     */
    function updatePledgeFulfillment(
        uint256 _pledgeId,
        bool _fulfilled
    ) external {
        require(_pledgeId < nextPledgeId, "Invalid pledge ID");
        Pledge storage pledge = pledges[_pledgeId];
        require(msg.sender == pledge.pledger, "Only pledger can update status");
        
        pledge.fulfilled = _fulfilled;
        emit PledgeUpdated(_pledgeId, _fulfilled);
    }
    
    /**
     * @dev Get pledge details
     * @param _pledgeId ID of the pledge to retrieve
     * @return Pledge details
     */
    function getPledge(uint256 _pledgeId) external view returns (
        address,
        string memory,
        uint256,
        uint256,
        bool
    ) {
        require(_pledgeId < nextPledgeId, "Invalid pledge ID");
        Pledge memory pledge = pledges[_pledgeId];
        return (
            pledge.pledger,
            pledge.description,
            pledge.amount,
            pledge.deadline,
            pledge.fulfilled
        );
    }
    
    /**
     * @dev Get total number of pledges
     * @return Total pledge count
     */
    function getPledgeCount() external view returns (uint256) {
        return nextPledgeId;
    }
}
```

```javascript
// Deployment script using Hardhat and ethers.js
const { ethers } = require("hardhat");

async function main() {
    // Get the contract factory
    const PledgeTracker = await ethers.getContractFactory("PledgeTracker");
    
    // Deploy the contract
    console.log("Deploying PledgeTracker...");
    const pledgeTracker = await PledgeTracker.deploy();
    
    // Wait for deployment to complete
    await pledgeTracker.deployed();
    
    console.log("PledgeTracker deployed to:", pledgeTracker.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```javascript
// Test script using Hardhat and ethers.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PledgeTracker", function () {
    let PledgeTracker;
    let pledgeTracker;
    let owner;
    let addr1;

    beforeEach(async function () {
        [owner, addr1] = await ethers.getSigners();
        PledgeTracker = await ethers.getContractFactory("PledgeTracker");
        pledgeTracker = await PledgeTracker.deploy();
    });

    describe("Deployment", function () {
        it("Should deploy successfully", async function () {
            expect(pledgeTracker.address).to.not.equal(0);
        });
    });

    describe("Pledge Management", function () {
        it("Should allow adding a pledge", async function () {
            await expect(
                pledgeTracker.connect(addr1).addPledge(
                    "Test pledge",
                    ethers.utils.parseEther("1"),
                    Math.floor(Date.now() / 1000) + 3600
                )
            ).to.emit(pledgeTracker, "PledgeAdded");
        });

        it("Should reject invalid pledge data", async function () {
            await expect(
                pledgeTracker.connect(addr1).addPledge(
                    "",
                    ethers.utils.parseEther("1"),
                    Math.floor(Date.now() / 1000) + 3600
                )
            ).to.be.revertedWith("Description cannot be empty");

            await expect(
                pledgeTracker.connect(addr1).addPledge(
                    "Test pledge",
                    0,
                    Math.floor(Date.now() / 1000) + 3600
                )
            ).to.be.revertedWith("Amount must be greater than 0");

            await expect(
                pledgeTracker.connect(addr1).addPledge(
                    "Test pledge",
                    ethers.utils.parseEther("1"),
                    Math.floor(Date.now() / 1000) - 3600
                )
            ).to.be.revertedWith("Deadline must be in the future");
        });

        it("Should allow updating pledge status", async function () {
            await pledgeTracker.connect(addr1).addPledge(
                "Test pledge",
                ethers.utils.parseEther("1"),
                Math.floor(Date.now() / 1000) + 3600
            );

            await expect(
                pledgeTracker.connect(addr1).updatePledgeFulfillment(0, true)
            ).to.emit(pledgeTracker, "PledgeUpdated");
        });

        it("Should reject unauthorized status updates", async function () {
            await pledgeTracker.connect(addr1).addPledge(
                "Test pledge",
                ethers.utils.parseEther("1"),
                Math.floor(Date.now() / 1000) + 3600
            );

            await expect(
                pledgeTracker.updatePledgeFulfillment(0, true)
            ).to.be.revertedWith("Only pledger can update status");
        });

        it("Should retrieve pledge data correctly", async function () {
            const description = "Test pledge";
            const amount = ethers.utils.parseEther("1");
            const deadline = Math.floor(Date.now() / 1000) + 3600;

            await pledgeTracker.connect(addr1).addPledge(
                description,
                amount,
                deadline
            );

            const pledge = await pledgeTracker.getPledge(0);
            expect(pledge[0]).to.equal(addr1.address);
            expect(pledge[1]).to.equal(description);
            expect(pledge[2]).to.equal(amount);
            expect(pledge[3]).to.equal(deadline);
            expect(pledge[4]).to.equal(false);
        });
    });
});
```
