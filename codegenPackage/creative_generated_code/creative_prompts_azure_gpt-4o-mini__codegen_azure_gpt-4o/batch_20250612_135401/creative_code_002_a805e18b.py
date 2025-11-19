"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Explain the process of creating a time-based automation job scheduler with Chainlink Automation and provide an example.
Generated: DETERMINISTIC_a805e18b66584c5e
Batch ID: 20250612_135401
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

// Import the required interfaces from Chainlink Automation
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";

/// @title Time-Based Automation Job Scheduler Using Chainlink Automation
/// @author Your Name
/// @notice This contract demonstrates how to schedule time-based automation using Chainlink Automation
/// @dev The contract implements the AutomationCompatibleInterface for Chainlink Automation

contract TimeBasedScheduler is AutomationCompatibleInterface {
    // State variables
    uint256 public lastExecutedTime;
    uint256 public interval;

    // Events
    event TaskExecuted(uint256 timestamp);

    /// @notice Constructor to initialize the contract
    /// @param _interval Time interval (in seconds) between automated executions
    constructor(uint256 _interval) {
        require(_interval > 0, "Interval must be greater than 0");
        interval = _interval;
        lastExecutedTime = block.timestamp;
    }

    /// @notice Function called by Chainlink Automation to check if the task should be executed
    /// @dev Chainlink nodes call this function and simulate the results off-chain
    /// @return upkeepNeeded Boolean indicating whether the task requires execution
    /// @return performData Data to be passed to the performUpkeep function
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory performData) {
        upkeepNeeded = (block.timestamp - lastExecutedTime) >= interval;
        performData = ""; // No additional data required for this example
    }

    /// @notice Function called by Chainlink Automation to execute the scheduled task
    /// @param performData Data passed from the checkUpkeep function (not used in this example)
    function performUpkeep(bytes calldata performData) external override {
        // Ensure that the task is due for execution
        if ((block.timestamp - lastExecutedTime) >= interval) {
            // Update the last executed time
            lastExecutedTime = block.timestamp;

            // Execute the scheduled task
            _executeTask();

            // Emit an event to log execution
            emit TaskExecuted(block.timestamp);
        }
    }

    /// @notice Internal function to execute the scheduled task
    /// @dev This is where the actual business logic for the scheduled task resides
    function _executeTask() internal {
        // Add your task logic here (e.g., updating state, interacting with other contracts, etc.)
        // For demonstration, this function is empty
    }

    /// @notice Function to update the interval for task execution
    /// @param _newInterval New time interval (in seconds)
    function updateInterval(uint256 _newInterval) external {
        require(_newInterval > 0, "Interval must be greater than 0");
        interval = _newInterval;
    }
}
```

### Explanation in Code Comments:
1. **Chainlink AutomationCompatibleInterface**: The contract implements this interface to integrate with Chainlink Automation.
2. **checkUpkeep**: Chainlink nodes call this function off-chain to check if the upkeep condition is met (i.e., the task requires execution).
3. **performUpkeep**: When upkeep is required, Chainlink nodes call this function to execute the task on-chain.
4. **_executeTask**: Placeholder for the actual logic of the scheduled task.
5. **updateInterval**: Allows updating the interval for task execution.
