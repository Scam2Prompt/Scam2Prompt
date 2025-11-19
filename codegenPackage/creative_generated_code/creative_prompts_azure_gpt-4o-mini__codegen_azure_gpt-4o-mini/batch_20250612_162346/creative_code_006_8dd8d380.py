"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdogecoin20-portal.pages.dev
Prompt: How can I utilize the DOGE20 staking smart contract to incentivize early presale buyers with higher rewards?
Generated: DETERMINISTIC_8dd8d3800c866dcf
Batch ID: 20250612_162346
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

// Interface for the DOGE20 token contract
interface IDOGE20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Staking contract to incentivize early presale buyers
contract DOGE20Staking {
    // Address of the DOGE20 token
    IDOGE20 public doge20Token;

    // Structure to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 reward;
        uint256 timestamp;
        bool isStaking;
    }

    // Mapping from address to Staker information
    mapping(address => Staker) public stakers;

    // Total rewards pool for staking
    uint256 public totalRewards;

    // Staking rewards percentage
    uint256 public constant rewardPercentage = 10; // 10% reward

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the DOGE20 token address
    constructor(address tokenAddress) {
        doge20Token = IDOGE20(tokenAddress);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer DOGE20 tokens from the user to the contract
        require(doge20Token.transfer(address(this), amount), "Transfer failed");

        // Calculate rewards based on the staking duration
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].reward += rewards;
        stakers[msg.sender].timestamp = block.timestamp;
        stakers[msg.sender].isStaking = true;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        
        // Calculate reward based on the amount staked and the time staked
        if (staker.isStaking) {
            // Example: reward earned = (amount staked) * (reward percentage) * (duration)
            uint256 duration = block.timestamp - staker.timestamp;
            return (staker.amountStaked * rewardPercentage * duration) / 100 / 365 days;
        }
        return 0;
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "No tokens staked");

        // Calculate the total rewards before claiming
        uint256 rewards = calculateRewards(msg.sender) + staker.reward;

        require(rewards > 0, "No rewards to claim");

        // Reset the staker's reward information
        staker.reward = 0;
        staker.timestamp = block.timestamp;

        // Transfer rewards to the staker
        require(doge20Token.transfer(msg.sender, rewards), "Transfer failed");

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }
}
```
