"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-cosmicnetwork.pages.dev
Prompt: Create a smart contract example for staking tokens on the Cosmic Network.
Generated: DETERMINISTIC_d6b08f4ecf3618f3
Batch ID: 20250612_145810
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

// Importing necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple staking contract for ERC20 tokens
contract StakingContract is ReentrancyGuard, Ownable {
    // The ERC20 token being staked
    IERC20 public immutable stakingToken;

    // Variables to keep track of the staked amounts and rewards
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    
    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging significant actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Constructor to initialize the staking contract with an ERC20 token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Stake tokens in the contract
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens from the contract
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");
        
        // Update the user's stake
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Calculate rewards based on staked time (for demonstration purposes)
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        // Example reward calculation: 1 token for every day staked
        uint256 daysStaked = (block.timestamp - userStake.timestamp) / 1 days;
        return userStake.amount * daysStaked;
    }

    // Claim rewards for the user
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewards);
        // Update the stake timestamp after claiming rewards
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        stakingToken.transfer(msg.sender, _amount);
    }
}
```

This code represents a simple staking contract for an ERC20 token, implementing the necessary functionality for staking, unstaking, and reward calculations, while following best practices for Solidity development.
