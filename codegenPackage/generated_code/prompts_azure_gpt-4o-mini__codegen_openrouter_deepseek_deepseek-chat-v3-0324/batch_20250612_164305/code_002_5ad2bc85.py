"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Generate a code snippet that demonstrates how to tokenize shares of Spiko MMFs for storage in a wallet using Ethereum smart contracts.
Generated: DETERMINISTIC_5ad2bc85abbb05eb
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract that demonstrates tokenizing shares of Spiko MMFs using ERC-20 standards:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title SpikoMMFToken
 * @dev ERC20 token representing shares of Spiko Money Market Funds
 */
contract SpikoMMFToken is ERC20, Ownable, Pausable {
    /**
     * @dev Constructor that initializes the token with name and symbol
     * @param initialSupply Initial supply of tokens to be minted
     * @param name Name of the token
     * @param symbol Symbol of the token
     */
    constructor(
        uint256 initialSupply,
        string memory name,
        string memory symbol
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mints new tokens, only callable by owner
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens, only callable by owner
     * @param from Address whose tokens will be burned
     * @param amount Amount of tokens to burn
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     * @param from Address sending the tokens
     * @param to Address receiving the tokens
     * @param amount Amount of tokens being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        
        require(!paused(), "SpikoMMFToken: token transfer while paused");
    }
}
```

And here's a deployment script using Hardhat:

```javascript
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  
  const initialSupply = ethers.utils.parseUnits("1000000", 18); // 1 million tokens
  const tokenName = "Spiko MMF Share";
  const tokenSymbol = "SPIKO-MMF";

  const SpikoMMFToken = await ethers.getContractFactory("SpikoMMFToken");
  const token = await SpikoMMFToken.deploy(
    initialSupply,
    tokenName,
    tokenSymbol
  );

  await token.deployed();

  console.log("Token deployed to:", token.address);
  console.log(`Token details: ${await token.name()} (${await token.symbol()})`);
  console.log(`Initial supply: ${ethers.utils.formatUnits(initialSupply, 18)}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

And a test file:

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SpikoMMFToken", function () {
  let Token;
  let token;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();

    Token = await ethers.getContractFactory("SpikoMMFToken");
    token = await Token.deploy(
      ethers.utils.parseUnits("1000000", 18),
      "Spiko MMF Share",
      "SPIKO-MMF"
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
      await token.transfer(addr1.address, 50);
      expect(await token.balanceOf(addr1.address)).to.equal(50);

      await token.connect(addr1).transfer(addr2.address, 50);
      expect(await token.balanceOf(addr2.address)).to.equal(50);
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
  });

  describe("Minting and Burning", function () {
    it("Should mint new tokens", async function () {
      const initialSupply = await token.totalSupply();
      await token.mint(addr1.address, 100);
      expect(await token.totalSupply()).to.equal(initialSupply.add(100));
    });

    it("Should burn tokens", async function () {
      const initialSupply = await token.totalSupply();
      await token.burn(owner.address, 100);
      expect(await token.totalSupply()).to.equal(initialSupply.sub(100));
    });
  });

  describe("Pausable", function () {
    it("Should pause and unpause transfers", async function () {
      await token.pause();
      await expect(token.transfer(addr1.address, 50))
        .to.be.revertedWith("SpikoMMFToken: token transfer while paused");

      await token.unpause();
      await token.transfer(addr1.address, 50);
      expect(await token.balanceOf(addr1.address)).to.equal(50);
    });
  });
});
```
