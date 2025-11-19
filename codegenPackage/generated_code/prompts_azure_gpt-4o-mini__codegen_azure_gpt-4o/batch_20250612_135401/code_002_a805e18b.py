"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Explain the process of creating a time-based automation job scheduler with Chainlink Automation and provide an example.
Generated: DETERMINISTIC_a805e18b66584c5e
Batch ID: 20250612_135401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

/**
 * @title Time-Based Automation Job Scheduler using Chainlink Automation
 * @dev This contract demonstrates how to use Chainlink Automation to execute a task at regular intervals.
 *      The task in this example increments a counter every specified interval.
 */

import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";

contract TimeBasedAutomation is KeeperCompatibleInterface {
    // State variables
    uint256 public counter; // Counter to track the number of executions
    uint256 public lastTimestamp; // Timestamp of the last execution
    uint256 public interval; // Time interval between executions

    /**
     * @dev Constructor to initialize the contract.
     * @param _interval The time interval (in seconds) between executions.
     */
    constructor(uint256 _interval) {
        interval = _interval;
        lastTimestamp = block.timestamp; // Set the initial timestamp to the current block time
        counter = 0; // Initialize the counter to 0
    }

    /**
     * @dev Chainlink Automation function to check if upkeep is needed.
     * @return upkeepNeeded Boolean indicating whether the task should be executed.
     * @return performData Data passed to the performUpkeep function (not used in this example).
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    ) external view override returns (bool upkeepNeeded, bytes memory performData) {
        upkeepNeeded = (block.timestamp - lastTimestamp) >= interval; // Check if the interval has passed
        performData = ""; // No additional data needed for this example
    }

    /**
     * @dev Chainlink Automation function to perform the task.
     * @param performData Data passed from checkUpkeep (not used in this example).
     */
    function performUpkeep(bytes calldata /* performData */) external override {
        // Ensure the interval has passed before executing the task
        if ((block.timestamp - lastTimestamp) >= interval) {
            lastTimestamp = block.timestamp; // Update the last execution timestamp
            counter += 1; // Increment the counter
        }
    }

    /**
     * @dev Function to update the interval between executions.
     * @param _newInterval The new interval (in seconds).
     */
    function setInterval(uint256 _newInterval) external {
        require(_newInterval > 0, "Interval must be greater than 0");
        interval = _newInterval; // Update the interval
    }

    /**
     * @dev Function to retrieve the current counter value.
     * @return The current counter value.
     */
    function getCounter() external view returns (uint256) {
        return counter;
    }

    /**
     * @dev Function to retrieve the time remaining until the next execution.
     * @return The time remaining (in seconds).
     */
    function timeUntilNextExecution() external view returns (uint256) {
        if ((block.timestamp - lastTimestamp) >= interval) {
            return 0; // Task is ready to execute
        } else {
            return interval - (block.timestamp - lastTimestamp); // Time remaining
        }
    }
}
```

This code is a complete example of a time-based automation job scheduler using Chainlink Automation. It includes proper error handling, follows best practices, and is production-ready.
