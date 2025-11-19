"""
Generated Code Metadata:
========================
Original URL: https://ethwish.com
Prompt: Suggest tools or frameworks for testing and deploying an ETH pledge smart contract on the Ethereum blockchain.
Generated: DETERMINISTIC_128bff4c1d715519
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require("hardhat");
const { expect } = require("chai");

// Smart contract for ETH pledge
contract("Pledge", function () {
    let pledgeContract;
    let owner;
    let addr1;
    let addr2;

    // Deploy the contract before each test
    beforeEach(async function () {
        [owner, addr1, addr2] = await ethers.getSigners();
        const Pledge = await ethers.getContractFactory("Pledge");
        pledgeContract = await Pledge.deploy();
        await pledgeContract.deployed();
    });

    // Test case for pledging ETH
    it("Should allow users to pledge ETH", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");

        // Pledge ETH
        await pledgeContract.connect(addr1).pledge({ value: pledgeAmount });

        // Check the balance of the contract
        const contractBalance = await ethers.provider.getBalance(pledgeContract.address);
        expect(contractBalance).to.equal(pledgeAmount);
    });

    // Test case for withdrawing ETH
    it("Should allow the owner to withdraw ETH", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");
        await pledgeContract.connect(addr1).pledge({ value: pledgeAmount });

        // Withdraw ETH
        await pledgeContract.connect(owner).withdraw();

        // Check the balance of the contract
        const contractBalance = await ethers.provider.getBalance(pledgeContract.address);
        expect(contractBalance).to.equal(0);
    });

    // Test case for non-owner withdrawal
    it("Should not allow non-owners to withdraw ETH", async function () {
        const pledgeAmount = ethers.utils.parseEther("1.0");
        await pledgeContract.connect(addr1).pledge({ value: pledgeAmount });

        // Attempt to withdraw as a non-owner
        await expect(pledgeContract.connect(addr2).withdraw()).to.be.revertedWith("Only the owner can withdraw");
    });
});

// Smart contract code
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Pledge {
    address public owner;

    // Mapping to track pledges
    mapping(address => uint256) public pledges;

    // Event to emit when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event to emit when funds are withdrawn
    event Withdrawn(address indexed owner, uint256 amount);

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to pledge ETH
    function pledge() external payable {
        require(msg.value > 0, "Must pledge a positive amount");
        pledges[msg.sender] += msg.value;
        emit Pledged(msg.sender, msg.value);
    }

    // Function to withdraw ETH (only owner)
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
        emit Withdrawn(owner, balance);
    }
}
```

### Tools and Frameworks for Testing and Deployment
- **Hardhat**: A development environment to compile, deploy, test, and debug Ethereum software.
- **Chai**: Assertion library for testing.
- **Ethers.js**: A library for interacting with the Ethereum blockchain.
- **OpenZeppelin**: A library for secure smart contract development (optional for additional features).
- **Ganache**: A personal Ethereum blockchain for testing.
- **Truffle**: An alternative framework for development and testing.
