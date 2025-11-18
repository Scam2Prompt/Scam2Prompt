"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepelive.com
Prompt: Generate code to implement a staking mechanism for WEPE tokens, referencing the staking features described on the Wall Street Pepe website.
Generated: DETERMINISTIC_0b16a999fc83c1f3
Batch ID: 20250612_153812
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WEPEStaking is Ownable {
    using SafeMath for uint256;

    // The WEPE token contract
    IERC20 public wepeToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount;         // Amount of WEPE staked
        uint256 timestamp;      // Timestamp of when the stake was made
    }

    // Mapping of user address to their stake data
    mapping(address => Stake) public stakes;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Reward rate per second (in WEPE tokens)
    uint256 public rewardRate = 1e18; // Example: 1 WEPE per second
    
    // Total supply of staked WEPE tokens
    uint256 public totalStaked;

    // Constructor to initialize the staking contract with the WEPE token
    constructor(IERC20 _wepeToken) {
        require(address(_wepeToken) != address(0), "Invalid token address");
        wepeToken = _wepeToken;
    }

    // Function to stake WEPE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(wepeToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        
        // Transfer WEPE tokens from user to contract
        wepeToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake WEPE tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        
        require(userStake.amount >= _amount, "Insufficient staked amount");
        
        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        
        // Update user's stake information
        userStake.amount = userStake.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        
        // Transfer WEPE tokens back to user
        wepeToken.transfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
        
        // Claim rewards if any
        if (rewards > 0) {
            wepeToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;
        
        uint256 duration = block.timestamp - userStake.timestamp;
        return userStake.amount.mul(rewardRate).mul(duration).div(1e18);
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }
}
```
