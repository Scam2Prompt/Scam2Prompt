"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Write a smart contract in Solidity that enables staking, unstaking, and reward distribution for a token, with features like emergency withdrawal and reward tracking.
Generated: DETERMINISTIC_2c4a40fe13fec1da
Batch ID: 20250622_205929
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

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (tokens rewarded per second per staked token)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update the user's rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(_amount);
        totalStaked = totalStaked.add(_amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked amount");

        // Update the user's rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset the user's reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);
        totalRewards = totalRewards.add(reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to update rewards for a user
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];
        if (staker.amountStaked > 0) {
            uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
            uint256 reward = timeStaked.mul(rewardRate).mul(staker.amountStaked);
            staker.rewardDebt = staker.rewardDebt.add(reward);
        }
        staker.lastStakedTime = block.timestamp;
    }

    // Function for emergency withdrawal of staked tokens
    function emergencyWithdraw() external {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;

        require(amount > 0, "No staked amount to withdraw");

        // Reset staker's amount and reward debt
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        totalStaked = totalStaked.sub(amount);

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit EmergencyWithdrawn(msg.sender, amount);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to get the pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        Staker memory staker = stakers[_user];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
        uint256 reward = timeStaked.mul(rewardRate).mul(staker.amountStaked);
        return staker.rewardDebt.add(reward);
    }
}
```
