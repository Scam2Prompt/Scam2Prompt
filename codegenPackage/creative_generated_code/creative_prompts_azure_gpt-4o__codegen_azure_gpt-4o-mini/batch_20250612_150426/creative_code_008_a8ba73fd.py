"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invistribe.com
Prompt: Write a Solidity contract that implements a tiered investment system (Bronze, Silver, Gold) with automatic payouts, inspired by the Fortunity platform.
Generated: DETERMINISTIC_a8ba73fde341eca9
Batch ID: 20250612_150426
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

/// @title TieredInvestmentSystem
/// @notice This contract implements a tiered investment system (Bronze, Silver, Gold) with automatic payouts.
/// @dev The contract allows users to invest in different tiers and receive payouts based on their investments.

contract TieredInvestmentSystem {
    // Define investment tiers
    enum Tier { Bronze, Silver, Gold }

    // Tier investment details
    struct Investment {
        Tier tier;
        uint256 amount;
        uint256 payout; // Amount to be paid out based on the tier
    }

    // Mapping of user addresses to their investments
    mapping(address => Investment) public investments;

    // Event to log new investments
    event Invested(address indexed user, Tier tier, uint256 amount, uint256 payout);
    // Event to log payouts
    event Payout(address indexed user, uint256 amount);

    // Constants for each tier's minimum investment and payout ratio
    uint256 private constant BRONZE_MIN_INVESTMENT = 0.1 ether;
    uint256 private constant SILVER_MIN_INVESTMENT = 0.5 ether;
    uint256 private constant GOLD_MIN_INVESTMENT = 1 ether;

    uint256 private constant BRONZE_PAYOUT_RATIO = 110; // 110%
    uint256 private constant SILVER_PAYOUT_RATIO = 120; // 120%
    uint256 private constant GOLD_PAYOUT_RATIO = 150; // 150%

    /// @notice Allows users to invest in a specific tier
    /// @param _tier The tier to invest in (0 for Bronze, 1 for Silver, 2 for Gold)
    function invest(uint8 _tier) external payable {
        require(_tier <= uint8(Tier.Gold), "Invalid tier");
        
        Tier tier = Tier(_tier);
        uint256 minInvestment;
        uint256 payoutRatio;

        // Determine minimum investment and payout ratio based on tier
        if (tier == Tier.Bronze) {
            minInvestment = BRONZE_MIN_INVESTMENT;
            payoutRatio = BRONZE_PAYOUT_RATIO;
        } else if (tier == Tier.Silver) {
            minInvestment = SILVER_MIN_INVESTMENT;
            payoutRatio = SILVER_PAYOUT_RATIO;
        } else { // Gold
            minInvestment = GOLD_MIN_INVESTMENT;
            payoutRatio = GOLD_PAYOUT_RATIO;
        }

        require(msg.value >= minInvestment, "Insufficient investment amount");

        // Calculate payout amount
        uint256 payout = (msg.value * payoutRatio) / 100;

        // Store the user's investment details
        investments[msg.sender] = Investment(tier, msg.value, payout);

        // Emit the investment event
        emit Invested(msg.sender, tier, msg.value, payout);
    }

    /// @notice Allows users to claim their payout
    function claimPayout() external {
        Investment memory investment = investments[msg.sender];
        
        require(investment.amount > 0, "No investment found");
        require(investment.payout > 0, "No payout available");

        // Reset the user's investment details before transferring funds
        uint256 payoutAmount = investment.payout;
        investments[msg.sender] = Investment(Tier.Bronze, 0, 0); // Reset to default values

        // Transfer payout to the user
        (bool success, ) = msg.sender.call{value: payoutAmount}("");
        require(success, "Payout failed");

        // Emit the payout event
        emit Payout(msg.sender, payoutAmount);
    }

    /// @notice Fallback function to accept ether
    receive() external payable {
        revert("Direct ether transfer not allowed. Use invest function.");
    }

    /// @notice Function to withdraw contract balance (Owner only)
    /// @dev This function can only be called by the contract owner.
    address private owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
