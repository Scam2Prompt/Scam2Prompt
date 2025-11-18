"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogeverse-com.pages.dev
Prompt: Write a smart contract in Solidity for staking $DOGEVERSE tokens on the Ethereum blockchain, ensuring dynamic reward rates over time as described in the Dogeverse staking documentation.
Generated: DETERMINISTIC_47746559d40333e7
Batch ID: 20250612_150946
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

// Staking contract for $DOGEVERSE tokens
contract DogeverseStaking is Ownable {
    // Token to stake
    IERC20 public dogeverseToken;

    // Struct to hold user staking data
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt
    }

    // Mapping of user address to their staking data
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;

    // Dynamic reward rate (in tokens per block)
    uint256 public rewardRate;

    // Last block number when rewards were updated
    uint256 public lastRewardBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    // Constructor to set the token address and initial reward rate
    constructor(IERC20 _dogeverseToken, uint256 _initialRewardRate) {
        dogeverseToken = _dogeverseToken;
        rewardRate = _initialRewardRate;
        lastRewardBlock = block.number;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        
        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        dogeverseToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user info
        user.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to user
        user.amount -= _amount;
        totalStaked -= _amount;
        dogeverseToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to update rewards based on the current state
    function _updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        
        // Calculate pending rewards
        uint256 pending = (user.amount * rewardRate * (block.number - lastRewardBlock)) / 1e18;
        
        // Update user's reward debt
        user.rewardDebt += pending;

        // Update last reward block
        lastRewardBlock = block.number;
    }

    // Function to set a new dynamic reward rate
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    // Function to withdraw all tokens (only in case of emergency)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = dogeverseToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        dogeverseToken.transfer(msg.sender, balance);
    }
}
```
