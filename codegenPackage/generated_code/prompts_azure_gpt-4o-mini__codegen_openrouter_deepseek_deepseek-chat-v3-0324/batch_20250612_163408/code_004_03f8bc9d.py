"""
Generated Code Metadata:
========================
Original URL: https://docs.matrixinfos.com
Prompt: Develop a Solidity contract that facilitates the staking of $MATRIX Tokens, ensuring decentralized governance and user privacy.
Generated: DETERMINISTIC_03f8bc9d3a6d8f47
Batch ID: 20250612_163408
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MatrixTokenStaking
 * @dev A contract that allows users to stake $MATRIX Tokens for rewards while ensuring decentralized governance and privacy.
 */
contract MatrixTokenStaking is ReentrancyGuard, Ownable {
    IERC20 public matrixToken;

    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool active;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public userStakes;

    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public stakingDuration;
    uint256 public rewardRate; // Rewards per token per second

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event GovernanceUpdated(address indexed owner, uint256 newMinStake, uint256 newDuration, uint256 newRate);

    /**
     * @dev Initializes the contract with the $MATRIX Token address and staking parameters.
     * @param _matrixToken Address of the $MATRIX Token contract.
     * @param _minStakeAmount Minimum amount of tokens required to stake.
     * @param _stakingDuration Duration (in seconds) for which tokens must be staked.
     * @param _rewardRate Reward rate (per token per second).
     */
    constructor(
        address _matrixToken,
        uint256 _minStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardRate
    ) {
        require(_matrixToken != address(0), "Invalid token address");
        matrixToken = IERC20(_matrixToken);
        minStakeAmount = _minStakeAmount;
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake $MATRIX Tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(matrixToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        userStakes[msg.sender].push(Stake({
            amount: amount,
            timestamp: block.timestamp,
            active: true
        }));

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     * @param stakeIndex The index of the stake to unstake.
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.active, "Stake already withdrawn");

        uint256 stakedAmount = userStake.amount;
        uint256 stakedTime = block.timestamp - userStake.timestamp;
        require(stakedTime >= stakingDuration, "Staking period not ended");

        uint256 reward = calculateReward(stakedAmount, stakedTime);
        userStake.active = false;

        uint256 totalToTransfer = stakedAmount + reward;
        require(matrixToken.transfer(msg.sender, totalToTransfer), "Transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculates the reward for a given stake amount and duration.
     * @param amount The staked amount.
     * @param duration The duration of the stake in seconds.
     * @return The calculated reward.
     */
    function calculateReward(uint256 amount, uint256 duration) public view returns (uint256) {
        return amount * duration * rewardRate / 1e18;
    }

    /**
     * @dev Updates staking parameters (only callable by owner).
     * @param newMinStake New minimum stake amount.
     * @param newDuration New staking duration.
     * @param newRate New reward rate.
     */
    function updateGovernanceParameters(
        uint256 newMinStake,
        uint256 newDuration,
        uint256 newRate
    ) external onlyOwner {
        minStakeAmount = newMinStake;
        stakingDuration = newDuration;
        rewardRate = newRate;

        emit GovernanceUpdated(msg.sender, newMinStake, newDuration, newRate);
    }

    /**
     * @dev Gets the number of stakes for a user.
     * @param user The address of the user.
     * @return The number of stakes.
     */
    function getUserStakesCount(address user) external view returns (uint256) {
        return userStakes[user].length;
    }
}
```
