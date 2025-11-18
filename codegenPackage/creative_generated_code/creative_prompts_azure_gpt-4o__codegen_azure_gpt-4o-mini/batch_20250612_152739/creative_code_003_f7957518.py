"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakelayerai.pages.dev
Prompt: Create a smart contract in Solidity for staking $LAI tokens and distributing AI Capsule rewards, ensuring compatibility with ERC-20 and BEP-20 standards as described in the LayerAI documentation.
Generated: DETERMINISTIC_f7957518bac50d34
Batch ID: 20250612_152739
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking LAI tokens and distributing AI Capsule rewards
contract StakingContract is Ownable {
    // Token interface for the $LAI token
    IERC20 public laiToken;

    // Struct to hold staking information for each user
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastUpdated;
    }

    // Mapping to store the staker's information by their address
    mapping(address => Staker) public stakers;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate (in $LAI tokens) per second
    uint256 public rewardRate = 1e18; // 1 token per second

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event to emit when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $LAI token address
    constructor(address _laiToken) {
        laiToken = IERC20(_laiToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the staker's rewards before staking new amount
        _updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        laiToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        // Emit Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker's information
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        laiToken.transfer(msg.sender, amount);

        // Emit Unstaked event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 rewards = stakers[msg.sender].rewardsEarned;

        require(rewards > 0, "No rewards to claim");

        // Reset rewards after claiming
        stakers[msg.sender].rewardsEarned = 0;

        // Transfer rewards to the staker
        laiToken.transfer(msg.sender, rewards);

        // Emit RewardsClaimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards for a staker
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];

        // Calculate the time elapsed since the last update
        uint256 timeElapsed = block.timestamp - staker.lastUpdated;

        // Update the rewards earned based on the staked amount and time elapsed
        if (staker.amountStaked > 0) {
            staker.rewardsEarned += staker.amountStaked * rewardRate * timeElapsed;
        }

        // Update the last updated time
        staker.lastUpdated = block.timestamp;
    }

    // Function to view the staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256 stakedAmount, uint256 rewards) {
        Staker storage staker = stakers[stakerAddress];
        stakedAmount = staker.amountStaked;
        rewards = staker.rewardsEarned + (staker.amountStaked * rewardRate * (block.timestamp - staker.lastUpdated));
    }
}
```
