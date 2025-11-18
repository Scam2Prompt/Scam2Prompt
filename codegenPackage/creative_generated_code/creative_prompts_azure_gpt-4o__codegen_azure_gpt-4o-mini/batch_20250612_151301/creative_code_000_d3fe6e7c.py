"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Write a smart contract in Solidity for staking `$LEGEND` tokens, including functionality for claiming rewards and unlocking exclusive benefits.
Generated: DETERMINISTIC_d3fe6e7ce98e443e
Batch ID: 20250612_151301
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

// Importing the OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Staking contract for $LEGEND tokens
contract LegendStaking {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 since;       // Timestamp when the tokens were staked
        bool active;         // Whether the stake is active
    }

    // State variables
    IERC20 public legendToken;                      // Reference to the LEGEND token contract
    mapping(address => Stake) public stakes;        // Mapping of user addresses to their stakes
    uint256 public rewardRate;                       // Reward rate (tokens per second)
    uint256 public totalStaked;                     // Total amount of tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address and reward rate
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        legendToken = IERC20(_tokenAddress);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(legendToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // If the user already has an active stake, we will accumulate their tokens
        if (userStake.active) {
            userStake.amount += amount; // Increase staked amount
        } else {
            userStake.amount = amount;   // Set initial stake
            userStake.since = block.timestamp; // Set staking start time
            userStake.active = true;     // Mark stake as active
        }

        totalStaked += amount; // Update total staked amount
        emit Staked(msg.sender, amount); // Emit stake event
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.active, "No active stake found");
        require(amount > 0 && amount <= userStake.amount, "Invalid unstake amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // If all tokens are unstaked, deactivate the stake
        if (userStake.amount == 0) {
            userStake.active = false;
        }

        // Transfer tokens back to the user
        require(legendToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit events
        emit Unstaked(msg.sender, amount);
        if (rewards > 0) {
            claimRewards(); // Automatically claim rewards
        }
    }

    // Function to claim rewards
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        Stake storage userStake = stakes[msg.sender];
        userStake.since = block.timestamp; // Reset the timestamp

        // Transfer rewards to the user
        require(legendToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewards); // Emit reward claim event
    }

    // Internal function to calculate rewards based on staked time
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (!userStake.active) {
            return 0;
        }
        // Calculate elapsed time in seconds
        uint256 elapsedTime = block.timestamp - userStake.since;
        return (elapsedTime * userStake.amount * rewardRate) / 1e18; // Adjust for decimals
    }

    // Function to get the user’s staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the user's rewards
    function getRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
