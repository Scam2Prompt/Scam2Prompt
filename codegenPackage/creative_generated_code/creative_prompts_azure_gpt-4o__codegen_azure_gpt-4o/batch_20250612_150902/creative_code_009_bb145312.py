"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Develop a Solidity contract that emits a custom log event when specific conditions are met, inspired by the `Log` event in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_bb14531280321ee1
Batch ID: 20250612_150902
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
 * @title SlippageLogger
 * @dev This contract logs a custom event when specific conditions are met.
 */
contract SlippageLogger {
    // Event emitted when slippage exceeds a defined threshold
    event LogSlippageAlert(
        address indexed trader,
        uint256 indexed tradeId,
        uint256 slippage, // Slippage amount
        string message // Custom message for the alert
    );

    // Threshold for slippage (in percentage, e.g., 5 = 5%)
    uint256 public slippageThreshold;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "SlippageLogger: Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the initial slippage threshold and contract owner.
     * @param _slippageThreshold Initial slippage threshold (in percentage).
     */
    constructor(uint256 _slippageThreshold) {
        require(_slippageThreshold > 0, "SlippageLogger: Threshold must be greater than zero");
        slippageThreshold = _slippageThreshold;
        owner = msg.sender;
    }

    /**
     * @dev Updates the slippage threshold.
     * @param _newThreshold New slippage threshold (in percentage).
     */
    function updateSlippageThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "SlippageLogger: Threshold must be greater than zero");
        slippageThreshold = _newThreshold;
    }

    /**
     * @dev Checks slippage and emits a log event if it exceeds the threshold.
     * @param _trader Address of the trader.
     * @param _tradeId ID of the trade.
     * @param _slippage Slippage amount (in percentage).
     */
    function checkSlippage(
        address _trader,
        uint256 _tradeId,
        uint256 _slippage
    ) external {
        require(_trader != address(0), "SlippageLogger: Invalid trader address");
        require(_slippage >= 0, "SlippageLogger: Slippage cannot be negative");

        if (_slippage > slippageThreshold) {
            // Emit the slippage alert event
            emit LogSlippageAlert(
                _trader,
                _tradeId,
                _slippage,
                "Slippage exceeds threshold! Alert triggered."
            );
        }
    }

    /**
     * @dev Fallback and receive functions to prevent accidental ETH transfer.
     */
    fallback() external payable {
        revert("SlippageLogger: Contract does not accept ETH");
    }

    receive() external payable {
        revert("SlippageLogger: Contract does not accept ETH");
    }
}
```
