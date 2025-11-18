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
// Import necessary dependencies
const { ethers } = require("hardhat");
const { expect } = require("chai");

// Define the contract to be tested
describe("ETH to USDC Swapper", function () {
    let ethToUsdcSwapper;
    let usdcToken;
    let owner, addr1, addr2;

    // Deploy contracts before each test
    beforeEach(async function () {
        // Get signers
        [owner, addr1, addr2] = await ethers.getSigners();

        // Deploy USDC mock token
        const USDC = await ethers.getContractFactory("MockUSDC");
        usdcToken = await USDC.deploy();
        await usdcToken.deployed();

        // Deploy the ETH to USDC swapper contract
        const EthToUsdcSwapper = await ethers.getContractFactory("EthToUsdcSwapper");
        ethToUsdcSwapper = await EthToUsdcSwapper.deploy(usdcToken.address);
        await ethToUsdcSwapper.deployed();
    });

    // Test the swap function
    it("should swap ETH for USDC", async function () {
        const swapAmount = ethers.utils.parseEther("1"); // 1 ETH
        
        // Approve the swapper to spend USDC on behalf of the owner
        await usdcToken.mint(owner.address, ethers.utils.parseUnits("1000", 6)); // Mint 1000 USDC
        await usdcToken.approve(ethToUsdcSwapper.address, ethers.utils.parseUnits("1000", 6));

        // Perform the swap
        const tx = await ethToUsdcSwapper.connect(addr1).swap({ value: swapAmount });
        await tx.wait();

        // Check USDC balance of the addr1
        const usdcBalance = await usdcToken.balanceOf(addr1.address);
        expect(usdcBalance).to.equal(ethers.utils.parseUnits("1000", 6)); // Ensure 1000 USDC is received

        // Check the contract's balance
        const contractBalance = await ethers.provider.getBalance(ethToUsdcSwapper.address);
        expect(contractBalance).to.equal(swapAmount); // Ensure the contract holds the swapped ETH
    });

    // Test for insufficient funds
    it("should revert if insufficient ETH is provided", async function () {
        const swapAmount = ethers.utils.parseEther("0.1"); // Set a small amount for testing
        
        // Attempt to swap with insufficient ETH and expect a revert
        await expect(
            ethToUsdcSwapper.connect(addr2).swap({ value: 0 }) // Sending 0 ETH
        ).to.be.revertedWith("Insufficient ETH sent for swap");
    });

    // Test for correct event emission
    it("should emit SwapExecuted event upon successful swap", async function () {
        const swapAmount = ethers.utils.parseEther("1"); // 1 ETH

        // Listen to the event
        await expect(
            ethToUsdcSwapper.connect(addr1).swap({ value: swapAmount })
        ).to.emit(ethToUsdcSwapper, "SwapExecuted")
         .withArgs(addr1.address, swapAmount);
    });
});
```

*Note: Make sure to define the `EthToUsdcSwapper` and `MockUSDC` contracts with proper logic and the `SwapExecuted` event in the contract for this test to work as expected.*
