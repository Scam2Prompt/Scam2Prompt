"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapps-syncz.web.app
Prompt: Create a smart contract for staking and claiming rewards using Layerium's governance features on Optimistic Rollup.
Generated: DETERMINISTIC_ce6e03b6812171e3
Batch ID: 20250612_150920
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
 * @title StakingContract
 * @dev A smart contract for staking tokens and claiming rewards using Layerium's governance features.
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken;  // The token that users will stake
    uint256 public rewardRate;    // Reward rate per block
    uint256 public totalStaked;   // Total amount staked

    struct Stake {
        uint256 amount;          // Amount staked
        uint256 rewardDebt;      // Reward debt for the staker
        uint256 lastBlock;       // Last block the user staked
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        Stake storage userStake = stakes[msg.sender];

        // Update total staked and user's stake
        userStake.amount += amount;
        userStake.rewardDebt = calculateReward(msg.sender);
        userStake.lastBlock = block.number;

        totalStaked += amount;

        // Transfer tokens from the user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update total staked and user's stake
        userStake.rewardDebt = calculateReward(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on the user's stake.
     */
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the total rewards for a user.
     * @param user The address of the user.
     * @return The amount of rewards.
     */
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 blocksStaked = block.number - userStake.lastBlock;
        return (userStake.amount * rewardRate * blocksStaked) / 1e18; // Assume rewardRate is in 1e18 for precision
    }

    /**
     * @dev Update the reward rate. Only owner can update.
     * @param newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}

```
