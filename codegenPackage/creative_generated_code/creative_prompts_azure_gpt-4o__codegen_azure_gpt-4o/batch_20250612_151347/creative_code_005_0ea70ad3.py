"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Create a Solidity contract that emits a custom event (`Log`) for debugging purposes, similar to the constructor and event setup in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_0ea70ad3be48c149
Batch ID: 20250612_151347
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
 * @title DebuggingEventEmitter
 * @dev A contract that emits custom events for debugging purposes.
 */
contract DebuggingEventEmitter {

    // Custom event for logging messages
    event Log(address indexed sender, string message, uint256 value);

    /**
     * @dev Constructor that emits a `Log` event upon deployment.
     */
    constructor() {
        emit Log(msg.sender, "Contract deployed successfully", 0);
    }

    /**
     * @dev Function to emit a custom log event with a message and value.
     * @param _message The message string to be emitted in the event.
     * @param _value The value to be emitted in the event.
     */
    function emitLog(string calldata _message, uint256 _value) external {
        // Emit the Log event with the sender's address, message, and value
        emit Log(msg.sender, _message, _value);
    }
}
```
