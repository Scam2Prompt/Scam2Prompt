"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: How can I implement a staking smart contract for DOGE20 tokens on Ethereum to distribute rewards over two years?
Generated: DETERMINISTIC_d5ebec2c83bb1b2e
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; // SPDX version for Solidity compiler

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract for DOGE20 Tokens
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards over a period of two years.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public doge20Token;

    // Reward distribution parameters
    uint256 public constant REWARD_RATE = 100; // Reward rate for stakers
    uint256 public constant STAKING_DURATION = 2 * 365 days; // Duration for staking rewards

    // Information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping from user address to Staker details
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the token address
     * @param _doge20Token Address of the DOGE20 token contract
     */
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param amount Amount of DOGE20 tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer the tokens from the staker to this contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.rewardDebt = staker.rewardDebt.add(calculateRewards(msg.sender));
        staker.lastStakedTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked DOGE20 tokens
     * @param amount Amount of DOGE20 tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Calculate rewards first
        uint256 pendingRewards = calculateRewards(msg.sender);
        staker.rewardDebt = staker.rewardDebt.add(pendingRewards);

        // Update staker information
        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer the tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update the reward debt
        staker.rewardDebt = staker.rewardDebt.add(rewards);
        
        // Transfer the rewards to the staker
        doge20Token.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a given staker
     * @param stakerAddress Address of the staker
     * @return The calculated rewards
     */
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
        // Calculate rewards based on time staked and staked amount
        return staker.amountStaked.mul(REWARD_RATE).mul(timeStaked).div(STAKING_DURATION);
    }

    /**
     * @dev Get the staker's details
     * @param stakerAddress Address of the staker
     * @return amountStaked Amount staked by the user
     * @return rewardDebt Amount of rewards owed to the user
     */
    function getStakerInfo(address stakerAddress) external view returns (uint256 amountStaked, uint256 rewardDebt) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardDebt);
    }
}
```
