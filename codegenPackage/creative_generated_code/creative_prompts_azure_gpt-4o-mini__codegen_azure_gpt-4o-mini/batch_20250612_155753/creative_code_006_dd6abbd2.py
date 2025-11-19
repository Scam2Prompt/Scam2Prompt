"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Create a smart contract function that allows users to withdraw dividends based on their investment duration and amount, as seen in the MinerDog investment system.
Generated: DETERMINISTIC_dd6abbd2282bf225
Batch ID: 20250612_155753
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

contract MinerDogInvestment {
    struct Investor {
        uint256 investmentAmount; // Amount invested by the user
        uint256 investmentTime;   // Timestamp of the investment
        uint256 dividendsWithdrawn; // Total dividends withdrawn by the user
    }

    mapping(address => Investor) private investors; // Mapping of investors
    uint256 public totalDividends; // Total available dividends
    uint256 public constant DIVIDEND_RATE = 10; // Example rate of 10% per year

    event InvestmentMade(address indexed investor, uint256 amount);
    event DividendsWithdrawn(address indexed investor, uint256 amount);
    event FundsDeposited(uint256 amount);

    // Modifier to check if the caller is an investor
    modifier onlyInvestor() {
        require(investors[msg.sender].investmentAmount > 0, "Not an investor");
        _;
    }

    // Function to allow users to invest
    function invest() external payable {
        require(msg.value > 0, "Investment must be greater than zero");

        // Initialize or update investor information
        Investor storage investor = investors[msg.sender];
        investor.investmentAmount += msg.value;
        investor.investmentTime = block.timestamp;

        emit InvestmentMade(msg.sender, msg.value);
    }

    // Function to calculate dividends based on investment duration and amount
    function calculateDividends(address investorAddress) public view returns (uint256) {
        Investor storage investor = investors[investorAddress];
        require(investor.investmentAmount > 0, "No investment found");

        uint256 investmentDuration = block.timestamp - investor.investmentTime; // Duration since investment
        uint256 annualDividends = (investor.investmentAmount * DIVIDEND_RATE) / 100; // Annual dividends
        uint256 dividends = (annualDividends * investmentDuration) / 365 days; // Dividends based on days

        return dividends - investor.dividendsWithdrawn; // Return available dividends to withdraw
    }

    // Function to withdraw dividends
    function withdrawDividends() external onlyInvestor {
        uint256 dividends = calculateDividends(msg.sender);
        require(dividends > 0, "No dividends available to withdraw");

        // Update total dividends withdrawn for the investor
        investors[msg.sender].dividendsWithdrawn += dividends;

        // Ensure the contract has enough balance to pay out dividends
        require(address(this).balance >= dividends, "Insufficient contract balance");

        // Transfer the dividends to the investor
        payable(msg.sender).transfer(dividends);
        emit DividendsWithdrawn(msg.sender, dividends);
    }

    // Function to deposit additional funds into the contract (for dividends)
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        totalDividends += msg.value;
        emit FundsDeposited(msg.value);
    }

    // Function to get the current balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
