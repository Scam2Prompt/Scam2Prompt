"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements the staking mechanism for $POODL tokens, ensuring it distributes rewards at the specified rate per Ethereum block.
Generated: DETERMINISTIC_b7d31b7d58239734
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking $POODL tokens and distributing rewards
 */
contract StakingContract is Ownable {
    IERC20 public poodlToken; // The $POODL token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to their stakes

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _poodlToken Address of the $POODL token contract
     * @param _rewardRate Reward rate per block
     */
    constructor(IERC20 _poodlToken, uint256 _rewardRate) {
        poodlToken = _poodlToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(poodlToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        require(poodlToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the staker
     */
    function claimRewards() external {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0; // Reset reward debt
        require(poodlToken.transfer(msg.sender, pendingRewards), "Transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param user Address of the staker
     * @return The amount of pending rewards
     */
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (block.number - userStake.rewardDebt) * rewardRate * userStake.amount / totalStaked;
    }

    /**
     * @dev Update the reward rate (only owner)
     * @param newRewardRate New reward rate per block
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
