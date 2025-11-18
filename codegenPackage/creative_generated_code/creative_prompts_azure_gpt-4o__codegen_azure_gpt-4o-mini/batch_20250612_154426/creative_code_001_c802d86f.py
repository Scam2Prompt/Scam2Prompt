"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-1rj55ugoo-percenal-miketoken.vercel.app
Prompt: Generate Solidity code for creating a farming pool smart contract that rewards users for staking Mike Token ($MKT), ensuring safety through audits.
Generated: DETERMINISTIC_c802d86f6b967289
Batch ID: 20250612_154426
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

// FarmingPool contract for staking $MKT tokens and earning rewards
contract FarmingPool is Ownable {
    // Declare state variables
    IERC20 public token; // Reference to $MKT token
    uint256 public rewardRate; // Rate at which rewards are calculated
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewards; // Total rewards distributed

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => StakeInfo) private stakes; // Tracking user stakes
    mapping(address => uint256) private rewards; // Tracking user rewards

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the token and reward rate
    constructor(IERC20 _token, uint256 _rewardRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens in the pool
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += _amount;
        stakeInfo.rewardDebt = pendingReward(msg.sender); // Update reward debt for the user

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= _amount, "Insufficient staked amount");

        // Calculate and distribute rewards before withdrawal
        distributeRewards(msg.sender);

        // Update user's stake information
        stakeInfo.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimReward() external {
        distributeRewards(msg.sender);
    }

    // Internal function to distribute rewards to the user
    function distributeRewards(address _user) internal {
        uint256 reward = pendingReward(_user);
        require(reward > 0, "No reward available to claim");

        // Update the user's reward debt
        stakes[_user].rewardDebt = 0;
        rewards[_user] += reward;
        totalRewards += reward;

        // Transfer rewards to the user (assumed the contract itself has sufficient balance)
        payable(_user).transfer(reward);

        emit RewardClaimed(_user, reward);
    }

    // Function to calculate pending rewards for a user
    function pendingReward(address _user) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[_user];
        return (stakeInfo.amount * rewardRate) - stakeInfo.rewardDebt;
    }

    // Function to withdraw the contract's balance (only owner)
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(_amount > 0, "Amount must be greater than zero");

        payable(_to).transfer(_amount);
    }
}
```
