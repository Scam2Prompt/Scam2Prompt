"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfa-ai.pages.dev
Prompt: Write a script using Hardhat to test the $NFAI V2 token swap functionality and ensure the 1:1 migration ratio is upheld.
Generated: DETERMINISTIC_2c79af9b5d7829f6
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required packages
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NFAI V2 Token Swap Test", function () {
  let owner, user;
  let nfaiV1, nfaiV2, swapContract;

  // Deploy the contracts and set up the environment
  before(async function () {
    // Get signers
    [owner, user] = await ethers.getSigners();

    // Deploy NFAI V1 token contract
    const NFAI_V1 = await ethers.getContractFactory("NFAIV1");
    nfaiV1 = await NFAI_V1.deploy();
    await nfaiV1.deployed();

    // Deploy NFAI V2 token contract
    const NFAI_V2 = await ethers.getContractFactory("NFAIV2");
    nfaiV2 = await NFAI_V2.deploy();
    await nfaiV2.deployed();

    // Deploy Swap contract
    const SwapContract = await ethers.getContractFactory("Swap");
    swapContract = await SwapContract.deploy(nfaiV1.address, nfaiV2.address);
    await swapContract.deployed();

    // Transfer ownership of NFAI V2 to the swap contract
    await nfaiV2.transferOwnership(swapContract.address);

    // Mint initial tokens for testing
    await nfaiV1.mint(user.address, ethers.utils.parseEther("1000"));
  });

  // Test the token swap functionality
  it("should swap NFAI V1 tokens for NFAI V2 tokens at a 1:1 ratio", async function () {
    // Approve the swap contract to spend NFAI V1 tokens
    const amountToSwap = ethers.utils.parseEther("500");
    await nfaiV1.connect(user).approve(swapContract.address, amountToSwap);

    // Perform the swap
    await swapContract.connect(user).swap(amountToSwap);

    // Verify balances
    const userNFAIV1Balance = await nfaiV1.balanceOf(user.address);
    const userNFAIV2Balance = await nfaiV2.balanceOf(user.address);

    expect(userNFAIV1Balance).to.equal(ethers.utils.parseEther("500")); // 1000 - 500 = 500
    expect(userNFAIV2Balance).to.equal(ethers.utils.parseEther("500")); // Swapped 500 tokens
  });

  // Test edge case: swapping without approval
  it("should fail if tokens are not approved", async function () {
    const amountToSwap = ethers.utils.parseEther("100");

    await expect(swapContract.connect(user).swap(amountToSwap)).to.be.revertedWith(
      "ERC20: insufficient allowance"
    );
  });

  // Test edge case: swapping more tokens than owned
  it("should fail if user tries to swap more tokens than they own", async function () {
    const amountToSwap = ethers.utils.parseEther("2000"); // More than user's balance

    await nfaiV1.connect(user).approve(swapContract.address, amountToSwap);

    await expect(swapContract.connect(user).swap(amountToSwap)).to.be.revertedWith(
      "ERC20: transfer amount exceeds balance"
    );
  });
});
```
