"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Create a smart contract in Solidity for staking $99BTC tokens, ensuring rewards are distributed on every Ethereum block as outlined in the 99Bitcoins staking system.
Generated: DETERMINISTIC_7c574a1680ffdbf3
Batch ID: 20250612_153606
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
 * @dev A smart contract for staking $99BTC tokens and distributing rewards.
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken;  // The ERC20 token being staked
    uint256 public rewardRate;    // Reward rate per block
    uint256 public totalStaked;   // Total amount of tokens staked
    uint256 public totalRewards;   // Total rewards distributed

    struct Staker {
        uint256 amount;             // Amount of tokens staked by the user
        uint256 rewardDebt;         // Reward debt for the user
    }

    mapping(address => Staker) public stakers; // Records of stakers

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken The address of the $99BTC token.
     * @param _rewardRate The reward rate to be distributed per block.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update total staked amount and staker information
        totalStaked += amount;
        stakers[msg.sender].amount += amount;

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update total staked amount and staker information
        totalStaked -= amount;
        stakers[msg.sender].amount -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Reset the user's reward debt
        stakers[msg.sender].rewardDebt += reward;
        totalRewards += reward;

        // Transfer rewards to the user (from contract balance)
        stakingToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards for a specific staker.
     * @param staker The address of the staker.
     * @return The calculated reward for the staker.
     */
    function calculateRewards(address staker) internal view returns (uint256) {
        Staker memory user = stakers[staker];
        uint256 pendingReward = (block.number * rewardRate) - user.rewardDebt;
        return pendingReward * user.amount / totalStaked;
    }
}
```
