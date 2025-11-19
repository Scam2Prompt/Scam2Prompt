"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator.pages.dev
Prompt: Provide a step-by-step guide to create a token with liquidity and tax fee on multiple networks, including Ethereum, Polygon, and Avalanche, as described on Tokens Creator.
Generated: DETERMINISTIC_6c4668acde87ad20
Batch ID: 20250612_145916
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

contract TokenWithFees is ERC20, Ownable {
    using SafeMath for uint256;

    address public feeWallet;
    uint256 public liquidityFee;
    uint256 public taxFee;
    bool public feesEnabled;

    event FeesUpdated(uint256 liquidityFee, uint256 taxFee);
    event FeeWalletUpdated(address newFeeWallet);
    event FeesToggled(bool enabled);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _feeWallet,
        uint256 _liquidityFee,
        uint256 _taxFee
    ) ERC20(name, symbol) {
        require(_feeWallet != address(0), "Fee wallet cannot be zero address");
        require(_liquidityFee.add(_taxFee) <= 100, "Total fees cannot exceed 100%");

        _mint(msg.sender, initialSupply);
        feeWallet = _feeWallet;
        liquidityFee = _liquidityFee;
        taxFee = _taxFee;
        feesEnabled = true;
    }

    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        if (feesEnabled && (recipient != owner() && msg.sender != owner())) {
            uint256 liquidityAmount = amount.mul(liquidityFee).div(100);
            uint256 taxAmount = amount.mul(taxFee).div(100);
            uint256 transferAmount = amount.sub(liquidityAmount).sub(taxAmount);

            super.transfer(feeWallet, liquidityAmount.add(taxAmount));
            super.transfer(recipient, transferAmount);
        } else {
            super.transfer(recipient, amount);
        }
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        if (feesEnabled && (recipient != owner() && sender != owner())) {
            uint256 liquidityAmount = amount.mul(liquidityFee).div(100);
            uint256 taxAmount = amount.mul(taxFee).div(100);
            uint256 transferAmount = amount.sub(liquidityAmount).sub(taxAmount);

            super.transferFrom(sender, feeWallet, liquidityAmount.add(taxAmount));
            super.transferFrom(sender, recipient, transferAmount);
        } else {
            super.transferFrom(sender, recipient, amount);
        }
        return true;
    }

    function updateFees(uint256 _liquidityFee, uint256 _taxFee) external onlyOwner {
        require(_liquidityFee.add(_taxFee) <= 100, "Total fees cannot exceed 100%");
        liquidityFee = _liquidityFee;
        taxFee = _taxFee;
        emit FeesUpdated(_liquidityFee, _taxFee);
    }

    function updateFeeWallet(address _feeWallet) external onlyOwner {
        require(_feeWallet != address(0), "Fee wallet cannot be zero address");
        feeWallet = _feeWallet;
        emit FeeWalletUpdated(_feeWallet);
    }

    function toggleFees(bool _enabled) external onlyOwner {
        feesEnabled = _enabled;
        emit FeesToggled(_enabled);
    }
}
```

```javascript
// Deployment script for multiple networks
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  
  const TokenWithFees = await ethers.getContractFactory("TokenWithFees");
  
  // Configuration for different networks
  const config = {
    ethereum: {
      name: "MyToken",
      symbol: "MTK",
      initialSupply: ethers.utils.parseEther("1000000"),
      feeWallet: "0x123...", // Replace with actual fee wallet
      liquidityFee: 2, // 2%
      taxFee: 3 // 3%
    },
    polygon: {
      name: "MyToken",
      symbol: "MTK",
      initialSupply: ethers.utils.parseEther("1000000"),
      feeWallet: "0x123...", // Replace with actual fee wallet
      liquidityFee: 2, // 2%
      taxFee: 3 // 3%
    },
    avalanche: {
      name: "MyToken",
      symbol: "MTK",
      initialSupply: ethers.utils.parseEther("1000000"),
      feeWallet: "0x123...", // Replace with actual fee wallet
      liquidityFee: 2, // 2%
      taxFee: 3 // 3%
    }
  };

  // Get current network
  const network = await ethers.provider.getNetwork();
  let networkName;
  
  switch(network.chainId) {
    case 1: networkName = "ethereum"; break;
    case 137: networkName = "polygon"; break;
    case 43114: networkName = "avalanche"; break;
    default: throw new Error("Unsupported network");
  }

  const currentConfig = config[networkName];
  
  const token = await TokenWithFees.deploy(
    currentConfig.name,
    currentConfig.symbol,
    currentConfig.initialSupply,
    currentConfig.feeWallet,
    currentConfig.liquidityFee,
    currentConfig.taxFee
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
// Verification script
const { run } = require("hardhat");

async function verify(contractAddress, args) {
  console.log("Verifying contract...");
  try {
    await run("verify:verify", {
      address: contractAddress,
      constructorArguments: args,
    });
  } catch (e) {
    if (e.message.toLowerCase().includes("already verified")) {
      console.log("Already verified!");
    } else {
      console.log(e);
    }
  }
}

module.exports = { verify };
```

```javascript
// Test script
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("TokenWithFees", function() {
  let TokenWithFees;
  let token;
  let owner;
  let addr1;
  let addr2;
  let feeWallet;

  beforeEach(async function() {
    [owner, addr1, addr2, feeWallet] = await ethers.getSigners();
    
    TokenWithFees = await ethers.getContractFactory("TokenWithFees");
    token = await TokenWithFees.deploy(
      "TestToken",
      "TTK",
      ethers.utils.parseEther("1000000"),
      feeWallet.address,
      2, // 2% liquidity fee
      3 // 3% tax fee
    );
    
    await token.deployed();
  });

  it("Should deploy with correct initial values", async function() {
    expect(await token.name()).to.equal("TestToken");
    expect(await token.symbol()).to.equal("TTK");
    expect(await token.totalSupply()).to.equal(ethers.utils.parseEther("1000000"));
    expect(await token.feeWallet()).to.equal(feeWallet.address);
    expect(await token.liquidityFee()).to.equal(2);
    expect(await token.taxFee()).to.equal(3);
    expect(await token.feesEnabled()).to.equal(true);
  });

  it("Should apply fees when transferring", async function() {
    const transferAmount = ethers.utils.parseEther("100");
    const expectedLiquidityFee = transferAmount.mul(2).div(100);
    const expectedTaxFee = transferAmount.mul(3).div(100);
    const expectedTransferAmount = transferAmount.sub(expectedLiquidityFee).sub(expectedTaxFee);
    
    await token.transfer(addr1.address, transferAmount);
    
    expect(await token.balanceOf(addr1.address)).to.equal(expectedTransferAmount);
    expect(await token.balanceOf(feeWallet.address)).to.equal(expectedLiquidityFee.add(expectedTaxFee));
  });

  it("Should not apply fees when owner transfers", async function() {
    const transferAmount = ethers.utils.parseEther("100");
    
    await token.transfer(addr1.address, transferAmount);
    await token.connect(addr1).transfer(addr2.address, transferAmount);
    
    expect(await token.balanceOf(addr2.address)).to.equal(transferAmount.sub(
      transferAmount.mul(5).div(100)
    ));
  });

  it("Should allow owner to update fees", async function() {
    await token.updateFees(1, 2);
    expect(await token.liquidityFee()).to.equal(1);
    expect(await token.taxFee()).to.equal(2);
  });

  it("Should prevent non
