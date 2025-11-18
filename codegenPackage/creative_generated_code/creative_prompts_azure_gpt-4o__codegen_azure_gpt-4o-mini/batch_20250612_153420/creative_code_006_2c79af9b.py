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
// Import required dependencies
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NFAI Token Swap Test", function () {
    let owner, addr1, addr2;
    let nfaiv2, nfaiv1;

    // Deploy NFAI V1 and V2 contracts before each test
    beforeEach(async function () {
        // Get the signers
        [owner, addr1, addr2] = await ethers.getSigners();

        // Deploy NFAI V1 token contract
        const NFAIV1 = await ethers.getContractFactory("NFAIV1");
        nfaiv1 = await NFAIV1.deploy();
        await nfaiv1.deployed();

        // Deploy NFAI V2 token contract with the swap function
        const NFAIV2 = await ethers.getContractFactory("NFAIV2");
        nfaiv2 = await NFAIV2.deploy(nfaiv1.address);
        await nfaiv2.deployed();
    });

    // Test the token swap functionality
    it("Should swap NFAI V1 tokens for NFAI V2 tokens at a 1:1 ratio", async function () {
        // Mint some NFAI V1 tokens to the owner
        await nfaiv1.mint(owner.address, ethers.utils.parseEther("1000"));

        // Approve the NFAI V2 contract to spend NFAI V1 tokens
        await nfaiv1.approve(nfaiv2.address, ethers.utils.parseEther("1000"));

        // Perform the swap
        await nfaiv2.swapTokens(ethers.utils.parseEther("1000"));

        // Check the balances after swap
        const v1BalanceOwner = await nfaiv1.balanceOf(owner.address);
        const v2BalanceOwner = await nfaiv2.balanceOf(owner.address);

        // Assert that the NFAI V1 balance is now 0
        expect(v1BalanceOwner).to.equal(ethers.constants.Zero);

        // Assert that the NFAI V2 balance is 1000
        expect(v2BalanceOwner).to.equal(ethers.utils.parseEther("1000"));
    });

    // Test to ensure that the swap can only happen once per address
    it("Should revert if trying to swap more than once", async function () {
        // Mint some NFAI V1 tokens to the owner
        await nfaiv1.mint(owner.address, ethers.utils.parseEther("1000"));

        // Approve the NFAI V2 contract to spend NFAI V1 tokens
        await nfaiv1.approve(nfaiv2.address, ethers.utils.parseEther("1000"));

        // Perform the swap
        await nfaiv2.swapTokens(ethers.utils.parseEther("1000"));

        // Try to perform the swap again and expect to revert
        await expect(nfaiv2.swapTokens(ethers.utils.parseEther("1000"))).to.be.revertedWith("Already swapped");
    });

    // Test for insufficient NFAI V1 balance
    it("Should revert if trying to swap more than available NFAI V1 tokens", async function () {
        // Mint less NFAI V1 tokens
        await nfaiv1.mint(owner.address, ethers.utils.parseEther("500"));

        // Approve the NFAI V2 contract to spend NFAI V1 tokens
        await nfaiv1.approve(nfaiv2.address, ethers.utils.parseEther("500"));

        // Try to perform the swap with more tokens than available
        await expect(nfaiv2.swapTokens(ethers.utils.parseEther("1000"))).to.be.revertedWith("Insufficient NFAI V1 balance");
    });

    // Test for improper approval
    it("Should revert if no NFAI V1 tokens are approved", async function () {
        // Mint some NFAI V1 tokens to the owner
        await nfaiv1.mint(owner.address, ethers.utils.parseEther("1000"));

        // Do not approve any tokens

        // Try to perform the swap and expect to revert
        await expect(nfaiv2.swapTokens(ethers.utils.parseEther("1000"))).to.be.revertedWith("No allowance for NFAI V1 tokens");
    });
});
```

**Note:** This script assumes you have already defined the `NFAIV1` and `NFAIV2` smart contracts with methods such as `mint`, `approve`, and `swapTokens`. Make sure your contracts include the necessary checks and proper events for production readiness.
