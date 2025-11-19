"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.web.app
Prompt: Explain how to integrate the Scorpion Casino's tokenomics into a decentralized application (dApp) that allows users to buy and stake $SCORP tokens.
Generated: DETERMINISTIC_4ce9f4ceb5e797e0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import required libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the contract for staking $SCORP tokens
contract ScorpionCasinoStaking is Ownable {
    // The token being staked
    IERC20 public scorpToken;

    // Structure to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 since;  // Timestamp of when staking started
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user un-stakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _scorpToken) {
        scorpToken = _scorpToken;
    }

    // Function to stake $SCORP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scorpToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].since = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $SCORP tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0; // Reset user's stake

        // Transfer tokens back to the user
        require(scorpToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to claim rewards (stub for future implementation)
    // This function could be enhanced to calculate and distribute rewards based on staked amount and duration
    function claimRewards() external {
        // Placeholder: implement reward logic based on your tokenomics
        uint256 rewardAmount = 0; // Calculate reward based on your logic

        require(rewardAmount > 0, "No rewards to claim");
        
        // Implement reward distribution logic here

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to check staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
