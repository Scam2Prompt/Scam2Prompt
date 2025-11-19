"""
Generated Code Metadata:
========================
Original URL: https://bitcoinpepe-en.xyz
Prompt: Develop a smart contract in Solidity for a simple staking and rewards system similar to what is described in the $BPEP tokenomics, where 15% of tokens are allocated for staking and rewards.
Generated: DETERMINISTIC_379381ec5c84530c
Batch ID: 20250622_212238
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
 * @title Staking and Rewards Contract
 * @author [Your Name]
 * @notice A simple staking and rewards system
 */
contract StakingRewards is ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract instance
    ERC20 public token;

    // Staking and rewards parameters
    uint256 public totalStakingAllocation; // 15% of total token supply
    uint256 public stakingEndTime;
    uint256 public rewardPerBlock;
    uint256 public startBlock;
    uint256 public endBlock;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        uint256 lastClaimedBlock;
    }

    /**
     * @notice Constructor
     * @param _token Token contract instance
     * @param _totalStakingAllocation Total staking allocation (15% of total token supply)
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        ERC20 _token,
        uint256 _totalStakingAllocation,
        uint256 _stakingDuration,
        uint256 _rewardPerBlock
    ) public {
        token = _token;
        totalStakingAllocation = _totalStakingAllocation;
        stakingEndTime = block.timestamp.add(_stakingDuration);
        rewardPerBlock = _rewardPerBlock;
        startBlock = block.number;
        endBlock = startBlock.add(_stakingDuration.div(10)); // assume 10 seconds per block
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(stakingEndTime > block.timestamp, "Staking period ended");

        // Transfer tokens to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");
        require(stakingEndTime <= block.timestamp, "Staking period not ended");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);

        // Transfer tokens to user
        token.transfer(msg.sender, _amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.rewardsEarned = staker.rewardsEarned.add(rewards);
        staker.lastClaimedBlock = block.number;

        // Transfer rewards to user
        token.transfer(msg.sender, rewards);

        // Emit event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 blocksElapsed = block.number.sub(staker.lastClaimedBlock);
        uint256 rewards = blocksElapsed.mul(rewardPerBlock).mul(staker.stakedAmount).div(totalStakingAllocation);
        return rewards;
    }

    /**
     * @notice Get staker information
     * @param _user User address
     * @return Staker information
     */
    function getStakerInfo(address _user) external view returns (uint256, uint256, uint256) {
        Staker storage staker = stakers[_user];
        return (staker.stakedAmount, staker.rewardsEarned, staker.lastClaimedBlock);
    }
}
```
