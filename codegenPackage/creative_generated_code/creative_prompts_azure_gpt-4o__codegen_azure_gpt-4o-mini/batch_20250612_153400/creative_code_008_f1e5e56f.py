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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is Ownable {
    // ERC20 token to be staked
    IERC20 public stakingToken;

    // Reward variables
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock;

    // User stakes and rewards
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => UserInfo) public userInfo;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    // Modifier to update rewards before any staking/unstaking
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardRate;
            for (address userAddress : users) {
                UserInfo storage user = userInfo[userAddress];
                if (user.amount > 0) {
                    uint256 userReward = (user.amount * reward) / totalStaked;
                    user.rewardDebt += userReward;
                }
            }
        }
        lastRewardBlock = block.number;
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Transfer the staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external updateRewards {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update total staked amount
        user.amount -= amount;
        totalStaked -= amount;

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
        payReward(msg.sender); // Pay reward upon unstaking
    }

    // Function to calculate and pay rewards to the user
    function payReward(address userAddress) internal {
        UserInfo storage user = userInfo[userAddress];
        uint256 reward = user.rewardDebt;
        if (reward > 0) {
            user.rewardDebt = 0; // Reset reward debt
            // Transfer the reward (in tokens or ETH as applicable) to the user
            stakingToken.transfer(userAddress, reward);
            emit RewardPaid(userAddress, reward);
        }
    }

    // Function to change the reward rate (only by owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
