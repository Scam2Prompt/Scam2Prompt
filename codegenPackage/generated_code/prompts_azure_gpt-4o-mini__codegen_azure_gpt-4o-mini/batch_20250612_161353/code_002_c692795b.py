"""
Generated Code Metadata:
========================
Original URL: https://claim-dogecoin20.web.app
Prompt: Generate a Solidity smart contract that mimics the DOGE20 staking mechanism, distributing rewards to stakers over a specified period.
Generated: DETERMINISTIC_c692795b58a9adac
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
 * @title DOGE20Staking
 * @dev A smart contract for staking DOGE20 tokens and distributing rewards.
 */
contract DOGE20Staking is Ownable {
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public startTime; // Staking start time
    uint256 public endTime; // Staking end time

    struct Staker {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => Staker) public stakers; // Mapping of stakers

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the DOGE20 token and reward rate.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardRate Reward rate per block.
     * @param _duration Duration for staking in seconds.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardRate, uint256 _duration) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
        startTime = block.timestamp;
        endTime = startTime + _duration;
    }

    /**
     * @dev Stake DOGE20 tokens to earn rewards.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(block.timestamp >= startTime, "Staking has not started yet");
        require(block.timestamp <= endTime, "Staking has ended");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer DOGE20 tokens from the staker to the contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens and claim rewards.
     * @param amount Amount of DOGE20 tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        if (pendingRewards > 0) {
            // Transfer rewards to the staker
            doge20Token.transfer(msg.sender, pendingRewards);
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        // Update staker information
        staker.amount -= amount;
        staker.rewardDebt += pendingRewards;

        // Transfer DOGE20 tokens back to the staker
        doge20Token.transfer(msg.sender, amount);
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Calculate pending rewards for a staker.
     * @param stakerAddress Address of the staker.
     * @return The amount of pending rewards.
     */
    function calculatePendingRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 blocksStaked = block.timestamp - startTime;
        return (staker.amount * rewardRate * blocksStaked) / 1e18 - staker.rewardDebt;
    }

    /**
     * @dev Get the total amount of rewards earned by a staker.
     * @param stakerAddress Address of the staker.
     * @return The total rewards earned.
     */
    function getTotalRewards(address stakerAddress) external view returns (uint256) {
        return calculatePendingRewards(stakerAddress);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param amount Amount of DOGE20 tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= doge20Token.balanceOf(address(this)), "Insufficient balance");
        doge20Token.transfer(msg.sender, amount);
    }
}
```
