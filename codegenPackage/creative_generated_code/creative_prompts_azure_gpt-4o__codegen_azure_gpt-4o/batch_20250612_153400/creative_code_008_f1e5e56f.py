"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge-live.pages.dev
Prompt: Generate a Solidity contract that mirrors the DOGE20 staking rewards system, including dynamic reward rates and per-block payouts.
Generated: DETERMINISTIC_f1e5e56f3d0ab1c3
Batch ID: 20250612_153400
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

/**
 * @title DOGE20 Staking Rewards System
 * @notice This contract implements a staking system with dynamic reward rates and per-block payouts.
 */
contract Doge20StakingRewards {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public immutable stakingToken; // Token used for staking
    IERC20 public immutable rewardToken;  // Token used for rewards

    uint256 public rewardRate; // Rewards per block
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public lastRewardBlock; // Last block when rewards were calculated
    
    mapping(address => uint256) public stakedBalance; // Tracks staked balance per user
    mapping(address => uint256) public rewardDebt;    // Tracks rewards per user

    // Events
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event ClaimRewards(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    modifier updateRewards(address _user) {
        _updateRewards(_user);
        _;
    }

    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens to earn rewards.
     * @param _amount Amount of staking tokens to deposit.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than 0");
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        stakedBalance[msg.sender] += _amount;
        totalStaked += _amount;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens and optionally claim accumulated rewards.
     * @param _amount Amount of staking tokens to withdraw.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakedBalance[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalance[msg.sender] -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = pendingRewards(msg.sender);
        rewardDebt[msg.sender] = stakedBalance[msg.sender] * rewardRate;
        
        if (rewards > 0) {
            rewardToken.transfer(msg.sender, rewards);
            emit ClaimRewards(msg.sender, rewards);
        }
    }

    /**
     * @notice View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) public view returns (uint256) {
        uint256 accruedRewards = stakedBalance[_user] * rewardRate * (block.number - lastRewardBlock);
        return accruedRewards + rewardDebt[_user];
    }

    /**
     * @notice Internal function to update user rewards.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        if (block.number > lastRewardBlock) {
            lastRewardBlock = block.number;
        }

        uint256 rewards = pendingRewards(_user);
        rewardDebt[_user] = stakedBalance[_user] * rewardRate;

        if (rewards > 0) {
            rewardToken.transfer(_user, rewards);
            emit ClaimRewards(_user, rewards);
        }
    }

    /**
     * @notice Update reward rate (callable by owner/admin only).
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _newRewardRate) external {
        // Access control mechanism (e.g., onlyOwner) should be implemented here.
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }
}
```
