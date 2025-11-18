"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales99bitcoins.pages.dev
Prompt: Generate code to stake $99BTC tokens on the Ethereum blockchain using a smart contract. Ensure the code calculates dynamic rewards based on the staking pool percentage.
Generated: DETERMINISTIC_a97eaff61a201381
Batch ID: 20250612_152235
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

// Staking contract to stake 99BTC tokens and calculate dynamic rewards
contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Structure to hold user staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event for staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake and total staked amount
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = calculateReward(userStake.amount);
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user's stake and total staked amount
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the user's stake
    function calculateReward(uint256 _userStake) internal view returns (uint256) {
        if (totalStaked == 0) return 0;
        return (_userStake * totalRewards) / totalStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(userStake.amount) - userStake.rewardDebt;

        require(reward > 0, "No rewards available to claim");

        // Update user's reward debt to the current state
        userStake.rewardDebt = calculateReward(userStake.amount);
        
        // Transfer rewards to user (Assuming rewards are in the stakingToken)
        stakingToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to set total distributed rewards (Owner only)
    function setTotalRewards(uint256 _totalRewards) external onlyOwner {
        totalRewards = _totalRewards;
    }

    // Function to get user's stake information
    function getUserStake(address _user) external view returns (uint256 amount, uint256 rewardDebt) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.rewardDebt);
    }

    // Function to view total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
