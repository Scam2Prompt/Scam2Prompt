"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levva.net
Prompt: Write a smart contract snippet that integrates with Levva's staking mechanism, enabling users to lock $LVVA tokens and automatically apply bonus rewards.
Generated: DETERMINISTIC_6ba881dcbe9337af
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Levva Staking Contract
 * @dev This contract allows users to lock $LVVA tokens and automatically apply bonus rewards.
 * It integrates with Levva's staking mechanism and ensures secure token management.
 */

interface ILevvaToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract LevvaStaking {
    // Address of the $LVVA token contract
    address public levvaTokenAddress;

    // Struct to store staking information for each user
    struct StakeInfo {
        uint256 amount;       // Amount of staked $LVVA tokens
        uint256 startTime;    // Timestamp when staking started
        uint256 reward;       // Bonus reward accumulated
    }

    // Mapping of user address to their staking info
    mapping(address => StakeInfo) public stakes;

    // Bonus reward rate (e.g., 5% annualized reward rate)
    uint256 public rewardRate; // per second rate
    uint256 public constant REWARD_DENOMINATOR = 1e18; // For precision

    // Events for logging staking activity
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    constructor(address _levvaTokenAddress, uint256 _rewardRate) {
        require(_levvaTokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        levvaTokenAddress = _levvaTokenAddress;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $LVVA tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer $LVVA tokens from the user to this contract
        ILevvaToken levvaToken = ILevvaToken(levvaTokenAddress);
        require(levvaToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        if (stakeInfo.amount > 0) {
            // Calculate pending rewards if user already has an active stake
            uint256 pendingReward = calculateReward(msg.sender);
            stakeInfo.reward += pendingReward;
        }

        stakeInfo.amount += _amount;
        stakeInfo.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens along with accumulated rewards.
     */
    function withdraw() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No active stake");

        // Calculate total reward and reset staking info
        uint256 totalReward = calculateReward(msg.sender) + stakeInfo.reward;
        uint256 stakedAmount = stakeInfo.amount;

        stakeInfo.amount = 0;
        stakeInfo.startTime = 0;
        stakeInfo.reward = 0;

        // Transfer staked tokens and rewards back to the user
        ILevvaToken levvaToken = ILevvaToken(levvaTokenAddress);
        require(levvaToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(levvaToken.transfer(msg.sender, totalReward), "Reward transfer failed");

        emit Withdrawn(msg.sender, stakedAmount, totalReward);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        StakeInfo memory stakeInfo = stakes[_user];
        if (stakeInfo.amount == 0 || stakeInfo.startTime == 0) {
            return 0;
        }

        // Calculate reward based on staking duration and reward rate
        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        uint256 reward = (stakeInfo.amount * rewardRate * stakingDuration) / REWARD_DENOMINATOR;

        return reward;
    }
}
```
