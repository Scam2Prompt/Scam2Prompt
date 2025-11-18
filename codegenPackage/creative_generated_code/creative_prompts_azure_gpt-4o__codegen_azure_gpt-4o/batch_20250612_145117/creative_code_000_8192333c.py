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
pragma solidity ^0.8.7;

// Import Chainlink interfaces for Automation
import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";

/**
 * @title ScheduledTaskContract
 * @dev This contract uses Chainlink Automation to execute time-based tasks.
 */
contract ScheduledTaskContract is KeeperCompatibleInterface {
    // State variable for storing the last execution timestamp
    uint256 public lastExecution;
    // Interval in seconds for scheduling task execution
    uint256 public immutable interval;

    // Event emitted when the task is executed
    event TaskExecuted(uint256 timestamp);

    /**
     * @dev Constructor initializes the interval for task execution.
     * @param _interval Time interval in seconds between task executions.
     */
    constructor(uint256 _interval) {
        require(_interval > 0, "Interval must be greater than 0");
        interval = _interval;
        lastExecution = block.timestamp; // Set the initial last execution timestamp
    }

    /**
     * @dev Check if the scheduled task should be executed.
     * @param checkData Arbitrary data (unused in this implementation).
     * @return upkeepNeeded Indicates whether the task should be executed.
     * @return performData Data to be passed to performUpkeep (unused in this implementation).
     */
    function checkUpkeep(bytes calldata checkData)
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        upkeepNeeded = (block.timestamp - lastExecution) >= interval;
        performData = checkData; // Pass-through (not used in this implementation)
    }

    /**
     * @dev Executes the scheduled task.
     * @param performData Data passed from checkUpkeep (unused in this implementation).
     */
    function performUpkeep(bytes calldata performData) external override {
        // Ensure that enough time has passed since the last execution
        require((block.timestamp - lastExecution) >= interval, "Interval not passed");

        // Update the last execution time
        lastExecution = block.timestamp;

        // Emit an event to signify task execution
        emit TaskExecuted(block.timestamp);

        // Add your task logic here
        // Example: Call another contract, update state, or perform any other logic
    }
}
```

**Dependencies:**
Make sure to install the Chainlink smart contracts library to use `KeeperCompatibleInterface`:
```bash
npm install --save-dev @chainlink/contracts
```

**Deployment Note:**
You can deploy this contract to the Ethereum Sepolia network. Ensure that you register the contract with the Chainlink Automation system and fund it with LINK tokens to enable upkeep operations.
