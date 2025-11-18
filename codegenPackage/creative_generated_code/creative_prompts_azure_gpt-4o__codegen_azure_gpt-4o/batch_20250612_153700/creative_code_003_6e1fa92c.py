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

/**
 * @title GasPriceCalculator
 * @dev A contract to fetch and display the current gas price for transactions.
 */
contract GasPriceCalculator {
    /**
     * @dev Event emitted when the gas price is fetched and displayed.
     * @param gasPrice The current gas price in wei.
     */
    event GasPriceFetched(uint256 gasPrice);

    /**
     * @dev Function to calculate and display the current gas price.
     *      The gas price is fetched from the `tx.gasprice` global variable.
     *      Assumes `tx.gasprice` represents the gas price in wei.
     */
    function displayGasPrice() external {
        // Fetch the current gas price in wei
        uint256 gasPriceWei = tx.gasprice;

        // Emit an event with the gas price
        emit GasPriceFetched(gasPriceWei);
    }

    /**
     * @dev Helper function to convert wei to ether.
     * @param weiAmount The amount in wei to be converted.
     * @return The equivalent amount in ether as a string.
     */
    function convertWeiToEther(uint256 weiAmount) public pure returns (string memory) {
        // Ether has 18 decimal places, so divide by 10^18
        uint256 etherAmount = weiAmount / 1 ether;

        // Convert the result to a string
        return _uintToString(etherAmount);
    }

    /**
     * @dev Internal utility function to convert uint256 to string.
     * @param value The uint256 value to convert.
     * @return The string representation of the value.
     */
    function _uintToString(uint256 value) internal pure returns (string memory) {
        if (value == 0) {
            return "0";
        }

        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        bytes memory buffer = new bytes(digits);
        while (value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + uint256(value % 10)));
            value /= 10;
        }

        return string(buffer);
    }
}
```
