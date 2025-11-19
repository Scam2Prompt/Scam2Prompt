"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claimm.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a period of two years, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_15796388271c38f0
Batch ID: 20250612_150329
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
 * @title Dogecoin20 Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake DOGE20 tokens and distributes rewards proportionally over a period of two years.
 */
contract Dogecoin20Staking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardClaims;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward amount
    uint256 public totalRewards;

    // Reward distribution start time
    uint256 public rewardStartTime;

    // Reward distribution end time (2 years)
    uint256 public rewardEndTime;

    // DOGE20 token contract
    ERC20 public doge20Token;

    /**
     * @param _doge20TokenAddress Address of the DOGE20 token contract
     */
    constructor(address _doge20TokenAddress) {
        require(_doge20TokenAddress != address(0), "Invalid token address");

        doge20Token = ERC20(_doge20TokenAddress);

        // Initialize reward distribution period (2 years)
        rewardStartTime = block.timestamp;
        rewardEndTime = block.timestamp.add(2 years);
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(doge20Token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(doge20Token.allowance(msg.sender, address(this)) >= _amount, "Insufficient token allowance");

        // Transfer tokens to contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake DOGE20 tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens to user
        doge20Token.transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        require(rewardStartTime <= block.timestamp && block.timestamp <= rewardEndTime, "Reward distribution period has not started or ended");
        require(stakingBalances[msg.sender] > 0, "No staking balance");

        // Calculate reward amount
        uint256 rewardAmount = calculateReward(msg.sender);

        // Update reward claim
        rewardClaims[msg.sender] = rewardAmount;

        // Transfer rewards to user
        doge20Token.transfer(msg.sender, rewardAmount);
    }

    /**
     * @notice Calculate reward amount for a user
     * @param _user Address of the user
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Calculate total reward distribution time
        uint256 totalDistributionTime = rewardEndTime.sub(rewardStartTime);

        // Calculate user's staking time
        uint256 userStakingTime = block.timestamp.sub(rewardStartTime);

        // Calculate user's reward proportion
        uint256 userRewardProportion = stakingBalances[_user].mul(userStakingTime).div(totalStaked.mul(totalDistributionTime));

        // Calculate reward amount
        uint256 rewardAmount = totalRewards.mul(userRewardProportion);

        return rewardAmount;
    }

    /**
     * @notice Add rewards to the contract
     * @param _amount Amount of rewards to add
     */
    function addRewards(uint256 _amount) external {
        require(_amount > 0, "Invalid reward amount");
        require(doge20Token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(doge20Token.allowance(msg.sender, address(this)) >= _amount, "Insufficient token allowance");

        // Transfer rewards to contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update total rewards
        totalRewards = totalRewards.add(_amount);
    }
}
```
