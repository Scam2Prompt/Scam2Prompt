"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Generate a code snippet for a decentralized finance (DeFi) application that utilizes staking and farming features as described on EasyCake.
Generated: DETERMINISTIC_ba09d34743944c41
Batch ID: 20250612_160002
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

/**
 * @title EasyCake DeFi Staking and Farming Contract
 * @dev This contract allows users to stake tokens and earn rewards through farming.
 */
contract EasyCake is Ownable {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Reward debt of the user
    }

    // Mapping of users to their information
    mapping(address => UserInfo) public userInfo;
    
    // The staked token
    IERC20 public stakedToken;
    
    // The reward token
    IERC20 public rewardToken;
    
    // Total amount of staked tokens
    uint256 public totalStaked;
    
    // Reward per block
    uint256 public rewardPerBlock;
    
    // Last block number where rewards were distributed
    uint256 public lastRewardBlock;

    // Events for staking and harvesting
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 amount);

    /**
     * @dev Constructor for initializing the contract.
     * @param _stakedToken Address of the token to be staked.
     * @param _rewardToken Address of the token to be rewarded.
     * @param _rewardPerBlock Amount of reward tokens distributed per block.
     */
    constructor(address _stakedToken, address _rewardToken, uint256 _rewardPerBlock) {
        stakedToken = IERC20(_stakedToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        UserInfo storage user = userInfo[msg.sender];

        // Update user rewards and total staked amount
        updateRewards();

        // Transfer tokens from user to contract
        stakedToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and harvest rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance to unstake");

        // Update user rewards and total staked amount
        updateRewards();

        // Transfer tokens from contract back to user
        user.amount -= _amount;
        totalStaked -= _amount;

        stakedToken.transfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);

        // Harvest rewards
        harvest();
    }

    /**
     * @dev Harvest the rewards earned by the user.
     */
    function harvest() public {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.amount * (block.number - lastRewardBlock) * rewardPerBlock) / totalStaked;
        
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending);
            emit Harvested(msg.sender, pending);
        }
        
        user.rewardDebt += pending;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update rewards for all users.
     */
    function updateRewards() internal {
        if (totalStaked > 0) {
            // Update rewards for all users
            uint256 multiplier = block.number - lastRewardBlock;
            uint256 reward = multiplier * rewardPerBlock;

            // Update last reward block
            lastRewardBlock = block.number;
        }
    }

    /**
     * @dev Set new reward per block (owner only).
     * @param _rewardPerBlock New reward per block.
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```
