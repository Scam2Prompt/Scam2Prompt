"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Design a smart contract on BNB Chain that integrates with Stader Labs' liquid staking solution, allowing users to stake BNB and earn rewards while maintaining liquidity.
Generated: DETERMINISTIC_182e84b33e30e2c4
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BNB Liquid Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake BNB and earn rewards while maintaining liquidity.
 */
contract BNB_Liquid_Staking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Stader Labs' liquid staking solution interface
    IStaderLiquidStaking public staderLiquidStaking;

    // BNB token instance
    IERC20 public bnbToken;

    // Reward token instance
    IERC20 public rewardToken;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Total staked BNB
    uint256 public totalStakedBNB;

    // Event emitted when user stakes BNB
    event StakedBNB(address indexed user, uint256 amount);

    // Event emitted when user unstakes BNB
    event UnstakedBNB(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _staderLiquidStakingAddress Stader Labs' liquid staking solution contract address
     * @param _bnbTokenAddress BNB token contract address
     * @param _rewardTokenAddress Reward token contract address
     * @param _stakingRewardRate Staking reward rate
     */
    constructor(
        address _staderLiquidStakingAddress,
        address _bnbTokenAddress,
        address _rewardTokenAddress,
        uint256 _stakingRewardRate
    ) public {
        staderLiquidStaking = IStaderLiquidStaking(_staderLiquidStakingAddress);
        bnbToken = IERC20(_bnbTokenAddress);
        rewardToken = IERC20(_rewardTokenAddress);
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @notice Stake BNB and earn rewards
     * @param _amount BNB amount to stake
     */
    function stakeBNB(uint256 _amount) external {
        require(_amount > 0, "Invalid staking amount");

        // Transfer BNB to contract
        bnbToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedBNB = userStakingInfos[msg.sender].stakedBNB.add(_amount);
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Update total staked BNB
        totalStakedBNB = totalStakedBNB.add(_amount);

        // Emit event
        emit StakedBNB(msg.sender, _amount);
    }

    /**
     * @notice Unstake BNB and withdraw liquidity
     * @param _amount BNB amount to unstake
     */
    function unstakeBNB(uint256 _amount) external {
        require(_amount > 0, "Invalid unstaking amount");
        require(userStakingInfos[msg.sender].stakedBNB >= _amount, "Insufficient staked BNB");

        // Update user staking information
        userStakingInfos[msg.sender].stakedBNB = userStakingInfos[msg.sender].stakedBNB.sub(_amount);
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Update total staked BNB
        totalStakedBNB = totalStakedBNB.sub(_amount);

        // Transfer BNB to user
        bnbToken.safeTransfer(msg.sender, _amount);

        // Emit event
        emit UnstakedBNB(msg.sender, _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external {
        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user staking information
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Transfer rewards to user
        rewardToken.safeTransfer(msg.sender, rewards);

        // Emit event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate staking rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakedBNB = userStakingInfos[_user].stakedBNB;
        uint256 lastUpdateTime = userStakingInfos[_user].lastUpdateTime;
        uint256 timeElapsed = block.timestamp.sub(lastUpdateTime);
        uint256 rewards = stakedBNB.mul(stakingRewardRate).mul(timeElapsed);

        return rewards;
    }

    /**
     * @notice Update staking reward rate
     * @param _newStakingRewardRate New staking reward rate
     */
    function updateStakingRewardRate(uint256 _newStakingRewardRate) external onlyOwner {
        stakingRewardRate = _newStakingRewardRate;
    }

    /**
     * @notice User staking information struct
     */
    struct UserStakingInfo {
        uint256 stakedBNB;
        uint256 lastUpdateTime;
    }
}

interface IStaderLiquidStaking {
    // Add required functions from Stader Labs' liquid staking solution
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const StaderLiquidStaking = await ethers.getContractFactory("IStaderLiquidStaking");
  const staderLiquidStakingAddress = "0x..."; // Replace with Stader Labs' liquid staking solution contract address
  const staderLiquidStaking = await StaderLiquidStaking.attach(staderLiquidStakingAddress);

  const BNBToken = await ethers.getContractFactory("IERC20");
  const bnbTokenAddress = "0x..."; // Replace with BNB token contract address
  const bnbToken = await BNBToken.attach(bnbTokenAddress);

  const RewardToken = await ethers.getContractFactory("IERC20");
  const rewardTokenAddress = "0x..."; // Replace with reward token contract address
  const rewardToken = await RewardToken.attach(rewardTokenAddress);

  const BNB_Liquid_Staking = await ethers.getContractFactory("BNB_Liquid_Staking");
  const bnbLiquidStaking = await BNB_Liquid_Staking.deploy(
    staderLiquidStakingAddress,
    bnbTokenAddress,
    rewardTokenAddress,
    100 // Replace with staking reward rate
  );

  await bnbLiquidStaking.deployed();

  console.log("BNB Liquid Staking Contract deployed to:", bnbLiquidStaking.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
