"""
Generated Code Metadata:
========================
Original URL: https://berachain.pumpevm.net
Prompt: "Create a simple blockchain-based token using BeraChain's technology and PumpEVM's smart contract functionality."
Generated: DETERMINISTIC_eacb076b6f667a23
Batch ID: 20250622_211811
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
 * @title SimpleToken
 * @dev A simple ERC20 token implementation with minting functionality
 *      for BeraChain/PumpEVM compatibility.
 */
contract SimpleToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with a name, symbol, and initial supply.
     * @param name_ The name of the token
     * @param symbol_ The symbol of the token
     * @param initialSupply The initial supply of tokens to mint
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mints new tokens and assigns them to the specified address.
     *      Only the contract owner can call this function.
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's account.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Overrides the transfer function to include additional checks.
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        returns (bool) 
    {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }
}
```

```javascript
// Hardhat deployment script for SimpleToken
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const SimpleToken = await ethers.getContractFactory("SimpleToken");
  const token = await SimpleToken.deploy(
    "SimpleToken",   // Name
    "STK",           // Symbol
    ethers.utils.parseEther("1000000")  // Initial supply (1 million tokens)
  );

  await token.deployed();

  console.log("Token deployed to:", token.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Hardhat test script for SimpleToken
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SimpleToken", function () {
  let SimpleToken;
  let token;
  let owner;
  let addr1;
  let addr2;
  let addrs;

  beforeEach(async function () {
    [owner, addr1, addr2, ...addrs] = await ethers.getSigners();

    SimpleToken = await ethers.getContractFactory("SimpleToken");
    token = await SimpleToken.deploy(
      "SimpleToken",
      "STK",
      ethers.utils.parseEther("1000000")
    );
  });

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      expect(await token.owner()).to.equal(owner.address);
    });

    it("Should assign the total supply of tokens to the owner", async function () {
      const ownerBalance = await token.balanceOf(owner.address);
      expect(await token.totalSupply()).to.equal(ownerBalance);
    });
  });

  describe("Transactions", function () {
    it("Should transfer tokens between accounts", async function () {
      await token.transfer(addr1.address, 100);
      const addr1Balance = await token.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(100);

      await token.connect(addr1).transfer(addr2.address, 50);
      const addr2Balance = await token.balanceOf(addr2.address);
      expect(addr2Balance).to.equal(50);
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const initialOwnerBalance = await token.balanceOf(owner.address);

      await expect(
        token.connect(addr1).transfer(owner.address, 1)
      ).to.be.revertedWith("ERC20: transfer amount exceeds balance");

      expect(await token.balanceOf(owner.address)).to.equal(
        initialOwnerBalance
      );
    });

    it("Should update balances after transfers", async function () {
      const initialOwnerBalance = await token.balanceOf(owner.address);

      await token.transfer(addr1.address, 100);
      await token.transfer(addr2.address, 50);

      const finalOwnerBalance = await token.balanceOf(owner.address);
      expect(finalOwnerBalance).to.equal(initialOwnerBalance.sub(150));

      const addr1Balance = await token.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(100);

      const addr2Balance = await token.balanceOf(addr2.address);
      expect(addr2Balance).to.equal(50);
    });
  });

  describe("Minting", function () {
    it("Should mint new tokens", async function () {
      const initialSupply = await token.totalSupply();
      await token.mint(addr1.address, 1000);
      expect(await token.totalSupply()).to.equal(initialSupply.add(1000));
      expect(await token.balanceOf(addr1.address)).to.equal(1000);
    });

    it("Should fail if non-owner tries to mint", async function () {
      await expect(
        token.connect(addr1).mint(addr1.address, 1000)
      ).to.be.revertedWith("Ownable: caller is not the owner");
    });
  });

  describe("Burning", function () {
    it("Should burn tokens", async function () {
      await token.transfer(addr1.address, 100);
      const initialBalance = await token.balanceOf(addr1.address);
      await token.connect(addr1).burn(50);
      expect(await token.balanceOf(addr1.address)).to.equal(initialBalance.sub(50));
    });

    it("Should fail if trying to burn more than balance", async function () {
      await expect(
        token.connect(addr1).burn(1)
      ).to.be.revertedWith("ERC20: burn amount exceeds balance");
    });
  });
});
```
