"""
Generated Code Metadata:
========================
Original URL: https://doge20-claim.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking mechanism similar to DOGE20, where rewards are distributed every block based on the percentage of the staking pool and a dynamic annual return rate.
Generated: DETERMINISTIC_1ccff37d2f3a53ff
Batch ID: 20250612_153526
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
 * @dev A smart contract for staking tokens with dynamic rewards based on the staking pool.
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken; // The token that users will stake
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public annualReturnRate; // Annual return rate in basis points (1% = 100 basis points)
    uint256 public lastRewardBlock; // Last block number rewards were distributed

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, uint256 _annualReturnRate) {
        stakingToken = _stakingToken;
        annualReturnRate = _annualReturnRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        updateRewards(msg.sender);

        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        updateRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0; // Reset reward debt
        stakingToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards for a user.
     * @param user The address of the user to update rewards for.
     */
    function updateRewards(address user) internal {
        uint256 blocksPassed = block.number - lastRewardBlock;
        if (blocksPassed > 0 && totalStaked > 0) {
            uint256 reward = (blocksPassed * annualReturnRate * totalStaked) / (365 days * 10000);
            stakes[user].rewardDebt += (reward * stakes[user].amount) / totalStaked;
        }
        lastRewardBlock = block.number;
    }

    /**
     * @dev Set a new annual return rate.
     * @param newRate The new annual return rate in basis points.
     */
    function setAnnualReturnRate(uint256 newRate) external onlyOwner {
        annualReturnRate = newRate;
    }

    /**
     * @dev Get the staked amount of a user.
     * @param user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Get the pending rewards for a user.
     * @param user The address of the user.
     * @return The amount of pending rewards for the user.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        uint256 blocksPassed = block.number - lastRewardBlock;
        uint256 reward = (blocksPassed * annualReturnRate * totalStaked) / (365 days * 10000);
        return stakes[user].rewardDebt + (reward * stakes[user].amount) / totalStaked;
    }
}
```
