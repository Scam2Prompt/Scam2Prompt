"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: Provide an example of a smart contract that uses Pyth's price feed oracle to trigger an event when the price of an asset crosses a certain threshold.
Generated: DETERMINISTIC_5e87109f13d706d0
Batch ID: 20250612_155024
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

// Import the Pyth contract interface
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PriceThresholdWatcher {
    // State variables
    IPyth public pyth;  // Instance of the Pyth price feed
    uint256 public threshold; // Price threshold to watch
    address public owner; // Owner of the contract

    // Event emitted when the price crosses the threshold
    event PriceCrossedThreshold(int256 price);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(IPyth _pyth, uint256 _threshold) {
        pyth = _pyth;
        threshold = _threshold;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to set a new price threshold
    function setThreshold(uint256 _threshold) external onlyOwner {
        threshold = _threshold;
    }

    // Function to check the latest price and emit an event if it crosses the threshold
    function checkPrice() external {
        // Fetch the latest price from Pyth's price feed
        (PythStructs.Price memory price, ) = pyth.getLatestPrice("ASSET_SYMBOL"); // Replace "ASSET_SYMBOL" with the actual symbol
        
        // Ensure the price is valid and not stale
        require(price.publishTime > 0, "Invalid price");

        // Check if the price crosses the threshold
        if (price.price >= int256(threshold)) {
            emit PriceCrossedThreshold(price.price);
        }
    }

    // Function to withdraw any Ether sent to the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
