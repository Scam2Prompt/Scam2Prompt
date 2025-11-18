"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Write code to implement staking rewards for $DOP tokens, ensuring users can check their current rewards allocation.
Generated: DETERMINISTIC_8ec16701efa8f208
Batch ID: 20250612_150234
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract allows users to stake $DOP tokens and earn rewards.
contract StakingRewards is Ownable {
    // Token contract to be used for staking and rewards
    IERC20 public dopToken;

    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Amount of rewards owed to the user
    }

    // Mapping of user address to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Last update block for rewards
    uint256 public lastRewardBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token and reward rate
    constructor(IERC20 _dopToken, uint256 _rewardRate) {
        dopToken = _dopToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    // Modifier to update rewards before any staking actions
    modifier updateRewards() {
        uint256 multiplier = block.number - lastRewardBlock;
        if (totalStaked > 0 && multiplier > 0) {
            uint256 reward = multiplier * rewardRate;
            accRewardPerShare += reward * 1e12 / totalStaked;
        }
        lastRewardBlock = block.number;
        _;
    }

    // Function for users to stake their $DOP tokens
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];

        // Transfer tokens from user to contract
        dopToken.transferFrom(msg.sender, address(this), _amount);

        // Update user information
        user.amount += _amount;
        user.rewardDebt = user.amount * accRewardPerShare / 1e12;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function for users to unstake their $DOP tokens
    function unstake(uint256 _amount) external updateRewards {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update user's reward debt before unstaking
        uint256 pendingRewards = (user.amount * accRewardPerShare / 1e12) - user.rewardDebt;

        // Transfer pending rewards if any
        if (pendingRewards > 0) {
            dopToken.transfer(msg.sender, pendingRewards);
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        // Update user state and total staked amount
        user.amount -= _amount;
        user.rewardDebt = user.amount * accRewardPerShare / 1e12;
        totalStaked -= _amount;

        // Transfer the staked tokens back to the user
        dopToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to check current rewards allocation for a user
    function checkRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccumulated = user.amount * accRewardPerShare / 1e12;
        return currentAccumulated - user.rewardDebt;
    }
}
```
