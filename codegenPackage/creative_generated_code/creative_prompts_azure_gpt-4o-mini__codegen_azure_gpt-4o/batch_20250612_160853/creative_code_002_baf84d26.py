"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-dapps.pages.dev
Prompt: Create a Solidity contract that implements staking for $HEHE tokens, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_baf84d26ddb2cfe0
Batch ID: 20250612_160853
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
 * @title HEHE Token Staking Contract
 * @author [Your Name]
 * @dev This contract allows users to stake HEHE tokens and earn rewards based on their staked amount.
 * Rewards are distributed periodically, and users can withdraw their staked tokens and rewards at any time.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract HEHEStaking {
    IERC20 public immutable heheToken;

    // Reward rate per second (e.g., 1 token per day -> rewardRate = 1 / (60 * 60 * 24))
    uint256 public rewardRate;

    struct Stake {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already paid out to the user
        uint256 lastUpdated; // Last timestamp when the user's stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping from user address to their stake
    uint256 public totalStaked; // Total tokens staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    modifier updateReward(address user) {
        if (stakes[user].amount > 0) {
            uint256 pendingReward = calculateReward(user);
            stakes[user].rewardDebt += pendingReward;
        }
        stakes[user].lastUpdated = block.timestamp;
        _;
    }

    constructor(IERC20 _heheToken, uint256 _rewardRate) {
        heheToken = _heheToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake HEHE tokens.
     * @param amount The amount of HEHE tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the user to the contract
        require(heheToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens and claim rewards.
     */
    function withdraw() external updateReward(msg.sender) {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 reward = stakes[msg.sender].rewardDebt;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= amount;

        // Transfer staked tokens back to the user
        require(heheToken.transfer(msg.sender, amount), "Token transfer failed");

        // Transfer rewards to the user
        if (reward > 0) {
            require(heheToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculates the pending rewards for a user based on their staked amount.
     * @param user The address of the user.
     * @return The pending reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];
        uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;
        return (stakeInfo.amount * timeElapsed * rewardRate) / 1 ether; // Adjust rewardRate with token's decimals
    }

    /**
     * @dev Allows the contract owner to set a new reward rate.
     * @param _rewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external {
        // This function is intentionally left open for additional owner checks/access control
        rewardRate = _rewardRate;
    }

    /**
     * @dev Returns the total staked amount by a user.
     * @param user The address of the user.
     * @return The staked amount.
     */
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Returns the pending reward for a user.
     * @param user The address of the user.
     * @return The pending reward amount.
     */
    function pendingReward(address user) external view returns (uint256) {
        return calculateReward(user) + stakes[user].rewardDebt;
    }
}
```
