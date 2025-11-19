"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "How to implement a slippage control mechanism in a Solidity smart contract for automated trades on Ethereum mainnet?"
Generated: DETERMINISTIC_406973ea9325b2c1
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SlippageControl
 * @dev A smart contract to implement slippage control for automated trades on Ethereum mainnet.
 *      This contract ensures that trades are executed only if the price impact is within acceptable limits.
 */
contract SlippageControl {
    // Address of the owner of the contract
    address public owner;

    // Event emitted when a trade is executed
    event TradeExecuted(address indexed trader, uint256 amountIn, uint256 amountOut, uint256 slippage);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "SlippageControl: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Executes a trade with slippage control.
     * @param amountIn The amount of input tokens to trade.
     * @param expectedAmountOut The expected amount of output tokens.
     * @param maxSlippage The maximum allowable slippage percentage (e.g., 5 for 5%).
     * @param actualAmountOut The actual amount of output tokens received from the trade.
     */
    function executeTrade(
        uint256 amountIn,
        uint256 expectedAmountOut,
        uint256 maxSlippage,
        uint256 actualAmountOut
    ) external onlyOwner {
        // Validate input parameters
        require(amountIn > 0, "SlippageControl: amountIn must be greater than zero");
        require(expectedAmountOut > 0, "SlippageControl: expectedAmountOut must be greater than zero");
        require(maxSlippage > 0, "SlippageControl: maxSlippage must be greater than zero");

        // Calculate the slippage percentage
        uint256 slippage = calculateSlippage(expectedAmountOut, actualAmountOut);

        // Ensure the slippage is within the acceptable range
        require(slippage <= maxSlippage, "SlippageControl: Slippage exceeds maximum allowable limit");

        // Emit the trade execution event
        emit TradeExecuted(msg.sender, amountIn, actualAmountOut, slippage);
    }

    /**
     * @dev Calculates the slippage percentage.
     * @param expectedAmountOut The expected amount of output tokens.
     * @param actualAmountOut The actual amount of output tokens received.
     * @return The slippage percentage.
     */
    function calculateSlippage(uint256 expectedAmountOut, uint256 actualAmountOut) public pure returns (uint256) {
        // Ensure expectedAmountOut is greater than zero to avoid division by zero
        require(expectedAmountOut > 0, "SlippageControl: expectedAmountOut must be greater than zero");

        // Calculate the slippage percentage
        if (actualAmountOut >= expectedAmountOut) {
            return 0; // No slippage if actualAmountOut is greater than or equal to expectedAmountOut
        }
        uint256 difference = expectedAmountOut - actualAmountOut;
        return (difference * 100) / expectedAmountOut;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "SlippageControl: new owner cannot be the zero address");
        owner = newOwner;
    }
}
```
