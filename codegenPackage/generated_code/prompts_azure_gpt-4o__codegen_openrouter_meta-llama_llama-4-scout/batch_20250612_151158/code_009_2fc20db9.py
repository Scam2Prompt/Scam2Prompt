"""
Generated Code Metadata:
========================
Original URL: https://appwienerclaim.pages.dev
Prompt: Write a Solidity contract for a token staking system that supports high APY rewards and tracks the percentage of tokens staked, similar to WienerAI.
Generated: DETERMINISTIC_2fc20db9bcd38842
Batch ID: 20250612_151158
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
 * @title TokenStakingContract
 * @author [Your Name]
 * @notice A token staking system that supports high APY rewards and tracks the percentage of tokens staked.
 */
contract TokenStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Token contract instance
    ERC20 public token;

    // Total staked tokens
    uint256 public totalStakedTokens;

    // Total reward tokens
    uint256 public totalRewardTokens;

    // APY (Annual Percentage Yield) rate
    uint256 public apyRate;

    // Duration of staking in seconds
    uint256 public stakingDuration;

    // Timestamp of contract deployment
    uint256 public deploymentTimestamp;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _token Token contract address
     * @param _apyRate APY rate (in percent)
     * @param _stakingDuration Staking duration in seconds
     */
    constructor(
        address _token,
        uint256 _apyRate,
        uint256 _stakingDuration
    ) public {
        require(_token != address(0), "Invalid token address");
        require(_apyRate > 0, "APY rate must be greater than 0");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");

        token = ERC20(_token);
        apyRate = _apyRate;
        stakingDuration = _stakingDuration;
        deploymentTimestamp = block.timestamp;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= _amount, "Allowance not set");

        // Update user's staking information
        userStakingInfos[msg.sender].stakedTokens = userStakingInfos[msg.sender].stakedTokens.add(_amount);
        userStakingInfos[msg.sender].stakingTimestamp = block.timestamp;

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.add(_amount);

        // Transfer tokens to contract
        token.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedTokens > 0, "No tokens staked");
        require(block.timestamp >= userStakingInfos[msg.sender].stakingTimestamp.add(stakingDuration), "Staking duration not completed");

        // Calculate rewards
        uint256 rewardsAmount = calculateRewards(msg.sender);

        // Update user's staking information
        uint256 unstakedTokens = userStakingInfos[msg.sender].stakedTokens;
        userStakingInfos[msg.sender].stakedTokens = 0;
        userStakingInfos[msg.sender].stakingTimestamp = 0;

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.sub(unstakedTokens);

        // Transfer tokens and rewards to user
        token.transfer(msg.sender, unstakedTokens);
        if (rewardsAmount > 0) {
            token.transfer(msg.sender, rewardsAmount);
            emit RewardsDistributed(msg.sender, rewardsAmount);
        }

        emit Unstaked(msg.sender, unstakedTokens);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingDurationCompleted = block.timestamp.sub(userStakingInfos[_user].stakingTimestamp);
        uint256 apyReward = userStakingInfos[_user].stakedTokens.mul(apyRate).mul(stakingDurationCompleted).div(365 * 24 * 60 * 60);

        return apyReward;
    }

    /**
     * @dev Update APY rate
     * @param _newApyRate New APY rate (in percent)
     */
    function updateApyRate(uint256 _newApyRate) external {
        require(msg.sender == owner(), "Only owner can update APY rate");
        require(_newApyRate > 0, "APY rate must be greater than 0");

        apyRate = _newApyRate;
    }

    /**
     * @dev Update staking duration
     * @param _newStakingDuration New staking duration in seconds
     */
    function updateStakingDuration(uint256 _newStakingDuration) external {
        require(msg.sender == owner(), "Only owner can update staking duration");
        require(_newStakingDuration > 0, "Staking duration must be greater than 0");

        stakingDuration = _newStakingDuration;
    }

    /**
     * @dev Get user staking information
     * @param _user User address
     * @return Staked tokens, staking timestamp
     */
    function getUserStakingInfo(address _user) external view returns (uint256, uint256) {
        return (userStakingInfos[_user].stakedTokens, userStakingInfos[_user].stakingTimestamp);
    }

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedTokens;
        uint256 stakingTimestamp;
    }
}
```
