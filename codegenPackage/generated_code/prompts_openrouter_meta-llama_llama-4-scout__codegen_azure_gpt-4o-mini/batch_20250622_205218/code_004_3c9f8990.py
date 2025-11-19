"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: What are the steps to automate a smart contract using Chainlink Automation's job scheduler for time-based automation?
Generated: DETERMINISTIC_3c9f899022650732
Batch ID: 20250622_205218
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

// Import the Chainlink Automation interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/AutomationRegistryInterface.sol";

contract TimeBasedAutomation is AutomationCompatibleInterface {
    // State variables
    uint256 public lastTimeStamp;
    uint256 public interval;
    address public owner;

    // Event to log when the contract is automated
    event AutomatedAction(uint256 timestamp);

    // Constructor to initialize the contract
    constructor(uint256 _interval) {
        owner = msg.sender; // Set the contract deployer as the owner
        interval = _interval; // Set the time interval for automation
        lastTimeStamp = block.timestamp; // Initialize the last timestamp
    }

    // Function to check if the automation condition is met
    function checkUpkeep(bytes memory /* checkData */) public view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        // Check if the time interval has passed
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
    }

    // Function to perform the automated action
    function performUpkeep(bytes calldata /* performData */) external override {
        // Ensure that the upkeep is needed
        (bool upkeepNeeded, ) = checkUpkeep("");
        require(upkeepNeeded, "Upkeep not needed");

        // Update the last timestamp
        lastTimeStamp = block.timestamp;

        // Emit an event to log the automated action
        emit AutomatedAction(lastTimeStamp);
    }

    // Function to update the interval (only callable by the owner)
    function updateInterval(uint256 newInterval) external {
        require(msg.sender == owner, "Only the owner can update the interval");
        interval = newInterval;
    }

    // Function to withdraw any Ether sent to the contract (only callable by the owner)
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
