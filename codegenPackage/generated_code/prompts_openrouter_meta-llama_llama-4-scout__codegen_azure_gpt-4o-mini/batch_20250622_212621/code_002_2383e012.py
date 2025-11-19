"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Generate a smart contract code on Flare that triggers using data from Web2 APIs and the Flare Time Series Oracle (FTSO).
Generated: DETERMINISTIC_2383e012e0b684cc
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Flare Time Series Oracle (FTSO)
interface IFTSO {
    function getLatestPrice() external view returns (uint256);
}

// Smart contract to interact with Web2 APIs and FTSO
contract Web2DataTrigger is Ownable {
    using SafeMath for uint256;

    // State variables
    IFTSO public ftsO; // FTSO contract address
    uint256 public threshold; // Price threshold for triggering actions
    uint256 public lastTriggeredPrice; // Last price that triggered an action

    // Event to log when the action is triggered
    event ActionTriggered(uint256 price);

    // Constructor to initialize the contract with the FTSO address and threshold
    constructor(address _ftso, uint256 _threshold) {
        require(_ftso != address(0), "Invalid FTSO address");
        require(_threshold > 0, "Threshold must be greater than zero");
        
        ftsO = IFTSO(_ftso);
        threshold = _threshold;
    }

    // Function to update the threshold
    function updateThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Threshold must be greater than zero");
        threshold = _newThreshold;
    }

    // Function to check the latest price from FTSO and trigger action if conditions are met
    function checkPriceAndTrigger() external {
        uint256 latestPrice = ftsO.getLatestPrice();
        
        // Check if the latest price exceeds the threshold
        if (latestPrice > threshold && latestPrice != lastTriggeredPrice) {
            lastTriggeredPrice = latestPrice; // Update the last triggered price
            emit ActionTriggered(latestPrice); // Emit event for action triggered
            // Here you can add additional logic to interact with Web2 APIs
        }
    }

    // Function to withdraw any Ether sent to the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
