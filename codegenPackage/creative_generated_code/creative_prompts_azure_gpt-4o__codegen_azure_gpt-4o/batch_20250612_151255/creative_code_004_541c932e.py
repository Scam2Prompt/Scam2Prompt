"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethoq.xyz
Prompt: Write a smart contract in Solidity for a basic DeFi application that supports ETH staking and rewards distribution.
Generated: DETERMINISTIC_541c932e49dfa5c9
Batch ID: 20250612_151255
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
 * @title ETH Staking Smart Contract
 * @dev This contract allows users to stake ETH and earn rewards over time.
 * It supports staking, rewards distribution, and withdrawal of funds.
 */
contract ETHStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per second (ETH per second)
    uint256 public totalStaked; // Total ETH staked in the contract

    struct StakeInfo {
        uint256 amount; // Amount of ETH staked
        uint256 lastUpdate; // Last timestamp of reward calculation
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => StakeInfo) public stakes; // Mapping of staker address to stake info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract owner and sets the reward rate.
     * @param _rewardRate Reward rate per second (ETH per second).
     */
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ETH into the contract to earn rewards.
     * Rewards are updated before adding a new stake.
     */
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");

        // Update rewards before modifying stake
        updateRewards(msg.sender);

        // Update staking info
        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].lastUpdate = block.timestamp;
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked ETH along with accumulated rewards.
     * Rewards are updated and paid before withdrawal.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards before withdrawal
        updateRewards(msg.sender);

        // Transfer staked ETH
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;
        payable(msg.sender).transfer(_amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards without withdrawing staked ETH.
     */
    function claimRewards() external {
        // Update rewards before claiming
        updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards available");

        // Reset rewards and transfer to user
        stakes[msg.sender].rewards = 0;
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update rewards for a user based on elapsed time.
     * This is an internal function used before stake, withdraw, or claim operations.
     */
    function updateRewards(address _user) internal {
        StakeInfo storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.lastUpdate;
            stake.rewards += (stake.amount * rewardRate * timeElapsed) / 1 ether; // Scale reward rate for ETH units
            stake.lastUpdate = block.timestamp;
        }
    }

    /**
     * @dev Allow the owner to set a new reward rate.
     * @param _newRewardRate New reward rate per second (ETH per second).
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Fallback function to accept ETH deposits directly.
     */
    receive() external payable {}
}
```
