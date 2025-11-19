"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-in.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards proportionally to the percentage of the staking pool over a two-year period.
Generated: DETERMINISTIC_afe81618637d4d31
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake DOGE20 tokens and earn rewards over a two-year period.
 */
contract Doge20Staking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public token;

    // Staking pool
    uint256 public totalStaked;

    // Reward token address
    address public rewardToken;

    // Reward rate per second (2 years = 63072000 seconds)
    uint256 public rewardRate;

    // Reward duration in seconds
    uint256 public rewardDuration;

    // Last update timestamp
    uint256 public lastUpdateTime;

    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // User staking data
    mapping(address => UserInfo) public userInfo;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to store user staking data
    struct UserInfo {
        uint256 amount; // Staked amount
        uint256 rewardDebt; // Reward debt
        uint256 lastRewardClaimTime; // Last reward claim time
    }

    /**
     * @param _token DOGE20 token address
     * @param _rewardToken Reward token address
     * @param _rewardRate Reward rate per second
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _rewardRate
    ) public {
        token = IERC20(_token);
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        rewardDuration = 63072000; // 2 years in seconds
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking data
        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            // Calculate and pay rewards if any
            uint256 reward = getReward(msg.sender);
            if (reward > 0) {
                _safeTransfer(rewardToken, msg.sender, reward);
                emit RewardsClaimed(msg.sender, reward);
            }
        }

        // Update staking pool and user data
        totalStaked = totalStaked.add(_amount);
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DOGE20 tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update user staking data
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = getReward(msg.sender);
        if (reward > 0) {
            _safeTransfer(rewardToken, msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }

        // Update staking pool and user data
        totalStaked = totalStaked.sub(_amount);
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount);

        // Transfer tokens from contract to user
        token.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimReward() external {
        uint256 reward = getReward(msg.sender);
        if (reward > 0) {
            _safeTransfer(rewardToken, msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }
    }

    /**
     * @dev Get user reward
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 reward = 0;

        // Calculate reward
        if (user.amount > 0) {
            uint256 rewardPerToken = rewardPerTokenStored.add(
                (block.timestamp.sub(lastUpdateTime).mul(rewardRate))
            );
            reward = user.amount.mul(rewardPerToken.sub(user.rewardDebt)).div(1e18);
            user.rewardDebt = rewardPerToken;
        }

        return reward;
    }

    /**
     * @dev Update reward per token stored
     */
    function _updateRewardPerToken() internal {
        uint256 reward = rewardRate.mul(block.timestamp.sub(lastUpdateTime));
        rewardPerTokenStored = rewardPerTokenStored.add(reward.div(totalStaked));
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Safe transfer function
     * @param _token Token address
     * @param _to Recipient address
     * @param _amount Amount to transfer
     */
    function _safeTransfer(address _token, address _to, uint256 _amount) internal {
        IERC20(_token).safeTransfer(_to, _amount);
    }
}
```
