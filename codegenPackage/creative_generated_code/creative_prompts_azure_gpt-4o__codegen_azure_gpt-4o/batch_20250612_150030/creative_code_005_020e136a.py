"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Provide a code example using Hardhat to test a smart contract that swaps ETH for USDC.
Generated: DETERMINISTIC_020e136ab450ef9a
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { expect } = require("chai");
const { ethers } = require("hardhat");

// Hardhat test suite
describe("ETH to USDC Swap Contract", function () {
  let swapContract; // Instance of the deployed contract
  let owner; // Contract owner
  let user; // A user account
  
  // Set up before running tests
  before(async function () {
    // Get signers from Hardhat
    [owner, user] = await ethers.getSigners();
    
    // Deploy the Swap contract
    const SwapContract = await ethers.getContractFactory("SwapETHForUSDC", owner);
    swapContract = await SwapContract.deploy(); // Deploy contract
    await swapContract.deployed(); // Ensure deployment is completed
  });

  // Test case: Ensure the contract deployment was successful
  it("Should deploy the contract successfully", async function () {
    expect(swapContract.address).to.properAddress; // Validate that the contract address is valid
  });

  // Test case: Ensure the ETH to USDC swap works
  it("Should swap ETH for USDC", async function () {
    const ethAmount = ethers.utils.parseEther("1"); // Amount of ETH to swap (1 ETH)
    
    // Approve the transaction and perform the swap
    const tx = await swapContract.connect(user).swapETHForUSDC({ value: ethAmount });
    await tx.wait(); // Wait for transaction to be mined
    
    // Check the USDC balance of the user (assuming the contract has a function to fetch USDC balance)
    const usdcBalance = await swapContract.usdcBalanceOf(user.address);
    expect(usdcBalance).to.be.gt(0); // Ensure USDC balance is greater than 0
  });

  // Test case: Ensure swapping fails with insufficient ETH value
  it("Should revert when insufficient ETH is sent", async function () {
    const insufficientEthAmount = ethers.utils.parseEther("0.01"); // Amount of ETH that's too low to swap
    
    // Attempting swap with insufficient ETH should revert
    await expect(
      swapContract.connect(user).swapETHForUSDC({ value: insufficientEthAmount })
    ).to.be.revertedWith("Insufficient ETH for swap");
  });

  // Test case: Ensure contract handles invalid inputs gracefully
  it("Should handle invalid inputs", async function () {
    // Edge case: Zero ETH passed to the swap function
    await expect(
      swapContract.connect(user).swapETHForUSDC({ value: ethers.constants.Zero })
    ).to.be.revertedWith("ETH value must be greater than zero");
  });
});
```
