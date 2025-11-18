"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyai-claim.pages.dev
Prompt: Develop a Solidity smart contract function that distributes $SCOTTY staking rewards dynamically based on the user's share of the pool and the current reward rate of 82.5 $SCOTTY per ETH block.
Generated: DETERMINISTIC_f851472c3d5dbaf3
Batch ID: 20250612_152109
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

contract ScottyStaking is Ownable {
    // ERC20 token contract for $SCOTTY
    IERC20 public scottyToken;

    // Reward rate is fixed at 82.5 $SCOTTY per ETH block
    uint256 public constant REWARD_RATE = 82.5 ether; // using ether for fixed-point decimals (1 ether = 10^18)

    // Struct to hold user information
    struct UserInfo {
        uint256 amount;      // Amount of tokens staked by the user
        uint256 rewardDebt;  // Amount of $SCOTTY owed to the user
    }

    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;
    
    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $SCOTTY token address
    constructor(IERC20 _scottyToken) {
        scottyToken = _scottyToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];

        // Update user's reward debt before changing the state
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        scottyToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's staked amount and total staked amount
        user.amount += _amount;
        totalStaked += _amount;
    }

    // Function to withdraw tokens and claim rewards
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];

        require(user.amount >= _amount, "Insufficient balance to withdraw");

        // Update rewards before state changes
        _updateRewards(msg.sender);

        // Update user's staked amount and total staked amount
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        scottyToken.transfer(msg.sender, _amount);
    }

    // Internal function to update and distribute rewards to a user
    function _updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        
        // Calculate pending rewards based on the user's share
        uint256 pendingRewards = (user.amount * REWARD_RATE) / totalStaked - user.rewardDebt;

        // If there are pending rewards, transfer them to the user
        if (pendingRewards > 0) {
            // Update the user's reward debt
            user.rewardDebt += pendingRewards;

            // Transfer the calculated rewards to the user
            require(scottyToken.balanceOf(address(this)) >= pendingRewards, "Insufficient contract balance for rewards");
            scottyToken.transfer(_user, pendingRewards);
            
            // Emit an event for rewards distribution
            emit RewardsDistributed(_user, pendingRewards);
        }
    }

    // Function to view user's pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        if (totalStaked == 0) return 0;

        uint256 pending = (user.amount * REWARD_RATE) / totalStaked - user.rewardDebt;
        return pending;
    }
}
```
