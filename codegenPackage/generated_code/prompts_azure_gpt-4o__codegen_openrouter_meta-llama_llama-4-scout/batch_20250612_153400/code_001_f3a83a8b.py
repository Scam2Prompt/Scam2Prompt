"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20in.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the DOGE20 staking mechanism, distributing rewards to stakers over a two-year period.
Generated: DETERMINISTIC_f3a83a8bb7f02da5
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract manages the staking mechanism for DOGE20, distributing rewards over a two-year period.
 */
contract Doge20Staking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // DOGE20 token contract
    ERC20Burnable public token;

    // Total rewards to be distributed over 2 years
    uint256 public totalRewards;

    // Duration of the staking period in seconds (2 years)
    uint256 public stakingDuration;

    // Timestamp when staking starts
    uint256 public stakingStartTime;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _tokenAddress Address of the DOGE20 token contract
     * @param _totalRewards Total rewards to be distributed over 2 years
     */
    constructor(address _tokenAddress, uint256 _totalRewards) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        token = ERC20Burnable(_tokenAddress);
        totalRewards = _totalRewards;
        stakingDuration = 2 years;
        stakingStartTime = block.timestamp;
        rewardPerSecond = totalRewards.div(stakingDuration);
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.add(_amount);
        staker.lastClaimTime = block.timestamp;

        // Transfer tokens to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DOGE20 tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].stakeAmount >= _amount, "Insufficient staked amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.sub(_amount);

        // Transfer tokens back to the user
        token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakeAmount > 0, "No staked amount");

        // Calculate rewards
        uint256 rewards = calculateRewards(staker);
        require(rewards > 0, "No rewards to claim");

        // Update staker information
        staker.lastClaimTime = block.timestamp;
        staker.rewardsClaimed = staker.rewardsClaimed.add(rewards);

        // Transfer rewards to the user
        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param _staker Staker information
     * @return Rewards
     */
    function calculateRewards(Staker storage _staker) internal view returns (uint256) {
        uint256 stakingTime = block.timestamp.sub(_staker.lastClaimTime);
        uint256 rewards = stakingTime.mul(rewardPerSecond).mul(_staker.stakeAmount);
        return rewards.div(totalRewards);
    }

    // Struct to store staker information
    struct Staker {
        uint256 stakeAmount;
        uint256 lastClaimTime;
        uint256 rewardsClaimed;
    }
}
```
