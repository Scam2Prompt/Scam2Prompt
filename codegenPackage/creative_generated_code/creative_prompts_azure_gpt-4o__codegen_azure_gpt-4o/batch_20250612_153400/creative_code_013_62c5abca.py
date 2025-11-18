"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Develop a smart contract that implements a reward distribution mechanism for $POODL staking, ensuring proportional rewards based on the amount staked.
Generated: DETERMINISTIC_62c5abca5717e22d
Batch ID: 20250612_153400
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
 * @title RewardDistribution
 * @dev Smart contract for proportional reward distribution based on $POODL staking.
 */
contract RewardDistribution {
    // Mapping to store staked amounts of each address
    mapping(address => uint256) public stakes;

    // Mapping to store rewards of each address
    mapping(address => uint256) public rewards;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Address of the owner of the contract
    address public owner;

    // Event emitted when tokens are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed staker, uint256 reward);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed staker, uint256 amount, uint256 reward);

    /**
     * @dev Modifier to restrict access to owner-only functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Contract constructor to initialize the owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Sent value must match amount to stake");

        // Update the staked amount and total staked
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to distribute rewards proportionally
     * @param totalReward Total reward to distribute among stakers
     */
    function distributeRewards(uint256 totalReward) external onlyOwner {
        require(totalReward > 0, "Reward must be greater than zero");
        require(totalStaked > 0, "No stakes in the contract");

        // Iterate through all stakers and distribute rewards proportionally
        for (uint256 i = 0; i < getStakeholders().length; i++) {
            address staker = getStakeholders()[i];
            uint256 stakeAmount = stakes[staker];
            uint256 reward = (stakeAmount * totalReward) / totalStaked;
            rewards[staker] += reward;

            emit RewardDistributed(staker, reward);
        }
    }

    /**
     * @dev Function for stakers to withdraw their stake and rewards
     */
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        uint256 rewardAmount = rewards[msg.sender];

        require(stakedAmount > 0, "No stake to withdraw");

        // Reset staked and reward amounts for the sender
        stakes[msg.sender] = 0;
        rewards[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer staked amount and rewards to the sender
        uint256 totalAmount = stakedAmount + rewardAmount;
        (bool sent, ) = msg.sender.call{value: totalAmount}("");
        require(sent, "Failed to send the withdrawal amount");

        emit Withdrawn(msg.sender, stakedAmount, rewardAmount);
    }

    /**
     * @dev Helper function to retrieve all stakeholders' addresses
     * @return Array of stakeholder addresses
     */
    function getStakeholders() public view returns (address[] memory) {
        address[] memory stakeholders;
        uint256 count = 0;

        for (uint256...
```
