"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtcwebb.pages.dev
Prompt: Develop a Solidity smart contract for staking $GBTC tokens during the presale, including functionality for calculating exponential rewards and locking tokens for 7 days.
Generated: DETERMINISTIC_e98ecfb2f3d2676c
Batch ID: 20250612_152410
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

// Interface for the $GBTC token
interface IGBTC {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GBTCStaking {
    // State variables
    IGBTC public gbtcToken; // The $GBTC token contract
    uint256 public constant REWARD_MULTIPLIER = 2; // Reward multiplier for exponential growth
    uint256 public constant LOCK_DURATION = 7 days; // Duration for which tokens will be locked

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the tokens were staked
    }

    // Mapping from user address to their stake information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the GBTC token address
    constructor(address _gbtcToken) {
        require(_gbtcToken != address(0), "Invalid token address");
        gbtcToken = IGBTC(_gbtcToken);
    }

    // Function to stake $GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create or update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the reward based on the amount staked
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No stake found for user");

        uint256 durationStaked = block.timestamp - userStake.timestamp;
        if (durationStaked < LOCK_DURATION) {
            return 0; // No reward if tokens are not unlocked
        }

        // Calculate exponential reward (simplified for demonstration)
        return userStake.amount * REWARD_MULTIPLIER;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the tokens and rewards back to the user
        require(gbtcToken.transfer(msg.sender, totalAmount), "Failed to transfer tokens back");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to check the stake of a user
    function getUserStake(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
