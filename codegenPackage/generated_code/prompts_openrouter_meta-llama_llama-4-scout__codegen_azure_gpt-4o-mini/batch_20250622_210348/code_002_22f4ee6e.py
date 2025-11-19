"""
Generated Code Metadata:
========================
Original URL: https://stethclaim.pages.dev
Prompt: "Generate a Solidity smart contract code snippet for a staking rewards pool similar to stETH, with features like APY calculation, multiplier application, and reward claiming."
Generated: DETERMINISTIC_22f4ee6eb9a19074
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingRewardsPool is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;
    // Token for rewards
    IERC20 public rewardsToken;

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total staked amount
    uint256 public totalStaked;
    // APY (Annual Percentage Yield) in basis points (e.g., 500 = 5%)
    uint256 public apy;
    // Multiplier for rewards
    uint256 public rewardMultiplier;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardsToken, uint256 _apy, uint256 _rewardMultiplier) {
        stakingToken = _stakingToken;
        rewardsToken = _rewardsToken;
        apy = _apy;
        rewardMultiplier = _rewardMultiplier;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        updateRewards(msg.sender);

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);
        user.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        updateRewards(msg.sender);

        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        UserInfo storage user = userInfo[msg.sender];
        uint256 pendingRewards = user.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");
        user.rewardDebt = 0; // Reset reward debt

        rewardsToken.transfer(msg.sender, pendingRewards);
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to update rewards for a user
    function updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        if (user.amount > 0) {
            uint256 timeStaked = block.timestamp.sub(user.lastStakedTime);
            uint256 reward = calculateReward(user.amount, timeStaked);
            user.rewardDebt = user.rewardDebt.add(reward);
        }
        user.lastStakedTime = block.timestamp;
    }

    // Function to calculate rewards based on staked amount and time
    function calculateReward(uint256 _amount, uint256 _timeStaked) internal view returns (uint256) {
        // APY is in basis points, convert to a percentage
        uint256 reward = _amount.mul(apy).mul(_timeStaked).div(365 days).div(10000);
        return reward.mul(rewardMultiplier).div(100); // Apply multiplier
    }

    // Function to set new APY
    function setAPY(uint256 _apy) external onlyOwner {
        apy = _apy;
    }

    // Function to set new reward multiplier
    function setRewardMultiplier(uint256 _multiplier) external onlyOwner {
        rewardMultiplier = _multiplier;
    }
}
```
