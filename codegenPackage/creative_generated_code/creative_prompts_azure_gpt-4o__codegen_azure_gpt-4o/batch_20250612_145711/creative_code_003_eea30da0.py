"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: Write a smart contract in Solidity to simulate staking Ethereum with Bake's zero lockup feature.
Generated: DETERMINISTIC_eea30da0dcc3497d
Batch ID: 20250612_145711
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
 * @title ETH Staking Contract with Zero Lockup
 * @notice This contract allows users to stake ETH and withdraw their stake or rewards at any time.
 */
contract EthStaking {

    // Mapping to store user stakes
    mapping(address => uint256) private stakes;

    // Mapping to store user rewards
    mapping(address => uint256) private rewards;

    // Total ETH staked in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Reward rate (e.g., 10% annualized, scaled by 1e18 for precision)
    uint256 public rewardRate;

    // Last update timestamp for each user
    mapping(address => uint256) private lastUpdate;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier updateRewards(address user) {
        if (stakes[user] > 0) {
            rewards[user] += calculateReward(user);
        }
        lastUpdate[user] = block.timestamp;
        _;
    }

    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate; // Reward rate needs to be provided in 1e18 scale.
    }

    /**
     * @notice Allows a user to stake ETH into the contract.
     */
    function stake() external payable updateRewards(msg.sender) {
        require(msg.value > 0, "Stake amount must be greater than zero");
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @notice Allows a user to withdraw their staked ETH along with any rewards.
     * @param _amount Amount of ETH to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender] >= _amount, "Insufficient staked balance");

        stakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer the ETH back to the user
        payable(msg.sender).transfer(_amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to claim their accumulated rewards without withdrawing their stake.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate the pending rewards for a user.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdate[user];
        uint256 userStake = stakes[user];

        // Reward formula: stake * rewardRate * timeElapsed / (seconds in a year) / 1e18
        return (userStake * rewardRate * timeElapsed) / (365 days * 1e18);
    }

    /**
     * @notice Returns the staked balance of a user.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function stakedBalance(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @notice Returns the reward balance of a user.
     * @param user Address of the user.
     * @return The reward balance of the user.
     */
    function rewardBalance(address user) external view returns (uint256) {
        return rewards[user] + calculateReward(user);
    }

    /**
     * @notice Allows the owner to update the reward rate.
     * @param _newRate New reward rate (scaled by 1e18).
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    /**
     * @notice Fallback function to accept ETH deposits directly.
     */
    receive() external payable {}
}
```
