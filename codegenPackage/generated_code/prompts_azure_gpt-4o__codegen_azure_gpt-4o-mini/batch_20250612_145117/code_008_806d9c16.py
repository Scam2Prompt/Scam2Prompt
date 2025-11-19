"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Generate a Solidity contract that uses Chainlink Automation to perform a task based on a custom logic condition on BNB Chain Testnet.
Generated: DETERMINISTIC_806d9c16040ff205
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
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/AutomationRegistryInterface.sol";

contract CustomLogicAutomation is AutomationCompatibleInterface {
    // State variables
    uint256 public lastTimeStamp;
    uint256 public interval;
    uint256 public threshold;
    uint256 public counter;

    // Event to emit when the task is performed
    event TaskPerformed(uint256 newCounter);

    // Constructor to initialize the contract
    constructor(uint256 _interval, uint256 _threshold) {
        interval = _interval; // Set the interval for automation
        threshold = _threshold; // Set the threshold for custom logic
        lastTimeStamp = block.timestamp; // Initialize last timestamp
        counter = 0; // Initialize counter
    }

    // Function to check if the task should be performed
    function checkUpkeep(bytes memory /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        // Check if the time interval has passed and if the counter is below the threshold
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval && counter < threshold;
    }

    // Function to perform the task
    function performUpkeep(bytes calldata /* performData */) external override {
        // Ensure that the upkeep is needed
        (bool upkeepNeeded, ) = checkUpkeep("");
        require(upkeepNeeded, "Upkeep not needed");

        // Update the last timestamp
        lastTimeStamp = block.timestamp;

        // Increment the counter
        counter++;

        // Emit an event to signal that the task has been performed
        emit TaskPerformed(counter);
    }

    // Function to set a new interval (onlyOwner can call this)
    function setInterval(uint256 _interval) external {
        interval = _interval;
    }

    // Function to set a new threshold (onlyOwner can call this)
    function setThreshold(uint256 _threshold) external {
        threshold = _threshold;
    }

    // Function to get the current counter value
    function getCounter() external view returns (uint256) {
        return counter;
    }
}
```
