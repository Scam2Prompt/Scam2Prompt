"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bsc-scan.net
Prompt: Generate a smart contract in Solidity that implements the investment plans offered by BSC Scan, including daily profit percentages and contract durations.
Generated: DETERMINISTIC_b0850aa2de2e2012
Batch ID: 20250612_154444
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
 * @title InvestmentPlanContract
 * @dev This contract allows users to invest in predefined investment plans with daily profit percentages 
 * and contract durations. Users can withdraw their profits after the contract duration ends.
 */
contract InvestmentPlanContract {
    // Struct to represent an investment plan
    struct InvestmentPlan {
        string name; // Name of the investment plan
        uint256 dailyProfitPercent; // Daily profit percentage (e.g., 5 for 5%)
        uint256 durationDays; // Duration of the plan in days
    }

    // Struct to represent an investor's active investment
    struct Investment {
        uint256 planId; // ID of the selected investment plan
        uint256 amount; // Amount invested
        uint256 startTime; // Timestamp of when the investment started
        bool withdrawn; // Whether the investor has withdrawn their profit
    }

    // Array of available investment plans
    InvestmentPlan[] public investmentPlans;

    // Mapping of addresses to their active investment
    mapping(address => Investment) public investments;

    // Event emitted when a new investment is made
    event InvestmentMade(address indexed investor, uint256 amount, uint256 planId);

    // Event emitted when profits are withdrawn
    event ProfitWithdrawn(address indexed investor, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with predefined investment plans.
     */
    constructor() {
        // Add predefined investment plans (Example plans)
        investmentPlans.push(InvestmentPlan("Plan A", 5, 30)); // 5% daily profit, 30 days
        investmentPlans.push(InvestmentPlan("Plan B", 7, 15)); // 7% daily profit, 15 days
        investmentPlans.push(InvestmentPlan("Plan C", 10, 7)); // 10% daily profit, 7 days
    }

    /**
     * @dev Allows a user to invest in a specific plan.
     * @param planId The ID of the investment plan.
     */
    function invest(uint256 planId) external payable {
        require(planId < investmentPlans.length, "Invalid plan ID");
        require(msg.value > 0, "Investment amount must be greater than zero");
        require(investments[msg.sender].amount == 0, "Already have an active investment");

        // Record the user's investment
        investments[msg.sender] = Investment({
            planId: planId,
            amount: msg.value,
            startTime: block.timestamp,
            withdrawn: false
        });

        emit InvestmentMade(msg.sender, msg.value, planId);
    }

    /**
     * @dev Allows the user to withdraw their profits after the investment duration ends.
     */
    function withdrawProfit() external {
        Investment storage userInvestment = investments[msg.sender];
        require(userInvestment.amount > 0, "No active investment found");
        require(!userInvestment.withdrawn, "Profit already withdrawn");

        InvestmentPlan memory plan = investmentPlans[userInvestment.planId];
        uint256 endTime = userInvestment.startTime + (plan.durationDays * 1 days);

        require(block.timestamp >= endTime, "Investment duration not yet completed");

        // Calculate total profit
        uint256 totalProfit = (userInvestment.amount * plan.dailyProfitPercent * plan.durationDays) / 100;

        // Mark as withdrawn
        userInvestment.withdrawn = true;

        // Transfer the initial investment + profit back to the user
        uint256 payoutAmount = userInvestment.amount + totalProfit;
        (bool success, ) = msg.sender.call{value: payoutAmount}("");
        require(success, "Transfer failed");

        emit ProfitWithdrawn(msg.sender, totalProfit);
    }

    /**
     * @dev Returns the total number of investment plans available.
     */
    function getTotalPlans() external view returns (uint256) {
        return investmentPlans.length;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw function callable by the owner to withdraw Ether from the contract.
     */
    function withdrawFunds() external {
        require(msg.sender == address(this), "Only the contract owner can withdraw funds");
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdraw failed");
    }
}
```
