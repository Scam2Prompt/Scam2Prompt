"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements the staking mechanism for $POODL tokens, ensuring it distributes rewards at the specified rate per Ethereum block.
Generated: DETERMINISTIC_b7d31b7d58239734
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PoodlStaking
 * @dev Smart contract for staking $POODL tokens with reward distribution
 */
contract PoodlStaking is Ownable {
    IERC20 public poodlToken; // The address of the $POODL token contract

    struct Stake {
        uint256 amount; // Amount of $POODL tokens staked
        uint256 lastRewardBlock; // Last block number rewards were calculated
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the $POODL token address and reward rate.
     * @param _poodlToken Address of the $POODL token contract
     * @param _rewardRate Reward rate per block
     */
    constructor(IERC20 _poodlToken, uint256 _rewardRate) {
        poodlToken = _poodlToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake $POODL tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(poodlToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastRewardBlock = block.number;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $POODL tokens and claim rewards
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake and last reward block
        userStake.amount = 0;
        userStake.lastRewardBlock = block.number;

        totalStaked -= amountToUnstake;

        // Transfer staked tokens and reward
        require(poodlToken.transfer(msg.sender, amountToUnstake), "Transfer failed");
        if (reward > 0) {
            require(poodlToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Function to calculate the reward for the user
     * @param user Address of the user
     * @return Reward amount
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the number of blocks since the last reward calculation
        uint256 blockDifference = block.number - userStake.lastRewardBlock;
        return userStake.amount * blockDifference * rewardRate;
    }

    /**
     * @dev Function to update the reward rate (only owner)
     * @param newRewardRate New reward rate per block
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
