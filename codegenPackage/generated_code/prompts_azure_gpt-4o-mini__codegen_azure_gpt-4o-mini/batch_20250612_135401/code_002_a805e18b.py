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
pragma solidity ^0.8.0;

// Import the Chainlink Automation interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/AutomationRegistryInterface.sol";

// A simple contract that demonstrates a time-based automation job scheduler using Chainlink Automation
contract TimeBasedScheduler is AutomationCompatibleInterface {
    // State variable to store the last time the job was executed
    uint256 public lastExecutedTime;
    // Interval in seconds for the job execution
    uint256 public interval;
    // Owner of the contract
    address public owner;

    // Event emitted when the job is executed
    event JobExecuted(uint256 timestamp);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _interval) {
        owner = msg.sender; // Set the contract deployer as the owner
        interval = _interval; // Set the interval for job execution
        lastExecutedTime = block.timestamp; // Initialize last executed time
    }

    // Function to check if the job can be executed
    function checkUpkeep(bytes memory /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        upkeepNeeded = (block.timestamp - lastExecutedTime) >= interval; // Check if the interval has passed
    }

    // Function to perform the job execution
    function performUpkeep(bytes calldata /* performData */) external override {
        (bool upkeepNeeded, ) = checkUpkeep(""); // Check if upkeep is needed
        require(upkeepNeeded, "Upkeep not needed"); // Ensure upkeep is needed

        // Execute the job logic
        lastExecutedTime = block.timestamp; // Update the last executed time
        emit JobExecuted(lastExecutedTime); // Emit the event
    }

    // Function to update the interval (only callable by the owner)
    function updateInterval(uint256 _newInterval) external onlyOwner {
        interval = _newInterval; // Update the interval
    }

    // Function to withdraw any Ether sent to the contract (only callable by the owner)
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance); // Transfer the contract balance to the owner
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

This Solidity contract demonstrates a time-based automation job scheduler using Chainlink Automation. It includes proper error handling, access control, and emits events for job execution. The contract is designed to be production-ready, following best practices for smart contract development.
