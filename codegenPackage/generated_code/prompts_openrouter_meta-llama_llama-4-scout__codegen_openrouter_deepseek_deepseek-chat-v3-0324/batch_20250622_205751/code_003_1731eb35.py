"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Design a staking protocol for a cryptocurrency on both BSC and ETH chains, similar to the FEG Staking feature.
Generated: DETERMINISTIC_1731eb35a9e1ce2f
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Solidity Staking Contract for BSC and ETH Chains

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainStaking
 * @dev A staking contract that supports both BSC and ETH chains
 */
contract CrossChainStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // Token to be staked
    IERC20 public stakingToken;
    // Reward token (can be same as staking token)
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardDuration = 7 days;
    uint256 public lockDuration = 1 days;

    // Chain ID (1 for ETH, 56 for BSC)
    uint256 public chainId;

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event Recovered(address token, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _chainId Chain ID (1 for ETH, 56 for BSC)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _chainId
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        chainId = _chainId;
    }

    /**
     * @dev Modifier to update reward calculations
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
        }
        _;
    }

    /**
     * @dev Returns the last time reward was applicable
     */
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    /**
     * @dev Calculates the reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    /**
     * @dev Calculates the earned rewards for an account
     * @param account The address of the staker
     */
    function earned(address account) public view returns (uint256) {
        return
            (stakes[account].amount * (rewardPerToken() - stakes[account].rewardDebt)) /
            1e18;
    }

    /**
     * @dev Stake tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;
        totalStaked += amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(
            block.timestamp >= stakes[msg.sender].lastStakeTime + lockDuration,
            "Tokens are locked"
        );
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].rewardDebt = rewardPerToken();
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    /**
     * @dev Set the reward rate (only owner)
     * @param _rewardRate New reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Recover any ERC20 token sent to the contract (only owner)
     * @param tokenAddress Address of the token to recover
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
        emit Recovered(tokenAddress, tokenAmount);
    }

    /**
     * @dev Set the lock duration (only owner)
     * @param _lockDuration New lock duration in seconds
     */
    function setLockDuration(uint256 _lockDuration) external onlyOwner {
        lockDuration = _lockDuration;
    }

    /**
     * @dev Set the reward duration (only owner)
     * @param _rewardDuration New reward duration in seconds
     */
    function setRewardDuration(uint256 _rewardDuration) external onlyOwner {
        rewardDuration = _rewardDuration;
    }
}
```

## Deployment Script (JavaScript with Hardhat)

```javascript
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with the account:", deployer.address);
  
  // Configuration - replace with your token addresses
  const stakingTokenAddress = "0x..."; // Your token address
  const rewardTokenAddress = "0x...";  // Can be same as staking token
  const chainId = 56; // 1 for ETH, 56 for BSC
  
  const StakingContract = await ethers.getContractFactory("CrossChainStaking");
  const staking = await StakingContract.deploy(
    stakingTokenAddress,
    rewardTokenAddress,
    chainId
  );
  
  await staking.deployed();
  
  console.log("Staking contract deployed to:", staking.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

## Interface File (TypeScript)

```typescript
export interface StakingContract {
  stake(amount: string): Promise<any>;
  withdraw(amount: string): Promise<any>;
  getReward(): Promise<any>;
  exit(): Promise<any>;
  earned(address: string): Promise<string>;
  rewardPerToken(): Promise<string>;
  totalStaked(): Promise<string>;
  rewardRate(): Promise<string>;
  lockDuration(): Promise<string>;
}
```

## Test File (JavaScript with Hardhat)

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CrossChainStaking", function () {
  let stakingToken, rewardToken, staking;
  let owner, user1, user2;

  beforeEach(async function () {
    [owner, user1, user2] = await ethers.getSigners();
    
    // Deploy mock tokens
    const Token = await ethers.getContractFactory("ERC20Mock");
    stakingToken = await Token.deploy("Staking Token", "STK");
    rewardToken = await Token.deploy("Reward Token", "RWD");
    
    // Deploy staking contract
    const Staking = await ethers.getContract
