"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Create a smart contract in Solidity for managing instant withdrawals and profit distributions for investment plans like those offered by Finvera Capitals.
Generated: DETERMINISTIC_42a9a99ad3da25c3
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

contract InvestmentManager {
    struct InvestmentPlan {
        uint256 id;
        uint256 minInvestment;
        uint256 maxInvestment;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
    }

    struct Investor {
        uint256 totalInvested;
        uint256 totalWithdrawn;
        uint256 profitEarned;
    }

    mapping(address => Investor) public investors;
    InvestmentPlan[] public investmentPlans;

    // Event emitted when an investment is made
    event Invested(address indexed investor, uint256 amount, uint256 planId);
    // Event emitted when a withdrawal is made
    event Withdrawn(address indexed investor, uint256 amount);
    // Event emitted when profit is distributed
    event ProfitDistributed(address indexed investor, uint256 amount);

    // Modifier to check if investment plan is valid
    modifier validPlan(uint256 _planId) {
        require(_planId < investmentPlans.length, "Invalid investment plan ID");
        _;
    }

    // Constructor to initialize investment plans
    constructor() {
        // Example: Initialize investment plans
        investmentPlans.push(InvestmentPlan(0, 1 ether, 10 ether, 500)); // 5% interest
        investmentPlans.push(InvestmentPlan(1, 10 ether, 50 ether, 800)); // 8% interest
    }

    // Function to invest in a specific plan
    function invest(uint256 _planId) external payable validPlan(_planId) {
        InvestmentPlan memory plan = investmentPlans[_planId];

        // Validate investment amount
        require(msg.value >= plan.minInvestment && msg.value <= plan.maxInvestment, "Investment amount out of range");

        // Update investor's data
        investors[msg.sender].totalInvested += msg.value;
        
        // Emit investment event
        emit Invested(msg.sender, msg.value, _planId);
    }

    // Function to calculate and withdraw profit
    function withdrawProfit() external {
        Investor storage investor = investors[msg.sender];

        // Calculate profit based on invested amount and interest rate
        uint256 profit = calculateProfit(investor.totalInvested);

        // Ensure there is profit to withdraw
        require(profit > 0, "No profit available to withdraw");

        // Update the investor's withdrawn amount and profits
        investor.totalWithdrawn += profit;
        investor.profitEarned += profit;

        // Transfer profit to the investor
        (bool success, ) = msg.sender.call{value: profit}("");
        require(success, "Transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, profit);
    }

    // Internal function to calculate profit
    function calculateProfit(uint256 _amount) internal view returns (uint256) {
        // Calculate total profit based on the latest investment plan (for simplicity)
        InvestmentPlan memory latestPlan = investmentPlans[investmentPlans.length - 1];
        return (_amount * latestPlan.interestRate) / 10000; // Convert basis points to percentage
    }

    // Function to distribute profits among all investors (could be called periodically)
    function distributeProfits() external {
        for (uint256 i = 0; i < investmentPlans.length; i++) {
            address investorAddress = msg.sender; // Replace with actual distribution logic
            uint256 profit = calculateProfit(investors[investorAddress].totalInvested);
            investors[investorAddress].profitEarned += profit;
            
            emit ProfitDistributed(investorAddress, profit);
        }
    }

    // Function to retrieve investment plans
    function getInvestmentPlans() external view returns (InvestmentPlan[] memory) {
        return investmentPlans;
    }
}
```
