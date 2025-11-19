"""
Generated Code Metadata:
========================
Original URL: https://angelwings.pages.dev
Prompt: Write a step-by-step guide for deploying a token contract similar to "Pepe 2.0" on the Ethereum blockchain.
Generated: DETERMINISTIC_d1933dab39c74bb6
Batch ID: 20250612_151329
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PepeTwoPointOh is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 420690000000000 * 10**18; // 420.69 trillion tokens
    uint256 public constant INITIAL_SUPPLY = 210345000000000 * 10**18; // 50% of max supply
    uint256 public constant TAX_PERCENTAGE = 5; // 5% tax on transfers
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Excluded addresses from tax (e.g., owner, staking contracts)
    mapping(address => bool) private _isExcludedFromTax;

    constructor() ERC20("Pepe 2.0", "PEPE2.0") {
        _mint(msg.sender, INITIAL_SUPPLY);
        _isExcludedFromTax[msg.sender] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (_isExcludedFromTax[_msgSender()] || _isExcludedFromTax[recipient]) {
            _transfer(_msgSender(), recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENTAGE).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            _transfer(_msgSender(), recipient, transferAmount);
            _transfer(_msgSender(), BURN_ADDRESS, taxAmount);
        }
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENTAGE).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            _transfer(sender, recipient, transferAmount);
            _transfer(sender, BURN_ADDRESS, taxAmount);
        }
        
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance.sub(amount));
        
        return true;
    }

    function excludeFromTax(address account) external onlyOwner {
        require(!_isExcludedFromTax[account], "Account is already excluded");
        _isExcludedFromTax[account] = true;
    }

    function includeInTax(address account) external onlyOwner {
        require(_isExcludedFromTax[account], "Account is already included");
        _isExcludedFromTax[account] = false;
    }

    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }
}
```

```javascript
// Deployment script using Hardhat
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString());

  const PepeTwoPointOh = await ethers.getContractFactory("PepeTwoPointOh");
  const pepeToken = await PepeTwoPointOh.deploy();
  
  await pepeToken.deployed();
  console.log("Pepe 2.0 Token deployed to:", pepeToken.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Test script using Hardhat/Waffle
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PepeTwoPointOh", function () {
  let PepeTwoPointOh;
  let pepeToken;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    PepeTwoPointOh = await ethers.getContractFactory("PepeTwoPointOh");
    pepeToken = await PepeTwoPointOh.deploy();
  });

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      expect(await pepeToken.owner()).to.equal(owner.address);
    });

    it("Should assign the initial supply to the owner", async function () {
      const ownerBalance = await pepeToken.balanceOf(owner.address);
      expect(await pepeToken.totalSupply()).to.equal(ownerBalance);
    });
  });

  describe("Transactions", function () {
    it("Should transfer tokens between accounts with tax", async function () {
      const transferAmount = ethers.utils.parseEther("1000");
      const expectedReceived = transferAmount.mul(95).div(100);
      const expectedTax = transferAmount.mul(5).div(100);

      await pepeToken.transfer(addr1.address, transferAmount);
      const addr1Balance = await pepeToken.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(expectedReceived);

      const burnBalance = await pepeToken.balanceOf("0x000000000000000000000000000000000000dEaD");
      expect(burnBalance).to.equal(expectedTax);
    });

    it("Should not apply tax to excluded accounts", async function () {
      await pepeToken.excludeFromTax(owner.address);
      const transferAmount = ethers.utils.parseEther("1000");
      
      await pepeToken.transfer(addr1.address, transferAmount);
      const addr1Balance = await pepeToken.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(transferAmount);
    });

    it("Should fail if trying to mint more than max supply", async function () {
      const maxSupply = await pepeToken.MAX_SUPPLY();
      const currentSupply = await pepeToken.totalSupply();
      const excessAmount = maxSupply.sub(currentSupply).add(1);
      
      await expect(pepeToken.mint(owner.address, excessAmount))
        .to.be.revertedWith("Exceeds max supply");
    });
  });
});
```
