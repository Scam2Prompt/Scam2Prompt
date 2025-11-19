"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Develop a staking and liquidity providing system using PepeSwap's innovative passive income reward system.
Generated: DETERMINISTIC_eaac59a06131d7fb
Batch ID: 20250622_212746
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking and Liquidity Providing Contract
contract PepeSwapStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Token being staked
    IERC20 public stakingToken;
    // Reward token
    IERC20 public rewardToken;

    // Total staked tokens
    uint256 public totalStaked;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Reward per block
    uint256 public rewardPerBlock;

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to update rewards for a user
    function updateUserRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        if (user.amount > 0) {
            uint256 pendingReward = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
            if (pendingReward > 0) {
                rewardToken.transfer(_user, pendingReward);
                emit RewardClaimed(_user, pendingReward);
            }
        }
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update rewards before staking
        updateUserRewards(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateUserRewards(msg.sender);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        // Update user info
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to update rewards periodically (to be called by an external scheduler)
    function updateRewards() external {
        // Calculate new rewards
        uint256 blocks = block.number.sub(totalStaked);
        if (blocks > 0) {
            uint256 newRewards = blocks.mul(rewardPerBlock);
            accRewardPerShare = accRewardPerShare.add(newRewards.mul(1e12).div(totalStaked));
        }
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
