"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity function that calculates dynamic APY rewards for staking $STARS tokens, based on the reward structure outlined in the Crypto All-Stars staking mechanism.
Generated: DETERMINISTIC_0484773140f925bf
Batch ID: 20250612_154307
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

// Interface for the ERC20 token (STARS)
interface IToken {
    function balanceOf(address account) external view returns (uint256);
}

// The CryptoAllStarsStaking contract
contract CryptoAllStarsStaking {
    // The token being staked
    IToken public starsToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardTimestamp;
        uint256 rewards;
    }
    
    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // APY percentage (e.g., 500 = 5.0%)
    uint256 public constant APY_PERCENTAGE = 500; // 5.0%
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _starsToken) {
        require(_starsToken != address(0), "Invalid token address");
        starsToken = IToken(_starsToken);
    }

    // Function to stake $STARS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(starsToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastRewardTimestamp = block.timestamp;

        // Transfer tokens from the user to the contract
        // Note: Assuming the tokens have been approved before calling this function
        // Use the ERC20 transfer function here
        // starsToken.transferFrom(msg.sender, address(this), amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked tokens");

        uint256 reward = calculateRewards(msg.sender);
        staker.rewards += reward;
        staker.lastRewardTimestamp = block.timestamp;

        // Emit an event for claiming rewards
        emit RewardsClaimed(msg.sender, staker.rewards);

        // Reset rewards for the user (if desired)
        // staker.rewards = 0; // Uncomment to reset after claiming
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 stakedDuration = block.timestamp - staker.lastRewardTimestamp;

        // Calculate rewards: (stakedAmount * APY / 100) * (time / seconds in a year)
        uint256 reward = (staker.stakedAmount * APY_PERCENTAGE / 10000) * stakedDuration / SECONDS_IN_A_YEAR;

        return reward;
    }

    // Function to withdraw staked tokens and rewards
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Calculate rewards before withdrawal
        uint256 reward = calculateRewards(msg.sender);
        staker.rewards += reward;

        // Update staker's staked amount
        staker.stakedAmount -= amount;

        // Transfer tokens back to the user
        // starsToken.transfer(msg.sender, amount);

        // Emit an event for withdrawal
        // emit Withdrawn(msg.sender, amount);
    }

    // Function to view total rewards of a user
    function totalRewards(address stakerAddress) external view returns (uint256) {
        return stakers[stakerAddress].rewards + calculateRewards(stakerAddress);
    }
}
```
