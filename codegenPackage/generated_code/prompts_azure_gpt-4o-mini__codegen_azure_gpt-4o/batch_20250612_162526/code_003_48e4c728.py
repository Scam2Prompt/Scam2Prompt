"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: Create a smart contract that allows users to stake their assets within the GROW DAO platform, ensuring transparency and community governance.
Generated: DETERMINISTIC_48e4c728fe879e4d
Batch ID: 20250612_162526
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
 * @title GROW DAO Staking Contract
 * @dev This contract allows users to stake their assets within the GROW DAO platform.
 * It ensures transparency and community governance.
 */
contract GrowDAOStaking {
    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount, uint256 timestamp);

    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second (e.g., tokens per second)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake or reward claim
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found for this user");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match the stake amount");

        // If the user already has a stake, calculate and update rewards
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            stakes[msg.sender].amount += pendingRewards;
        }

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 rewards = calculateRewards(msg.sender);

        // Reset the user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Update total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked amount and rewards back to the user
        uint256 totalPayout = stakedAmount + rewards;
        (bool success, ) = msg.sender.call{value: totalPayout}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
        emit RewardsClaimed(msg.sender, rewards, block.timestamp);
    }

    /**
     * @dev Calculates the rewards for a user based on their stake and time staked.
     * @param _user The address of the user.
     * @return The calculated rewards.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * stakingDuration) / 1e18;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw contract balance (for emergency purposes).
     * @param _amount The amount to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Transfer failed");
    }
}
```
