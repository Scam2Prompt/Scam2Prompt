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
pragma solidity ^0.8.7;

// Import Chainlink Automation interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";

// Example contract to demonstrate Chainlink Automation on BNB Chain Testnet
contract ChainlinkAutomationExample is AutomationCompatibleInterface {
    // Public state variables
    uint256 public lastCheckTimestamp; // Records the last timestamp the condition was checked
    uint256 public interval; // Interval for performing automation task
    address public owner; // Contract owner

    // Event emitted when the task is executed
    event TaskExecuted(uint256 timestamp);

    // Constructor to initialize contract parameters
    constructor(uint256 _interval) {
        require(_interval > 0, "Interval must be greater than 0");
        interval = _interval;
        lastCheckTimestamp = block.timestamp;
        owner = msg.sender;
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Chainlink's checkUpkeep function
    // This function is called off-chain by Chainlink nodes to check if upkeep is needed
    function checkUpkeep(bytes calldata /* checkData */)
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory /* performData */)
    {
        // Check if the time interval has passed
        upkeepNeeded = (block.timestamp - lastCheckTimestamp) >= interval;
    }

    // Chainlink's performUpkeep function
    // This function is called on-chain by Chainlink nodes to perform the task
    function performUpkeep(bytes calldata /* performData */) external override {
        // Ensure the condition is met before performing the task
        if ((block.timestamp - lastCheckTimestamp) >= interval) {
            // Update the last check timestamp
            lastCheckTimestamp = block.timestamp;

            // Execute the custom logic here
            emit TaskExecuted(block.timestamp);
        } else {
            revert("Condition not met for performUpkeep");
        }
    }

    // Function to update the interval (only callable by owner)
    function setInterval(uint256 _interval) external onlyOwner {
        require(_interval > 0, "Interval must be greater than 0");
        interval = _interval;
    }

    // Fallback function and receive function to accept BNB (if needed)
    receive() external payable {}

    fallback() external payable {}
}
```
