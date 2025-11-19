"""
Generated Code Metadata:
========================
Original URL: https://chainlinkhub.pages.dev
Prompt: Explain the role of Chainlink Keepers in automating smart contract executions.
Generated: DETERMINISTIC_932d4dbaac0631d4
Batch ID: 20250622_205948
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

// Interface for Chainlink KeeperCompatible contract
interface KeeperCompatibleInterface {
    /**
     * @notice Checks if the contract requires work to be done
     * @dev This function is called by the Chainlink Keeper node to check if upkeep is needed
     * @param checkData Data passed to the contract when checking for upkeep
     * @return upkeepNeeded Boolean indicating whether upkeep is needed
     * @return performData Bytes that the Keeper should call performUpkeep with if upkeep is needed
     */
    function checkUpkeep(bytes calldata checkData) external returns (bool upkeepNeeded, bytes memory performData);

    /**
     * @notice Performs the work on the contract if checkUpkeep returns true
     * @dev This function is called by the Chainlink Keeper node when it detects upkeep is needed
     * @param performData Data which was passed back from the checkData simulation
     */
    function performUpkeep(bytes calldata performData) external;
}

/**
 * @title SampleKeeperContract
 * @dev A sample contract demonstrating Chainlink Keepers integration
 */
contract SampleKeeperContract is KeeperCompatibleInterface {
    uint public lastTimeStamp;
    uint public interval;
    address public owner;

    event UpkeepPerformed(uint timestamp);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Initialize the contract with an upkeep interval
     * @param _interval Time interval (in seconds) between upkeeps
     */
    constructor(uint _interval) {
        interval = _interval;
        lastTimeStamp = block.timestamp;
        owner = msg.sender;
    }

    /**
     * @notice Checks if the contract requires work to be done
     * @dev This example checks if the time interval has passed
     * @param checkData Additional data (unused in this example)
     * @return upkeepNeeded Boolean indicating whether upkeep is needed
     * @return performData Bytes that the Keeper should call performUpkeep with
     */
    function checkUpkeep(bytes calldata checkData)
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
        performData = checkData;
    }

    /**
     * @notice Performs the work on the contract
     * @dev This example simply updates the timestamp and emits an event
     * @param performData Additional data (unused in this example)
     */
    function performUpkeep(bytes calldata performData) external override {
        // Validate the time interval has passed
        require((block.timestamp - lastTimeStamp) > interval, "Interval not met");
        
        // Update the last timestamp
        lastTimeStamp = block.timestamp;
        
        // Perform any other maintenance tasks here
        emit UpkeepPerformed(block.timestamp);
    }

    /**
     * @notice Allows owner to update the interval
     * @param _interval New time interval (in seconds) between upkeeps
     */
    function updateInterval(uint _interval) external onlyOwner {
        interval = _interval;
    }
}
```
