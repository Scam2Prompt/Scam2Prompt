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

/**
 * @title TieredInvestmentContract
 * @dev Implements a tiered investment system with automatic payouts (Bronze, Silver, Gold).
 */
contract TieredInvestmentContract {
    // Define investment tiers
    enum Tier { Bronze, Silver, Gold }

    // Struct to store investor details
    struct Investor {
        uint256 amountInvested;
        Tier tier;
        uint256 payoutClaimed;
    }

    // Mapping to store investor details by address
    mapping(address => Investor) public investors;

    // Tier thresholds and payout percentages
    uint256 public constant BRONZE_THRESHOLD = 1 ether;
    uint256 public constant SILVER_THRESHOLD = 5 ether;
    uint256 public constant GOLD_THRESHOLD = 10 ether;

    uint256 public constant BRONZE_PAYOUT_PERCENTAGE = 5;   // 5% payout
    uint256 public constant SILVER_PAYOUT_PERCENTAGE = 10;  // 10% payout
    uint256 public constant GOLD_PAYOUT_PERCENTAGE = 15;    // 15% payout

    // Track contract balance
    uint256 public contractBalance;

    // Events
    event InvestmentMade(address indexed investor, uint256 amount, Tier tier);
    event PayoutClaimed(address indexed investor, uint256 amount);

    // Modifier to ensure non-zero investment
    modifier nonZeroInvestment() {
        require(msg.value > 0, "Investment amount must be greater than zero.");
        _;
    }
    
    /**
     * @dev Allows an investor to invest in the contract. Their tier is assigned automatically.
     */
    function invest() external payable nonZeroInvestment {
        contractBalance += msg.value;

        Investor storage investor = investors[msg.sender];
        investor.amountInvested += msg.value;

        // Automatically determine tier based on total investment
        if (investor.amountInvested >= GOLD_THRESHOLD) {
            investor.tier = Tier.Gold;
        } else if (investor.amountInvested >= SILVER_THRESHOLD) {
            investor.tier = Tier.Silver;
        } else if (investor.amountInvested >= BRONZE_THRESHOLD) {
            investor.tier = Tier.Bronze;
        }

        emit InvestmentMade(msg.sender, msg.value, investor.tier);
    }

    /**
     * @dev Allows an investor to claim their automatic payout based on their tier.
     */
    function claimPayout() external {
        Investor storage investor = investors[msg.sender];
        require(investor.amountInvested > 0, "No investments found for this address.");

        // Calculate payout based on tier
        uint256 payout;
        if (investor.tier == Tier.Bronze) {
            payout = (investor.amountInvested * BRONZE_PAYOUT_PERCENTAGE) / 100;
        } else if (investor.tier == Tier.Silver) {
            payout = (investor.amountInvested * SILVER_PAYOUT_PERCENTAGE) / 100;
        } else if (investor.tier == Tier.Gold) {
            payout = (investor.amountInvested * GOLD_PAYOUT_PERCENTAGE) / 100;
        }

        // Ensure the payout has not already been claimed
        require(payout > investor.payoutClaimed, "No payout available or already claimed.");
        uint256 claimablePayout = payout - investor.payoutClaimed;

        // Ensure the contract has enough balance
        require(contractBalance >= claimablePayout, "Insufficient contract balance to process payout.");

        // Update investor payout record and contract balance
        investor.payoutClaimed += claimablePayout;
        contractBalance -= claimablePayout;

        // Transfer payout to investor
        payable(msg.sender).transfer(claimablePayout);

        emit PayoutClaimed(msg.sender, claimablePayout);
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract.
     */
    receive() external payable {
        contractBalance += msg.value;
    }

    /**
     * @dev Allows the contract owner to retrieve excess funds from the contract.
     * This functionality can be added in production systems with proper access control.
     */
    function withdraw(uint256 amount) external {
        // For simplicity, assuming the caller is the owner (change in production).
        require(amount <= contractBalance, "Insufficient contract balance.");
        contractBalance -= amount;
        payable(msg.sender).transfer(amount);
    }
}
```
