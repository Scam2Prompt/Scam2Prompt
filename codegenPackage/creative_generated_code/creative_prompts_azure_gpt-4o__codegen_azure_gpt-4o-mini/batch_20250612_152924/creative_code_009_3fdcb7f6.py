"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Recommend tools or frameworks for testing a cryptocurrency presale smart contract with specific constraints, such as a presale cap and token supply limit.
Generated: DETERMINISTIC_3fdcb7f61ec92389
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for testing
const { expect } = require("chai");
const { ethers } = require("hardhat");

// Describe the test suite for the cryptocurrency presale smart contract
describe("Presale Contract", function () {
    let Presale;
    let presale;
    let token;
    let owner;
    let addr1;
    let addr2;

    const PRESALE_CAP = ethers.utils.parseEther("100"); // Presale cap in ETH
    const TOKEN_SUPPLY_LIMIT = ethers.utils.parseUnits("10000", 18); // Token supply limit with 18 decimals

    // Before each test, deploy a new instance of the presale and token contracts
    beforeEach(async function () {
        // Get the ContractFactory and Signers
        [owner, addr1, addr2] = await ethers.getSigners();

        // Deploy the token contract
        const Token = await ethers.getContractFactory("Token");
        token = await Token.deploy(TOKEN_SUPPLY_LIMIT);
        await token.deployed();

        // Deploy the presale contract
        Presale = await ethers.getContractFactory("Presale");
        presale = await Presale.deploy(token.address, PRESALE_CAP);
        await presale.deployed();
    });

    // Test case: Check the initial state of the presale contract
    it("should have the correct initial state", async function () {
        expect(await presale.cap()).to.equal(PRESALE_CAP);
        expect(await presale.token()).to.equal(token.address);
        expect(await presale.totalRaised()).to.equal(0);
    });

    // Test case: Ensure that the presale caps the total raised amount
    it("should not allow contributions beyond the presale cap", async function () {
        // Simulate a contribution
        const contribution = ethers.utils.parseEther("50");
        await presale.connect(addr1).contribute({ value: contribution });

        // Try to exceed the presale cap
        const excessContribution = ethers.utils.parseEther("60");
        await expect(
            presale.connect(addr1).contribute({ value: excessContribution })
        ).to.be.revertedWith("Presale cap exceeded");
    });

    // Test case: Ensure the total raised amount does not exceed the cap
    it("should correctly track the total raised amount", async function () {
        await presale.connect(addr1).contribute({ value: ethers.utils.parseEther("30") });
        await presale.connect(addr2).contribute({ value: ethers.utils.parseEther("40") });

        expect(await presale.totalRaised()).to.equal(ethers.utils.parseEther("70"));
    });

    // Test case: Ensure tokens are distributed correctly after the presale ends
    it("should distribute tokens after the presale ends", async function () {
        await presale.connect(addr1).contribute({ value: ethers.utils.parseEther("30") });
        await presale.connect(addr2).contribute({ value: ethers.utils.parseEther("20") });

        // Simulate the end of the presale
        await presale.endPresale();

        // Check token balance after the presale
        const addr1Balance = await token.balanceOf(addr1.address);
        const addr2Balance = await token.balanceOf(addr2.address);

        expect(addr1Balance).to.be.greaterThan(0);
        expect(addr2Balance).to.be.greaterThan(0);
    });

    // Test case: Ensure users cannot contribute after the presale has ended
    it("should not allow contributions after the presale ends", async function () {
        await presale.connect(addr1).contribute({ value: ethers.utils.parseEther("30") });
        await presale.endPresale();

        await expect(
            presale.connect(addr2).contribute({ value: ethers.utils.parseEther("10") })
        ).to.be.revertedWith("Presale has ended");
    });
});
```

This code is a testing suite for a cryptocurrency presale smart contract using the Hardhat framework and Chai assertion library. It includes tests for the presale cap, token distribution, and proper handling of state transitions. Make sure to have the `Token` and `Presale` contract implementations ready for deployment to execute these tests properly.
