"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Create a DeFi staking contract that incorporates features for pledge mining and referral rewards, similar to the use cases mentioned on Trust Base.
Generated: DETERMINISTIC_5575bee0a7a8f3b0
Batch ID: 20250612_153814
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

/**
 * @title DeFiStaking
 * @dev A staking contract that allows users to stake tokens for rewards, 
 *      with features for pledge mining and referral rewards.
 */
contract DeFiStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt
        address referrer;   // Referrer address
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Events
    event Staked(address indexed user, uint256 amount, address indexed referrer);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     * @param referrer Address of the referrer.
     */
    function stake(uint256 amount, address referrer) external {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            // Update reward debt for existing staker
            uint256 pending = user.amount.mul(rewardPerBlock).sub(user.rewardDebt);
            if (pending > 0) {
                rewardToken.transfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        // Update user info
        user.amount = user.amount.add(amount);
        user.rewardDebt = user.amount.mul(rewardPerBlock);
        user.referrer = referrer;

        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount, referrer);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update reward debt before unstaking
        uint256 pending = user.amount.mul(rewardPerBlock).sub(user.rewardDebt);
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        // Update user info
        user.amount = user.amount.sub(amount);
        user.rewardDebt = user.amount.mul(rewardPerBlock);

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        totalStaked = totalStaked.sub(amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Update the reward per block.
     * @param _rewardPerBlock New reward per block.
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Withdraw tokens from the contract in case of emergency.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
