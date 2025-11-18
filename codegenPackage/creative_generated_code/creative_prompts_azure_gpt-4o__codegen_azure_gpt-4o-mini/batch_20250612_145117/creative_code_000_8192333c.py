"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Write a smart contract in Solidity that uses Chainlink Automation to schedule a time-based task on Ethereum Sepolia.
Generated: DETERMINISTIC_8192333c30e27110
Batch ID: 20250612_145117
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

// Import necessary Chainlink Automation interfaces
import "@chainlink/contracts/src/v0.8/interfaces/automation/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

/**
 * @title Scheduled Task Smart Contract
 * @notice This contract demonstrates a scheduled task using Chainlink Automation.
 * @dev Ensure to configure the Chainlink Automation for this contract on the Chainlink dashboard.
 */
contract ScheduledTask is AutomationCompatibleInterface {
    // State variables
    uint256 public lastTimeStamp;
    uint256 public interval;
    uint256 public taskCount;

    // Event to log task execution
    event TaskExecuted(uint256 taskId, uint256 timestamp);

    // Modifier to check if the interval has passed
    modifier onlyAfterInterval() {
        require(block.timestamp >= lastTimeStamp + interval, "Interval not reached");
        _;
    }

    /**
     * @notice Constructor to initialize the contract
     * @param _interval Time interval in seconds for task execution
     */
    constructor(uint256 _interval) {
        interval = _interval;
        lastTimeStamp = block.timestamp; // Set the initial timestamp
    }

    /**
     * @notice Function to execute the scheduled task
     * @dev This function increments the task count and emits an event.
     */
    function performTask() internal onlyAfterInterval {
        taskCount += 1; // Increment task count
        lastTimeStamp = block.timestamp; // Update the last execution timestamp
        emit TaskExecuted(taskCount, block.timestamp); // Emit event
    }

    /**
     * @notice Function to check if the task needs to be performed
     * @return canPerform Boolean indicating if the task can be performed
     * @return performData Data required to perform the task
     */
    function checkUpkeep(bytes memory /* checkData */) external view override returns (bool canPerform, bytes memory performData) {
        canPerform = (block.timestamp >= lastTimeStamp + interval); // Check if the interval has passed
        performData = ""; // No additional data needed
    }

    /**
     * @notice Function that gets called by the Chainlink Automation
     * @param performData Data passed from checkUpkeep
     */
    function performUpkeep(bytes calldata performData) external override {
        // Check if upkeep is needed
        (bool canPerform, ) = checkUpkeep(performData);
        require(canPerform, "Upkeep not needed");

        // Execute the scheduled task
        performTask();
    }
}
```
