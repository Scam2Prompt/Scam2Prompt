"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dioneprotocol-app.pages.dev
Prompt: Provide code to implement yield farming functionality for an ERC-20 token on Odyssey Chain, leveraging its staking benefits and low energy usage.
Generated: DETERMINISTIC_3f120f177f4e701b
Batch ID: 20250612_153527
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
 * @title YieldFarmingContract
 * @dev Implements yield farming functionality for ERC-20 tokens on Odyssey Chain.
 * Users can stake tokens, earn rewards, and unstake their tokens.
 */
contract YieldFarmingContract {
    // ERC-20 Token contract interface
    IERC20 public token;

    // Reward rate per second (tokens earned per second of staking)
    uint256 public rewardRate;

    // Mapping from user address to their staking information
    struct Staker {
        uint256 amountStaked;  // Amount of tokens staked by the user
        uint256 rewardDebt;    // Rewards already paid out or pending
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _token Address of the ERC-20 token used for staking.
     * @param _rewardRate Number of reward tokens distributed per second of staking.
     */
    constructor(IERC20 _token, uint256 _rewardRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        token = _token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens for reward generation.
     * @param _amount The number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating state
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker's state
        staker.amountStaked += _amount;
        staker.rewardDebt += pendingRewards;
        staker.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     * @param _amount The number of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Calculate pending rewards before updating state
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        // Update staker's state
        staker.amountStaked -= _amount;
        staker.rewardDebt += pendingRewards;
        staker.lastStakedTime = block.timestamp;

        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update staker's state
        staker.rewardDebt = 0;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Helper function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return The amount of pending rewards.
     */
    function calculatePendingRewards(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];

        if (staker.amountStaked == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.lastStakedTime;
        uint256 rewards = (stakingDuration * rewardRate * staker.amountStaked) / 1 ether; // Assumes reward rate is scaled by 1 ether

        return rewards + staker.rewardDebt;
    }

    /**
     * @dev Retrieve the total reward owed to the user (includes pending rewards).
     * @param _user Address of the user.
     * @return Total rewards accrued.
     */
    function getTotalRewards(address _user) external view returns (uint256) {
        return calculatePendingRewards(_user);
    }
}

// Minimal ERC-20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
