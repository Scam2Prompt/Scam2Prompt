"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.vip
Prompt: Suggest tools or frameworks for testing ERC-20 token contracts on Ethereum, with a focus on JavaScript-based environments.
Generated: DETERMINISTIC_f2011d0c6db58664
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Testing ERC-20 Token Contracts in Ethereum Using JavaScript-based Frameworks

// Import required libraries
const { expect } = require('chai');
const { ethers } = require('hardhat');

/**
 * @dev Main function to deploy and test ERC-20 token contract.
 */
async function main() {
    // Deploy the ERC20 token contract
    const Token = await ethers.getContractFactory("MyERC20Token");
    const token = await Token.deploy("MyToken", "MTK", 1000000);
  
    // Wait for deployment to complete
    await token.deployed();
    console.log("Token deployed to:", token.address);

    // Run tests
    await runTests(token);
}

/**
 * @dev Function to run various tests on the deployed ERC-20 token contract.
 * @param {Object} token - The deployed token contract instance.
 */
async function runTests(token) {
    // Test name retrieval
    it("Should return the correct name of the token", async () => {
        expect(await token.name()).to.equal("MyToken");
    });

    // Test symbol retrieval
    it("Should return the correct symbol of the token", async () => {
        expect(await token.symbol()).to.equal("MTK");
    });

    // Test total supply
    it("Should have the correct initial total supply", async () => {
        const totalSupply = await token.totalSupply();
        expect(totalSupply.toString()).to.equal("1000000");
    });

    // Test transferring tokens
    it("Should transfer tokens between accounts", async () => {
        const [owner, addr1] = await ethers.getSigners();

        // Transfer 50 tokens from owner to addr1
        await token.transfer(addr1.address, 50);
        const addr1Balance = await token.balanceOf(addr1.address);
        expect(addr1Balance.toString()).to.equal("50");

        // Check the remaining balance of the owner
        const ownerBalance = await token.balanceOf(owner.address);
        expect(ownerBalance.toString()).to.equal("999950");
    });

    // Test approval and transferFrom
    it("Should allow approved transfer of tokens", async () => {
        const [owner, addr1] = await ethers.getSigners();

        // Approve addr1 to spend 100 tokens
        await token.approve(addr1.address, 100);
        await token.connect(addr1).transferFrom(owner.address, addr1.address, 100);

        const addr1Balance = await token.balanceOf(addr1.address);
        expect(addr1Balance.toString()).to.equal("150");
    });
}

// Error handling for deployment failures
main().catch((error) => {
    console.error("Error deploying contract:", error);
    process.exit(1);
});
```

### Note:
The code assumes you have an ERC-20 Token contract named `MyERC20Token` with standard functions such as `name`, `symbol`, `totalSupply`, `transfer`, and `approve`. Make sure to adjust the contract name and methods as per your actual implementation.
