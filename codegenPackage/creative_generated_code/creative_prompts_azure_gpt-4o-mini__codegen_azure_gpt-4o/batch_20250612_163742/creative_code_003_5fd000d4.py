"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-in.pages.dev
Prompt: Provide an example of how to implement a staking mechanism for $WAI tokens in a decentralized application.
Generated: DETERMINISTIC_5fd000d4c5365258
Batch ID: 20250612_163742
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
 * @title WAI Token Staking Contract
 * @notice This contract allows users to stake $WAI tokens and earn rewards
 * based on the staking duration. It supports deposit, withdrawal, and reward claim functionality.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract WAIStaking {
    IERC20 public immutable waiToken; // Reference to the $WAI token contract
    uint256 public constant REWARD_RATE = 100; // Reward rate per second (example: 100 wei per second)
    
    struct Stake {
        uint256 amount;    // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last interaction
        uint256 rewards;   // Accumulated rewards (not claimed yet)
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake details
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the WAI token address.
     * @param _waiToken Address of the $WAI token contract.
     */
    constructor(IERC20 _waiToken) {
        waiToken = _waiToken;
    }

    /**
     * @notice Stake $WAI tokens into the contract.
     * @param amount Amount of $WAI tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update rewards before modifying the stake
        _updateRewards(msg.sender);

        // Transfer $WAI tokens from the user to the contract
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update the stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake $WAI tokens. Rewards are automatically updated and can still be claimed separately.
     * @param amount Amount of $WAI tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Insufficient staked balance");

        // Update rewards before modifying the stake
        _updateRewards(msg.sender);

        // Update the stake details
        stakeData.amount -= amount;

        // Transfer $WAI tokens back to the user
        require(waiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        Stake storage stakeData = stakes[msg.sender];
        uint256 rewardsToClaim = stakeData.rewards;
        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset rewards and transfer to the user
        stakeData.rewards = 0;
        require(waiToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @notice View the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards in $WAI tokens.
     */
    function viewPendingRewards(address user) external view returns (uint256) {
        Stake memory stakeData = stakes[user];
        uint256 additionalRewards = (block.timestamp - stakeData.timestamp) * REWARD_RATE * stakeData.amount / 1e18;
        return stakeData.rewards + additionalRewards;
    }

    /**
     * @dev Internal function to update rewards for a user based on the staking duration.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeData = stakes[user];
        if (stakeData.amount > 0) {
            uint256 additionalRewards = (block.timestamp - stakeData.timestamp) * REWARD_RATE * stakeData.amount / 1e18;
            stakeData.rewards += additionalRewards;
            stakeData.timestamp = block.timestamp;
        }
    }
}
```
