"""
Generated Code Metadata:
========================
Original URL: https://thedogeverser.pages.dev
Prompt: Write a Solidity function for locking $DOGEVERSE tokens in a staking contract and calculating rewards based on the locked duration.
Generated: DETERMINISTIC_73f71af317fcf1f0
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the DOGEVERSE token
interface IDOGEVERSE {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for locking DOGEVERSE tokens and calculating rewards
contract StakingContract {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The DOGEVERSE token contract
    IDOGEVERSE public dogeverseToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGEVERSE token address and reward rate
    constructor(address _dogeverseToken, uint256 _rewardRate) {
        require(_dogeverseToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        dogeverseToken = IDOGEVERSE(_dogeverseToken);
        rewardRate = _rewardRate;
    }

    // Function to stake DOGEVERSE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(dogeverseToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on the locked duration
    function calculateRewards(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        if (staker.amount == 0) {
            return 0; // No rewards if no tokens are staked
        }
        uint256 duration = block.timestamp - staker.startTime;
        return (staker.amount * rewardRate * duration) / 1e18; // Adjust for reward rate precision
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update staker's rewards and reset start time
        stakers[msg.sender].rewards += rewards;
        stakers[msg.sender].startTime = block.timestamp;

        // Transfer rewards to the user (assuming rewards are paid in DOGEVERSE tokens)
        require(dogeverseToken.transferFrom(address(this), msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the staker's total rewards
    function getTotalRewards(address user) external view returns (uint256) {
        return stakers[user].rewards + calculateRewards(user);
    }
}
```
