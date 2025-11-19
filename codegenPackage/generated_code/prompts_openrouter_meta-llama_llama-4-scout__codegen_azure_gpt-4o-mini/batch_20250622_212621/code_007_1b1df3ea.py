"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a code example for a Flare smart contract that uses the FTSO for decentralized price feeds and triggers actions based on price movements.
Generated: DETERMINISTIC_1b1df3eae8d04336
Batch ID: 20250622_212621
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

// Importing the interface for the FTSO (Flexible Tokenized Security Offering)
import "@flaredao/ftso/contracts/IFTSO.sol";

// Contract to demonstrate the use of FTSO for decentralized price feeds
contract PriceActionTrigger {
    // State variables
    IFTSO public ftso; // Instance of the FTSO contract
    address public owner; // Owner of the contract
    uint256 public priceThreshold; // Price threshold for triggering actions
    bool public actionTriggered; // Flag to indicate if action has been triggered

    // Events
    event ActionTriggered(uint256 price);
    event PriceThresholdUpdated(uint256 newThreshold);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _ftso, uint256 _priceThreshold) {
        require(_ftso != address(0), "Invalid FTSO address");
        ftso = IFTSO(_ftso);
        owner = msg.sender;
        priceThreshold = _priceThreshold;
        actionTriggered = false;
    }

    // Function to update the price threshold
    function updatePriceThreshold(uint256 newThreshold) external onlyOwner {
        priceThreshold = newThreshold;
        emit PriceThresholdUpdated(newThreshold);
    }

    // Function to check the current price and trigger action if necessary
    function checkPriceAndTriggerAction() external {
        // Fetch the current price from the FTSO
        uint256 currentPrice = ftso.getCurrentPrice();
        
        // Check if the current price exceeds the threshold and action has not been triggered
        if (currentPrice > priceThreshold && !actionTriggered) {
            actionTriggered = true; // Set the flag to true
            emit ActionTriggered(currentPrice); // Emit the action triggered event
            // Add logic for the action to be triggered here
        }
    }

    // Function to reset the action trigger status (can be called by the owner)
    function resetActionTrigger() external onlyOwner {
        actionTriggered = false;
    }

    // Function to retrieve the current price from the FTSO
    function getCurrentPrice() external view returns (uint256) {
        return ftso.getCurrentPrice();
    }
}
```
