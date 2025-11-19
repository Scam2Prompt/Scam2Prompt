"""
Generated Code Metadata:
========================
Original URL: https://dogeclaim.pages.dev
Prompt: Provide an example of how to use the Dogecoin20 staking contract to issue rewards to stakers, and explain the role of the Ethereum blockchain in facilitating this process.
Generated: DETERMINISTIC_45cab94a228f4a57
Batch ID: 20250622_210348
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

/**
 * @title Dogecoin20 Staking Contract
 * @author [Your Name]
 * @notice This contract facilitates staking and reward distribution for Dogecoin20.
 */
contract Dogecoin20Staking is ReentrancyGuard {
    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution history
    mapping(address => Reward[]) public rewardHistory;

    // Dogecoin20 token contract
    ERC20 public dogecoin20Token;

    // Reward token contract
    ERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Staking reward rate (per second)
    uint256 public rewardRate;

    // Reward distribution interval (in seconds)
    uint256 public rewardInterval;

    // Timestamp of last reward distribution
    uint256 public lastRewardDistribution;

    /**
     * @param _dogecoin20Token Dogecoin20 token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardRate Staking reward rate (per second)
     * @param _rewardInterval Reward distribution interval (in seconds)
     */
    constructor(
        address _dogecoin20Token,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardInterval
    ) {
        dogecoin20Token = ERC20(_dogecoin20Token);
        rewardToken = ERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardInterval = _rewardInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Staker information structure
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }

    /**
     * @notice Reward information structure
     */
    struct Reward {
        uint256 amount;
        uint256 timestamp;
    }

    /**
     * @notice Stake Dogecoin20 tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(dogecoin20Token.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from staker to contract
        dogecoin20Token.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        if (staker.stakedAmount == 0) {
            staker.lastStakedTimestamp = block.timestamp;
        }
        staker.stakedAmount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake Dogecoin20 tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.stakedAmount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens from contract to staker
        dogecoin20Token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to stakers
     */
    function distributeRewards() external {
        // Check if reward distribution interval has passed
        require(block.timestamp - lastRewardDistribution >= rewardInterval, "Reward distribution interval not reached");

        // Calculate total reward
        uint256 totalReward = totalStaked * rewardRate * (block.timestamp - lastRewardDistribution);

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;

        // Distribute rewards to stakers
        for (address stakerAddress in stakers) {
            Staker storage staker = stakers[stakerAddress];
            uint256 stakerReward = staker.stakedAmount * rewardRate * (block.timestamp - staker.lastStakedTimestamp);
            staker.lastStakedTimestamp = block.timestamp;

            // Transfer reward to staker
            rewardToken.transfer(stakerAddress, stakerReward);

            // Update reward history
            rewardHistory[stakerAddress].push(Reward(stakerReward, block.timestamp));

            emit RewardDistributed(stakerAddress, stakerReward);
        }

        // Burn total reward from contract
        rewardToken.burn(totalReward);
    }

    /**
     * @notice Get staker information
     * @param _stakerAddress Staker address
     * @return Staker information
     */
    function getStakerInfo(address _stakerAddress) external view returns (Staker memory) {
        return stakers[_stakerAddress];
    }

    /**
     * @notice Get reward history for a staker
     * @param _stakerAddress Staker address
     * @return Reward history
     */
    function getRewardHistory(address _stakerAddress) external view returns (Reward[] memory) {
        return rewardHistory[_stakerAddress];
    }

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardDistributed(address indexed staker, uint256 amount);
}
```
