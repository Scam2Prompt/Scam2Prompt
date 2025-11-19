"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20.web.app
Prompt: Generate a Solidity smart contract that mimics the DOGE20 staking mechanism, distributing rewards to stakers over a specified period.
Generated: DETERMINISTIC_c692795b58a9adac
Batch ID: 20250612_161353
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

contract DOGE20Staking {
    // Variables to hold the staking information
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for calculating rewards
        uint256 lastStakedTime; // Last time the staker staked
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount staked in the contract
    uint256 public totalStaked;
    
    // Reward rate per second (in wei)
    uint256 public rewardRate;
    
    // Duration for which rewards are distributed
    uint256 public rewardDuration;
    
    // Flag to indicate whether staking is active
    bool public stakingActive;

    // Event to log when a user stakes
    event Staked(address indexed user, uint256 amount);
    
    // Event to log when a user unstakes
    event Unstaked(address indexed user, uint256 amount);
    
    // Event to log when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate, uint256 _rewardDuration) {
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
        stakingActive = true;
    }

    // Modifier to check if staking is active
    modifier stakingEnabled() {
        require(stakingActive, "Staking is not active.");
        _;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external stakingEnabled {
        require(_amount > 0, "Amount must be greater than 0.");
        
        // Update total staked amount
        totalStaked += _amount;
        
        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakedTime = block.timestamp;

        // Emit staking event
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked.");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);
        
        // Update total staked amount
        totalStaked -= staker.amount;

        // Reset staker's information
        staker.amount = 0;
        staker.rewardDebt = 0;
        
        // Transfer staked amount back to user
        // Note: Implement your own token transfer logic here
        // token.transfer(msg.sender, staker.amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, staker.amount);

        // Transfer rewards to user if any
        if (reward > 0) {
            // Note: Implement your own reward payout logic here
            // token.transfer(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amount * rewardRate * timeStaked) / 1e18; // Assuming rewardRate is in wei
    }

    // Function to enable or disable staking
    function setStakingActive(bool _active) external {
        // Only the contract owner should be able to change this
        // require(msg.sender == owner, "Only owner can change staking status.");
        stakingActive = _active;
    }
}
```
