"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-manta-network.pages.dev
Prompt: Create a smart contract that facilitates staking $MANTA tokens and distributes rewards based on the Manta Network's staking mechanism.
Generated: DETERMINISTIC_7432640efc7bf90f
Batch ID: 20250612_150119
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $MANTA tokens
contract MantaStaking is Ownable {
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Token being staked
    IERC20 public mantaToken;

    // User staking details
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking details
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;
    
    // Accumulated rewards per token
    uint256 public accRewardPerToken;
    
    // Total accumulated rewards
    uint256 public totalRewards;

    // Reward distribution rate (example: rewards per second)
    uint256 public rewardRate;

    // Constructor to set the token and reward rate
    constructor(IERC20 _mantaToken, uint256 _rewardRate) {
        mantaToken = _mantaToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update rewards before changing balances
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        mantaToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        stakers[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(stakers[msg.sender].amount >= _amount, "Not enough staked tokens");

        // Update rewards before changing balances
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        mantaToken.transfer(msg.sender, _amount);

        // Update staker information
        stakers[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt to zero
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        totalRewards -= reward; // Update total rewards
        mantaToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address _user) internal {
        if (totalStaked > 0) {
            // Calculate accumulated rewards per token
            accRewardPerToken += (rewardRate * (block.timestamp - lastRewardTime)) / totalStaked;
            lastRewardTime = block.timestamp;

            // Update user's reward debt
            stakers[_user].rewardDebt += (stakers[_user].amount * accRewardPerToken);
        }
    }
}
```
