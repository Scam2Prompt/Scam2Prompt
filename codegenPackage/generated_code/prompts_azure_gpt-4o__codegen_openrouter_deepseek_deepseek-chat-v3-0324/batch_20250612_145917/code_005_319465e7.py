"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Develop a Solidity contract that emits a custom event `Log` with a string message, as shown in the constructor of the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_319465e790912e16
Batch ID: 20250612_145917
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

contract EventLogger {
    // Custom event to log messages
    event Log(string message);

    /**
     * @dev Constructor that emits a log message upon deployment
     */
    constructor() {
        emit Log("Contract deployed successfully");
    }

    /**
     * @dev Function to emit a custom log message
     * @param message The string message to log
     */
    function logMessage(string memory message) public {
        emit Log(message);
    }
}
```
