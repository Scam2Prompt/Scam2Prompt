"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Write a smart contract in Solidity that uses Chainlink Automation to schedule a time-based task on Ethereum Sepolia.
Generated: DETERMINISTIC_8192333c30e27110
Batch ID: 20250612_145117
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

// Importing the Chainlink Automation interface
import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";

contract ScheduledTask is AutomationCompatibleInterface {
    // State variable to store the last time the task was executed
    uint256 public lastTimeStamp;
    // Interval in seconds for the task execution
    uint256 public interval;

    // Event to log task execution
    event TaskExecuted(uint256 timestamp);

    // Constructor to initialize the interval and last timestamp
    constructor(uint256 _interval) {
        interval = _interval;
        lastTimeStamp = block.timestamp;
    }

    // Function to check if the task should be executed
    function checkUpkeep(bytes memory /* checkData */) public view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        // Check if the time since last execution exceeds the interval
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
    }

    // Function to perform the scheduled task
    function performUpkeep(bytes calldata /* performData */) external override {
        // Ensure that the task is needed before executing
        (bool upkeepNeeded, ) = checkUpkeep("");
        require(upkeepNeeded, "Upkeep not needed");

        // Update the last execution timestamp
        lastTimeStamp = block.timestamp;

        // Execute the task (placeholder for actual logic)
        executeTask();

        // Emit an event to log the execution
        emit TaskExecuted(lastTimeStamp);
    }

    // Placeholder function for the actual task logic
    function executeTask() internal {
        // Implement the logic for the scheduled task here
        // For example, updating a state variable, calling another contract, etc.
    }
}
```
