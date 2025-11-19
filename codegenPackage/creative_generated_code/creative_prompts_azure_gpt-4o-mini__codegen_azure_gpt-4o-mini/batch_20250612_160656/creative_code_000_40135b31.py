"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: How can I integrate Pyth Network's real-time price feeds into my smart contract on EVM using the provided API documentation?
Generated: DETERMINISTIC_40135b312ed32e31
Batch ID: 20250612_160656
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

interface IPyth {
    function getPrice(string memory assetId) external view returns (int256 price, uint256 timestamp);
}

contract PriceConsumer {
    // Pyth network price feed contract address (replace with actual address)
    IPyth public pyth;

    // Event to emit price updates
    event PriceUpdated(string indexed assetId, int256 price, uint256 timestamp);

    // Constructor to set the Pyth contract address
    constructor(address _pythContract) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        pyth = IPyth(_pythContract);
    }

    // Function to fetch price from Pyth network
    function updatePrice(string memory assetId) external {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");

        // Fetch the price from the Pyth network
        (int256 price, uint256 timestamp) = pyth.getPrice(assetId);
        
        // Error handling for price retrieval
        require(price > 0, "Invalid price retrieved");
        require(timestamp > 0, "Invalid timestamp retrieved");

        // Emit the price update event
        emit PriceUpdated(assetId, price, timestamp);
    }
}
```
