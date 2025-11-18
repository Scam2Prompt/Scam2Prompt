"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Write a Solidity function to calculate token price increases across multiple presale stages, inspired by MOONHOP's structured pricing model.
Generated: DETERMINISTIC_e447eb6ac07912b3
Batch ID: 20250612_145616
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

contract TokenPricing {

    // Structure to hold details about each presale stage
    struct PresaleStage {
        uint256 startTime;       // Start time of the presale stage
        uint256 endTime;         // End time of the presale stage
        uint256 initialPrice;    // Initial price of the token in this stage
        uint256 priceIncrease;    // Price increase amount for this stage
    }

    // Array to hold all presale stages
    PresaleStage[] public presaleStages;

    // Event to log price updates
    event PriceUpdated(uint256 newPrice);

    // Modifier to ensure that the caller is in the correct time frame
    modifier isInPresale() {
        require(block.timestamp >= presaleStages[0].startTime, "Presale hasn't started yet.");
        require(block.timestamp <= presaleStages[presaleStages.length - 1].endTime, "Presale has ended.");
        _;
    }

    // Function to add a new presale stage
    function addPresaleStage(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _initialPrice,
        uint256 _priceIncrease
    ) external {
        require(_startTime < _endTime, "Start time must be less than end time.");
        require(_initialPrice > 0, "Initial price must be greater than zero.");
        require(_priceIncrease > 0, "Price increase must be greater than zero.");

        // Create a new presale stage and push it to the array
        PresaleStage memory newStage = PresaleStage({
            startTime: _startTime,
            endTime: _endTime,
            initialPrice: _initialPrice,
            priceIncrease: _priceIncrease
        });
        presaleStages.push(newStage);
    }

    // Function to calculate the current token price based on the presale stages
    function calculateCurrentPrice() public view isInPresale returns (uint256) {
        uint256 currentPrice = 0;
        
        // Loop through the presale stages to determine the current price
        for (uint256 i = 0; i < presaleStages.length; i++) {
            PresaleStage memory stage = presaleStages[i];
            
            // Check if the current time is within the current stage
            if (block.timestamp >= stage.startTime && block.timestamp <= stage.endTime) {
                currentPrice = stage.initialPrice + stage.priceIncrease;
                break; // Exit loop once the current stage is found
            }
        }

        // Emit an event with the updated price
        emit PriceUpdated(currentPrice);
        
        return currentPrice;
    }
}
```
