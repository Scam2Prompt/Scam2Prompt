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
// This code provides a basic setup for testing and deploying an Ethereum smart contract
// using Hardhat and tools like ethers.js and mocha for testing. Ensure you have Node.js
// installed and the proper environment setup before running this code.

// Install necessary dependencies:
// npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers mocha chai

// Import required dependencies
const { ethers } = require("hardhat");
const { expect } = require("chai");

// Define a sample test file for testing the smart contract
describe("ETH Pledge Smart Contract", function () {
  let PledgeContract, pledge, owner, addr1, addr2;

  beforeEach(async function () {
    // Deploy the contract before running each test
    PledgeContract = await ethers.getContractFactory("Pledge");
    [owner, addr1, addr2] = await ethers.getSigners(); // Get test accounts
    pledge = await PledgeContract.deploy(); // Deploy contract
    await pledge.deployed(); // Wait until contract is deployed
  });

  it("Should allow pledging ETH and track balances properly", async function () {
    // addr1 pledges 1 ETH
    await pledge.connect(addr1).pledge({ value: ethers.utils.parseEther("1") });

    // addr2 pledges 0.5 ETH
    await pledge.connect(addr2).pledge({ value: ethers.utils.parseEther("0.5") });

    // Validate balances
    expect(await pledge.getBalance(addr1.address)).to.equal(
      ethers.utils.parseEther("1")
    );
    expect(await pledge.getBalance(addr2.address)).to.equal(
      ethers.utils.parseEther("0.5")
    );
  });

  it("Should not allow non-owners to withdraw", async function () {
    await expect(
      pledge.connect(addr1).withdraw(addr1.address)
    ).to.be.revertedWith("Caller is not the owner");
  });

  it("Should allow owner to withdraw funds", async function () {
    // addr1 pledges 1 ETH
    await pledge.connect(addr1).pledge({ value: ethers.utils.parseEther("1") });

    // Contract balance should be 1 ETH
    expect(await ethers.provider.getBalance(pledge.address)).to.equal(
      ethers.utils.parseEther("1")
    );

    // Owner withdraws funds
    await pledge.withdraw(owner.address);

    // Contract balance should be 0
    expect(await ethers.provider.getBalance(pledge.address)).to.equal(0);
  });
});

// Hardhat deployment script (deploy.js)
async function main() {
  const PledgeContract = await ethers.getContractFactory("Pledge");
  const pledge = await PledgeContract.deploy();
  await pledge.deployed();

  console.log("Pledge Contract deployed to:", pledge.address);
}

// Error handling for the deployment script
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Error deploying the contract:", error);
    process.exit(1);
  });

// Example smart contract (Pledge.sol) for reference:
// pragma solidity ^0.8.0;
//
// contract Pledge {
//     address public owner;
//     mapping(address => uint256) public balances;
//
//     constructor() {
//         owner = msg.sender;
//     }
//
//     function pledge() external payable {
//         require(msg.value > 0, "Must send ETH to pledge");
//         balances[msg.sender] += msg.value;
//     }
//
//     function getBalance(address addr) external view returns (uint256) {
//         return balances[addr];
//     }
//
//     function withdraw(address payable to) external {
//         require(msg.sender == owner, "Caller is not the owner");
//         to.transfer(address(this).balance);
//     }
// }
```
