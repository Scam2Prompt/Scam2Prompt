"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
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

// Interface for the CATGIRL¢ token contract
interface ICATGIRL {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for CATGIRL¢ tokens
contract CatgirlStaking {
    // Token interface
    ICATGIRL public catgirlToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;      // Amount staked
        uint256 timestamp;   // Time of staking
        bool isActive;       // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate in tokens per second
    uint256 public rewardRate;
    // Total rewards claimed
    mapping(address => uint256) public rewardsClaimed;

    // Events for logging actions on the contract
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the CATGIRL¢ token address and reward rate
    constructor(address _catgirlToken, uint256 _rewardRate) {
        catgirlToken = ICATGIRL(_catgirlToken);
        rewardRate = _rewardRate;
    }

    // Function to stake CATGIRL¢ tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero.");
        require(catgirlToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed.");

        // Update the stake information
        stakes[msg.sender] = Stake({
            amount: _amount,
            timestamp: block.timestamp,
            isActive: true
        });
        
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake CATGIRL¢ tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found.");
        
        // Calculate rewards based on the staking duration
        uint256 reward = calculateReward(msg.sender);
        rewardsClaimed[msg.sender] += reward;

        // Reset the user's stake
        uint256 amountStaked = userStake.amount;
        userStake.isActive = false;
        userStake.amount = 0;

        // Transfer staked tokens back to the user
        require(catgirlToken.transferFrom(address(this), msg.sender, amountStaked), "Transfer failed.");
        emit Unstaked(msg.sender, amountStaked);

        // Transfer rewards to the user
        require(catgirlToken.transferFrom(address(this), msg.sender, reward), "Reward transfer failed.");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the reward for a user based on their stake duration
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (!userStake.isActive) return 0;

        uint256 duration = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * duration);
    }

    // Function to withdraw contract balance (for owner or emergency purposes)
    function withdrawTokens(address _to, uint256 _amount) external {
        // Implement access control (e.g., onlyOwner) in production
        require(catgirlToken.transfer(_to, _amount), "Withdraw failed.");
    }

    // Fallback function to prevent accidental ETH deposits
    receive() external payable {
        revert("ETH deposits are not allowed.");
    }
}
```
