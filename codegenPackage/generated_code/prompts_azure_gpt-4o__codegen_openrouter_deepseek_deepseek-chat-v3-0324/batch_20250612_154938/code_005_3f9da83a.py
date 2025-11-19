"""
Generated Code Metadata:
========================
Original URL: https://riarus.ru
Prompt: Create a smart contract in Solidity that interacts with Perpetual Protocol's staking mechanism to automate staking and reward distribution for PERP token holders.
Generated: DETERMINISTIC_3f9da83a2804e99a
Batch ID: 20250612_154938
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IPerpStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimReward() external;
    function getReward(address account) external view returns (uint256);
}

contract PerpStakingAutomator is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable perpToken;
    IPerpStaking public immutable perpStaking;

    // Track user balances
    mapping(address => uint256) public userStakedBalance;
    uint256 public totalStaked;

    // Reward distribution variables
    uint256 public lastRewardDistribution;
    uint256 public rewardDistributionInterval = 7 days;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardDistributed(uint256 totalAmount);

    constructor(address _perpToken, address _perpStaking) {
        require(_perpToken != address(0), "Invalid PERP token address");
        require(_perpStaking != address(0), "Invalid staking contract address");
        
        perpToken = IERC20(_perpToken);
        perpStaking = IPerpStaking(_perpStaking);
    }

    /**
     * @notice Stake PERP tokens into the Perpetual Protocol staking contract
     * @param amount Amount of PERP tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer PERP tokens from user to this contract
        perpToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Approve and stake in Perpetual Protocol
        perpToken.approve(address(perpStaking), amount);
        perpStaking.stake(amount);
        
        // Update balances
        userStakedBalance[msg.sender] += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake PERP tokens from the Perpetual Protocol staking contract
     * @param amount Amount of PERP tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userStakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        
        // Unstake from Perpetual Protocol
        perpStaking.unstake(amount);
        
        // Transfer PERP tokens back to user
        perpToken.safeTransfer(msg.sender, amount);
        
        // Update balances
        userStakedBalance[msg.sender] -= amount;
        totalStaked -= amount;
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards for a user
     */
    function claimReward() external nonReentrant {
        uint256 reward = perpStaking.getReward(address(this));
        require(reward > 0, "No rewards to claim");
        
        perpStaking.claimReward();
        perpToken.safeTransfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Distribute rewards to all stakers (can be called by anyone after interval)
     */
    function distributeRewards() external nonReentrant {
        require(block.timestamp >= lastRewardDistribution + rewardDistributionInterval, 
                "Reward distribution too soon");
        
        uint256 totalReward = perpStaking.getReward(address(this));
        require(totalReward > 0, "No rewards to distribute");
        
        perpStaking.claimReward();
        lastRewardDistribution = block.timestamp;
        
        emit RewardDistributed(totalReward);
    }

    /**
     * @notice Set reward distribution interval (owner only)
     * @param interval New interval in seconds
     */
    function setRewardDistributionInterval(uint256 interval) external onlyOwner {
        require(interval > 0, "Interval must be greater than 0");
        rewardDistributionInterval = interval;
    }

    /**
     * @notice Emergency withdraw stuck tokens (owner only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
