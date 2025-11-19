"""
Generated Code Metadata:
========================
Original URL: https://flash-stake.pages.dev
Prompt: Create a tutorial for deploying a DApp on Arbitrum that utilizes Flashstake to provide instant upfront yield functionality for stETH and GLP tokens.
Generated: DETERMINISTIC_6c6724c88f2d4f27
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IFlashstake {
    function stake(
        address principalToken,
        uint256 amount,
        uint256 duration,
        uint256 minimumAmountOut
    ) external returns (uint256);
    
    function unstake(uint256 positionID) external returns (uint256);
    
    function getYield(
        address principalToken,
        uint256 amount,
        uint256 duration
    ) external view returns (uint256);
}

contract FlashstakeDApp is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;
    
    IFlashstake public flashstake;
    IERC20 public stETH;
    IERC20 public GLP;
    
    event Staked(address indexed user, address token, uint256 amount, uint256 duration, uint256 positionID);
    event Unstaked(address indexed user, uint256 positionID, uint256 amount);
    
    constructor(
        address _flashstake,
        address _stETH,
        address _GLP
    ) {
        require(_flashstake != address(0), "Invalid Flashstake address");
        require(_stETH != address(0), "Invalid stETH address");
        require(_GLP != address(0), "Invalid GLP address");
        
        flashstake = IFlashstake(_flashstake);
        stETH = IERC20(_stETH);
        GLP = IERC20(_GLP);
    }
    
    function stakeStETH(
        uint256 amount,
        uint256 duration,
        uint256 minimumAmountOut
    ) external nonReentrant returns (uint256) {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        
        stETH.safeTransferFrom(msg.sender, address(this), amount);
        stETH.safeApprove(address(flashstake), amount);
        
        uint256 positionID = flashstake.stake(
            address(stETH),
            amount,
            duration,
            minimumAmountOut
        );
        
        emit Staked(msg.sender, address(stETH), amount, duration, positionID);
        return positionID;
    }
    
    function stakeGLP(
        uint256 amount,
        uint256 duration,
        uint256 minimumAmountOut
    ) external nonReentrant returns (uint256) {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        
        GLP.safeTransferFrom(msg.sender, address(this), amount);
        GLP.safeApprove(address(flashstake), amount);
        
        uint256 positionID = flashstake.stake(
            address(GLP),
            amount,
            duration,
            minimumAmountOut
        );
        
        emit Staked(msg.sender, address(GLP), amount, duration, positionID);
        return positionID;
    }
    
    function unstake(uint256 positionID) external nonReentrant returns (uint256) {
        uint256 amount = flashstake.unstake(positionID);
        emit Unstaked(msg.sender, positionID, amount);
        return amount;
    }
    
    function getStETHYield(
        uint256 amount,
        uint256 duration
    ) external view returns (uint256) {
        return flashstake.getYield(address(stETH), amount, duration);
    }
    
    function getGLPYield(
        uint256 amount,
        uint256 duration
    ) external view returns (uint256) {
        return flashstake.getYield(address(GLP), amount, duration);
    }
    
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```

```javascript
// Deployment script (using Hardhat)
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  
  // Replace with actual addresses
  const FLASHSTAKE_ADDRESS = "0x...";
  const STETH_ADDRESS = "0x...";
  const GLP_ADDRESS = "0x...";
  
  const FlashstakeDApp = await ethers.getContractFactory("FlashstakeDApp");
  const flashstakeDApp = await FlashstakeDApp.deploy(
    FLASHSTAKE_ADDRESS,
    STETH_ADDRESS,
    GLP_ADDRESS
  );
  
  await flashstakeDApp.deployed();
  
  console.log("FlashstakeDApp deployed to:", flashstakeDApp.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Test script (using Hardhat)
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("FlashstakeDApp", function () {
  let FlashstakeDApp;
  let flashstakeDApp;
  let owner, user;
  
  const STETH_ADDRESS = "0x...";
  const GLP_ADDRESS = "0x...";
  
  before(async function () {
    [owner, user] = await ethers.getSigners();
    
    // Mock Flashstake contract
    const FlashstakeMock = await ethers.getContractFactory("FlashstakeMock");
    const flashstakeMock = await FlashstakeMock.deploy();
    await flashstakeMock.deployed();
    
    FlashstakeDApp = await ethers.getContractFactory("FlashstakeDApp");
    flashstakeDApp = await FlashstakeDApp.deploy(
      flashstakeMock.address,
      STETH_ADDRESS,
      GLP_ADDRESS
    );
    await flashstakeDApp.deployed();
  });
  
  describe("Staking", function () {
    it("Should stake stETH", async function () {
      // Test stETH staking
    });
    
    it("Should stake GLP", async function () {
      // Test GLP staking
    });
    
    it("Should fail with zero amount", async function () {
      // Test zero amount validation
    });
  });
  
  describe("Unstaking", function () {
    it("Should unstake position", async function () {
      // Test unstaking
    });
  });
  
  describe("Yield Calculation", function () {
    it("Should return stETH yield", async function () {
      // Test yield calculation for stETH
    });
    
    it("Should return GLP yield", async function () {
      // Test yield calculation for GLP
    });
  });
});
```

```javascript
// Frontend integration example (using ethers.js)
import { ethers } from "ethers";
import FlashstakeDAppABI from "./FlashstakeDAppABI.json";

const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

const FLASHSTAKE_DAPP_ADDRESS = "0x..."; // Replace with deployed address
const flashstakeDApp = new ethers.Contract(
  FLASHSTAKE_DAPP_ADDRESS,
  FlashstakeDAppABI,
  signer
);

async function stakeStETH(amount, duration, minimumAmountOut) {
  try {
    const tx = await flashstakeDApp.stakeStETH(
      ethers.utils.parseUnits(amount.toString(), 18),
      duration,
      ethers.utils.parseUnits(minimumAmountOut.toString(), 18)
    );
    await tx.wait();
    console.log("Staked successfully");
  } catch (error) {
    console.error("Staking failed:", error);
  }
}

async function getStETHYield(amount, duration) {
  try {
    const yield = await flashstakeDApp.getStETHYield(
      ethers.utils.parseUnits(amount.toString(), 18),
      duration
    );
    return ethers.utils.formatUnits(yield, 18);
  } catch (error) {
    console.error("Yield calculation failed:", error);
    return "0";
  }
}
```
