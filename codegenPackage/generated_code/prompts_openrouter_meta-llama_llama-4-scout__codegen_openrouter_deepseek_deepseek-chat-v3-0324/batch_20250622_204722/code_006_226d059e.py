"""
Generated Code Metadata:
========================
Original URL: https://saitachains.pages.dev
Prompt: "Develop a basic example of a cross-chain DeFi solution using SaitaChain, including smart contract code and deployment steps."
Generated: DETERMINISTIC_226d059e54d681cb
Batch ID: 20250622_204722
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainDeFi
 * @dev A basic cross-chain DeFi solution for SaitaChain
 */
contract CrossChainDeFi is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public totalDeposits;
    uint256 public rewardRate = 100; // 1% reward rate
    uint256 public constant PRECISION = 1e18;
    
    struct UserInfo {
        uint256 amount;
        uint256 lastUpdate;
    }
    
    mapping(address => UserInfo) public users;
    
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _token The ERC20 token address to be used
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }
    
    /**
     * @dev Deposit tokens into the contract
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        _updateRewards(msg.sender);
        
        users[msg.sender].amount += amount;
        totalDeposits += amount;
        
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Deposited(msg.sender, amount);
    }
    
    /**
     * @dev Withdraw tokens from the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(users[msg.sender].amount >= amount, "Insufficient balance");
        
        _updateRewards(msg.sender);
        
        users[msg.sender].amount -= amount;
        totalDeposits -= amount;
        
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        
        users[msg.sender].lastUpdate = block.timestamp;
        
        require(token.transfer(msg.sender, rewards), "Transfer failed");
        
        emit RewardsClaimed(msg.sender, rewards);
    }
    
    /**
     * @dev Calculate rewards for a user
     * @param user The user address
     * @return rewards The calculated rewards
     */
    function calculateRewards(address user) public view returns (uint256 rewards) {
        UserInfo memory userInfo = users[user];
        if (userInfo.amount == 0) return 0;
        
        uint256 timeElapsed = block.timestamp - userInfo.lastUpdate;
        rewards = (userInfo.amount * rewardRate * timeElapsed) / (PRECISION * 365 days);
    }
    
    /**
     * @dev Update user rewards
     * @param user The user address
     */
    function _updateRewards(address user) internal {
        uint256 rewards = calculateRewards(user);
        if (rewards > 0) {
            users[user].lastUpdate = block.timestamp;
        }
    }
    
    /**
     * @dev Set reward rate (only owner)
     * @param newRate The new reward rate
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 1000, "Rate too high"); // Max 10%
        rewardRate = newRate;
    }
    
    /**
     * @dev Recover ERC20 tokens (only owner)
     * @param tokenAddress The token address
     * @param amount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(token), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```

```javascript
// Deployment script (using Hardhat)
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  
  // Deploy token contract first (mock for testing)
  const Token = await ethers.getContractFactory("ERC20Mock");
  const token = await Token.deploy("Test Token", "TT", deployer.address, ethers.utils.parseEther("1000000"));
  await token.deployed();
  
  console.log("Token deployed to:", token.address);
  
  // Deploy CrossChainDeFi contract
  const CrossChainDeFi = await ethers.getContractFactory("CrossChainDeFi");
  const defi = await CrossChainDeFi.deploy(token.address);
  await defi.deployed();
  
  console.log("CrossChainDeFi deployed to:", defi.address);
  
  // Approve tokens for testing
  await token.approve(defi.address, ethers.utils.parseEther("1000"));
  console.log("Approved tokens for CrossChainDeFi contract");
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

describe("CrossChainDeFi", function () {
  let token, defi;
  let owner, user1;

  beforeEach(async function () {
    [owner, user1] = await ethers.getSigners();
    
    const Token = await ethers.getContractFactory("ERC20Mock");
    token = await Token.deploy("Test Token", "TT", owner.address, ethers.utils.parseEther("1000000"));
    
    const CrossChainDeFi = await ethers.getContractFactory("CrossChainDeFi");
    defi = await CrossChainDeFi.deploy(token.address);
    
    // Transfer some tokens to user1 for testing
    await token.transfer(user1.address, ethers.utils.parseEther("1000"));
  });

  it("Should deploy successfully", async function () {
    expect(await defi.token()).to.equal(token.address);
  });

  it("Should allow deposits and withdrawals", async function () {
    await token.connect(user1).approve(defi.address, ethers.utils.parseEther("100"));
    
    // Deposit
    await defi.connect(user1).deposit(ethers.utils.parseEther("50"));
    expect(await defi.users(user1.address)).to.have.property("amount", ethers.utils.parseEther("50"));
    
    // Withdraw
    await defi.connect(user1).withdraw(ethers.utils.parseEther("20"));
    expect(await defi.users(user1.address)).to.have.property("amount", ethers.utils.parseEther("30"));
  });

  it("Should calculate rewards correctly", async function () {
    await token.connect(user1).approve(defi.address, ethers.utils.parseEther("100"));
    await defi.connect(user1).deposit(ethers.utils.parseEther("100"));
    
    // Fast forward time
    await ethers.provider.send("evm_increaseTime", [86400]); // 1 day
    await ethers.provider.send("evm_mine");
    
    const rewards = await defi.calculateRewards(user1.address);
    expect(rewards).to.be.closeTo(ethers.utils.parseEther("0.002739"), ethers.utils.parseEther("0.000001"));
  });

  it("Should allow reward claims", async function () {
    await token.connect(user1).approve(defi.address, ethers.utils.parseEther("100"));
    await defi.connect(user1).deposit(ethers.utils.parseEther("100"));
    
    await ethers.provider.send("evm_increaseTime", [86400]); // 1 day
    await ethers.provider.send("evm_mine");
    
    const balanceBefore = await token.balanceOf(user1.address);
    await defi.connect(user1).claimRewards();
    const balanceAfter = await token.balanceOf(user1.address);
    
    expect(balanceAfter.sub(balanceBefore)).to.be.closeTo(ethers.utils.parseEther("0.002739"), ethers.utils.parseEther("0.000001"));
  });
});
```
