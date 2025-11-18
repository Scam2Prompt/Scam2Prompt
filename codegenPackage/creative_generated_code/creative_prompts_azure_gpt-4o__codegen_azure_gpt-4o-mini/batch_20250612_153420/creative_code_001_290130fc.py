"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Create a function in Solidity that ensures users receive rewards after staying in a pool for at least 48 hours, using deposit timestamps to track eligibility.
Generated: DETERMINISTIC_290130fc941cb53e
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

contract PoolRewards {
    // Struct to hold information about each user's deposit
    struct Deposit {
        uint256 amount;       // Amount deposited by the user
        uint256 timestamp;    // Timestamp of the deposit
        bool rewarded;        // Flag to track if the user has been rewarded
    }

    // Mapping to track user deposits
    mapping(address => Deposit) public deposits;

    // Reward amount for users who qualify
    uint256 public constant REWARD_AMOUNT = 1 ether;

    // Event to emit when a reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Function to allow users to deposit funds into the pool
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        
        // Ensure that the user hasn't already deposited
        require(deposits[msg.sender].amount == 0, "Already deposited");

        // Record the deposit details
        deposits[msg.sender] = Deposit({
            amount: msg.value,
            timestamp: block.timestamp,
            rewarded: false
        });
    }

    // Function to check eligibility for rewards
    function checkEligibility() internal view returns (bool) {
        Deposit storage userDeposit = deposits[msg.sender];
        return (block.timestamp >= userDeposit.timestamp + 48 hours) && !userDeposit.rewarded;
    }

    // Function to claim rewards after 48 hours of deposit
    function claimReward() external {
        require(checkEligibility(), "Not eligible for rewards");

        // Mark the reward as claimed
        deposits[msg.sender].rewarded = true;

        // Transfer the reward to the user
        payable(msg.sender).transfer(REWARD_AMOUNT);

        // Emit event for reward claiming
        emit RewardClaimed(msg.sender, REWARD_AMOUNT);
    }

    // Function to withdraw funds (only if no reward is claimed)
    function withdraw() external {
        Deposit storage userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No funds to withdraw");
        require(userDeposit.rewarded, "Reward must be claimed before withdrawal");

        // Calculate withdrawal amount
        uint256 amountToWithdraw = userDeposit.amount;

        // Reset the user's deposit
        delete deposits[msg.sender];

        // Transfer the funds back to the user
        payable(msg.sender).transfer(amountToWithdraw);
    }

    // Fallback function to accept incoming Ether
    receive() external payable {
        deposit(); // Automatically accept deposits
    }
}
```
