"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20s.pages.dev
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized wallet using the ERC-20 standard.
Generated: DETERMINISTIC_d275bb0229945c5f
Batch ID: 20250612_152656
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Create the Staking contract
contract Doge20Staking is Ownable {
    // Token to be staked
    IERC20 public doge20Token;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) public stakes;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event to emit when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token address
    constructor(address _doge20Token) {
        doge20Token = IERC20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to this contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the reward based on the stake duration
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No stakes found for user");

        // Simple reward calculation: 1% per week
        uint256 rewardRate = 1; // 1%
        uint256 duration = block.timestamp - userStake.timestamp;
        uint256 weeks = duration / 1 weeks;

        return (userStake.amount * rewardRate / 100) * weeks;
    }

    // Function to unstake DOGE20 tokens
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes to unstake");

        // Calculate the reward before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake
        uint256 amountToUnstake = userStake.amount;
        stakes[msg.sender].amount = 0;

        // Transfer the staked amount and reward back to the user
        doge20Token.transfer(msg.sender, amountToUnstake + reward);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to get the total staked amount for a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp for a user
    function getStakingTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
