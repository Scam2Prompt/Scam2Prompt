"""
Generated Code Metadata:
========================
Original URL: https://bogeonbase.pages.dev
Prompt: Develop a simple staking platform for $BOGE holders using a library like OpenZeppelin.
Generated: DETERMINISTIC_14bd616eeae8771d
Batch ID: 20250622_204829
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
 * @title BogeStakingContract
 * @author [Your Name]
 * @notice A simple staking platform for $BOGE holders
 */
contract BogeStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // BOGE token contract
    ERC20 public bogeToken;

    // Staking start and end timestamps
    uint256 public stakingStart;
    uint256 public stakingEnd;

    // Staking reward per second
    uint256 public rewardPerSecond;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes BOGE tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes BOGE tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims reward
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @param _bogeTokenAddress Address of the BOGE token contract
     * @param _stakingDuration Duration of the staking period in seconds
     * @param _rewardPerSecond Reward per second for stakers
     */
    constructor(
        address _bogeTokenAddress,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        require(_bogeTokenAddress != address(0), "Invalid BOGE token address");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");
        require(_rewardPerSecond > 0, "Reward per second must be greater than 0");

        bogeToken = ERC20(_bogeTokenAddress);
        stakingStart = block.timestamp;
        stakingEnd = stakingStart.add(_stakingDuration);
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Stake BOGE tokens
     * @param _amount Amount of BOGE tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(stakingStart <= block.timestamp, "Staking not started yet");
        require(stakingEnd > block.timestamp, "Staking period ended");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(bogeToken.balanceOf(msg.sender) >= _amount, "Insufficient BOGE token balance");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakers[msg.sender].lastClaimed = block.timestamp;

        // Transfer BOGE tokens to the contract
        bogeToken.transferFrom(msg.sender, address(this), _amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake BOGE tokens
     */
    function unstake() external nonReentrant {
        require(stakingEnd <= block.timestamp, "Staking period not ended yet");
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount found");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update staker information
        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].lastClaimed = block.timestamp;

        // Transfer BOGE tokens and reward to the user
        bogeToken.transfer(msg.sender, stakedAmount);
        bogeToken.transfer(msg.sender, reward);

        // Update total staked amount
        totalStaked = totalStaked.sub(stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Claim staking reward
     */
    function claimReward() external nonReentrant {
        require(stakingEnd > block.timestamp, "Staking period ended");
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount found");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update staker information
        stakers[msg.sender].lastClaimed = block.timestamp;

        // Transfer reward to the user
        bogeToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate staking reward for a user
     * @param _user Address of the user
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        Staker memory staker = stakers[_user];
        uint256 timeElapsed = block.timestamp.sub(staker.lastClaimed);
        uint256 reward = timeElapsed.mul(rewardPerSecond).mul(staker.stakedAmount).div(totalStaked);
        return reward;
    }

    /**
     * @dev Struct to represent a staker
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastClaimed;
    }
}
```
