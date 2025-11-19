"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Generate a Solidity code snippet for a smart contract that distributes staking rewards to users over a period of two years, similar to the Dogecoin20 staking contract.
Generated: DETERMINISTIC_2e3bf8de35029879
Batch ID: 20250622_204740
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingRewardContract
 * @author [Your Name]
 * @notice Distributes staking rewards to users over a period of two years.
 */
contract StakingRewardContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStaking) public userStakings;

    // Mapping of reward distribution
    mapping (address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward amount
    uint256 public totalReward;

    // Reward distribution period in seconds (2 years)
    uint256 public constant REWARD_PERIOD = 63072000; // 2 years

    // Reward start timestamp
    uint256 public rewardStart;

    // ERC20 token contract
    ERC20 public token;

    /**
     * @param _token ERC20 token contract address
     * @param _totalReward Total reward amount
     */
    constructor(ERC20 _token, uint256 _totalReward) public {
        token = _token;
        totalReward = _totalReward;
        rewardStart = block.timestamp;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakings[msg.sender].stakedAmount = userStakings[msg.sender].stakedAmount.add(_amount);
        userStakings[msg.sender].stakedAt = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external nonReentrant {
        // Get user staking information
        UserStaking memory userStaking = userStakings[msg.sender];

        // Check if user has staked
        require(userStaking.stakedAmount > 0, "User has not staked");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update user reward
        rewards[msg.sender] = reward;

        // Transfer staked tokens and reward to user
        token.transfer(msg.sender, userStaking.stakedAmount.add(reward));

        // Reset user staking information
        userStakings[msg.sender].stakedAmount = 0;
        userStakings[msg.sender].stakedAt = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(userStaking.stakedAmount);
    }

    /**
     * @notice Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Get user staking information
        UserStaking memory userStaking = userStakings[_user];

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp.sub(userStaking.stakedAt);

        // Check if staking duration is within reward period
        if (stakingDuration > REWARD_PERIOD) {
            stakingDuration = REWARD_PERIOD;
        }

        // Calculate reward
        uint256 reward = userStaking.stakedAmount.mul(stakingDuration).mul(totalReward).div(REWARD_PERIOD).div(totalStaked);

        return reward;
    }

    /**
     * @dev Struct for user staking information
     */
    struct UserStaking {
        uint256 stakedAmount;
        uint256 stakedAt;
    }
}
```
