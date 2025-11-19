"""
Generated Code Metadata:
========================
Original URL: https://roost-cys.pages.dev
Prompt: Write a script using Hardhat to simulate the allocation of $ROOST presale funds into liquidity pools and development expenses based on the 50/50 breakdown.
Generated: DETERMINISTIC_6940c1367a06dd6f
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RoostPresaleFundAllocator is Ownable {
    IERC20 public roostToken;
    address public liquidityPool;
    address public developmentFund;
    
    uint256 public constant ALLOCATION_PERCENTAGE = 50; // 50% to each
    
    event FundsAllocated(
        uint256 totalAmount,
        uint256 liquidityAmount,
        uint256 developmentAmount
    );

    constructor(
        address _roostToken,
        address _liquidityPool,
        address _developmentFund
    ) {
        require(_roostToken != address(0), "Invalid token address");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        require(_developmentFund != address(0), "Invalid development fund address");
        
        roostToken = IERC20(_roostToken);
        liquidityPool = _liquidityPool;
        developmentFund = _developmentFund;
    }

    function allocateFunds(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Amount must be greater than 0");
        
        uint256 liquidityAmount = (totalAmount * ALLOCATION_PERCENTAGE) / 100;
        uint256 developmentAmount = totalAmount - liquidityAmount;
        
        require(
            roostToken.transfer(liquidityPool, liquidityAmount),
            "Liquidity transfer failed"
        );
        
        require(
            roostToken.transfer(developmentFund, developmentAmount),
            "Development transfer failed"
        );
        
        emit FundsAllocated(totalAmount, liquidityAmount, developmentAmount);
    }

    function updateLiquidityPool(address _newPool) external onlyOwner {
        require(_newPool != address(0), "Invalid address");
        liquidityPool = _newPool;
    }

    function updateDevelopmentFund(address _newFund) external onlyOwner {
        require(_newFund != address(0), "Invalid address");
        developmentFund = _newFund;
    }
}
```

```javascript
const { ethers } = require("hardhat");
const { expect } = require("chai");

describe("RoostPresaleFundAllocator", function () {
  let RoostPresaleFundAllocator;
  let allocator;
  let roostToken;
  let owner, liquidityPool, developmentFund, otherAccount;

  before(async function () {
    [owner, liquidityPool, developmentFund, otherAccount] = await ethers.getSigners();
    
    // Deploy mock ROOST token
    const Token = await ethers.getContractFactory("ERC20Mock");
    roostToken = await Token.deploy("ROOST Token", "ROOST");
    await roostToken.deployed();
    
    // Mint tokens to allocator contract
    await roostToken.mint(owner.address, ethers.utils.parseEther("1000000"));
  });

  beforeEach(async function () {
    RoostPresaleFundAllocator = await ethers.getContractFactory("RoostPresaleFundAllocator");
    allocator = await RoostPresaleFundAllocator.deploy(
      roostToken.address,
      liquidityPool.address,
      developmentFund.address
    );
    await allocator.deployed();
    
    // Approve allocator to spend tokens
    await roostToken.connect(owner).approve(
      allocator.address,
      ethers.constants.MaxUint256
    );
  });

  it("Should deploy with correct parameters", async function () {
    expect(await allocator.roostToken()).to.equal(roostToken.address);
    expect(await allocator.liquidityPool()).to.equal(liquidityPool.address);
    expect(await allocator.developmentFund()).to.equal(developmentFund.address);
  });

  it("Should allocate funds 50/50", async function () {
    const amount = ethers.utils.parseEther("1000");
    
    await expect(allocator.connect(owner).allocateFunds(amount))
      .to.emit(allocator, "FundsAllocated")
      .withArgs(amount, amount.div(2), amount.div(2));
    
    const liquidityBalance = await roostToken.balanceOf(liquidityPool.address);
    const devBalance = await roostToken.balanceOf(developmentFund.address);
    
    expect(liquidityBalance).to.equal(amount.div(2));
    expect(devBalance).to.equal(amount.div(2));
  });

  it("Should reject allocation by non-owner", async function () {
    const amount = ethers.utils.parseEther("1000");
    await expect(
      allocator.connect(otherAccount).allocateFunds(amount)
    ).to.be.revertedWith("Ownable: caller is not the owner");
  });

  it("Should update liquidity pool address", async function () {
    await allocator.connect(owner).updateLiquidityPool(otherAccount.address);
    expect(await allocator.liquidityPool()).to.equal(otherAccount.address);
  });

  it("Should update development fund address", async function () {
    await allocator.connect(owner).updateDevelopmentFund(otherAccount.address);
    expect(await allocator.developmentFund()).to.equal(otherAccount.address);
  });

  it("Should reject zero amount allocation", async function () {
    await expect(
      allocator.connect(owner).allocateFunds(0)
    ).to.be.revertedWith("Amount must be greater than 0");
  });
});
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ERC20Mock is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}
    
    function mint(address account, uint256 amount) public {
        _mint(account, amount);
    }
    
    function burn(address account, uint256 amount) public {
        _burn(account, amount);
    }
}
```
