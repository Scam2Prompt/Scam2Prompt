"""
Generated Code Metadata:
========================
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Create a tutorial for deploying a Deadpool Inu-inspired ERC-20 token on the Ethereum blockchain, emphasizing branding elements like humor and nostalgia.
Generated: DETERMINISTIC_40975c25a87800a3
Batch ID: 20250612_145715
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeadpoolInuToken
 * @dev ERC20 token with Deadpool-inspired branding elements
 * Features:
 * - Custom token name and symbol
 * - Initial supply minting
 * - Ownership control
 * - Humorous and nostalgic branding elements
 */
contract DeadpoolInuToken is ERC20, Ownable {
    uint256 private constant INITIAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    
    /**
     * @dev Constructor that mints initial supply to contract deployer
     * Sets token name and symbol with Deadpool-inspired branding
     */
    constructor() ERC20("Deadpool Inu", "DPINU") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Override decimals to standard 18
     */
    function decimals() public view virtual override returns (uint8) {
        return 18;
    }

    /**
     * @dev Mint new tokens - only owner can call
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens - any holder can burn their own tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Special transfer function with Deadpool-style message
     * @param recipient Address to send tokens to
     * @param amount Amount of tokens to send
     * @return bool Whether transfer was successful
     */
    function chimichangaTransfer(address recipient, uint256 amount) public returns (bool) {
        require(amount > 0, "DPINU: Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "DPINU: Insufficient balance");
        
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override transfer with custom message
     * @param recipient Address to send tokens to
     * @param amount Amount of tokens to send
     * @return bool Whether transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "DPINU: You can't send zero, that's just sad");
        require(balanceOf(msg.sender) >= amount, "DPINU: Not enough DPINU to make it rain");
        
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override transferFrom with custom message
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to send
     * @return bool Whether transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(amount > 0, "DPINU: Zero? Really? That's your offer?");
        require(balanceOf(sender) >= amount, "DPINU: Sender needs more DPINU in their life");
        require(allowance(sender, msg.sender) >= amount, "DPINU: Not approved - ask nicely first");
        
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```

```javascript
// Deployment script using Hardhat
const hre = require("hardhat");

async function main() {
  // Get the contract factory
  const DeadpoolInuToken = await hre.ethers.getContractFactory("DeadpoolInuToken");
  
  // Deploy the contract
  const deadpoolInu = await DeadpoolInuToken.deploy();
  
  await deadpoolInu.deployed();
  
  console.log("Deadpool Inu Token deployed to:", deadpoolInu.address);
  
  // Verify contract on Etherscan
  if (hre.network.name !== "hardhat") {
    console.log("Waiting for 5 block confirmations...");
    await deadpoolInu.deployTransaction.wait(5);
    
    console.log("Verifying contract on Etherscan...");
    await hre.run("verify:verify", {
      address: deadpoolInu.address,
      constructorArguments: [],
    });
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Test script for DeadpoolInuToken
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("DeadpoolInuToken", function () {
  let DeadpoolInuToken, deadpoolInu, owner, addr1, addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    
    DeadpoolInuToken = await ethers.getContractFactory("DeadpoolInuToken");
    deadpoolInu = await DeadpoolInuToken.deploy();
    await deadpoolInu.deployed();
  });

  describe("Deployment", function () {
    it("Should set the correct name and symbol", async function () {
      expect(await deadpoolInu.name()).to.equal("Deadpool Inu");
      expect(await deadpoolInu.symbol()).to.equal("DPINU");
    });

    it("Should assign the total supply of tokens to the owner", async function () {
      const ownerBalance = await deadpoolInu.balanceOf(owner.address);
      expect(await deadpoolInu.totalSupply()).to.equal(ownerBalance);
    });
  });

  describe("Transactions", function () {
    it("Should transfer tokens between accounts", async function () {
      await deadpoolInu.transfer(addr1.address, 100);
      const addr1Balance = await deadpoolInu.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(100);

      await deadpoolInu.connect(addr1).transfer(addr2.address, 50);
      const addr2Balance = await deadpoolInu.balanceOf(addr2.address);
      expect(addr2Balance).to.equal(50);
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const initialOwnerBalance = await deadpoolInu.balanceOf(owner.address);

      await expect(
        deadpoolInu.connect(addr1).transfer(owner.address, 1)
      ).to.be.revertedWith("DPINU: Not enough DPINU to make it rain");

      expect(await deadpoolInu.balanceOf(owner.address)).to.equal(
        initialOwnerBalance
      );
    });

    it("Should update balances after transfers", async function () {
      const initialOwnerBalance = await deadpoolInu.balanceOf(owner.address);

      await deadpoolInu.transfer(addr1.address, 100);
      await deadpoolInu.transfer(addr2.address, 50);

      const finalOwnerBalance = await deadpoolInu.balanceOf(owner.address);
      expect(finalOwnerBalance).to.equal(initialOwnerBalance.sub(150));

      const addr1Balance = await deadpoolInu.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(100);

      const addr2Balance = await deadpoolInu.balanceOf(addr2.address);
      expect(addr2Balance).to.equal(50);
    });

    it("Should allow chimichanga transfers", async function () {
      await deadpoolInu.chimichangaTransfer(addr1.address, 100);
      const addr1Balance = await deadpoolInu.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(100);
    });
  });

  describe("Minting", function () {
    it("Should allow owner to mint new tokens", async function () {
      await deadpoolInu.mint(addr1.address, 1000);
      expect(await deadpoolInu.balanceOf(addr1.address)).to.equal(1000);
    });

    it("Should prevent non-owners from minting", async function () {
      await expect(
        deadpoolInu.connect(addr1).mint(addr1.address, 1000)
      ).to.be.revertedWith("Ownable: caller is not the owner");
    });
  });

  describe("Burning", function () {
    it("Should allow token holders to burn their tokens", async function () {
      await deadpoolInu.transfer(addr1.address, 100);
      await deadpoolInu.connect(addr1).burn(50);
      expect(await deadpoolInu.balanceOf(addr1.address)).to.equal(50);
    });

    it("Should prevent burning more tokens than balance
