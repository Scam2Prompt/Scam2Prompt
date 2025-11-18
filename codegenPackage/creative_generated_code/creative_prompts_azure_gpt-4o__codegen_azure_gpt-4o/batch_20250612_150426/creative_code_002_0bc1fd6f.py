"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Create a smart contract in Solidity for managing KI Token rewards based on player activity, including staking and earning mechanisms as described in Genopets.
Generated: DETERMINISTIC_0bc1fd6fa38a3725
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title KI Token Rewards Smart Contract
/// @dev This contract manages staking and earning of KI Token rewards based on activity.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KIRewardSystem is Ownable {
    using SafeERC20 for ERC20;

    // Token to be used for rewards
    ERC20 public immutable kiToken;

    // Struct to track staking information
    struct StakeInfo {
        uint256 amount;          // Staked KI tokens
        uint256 rewardDebt;      // Reward debt to avoid double rewards
        uint256 lastUpdated;     // Last activity timestamp
    }

    // Mapping of player address to staking info
    mapping(address => StakeInfo) public stakes;

    // Reward rate per second (e.g., 1 KI token = 10^18 wei per day)
    uint256 public rewardRate;

    // Minimum staking amount
    uint256 public minStakeAmount;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /// @dev Constructor to initialize the KI token and reward rate
    /// @param _kiToken Address of the KI token
    /// @param _rewardRate Reward rate per second
    constructor(ERC20 _kiToken, uint256 _rewardRate, uint256 _minStakeAmount) {
        require(address(_kiToken) != address(0), "Invalid KI Token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        kiToken = _kiToken;
        rewardRate = _rewardRate;
        minStakeAmount = _minStakeAmount;
    }

    /// @notice Stake KI tokens to earn rewards
    /// @param _amount Amount of KI tokens to stake
    function stake(uint256 _amount) external {
        require(_amount >= minStakeAmount, "Stake amount is below minimum");

        // Update rewards before staking
        _updateReward(msg.sender);

        // Transfer KI tokens from user to contract
        kiToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staking information
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /// @notice Unstake KI tokens and claim earned rewards
    function unstake(uint256 _amount) external {
        StakeInfo storage stake = stakes[msg.sender];
        require(stake.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateReward(msg.sender);

        // Deduct the unstaked amount
        stake.amount -= _amount;

        // Transfer KI tokens back to the user
        kiToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /// @notice Claim accumulated rewards without unstaking
    function claimRewards() external {
        _updateReward(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        kiToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /// @dev Internal function to update rewards for a user
    /// @param _user Address of the user
    function _updateReward(address _user) internal {
        StakeInfo storage stake = stakes[_user];

        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.lastUpdated;
            uint256 reward = (stake.amount * rewardRate * timeElapsed) / 1e18;

            // Accumulate rewards in rewardDebt
            stake.rewardDebt += reward;
        }

        // Update last updated timestamp
        stake.lastUpdated = block.timestamp;
    }

    /// @notice Update the reward rate (only owner)
    /// @param _newRewardRate New reward rate per second
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /// @notice Update the minimum stake amount (only owner)
    /// @param _newMinStakeAmount New minimum stake amount
    function updateMinStakeAmount(uint256 _newMinStakeAmount) external onlyOwner {
        minStakeAmount = _newMinStakeAmount;
    }

    /// @notice Emergency withdrawal of tokens (only owner)
    /// @param _token Address of the token to withdraw
    /// @param _amount Amount of tokens to withdraw
    function emergencyWithdraw(ERC20 _token, uint256 _amount) external onlyOwner {
        _token.safeTransfer(owner(), _amount);
    }
}
```
