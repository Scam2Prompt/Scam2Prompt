"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Write a Solidity function to calculate exponential rewards for Green Bitcoin ($GBTC) stakers based on their staking duration and token holdings."
Generated: DETERMINISTIC_a3a3afdcbc5772e2
Batch ID: 20250622_210243
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

contract GreenBitcoinStaking {
    // Mapping to store the staking information of each user
    mapping(address => Staker) public stakers;

    // Struct to hold staking details
    struct Staker {
        uint256 amount; // Amount of GBTC staked
        uint256 startTime; // Timestamp when staking started
        bool isStaking; // Staking status
    }

    // Event to emit when rewards are calculated
    event RewardsCalculated(address indexed staker, uint256 rewards);

    // Function to stake GBTC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        require(!staker.isStaking, "Already staking");

        staker.amount = _amount;
        staker.startTime = block.timestamp;
        staker.isStaking = true;

        // Transfer GBTC tokens from the staker to the contract (assumed to be implemented)
        // require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
    }

    // Function to calculate rewards based on staking duration and amount
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        require(staker.isStaking, "Not staking");

        uint256 stakingDuration = block.timestamp - staker.startTime; // Duration in seconds
        uint256 rewards = (staker.amount * stakingDuration) / 1 days; // Example reward calculation

        return rewards;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "Not staking");

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset the staking start time for the next reward calculation
        staker.startTime = block.timestamp;

        // Emit an event for the calculated rewards
        emit RewardsCalculated(msg.sender, rewards);

        // Transfer rewards to the staker (assumed to be implemented)
        // require(gbtcToken.transfer(msg.sender, rewards), "Transfer failed");
    }

    // Function to unstake GBTC tokens
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "Not staking");

        // Calculate any pending rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            // Emit an event for the calculated rewards
            emit RewardsCalculated(msg.sender, rewards);
            // Transfer rewards to the staker (assumed to be implemented)
            // require(gbtcToken.transfer(msg.sender, rewards), "Transfer failed");
        }

        // Reset staker information
        staker.amount = 0;
        staker.startTime = 0;
        staker.isStaking = false;

        // Transfer staked GBTC tokens back to the staker (assumed to be implemented)
        // require(gbtcToken.transfer(msg.sender, staker.amount), "Transfer failed");
    }
}
```
