"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupp.live
Prompt: Create a function in Solidity to calculate and display the gas price for transactions, referencing the Jupiter Network's example of showing "Gas Price 0,018 ETH."
Generated: DETERMINISTIC_6e1fa92c9bbae368
Batch ID: 20250612_153700
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

contract GasPriceCalculator {
    // Event to log the gas price with the corresponding transaction sender
    event GasPriceDisplayed(address indexed sender, uint256 gasPriceInEth);

    // Function to calculate and display the gas price for the transaction
    function displayGasPrice() external {
        // Get the gas price in wei
        uint256 gasPriceInWei = tx.gasprice;
        
        // Convert gas price from wei to ETH (1 ETH = 10^18 wei)
        uint256 gasPriceInEth = gasPriceInWei / 1e18;

        // Emit the gas price to the event log
        emit GasPriceDisplayed(msg.sender, gasPriceInEth);
    }

    // Function to retrieve the current gas price in wei
    function getCurrentGasPrice() external view returns (uint256) {
        return tx.gasprice;
    }
}
```
