"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Write code to automate the creation of smart contracts for blockchain token investments, ensuring ROI calculations are backed by smart contract agreements as described by Welstrade.
Generated: DETERMINISTIC_0742981c05be02df
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready smart contract code for automating blockchain token investments with ROI calculations using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenInvestmentContract
 * @dev A smart contract for automating investments in blockchain tokens with ROI calculation.
 */
contract TokenInvestmentContract {
    // Structure to hold investor information
    struct Investor {
        uint256 investedAmount; // Amount invested
        uint256 roi; // ROI percentage
        uint256 investmentTimestamp; // Timestamp when investment was made
        bool exists; // Flag to check if investor exists
    }

    // Mapping to store investors
    mapping(address => Investor) private investors;

    // Owner of the contract
    address public owner;

    // Event to log investments
    event InvestmentMade(address indexed investor, uint256 amount, uint256 roi);

    // Event to log ROI payouts
    event PayoutMade(address indexed investor, uint256 payoutAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only owner can perform this action.");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows owner to set up an investment for an investor.
     * @param investor Address of the investor
     * @param amount Amount invested by the investor (in wei)
     * @param roi ROI percentage for the investment
     */
    function setupInvestment(address investor, uint256 amount, uint256 roi) external onlyOwner {
        require(investor != address(0), "Invalid investor address.");
        require(amount > 0, "Investment amount must be greater than zero.");
        require(roi > 0 && roi <= 100, "Invalid ROI percentage.");

        Investor storage inv = investors[investor];
        require(!inv.exists, "Investor already exists.");

        investors[investor] = Investor({
            investedAmount: amount,
            roi: roi,
            investmentTimestamp: block.timestamp,
            exists: true
        });

        emit InvestmentMade(investor, amount, roi);
    }

    /**
     * @dev Allows investors to claim their ROI based on the investment agreement.
     */
    function claimROI() external {
        Investor storage inv = investors[msg.sender];
        require(inv.exists, "No investment found for this address.");

        // Ensure ROI can be claimed only once per investment cycle
        uint256 timeElapsed = block.timestamp - inv.investmentTimestamp;
        require(timeElapsed >= 30 days, "You can claim ROI after 30 days.");

        // Calculate ROI payout
        uint256 payoutAmount = (inv.investedAmount * inv.roi) / 100;

        // Reset investment details after payout
        delete investors[msg.sender];

        // Transfer payout to the investor
        (bool success, ) = msg.sender.call{value: payoutAmount}("");
        require(success, "ROI payout failed.");

        emit PayoutMade(msg.sender, payoutAmount);
    }

    /**
     * @dev Fallback function to accept ETH deposits to the contract.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param amount Amount to withdraw (in wei)
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance.");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Get investment details for a specific investor.
     * @param investor Address of the investor
     * @return investedAmount, roi, investmentTimestamp, exists
     */
    function getInvestmentDetails(address investor)
        external
        view
        returns (uint256 investedAmount, uint256 roi, uint256 investmentTimestamp, bool exists)
    {
        Investor storage inv = investors[investor];
        return (inv.investedAmount, inv.roi, inv.investmentTimestamp, inv.exists);
    }
}
```

This Solidity smart contract is designed for Ethereum-compatible blockchain platforms. It is thoroughly documented, follows best practices, has proper error handling, and is production-ready. Make sure to test the contract on a test network before deploying it to production.
