"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Create a smart contract for staking EGLD that includes the unstake period and reward distribution logic.
Generated: DETERMINISTIC_44955ba630defb26
Batch ID: 20250612_162207
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

/**
 * @title EGLD Staking Smart Contract
 * @dev This contract allows users to stake EGLD, earn rewards, and unstake after a defined period.
 */
contract EGLDStaking {
    // State variables
    uint256 public constant UNSTAKE_PERIOD = 7 days; // Unstake period in seconds
    uint256 public constant REWARD_RATE = 10; // Reward rate in percentage (10%)
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(address => uint256) public rewards; // Mapping of user rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake EGLD.
     * @param _amount Amount of EGLD to stake.
     */
    function stake(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value must match the staking amount");
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake EGLD after the unstake period.
     */
    function unstake() external hasStake(msg.sender) {
        Stake memory userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.timestamp + UNSTAKE_PERIOD, "Unstake period not reached");

        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        uint256 totalAmount = userStake.amount + reward;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Update rewards mapping
        rewards[msg.sender] += reward;

        // Transfer staked amount back to user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset user's rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a given stake.
     * @param _amount Amount staked.
     * @param _timestamp Timestamp of staking.
     * @return Reward amount.
     */
    function calculateReward(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - _timestamp;
        uint256 reward = (_amount * REWARD_RATE * stakingDuration) / (365 days * 100); // Annualized reward
        return reward;
    }

    /**
     * @dev Fallback function to receive EGLD.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
