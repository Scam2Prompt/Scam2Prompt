"""
Generated Code Metadata:
========================
Original URL: https://smartprotocolcoin.pages.dev
Prompt: Generate a smart contract code for a staking pool that allows multiple stakeholders to combine their computational resources and increase their chances of being rewarded.
Generated: DETERMINISTIC_d5fd2ff567bb6575
Batch ID: 20250622_210249
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
 * @title StakingPool
 * @dev A smart contract for a staking pool where multiple stakeholders can combine their resources.
 * Stakeholders can deposit and withdraw funds, and rewards are distributed proportionally.
 */
contract StakingPool {
    // State variables
    address public owner; // Owner of the staking pool
    uint256 public totalStaked; // Total amount of funds staked in the pool
    uint256 public rewardPool; // Total rewards available for distribution

    struct Stakeholder {
        uint256 stakedAmount; // Amount staked by the stakeholder
        uint256 rewardDebt; // Rewards already claimed by the stakeholder
    }

    mapping(address => Stakeholder) public stakeholders; // Mapping of stakeholders
    address[] public stakeholderAddresses; // List of stakeholder addresses

    // Events
    event Stake(address indexed stakeholder, uint256 amount);
    event Withdraw(address indexed stakeholder, uint256 amount);
    event RewardDistributed(address indexed stakeholder, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasStake(address _stakeholder) {
        require(stakeholders[_stakeholder].stakedAmount > 0, "No stake found for this address");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a stakeholder to deposit funds into the staking pool.
     * @param _amount The amount to be staked.
     */
    function stake(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value must match the staking amount");
        require(_amount > 0, "Stake amount must be greater than zero");

        if (stakeholders[msg.sender].stakedAmount == 0) {
            stakeholderAddresses.push(msg.sender); // Add new stakeholder
        }

        stakeholders[msg.sender].stakedAmount += _amount;
        totalStaked += _amount;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Allows a stakeholder to withdraw their staked funds.
     * @param _amount The amount to be withdrawn.
     */
    function withdraw(uint256 _amount) external hasStake(msg.sender) {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakeholders[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        stakeholders[msg.sender].stakedAmount -= _amount;
        totalStaked -= _amount;

        payable(msg.sender).transfer(_amount);

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to deposit rewards into the reward pool.
     */
    function depositRewards() external payable onlyOwner {
        require(msg.value > 0, "Reward amount must be greater than zero");
        rewardPool += msg.value;
    }

    /**
     * @dev Distributes rewards proportionally to stakeholders based on their staked amount.
     */
    function distributeRewards() external onlyOwner {
        require(rewardPool > 0, "No rewards available for distribution");
        require(totalStaked > 0, "No funds staked in the pool");

        for (uint256 i = 0; i < stakeholderAddresses.length; i++) {
            address stakeholder = stakeholderAddresses[i];
            uint256 stakedAmount = stakeholders[stakeholder].stakedAmount;

            if (stakedAmount > 0) {
                uint256 reward = (stakedAmount * rewardPool) / totalStaked;
                stakeholders[stakeholder].rewardDebt += reward;

                payable(stakeholder).transfer(reward);
                emit RewardDistributed(stakeholder, reward);
            }
        }

        rewardPool = 0; // Reset reward pool after distribution
    }

    /**
     * @dev Returns the total staked amount for a stakeholder.
     * @param _stakeholder The address of the stakeholder.
     * @return The staked amount.
     */
    function getStake(address _stakeholder) external view returns (uint256) {
        return stakeholders[_stakeholder].stakedAmount;
    }

    /**
     * @dev Returns the total reward debt for a stakeholder.
     * @param _stakeholder The address of the stakeholder.
     * @return The reward debt.
     */
    function getRewardDebt(address _stakeholder) external view returns (uint256) {
        return stakeholders[_stakeholder].rewardDebt;
    }
}
```
