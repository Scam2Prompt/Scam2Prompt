"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum, ensuring rewards distribution over a two-year period based on the percentage of the staking pool.
Generated: DETERMINISTIC_089bf7122095e99b
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake DOGE20 tokens and earn rewards over a two-year period.
 */
contract Doge20StakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // DOGE20 token contract
    IERC20 public doge20Token;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Reward token contract (assuming DAI for simplicity)
    IERC20 public rewardToken;

    // Total reward amount to be distributed over 2 years
    uint256 public totalRewardAmount;

    // Reward distribution period in seconds (2 years)
    uint256 public rewardDistributionPeriod;

    // Start time of reward distribution
    uint256 public rewardDistributionStartTime;

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastRewardClaimTime;
    }

    /**
     * @notice Constructor
     * @param _doge20TokenAddress DOGE20 token contract address
     * @param _rewardTokenAddress Reward token contract address
     */
    constructor(address _doge20TokenAddress, address _rewardTokenAddress) public {
        require(_doge20TokenAddress != address(0), "DOGE20 token address cannot be zero");
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");

        doge20Token = IERC20(_doge20TokenAddress);
        rewardToken = IERC20(_rewardTokenAddress);

        // Assuming 1 million reward tokens to be distributed over 2 years
        totalRewardAmount = 1000000 * 10**18; // 10**18 for 18 decimals (DAI)
        rewardDistributionPeriod = 2 * 365 * 24 * 60 * 60; // 2 years in seconds
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param _amount Amount of DOGE20 tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Failed to transfer DOGE20 tokens");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        totalStakedAmount = totalStakedAmount.add(_amount);

        if (userStakingInfo.stakedAmount == _amount) {
            userStakingInfo.lastRewardClaimTime = block.timestamp;
            userStakingInfo.rewardDebt = 0;
        } else {
            _updateRewardDebt(msg.sender);
        }
    }

    /**
     * @notice Unstake DOGE20 tokens
     * @param _amount Amount of DOGE20 tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Unstake amount exceeds staked amount");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);
        totalStakedAmount = totalStakedAmount.sub(_amount);

        require(doge20Token.transfer(msg.sender, _amount), "Failed to transfer DOGE20 tokens");

        _updateRewardDebt(msg.sender);
    }

    /**
     * @notice Claim rewards
     */
    function claimReward() external {
        _updateRewardDebt(msg.sender);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        uint256 reward = _calculateReward(msg.sender);

        userStakingInfo.rewardDebt = 0;
        userStakingInfo.lastRewardClaimTime = block.timestamp;

        require(rewardToken.transfer(msg.sender, reward), "Failed to transfer reward tokens");
    }

    /**
     * @dev Update reward debt for a user
     * @param _user User address
     */
    function _updateRewardDebt(address _user) internal {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        if (userStakingInfo.stakedAmount > 0) {
            uint256 reward = _calculateReward(_user);
            userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.add(reward);
        }
    }

    /**
     * @dev Calculate reward for a user
     * @param _user User address
     * @return Reward amount
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        uint256 stakedDuration = block.timestamp.sub(userStakingInfo.lastRewardClaimTime);
        uint256 totalStakedDuration = rewardDistributionPeriod;

        if (stakedDuration > totalStakedDuration) {
            stakedDuration = totalStakedDuration;
        }

        uint256 userStakedPercentage = userStakingInfo.stakedAmount.mul(100).div(totalStakedAmount);
        uint256 reward = totalRewardAmount.mul(stakedDuration).div(totalStakedDuration).mul(userStakedPercentage).div(100);

        return reward;
    }

    /**
     * @dev Update reward distribution start time
     * @param _startTime New start time
     */
    function updateRewardDistributionStartTime(uint256 _startTime) external onlyOwner {
        rewardDistributionStartTime = _startTime;
    }

    /**
     * @dev Update total reward amount
     * @param _newTotalRewardAmount New total reward amount
     */
    function updateTotalRewardAmount(uint256 _newTotalRewardAmount) external onlyOwner {
        totalRewardAmount = _newTotalRewardAmount;
    }
}
```
