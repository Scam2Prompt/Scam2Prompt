"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Generate Solidity code for a staking smart contract that mimics the DOGE20 reward distribution mechanism, providing rewards to stakers over a two-year period based on their share of the staking pool.
Generated: DETERMINISTIC_0397cc25d96a50c1
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract distributes rewards to stakers over a two-year period based on their share of the staking pool.
 */
contract Doge20Staking is Ownable {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward amount
    uint256 public totalRewards;

    // Reward distribution start time
    uint256 public startTime;

    // Reward distribution end time (2 years)
    uint256 public endTime;

    // ERC20 token contract for rewards
    IERC20 public rewardsToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _rewardsToken ERC20 token contract for rewards
     * @param _startTime Reward distribution start time
     */
    constructor(IERC20 _rewardsToken, uint256 _startTime) {
        require(_startTime > block.timestamp, "Start time must be in the future");

        rewardsToken = _rewardsToken;
        startTime = _startTime;
        endTime = _startTime.add(2 years);

        // Initialize total rewards (e.g., 1 million tokens)
        totalRewards = 1_000_000 * 10**18; // Assuming 18 decimals for rewards token
    }

    /**
     * @dev Stake tokens and start earning rewards
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakers[msg.sender].stakedAmount == 0, "User already has staked tokens");

        stakers[msg.sender].stakedAmount = _amount;
        stakers[msg.sender].stakedAt = block.timestamp;

        totalStaked = totalStaked.add(_amount);

        // Transfer staked tokens to the contract
        IERC20(stakers[msg.sender].token).transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and stop earning rewards
     */
    function unstake() external {
        require(stakers[msg.sender].stakedAmount > 0, "User has no staked tokens");

        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        uint256 rewards = calculateRewards(msg.sender);

        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].stakedAt = 0;
        stakers[msg.sender].rewardsClaimed = rewards;

        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer staked tokens and rewards back to the user
        IERC20(stakers[msg.sender].token).transfer(msg.sender, stakedAmount);
        rewardsToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsDistributed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param _staker Address of the staker
     * @return Rewards amount
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(stakers[_staker].stakedAt);
        if (stakedDuration > endTime.sub(startTime)) {
            stakedDuration = endTime.sub(startTime);
        }

        uint256 stakerShare = stakers[_staker].stakedAmount.mul(stakedDuration).div(totalStaked.mul(endTime.sub(startTime)));
        return totalRewards.mul(stakerShare).div(1e18);
    }

    // Update start time
    function updateStartTime(uint256 _newStartTime) external onlyOwner {
        require(_newStartTime > block.timestamp, "New start time must be in the future");
        startTime = _newStartTime;
        endTime = _newStartTime.add(2 years);
    }

    // Update total rewards
    function updateTotalRewards(uint256 _newTotalRewards) external onlyOwner {
        totalRewards = _newTotalRewards;
    }

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 rewardsClaimed;
        address token; // token being staked (DOGE20)
    }
}
```
