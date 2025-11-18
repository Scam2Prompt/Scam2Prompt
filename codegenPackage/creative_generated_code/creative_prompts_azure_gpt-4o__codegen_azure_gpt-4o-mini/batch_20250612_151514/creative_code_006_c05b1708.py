"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futurespaceinvestment.com
Prompt: Write a Solidity smart contract that implements the investment plans described on FutureSpaceInvestments, ensuring capital back, daily profit distribution, and withdrawal functionality.
Generated: DETERMINISTIC_c05b17087d52ad4f
Batch ID: 20250612_151514
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

contract FutureSpaceInvestments {
    // Struct to represent an investor's details
    struct Investor {
        uint256 totalInvestment;
        uint256 dailyProfit;
        uint256 lastWithdrawnTimestamp;
        bool isInvested;
    }

    // Mapping to track each investor's details
    mapping(address => Investor) private investors;

    // Events for logging actions
    event InvestmentMade(address indexed investor, uint256 amount);
    event ProfitDistributed(address indexed investor, uint256 amount);
    event Withdrawal(address indexed investor, uint256 amount);
    
    // Daily profit rate (e.g., 1% daily)
    uint256 public dailyProfitRate = 100; // in basis points (1% = 100 basis points)
    uint256 constant public SECONDS_IN_A_DAY = 86400;

    // Modifier to check if the investor is already invested
    modifier onlyInvested() {
        require(investors[msg.sender].isInvested, "You have not invested yet!");
        _;
    }

    // Function to invest in the plan
    function invest() external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");
        
        Investor storage investor = investors[msg.sender];

        // If the investor is already invested, we don't allow new investments
        require(!investor.isInvested, "You are already invested!");

        // Update investor details
        investor.totalInvestment = msg.value;
        investor.dailyProfit = (msg.value * dailyProfitRate) / 10000; // Calculate daily profit
        investor.lastWithdrawnTimestamp = block.timestamp;
        investor.isInvested = true;

        emit InvestmentMade(msg.sender, msg.value);
    }

    // Function to distribute profits
    function distributeProfits() external onlyInvested {
        Investor storage investor = investors[msg.sender];

        // Calculate the number of days since last withdrawal
        uint256 numberOfDays = (block.timestamp - investor.lastWithdrawnTimestamp) / SECONDS_IN_A_DAY;
        require(numberOfDays > 0, "Profit can only be distributed once per day");

        // Calculate total profit to distribute
        uint256 totalProfit = investor.dailyProfit * numberOfDays;

        // Update the last withdrawn timestamp
        investor.lastWithdrawnTimestamp = block.timestamp;

        // Emit event for profit distribution
        emit ProfitDistributed(msg.sender, totalProfit);
    }

    // Function to withdraw profits
    function withdraw() external onlyInvested {
        Investor storage investor = investors[msg.sender];

        // Calculate the available profit to withdraw
        uint256 numberOfDays = (block.timestamp - investor.lastWithdrawnTimestamp) / SECONDS_IN_A_DAY;
        require(numberOfDays > 0, "No profit available for withdrawal");

        uint256 totalProfit = investor.dailyProfit * numberOfDays;

        // Transfer the total profit to the investor
        (bool sent, ) = payable(msg.sender).call{value: totalProfit}("");
        require(sent, "Failed to send Ether");
        
        // Update the last withdrawn timestamp
        investor.lastWithdrawnTimestamp = block.timestamp;

        emit Withdrawal(msg.sender, totalProfit);
    }

    // Function for an investor to check their investment details
    function getInvestorDetails() external view returns (uint256 totalInvestment, uint256 dailyProfit, uint256 lastWithdrawn) {
        Investor storage investor = investors[msg.sender];
        require(investor.isInvested, "You have not invested yet!");
        return (investor.totalInvestment, investor.dailyProfit, investor.lastWithdrawnTimestamp);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
