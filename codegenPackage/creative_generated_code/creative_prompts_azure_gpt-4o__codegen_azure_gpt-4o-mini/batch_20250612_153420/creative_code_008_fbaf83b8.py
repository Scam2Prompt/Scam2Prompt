"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Create a step-by-step guide for integrating BTCMTX token staking functionality into an existing Ethereum dApp.
Generated: DETERMINISTIC_fbaf83b81a205bee
Batch ID: 20250612_153420
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for BTCMTX Token Staking
contract BTCMTXStaking is Ownable {
    // Define a struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 startTime;
        bool isActive;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token instance
    IERC20 public btcmtxToken;

    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _btcmtxToken) {
        require(_btcmtxToken != address(0), "Invalid token address");
        btcmtxToken = IERC20(_btcmtxToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(btcmtxToken.allowance(msg.sender, address(this)) >= _amount, "Insufficient allowance");

        // Transfer tokens from user to the contract
        btcmtxToken.transferFrom(msg.sender, address(this), _amount);

        // Update user stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;
        stakes[msg.sender].isActive = true;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update the stake amount
        userStake.amount -= _amount;

        // If the stake amount is zero, deactivate it
        if (userStake.amount == 0) {
            userStake.isActive = false;
        }

        // Transfer tokens back to the user
        btcmtxToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards (example implementation)
    function claimRewards() external {
        // This is a placeholder for reward calculation logic
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        btcmtxToken.transfer(msg.sender, rewards);
        
        emit Claimed(msg.sender, rewards);
    }

    // Placeholder function for reward calculation
    function calculateRewards(address user) internal view returns (uint256) {
        // Implement reward calculation logic based on user's stake
        Stake storage userStake = stakes[user];
        if (!userStake.isActive) {
            return 0;
        }
        // Example: return 10% of the staked amount as rewards
        return (userStake.amount * 10) / 100;
    }

    // Function to view user stake details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 startTime, bool isActive) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.isActive);
    }
}
```

This smart contract provides a staking functionality for the BTCMTX token utilizing the ERC20 standard. It covers staking, unstaking, and claiming rewards, with proper error handling and event logging.
