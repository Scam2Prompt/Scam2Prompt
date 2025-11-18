"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a Solidity function that calculates the percentage share of dividends for a token holder based on their token holdings and the total supply, as explained on BibbyDivs.com.
Generated: DETERMINISTIC_090ae5805cb815b3
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

/// @title Dividend Calculator
/// @notice This contract allows calculation of dividend shares for token holders
contract DividendCalculator {
    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to store the balance of each token holder
    mapping(address => uint256) public balances;

    /// @notice Event emitted when a new balance is added
    /// @param holder The address of the token holder
    /// @param amount The amount of tokens held
    event BalanceUpdated(address indexed holder, uint256 amount);

    /// @param _totalSupply The initial total supply of tokens
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;
    }

    /// @notice Function to update the balance of a token holder
    /// @param holder The address of the token holder
    /// @param amount The amount of tokens to add to the holder's balance
    function updateBalance(address holder, uint256 amount) external {
        require(holder != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the balance
        balances[holder] += amount;
        emit BalanceUpdated(holder, balances[holder]);
    }

    /// @notice Calculate the percentage share of dividends for a token holder
    /// @param holder The address of the token holder
    /// @return The percentage share of dividends as an integer
    function calculateDividendShare(address holder) external view returns (uint256) {
        require(totalSupply > 0, "Total supply must be greater than zero");
        require(balances[holder] > 0, "Holder has no tokens");

        // Calculate the dividend share percentage
        uint256 holderBalance = balances[holder];
        uint256 dividendShare = (holderBalance * 100) / totalSupply;

        return dividendShare;
    }
}
```
