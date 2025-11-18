"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a Solidity function that allows users to reinvest their earned dividends, deducting a 2% reinvestment fee, and updates their token balance accordingly, as outlined on BibbyDivs.com.
Generated: DETERMINISTIC_e55db9cce662d0eb
Batch ID: 20250612_150316
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

contract BibbyDivs {
    // Mapping to track user balances
    mapping(address => uint256) public tokenBalance;
    mapping(address => uint256) public dividendsEarned;

    // Reinvestment fee (2%) as a percentage
    uint256 public constant REINVESTMENT_FEE_PERCENT = 2;

    // Event emitted when a user reinvests dividends
    event DividendsReinvested(address indexed user, uint256 amount, uint256 fee);

    /**
     * @notice Function to reinvest earned dividends, deducting a reinvestment fee
     */
    function reinvestDividends() external {
        uint256 earnedDividends = dividendsEarned[msg.sender];
        require(earnedDividends > 0, "No dividends to reinvest");

        // Calculate the fee and net amount to reinvest
        uint256 reinvestmentFee = (earnedDividends * REINVESTMENT_FEE_PERCENT) / 100;
        uint256 netReinvestment = earnedDividends - reinvestmentFee;

        // Update the user's token balance
        tokenBalance[msg.sender] += netReinvestment;

        // Reset the user's earned dividends
        dividendsEarned[msg.sender] = 0;

        // Emit the reinvestment event
        emit DividendsReinvested(msg.sender, netReinvestment, reinvestmentFee);
    }

    /**
     * @dev Helper function to simulate adding dividends for a user
     * (not part of the production-ready reinvestDividends function)
     */
    function addDividends(address user, uint256 amount) external {
        dividendsEarned[user] += amount;
    }
}
```
