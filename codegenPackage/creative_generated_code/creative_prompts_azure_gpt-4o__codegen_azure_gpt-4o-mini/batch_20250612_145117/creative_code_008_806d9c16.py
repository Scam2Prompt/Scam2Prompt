"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Generate a Solidity contract that uses Chainlink Automation to perform a task based on a custom logic condition on BNB Chain Testnet.
Generated: DETERMINISTIC_806d9c16040ff205
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

// Importing Chainlink Automation Interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomAutomation is AutomationCompatibleInterface, Ownable {
    // State variables
    uint256 public lastCheck;
    uint256 public threshold;
    uint256 public storedData;

    // Event declaration
    event DataUpdated(uint256 newData);

    // Constructor to initialize the contract with a threshold
    constructor(uint256 _threshold) {
        threshold = _threshold;
        lastCheck = block.timestamp;
    }

    // Function to update the stored data
    function updateData(uint256 newData) external onlyOwner {
        require(newData > 0, "Data must be greater than zero");
        storedData = newData;
        emit DataUpdated(newData);
    }

    // Function to check if the condition for automation is met
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        // Check if stored data exceeds the threshold
        upkeepNeeded = (storedData > threshold) && (block.timestamp - lastCheck >= 1 hours);
    }

    // Function that performs the task when the condition is met
    function performUpkeep(bytes calldata) external override {
        // Check if upkeep is needed
        (bool upkeepNeeded, ) = checkUpkeep("");
        require(upkeepNeeded, "Upkeep not needed");

        // Update the last check timestamp
        lastCheck = block.timestamp;

        // Custom logic can be added here
        // For demonstration, we'll reset storedData
        storedData = 0;
        emit DataUpdated(storedData);
    }
}
```
