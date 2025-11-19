"""
Generated Code Metadata:
========================
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards proportionally to stakers over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_0b524440a48d9a87
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake DOGE20 tokens and distributes rewards proportionally over a two-year period.
 */
contract Doge20Staking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public token;

    // Reward token contract instance
    IERC20 public rewardToken;

    // Staker struct to hold staking information
    struct Staker {
        uint256 amount; // Staked amount
        uint256 rewardDebt; // Reward debt
        uint256 lastStakeTime; // Last stake time
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward distributed
    uint256 public totalRewardDistributed;

    // Reward per second
    uint256 public rewardPerSecond;

    // Two-year period in seconds
    uint256 public constant TWO_YEARS = 63072000;

    // Start time of staking
    uint256 public startTime;

    // End time of staking
    uint256 public endTime;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token Token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _rewardPerSecond
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerSecond > 0, "Reward per second must be greater than zero");

        token = IERC20(_token);
        rewardToken = IERC20(_rewardToken);
        rewardPerSecond = _rewardPerSecond;
        startTime = block.timestamp;
        endTime = startTime.add(TWO_YEARS);
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakers[msg.sender].amount.add(_amount) <= token.balanceOf(msg.sender), "Insufficient balance");

        Staker storage staker = stakers[msg.sender];

        if (staker.amount > 0) {
            _distributeReward(msg.sender);
        }

        staker.amount = staker.amount.add(_amount);
        staker.lastStakeTime = block.timestamp;
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);

        token.SafeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake DOGE20 tokens
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];

        require(staker.amount > 0, "Staker has no staked tokens");

        _distributeReward(msg.sender);

        uint256 stakedAmount = staker.amount;
        staker.amount = 0;
        staker.rewardDebt = 0;

        totalStaked = totalStaked.sub(stakedAmount);

        token.SafeTransfer(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Distribute reward to staker
     * @param _user User address
     */
    function _distributeReward(address _user) internal {
        Staker storage staker = stakers[_user];

        uint256 reward = _calculateReward(staker);

        if (reward > 0) {
            staker.rewardDebt = staker.rewardDebt.sub(reward);
            totalRewardDistributed = totalRewardDistributed.add(reward);

            rewardToken.SafeTransfer(_user, reward);

            emit RewardDistributed(_user, reward);
        }
    }

    /**
     * @notice Calculate reward for staker
     * @param _staker Staker struct
     * @return Reward amount
     */
    function _calculateReward(Staker storage _staker) internal view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(_staker.lastStakeTime);
        uint256 reward = stakedDuration.mul(rewardPerSecond).mul(_staker.amount).div(totalStaked);

        // Ensure reward is not distributed after end time
        if (block.timestamp > endTime) {
            reward = 0;
        }

        return reward;
    }

    /**
     * @notice Update reward per second
     * @param _newRewardPerSecond New reward per second
     */
    function updateRewardPerSecond(uint256 _newRewardPerSecond) external onlyOwner {
        rewardPerSecond = _newRewardPerSecond;
    }

    /**
     * @notice Withdraw reward tokens
     */
    function withdrawReward() external {
        uint256 reward = _calculateReward(stakers[msg.sender]);

        require(reward > 0, "No reward to withdraw");

        stakers[msg.sender].rewardDebt = stakers[msg.sender].rewardDebt.sub(reward);

        rewardToken.SafeTransfer(msg.sender, reward);

        emit RewardDistributed(msg.sender, reward);
    }
}
```
