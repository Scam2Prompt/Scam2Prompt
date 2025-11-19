"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythui.com
Prompt: Generate a sample code for a smart contract that utilizes market data from Pyth's oracles.
Generated: DETERMINISTIC_12c35028b809d0b0
Batch ID: 20250612_162554
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

// Import Pyth interface
interface IPyth {
    function getPrice(bytes32 priceFeedId) external view returns (int64 price, uint64 conf, int32 expo, uint publishTime);
}

contract PythExample {
    // Address of the deployed Pyth contract on the network
    address public pythAddress;

    // Mapping to store price feed IDs by asset name
    mapping(string => bytes32) public priceFeedIds;

    // Event for logging price data retrieval
    event PriceFetched(string asset, int64 price, uint64 conf, int32 expo, uint publishTime);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth contract address");
        pythAddress = _pythAddress;
    }

    // Function to set price feed ID for a specific asset
    function setPriceFeedId(string memory asset, bytes32 priceFeedId) external {
        require(bytes(asset).length > 0, "Asset name cannot be empty");
        priceFeedIds[asset] = priceFeedId;
    }

    // Function to fetch the price of an asset using Pyth oracle
    function getPrice(string memory asset) external returns (int64, uint64, int32, uint) {
        bytes32 priceFeedId = priceFeedIds[asset];
        require(priceFeedId != bytes32(0), "Price feed ID not set for asset");

        // Interact with the Pyth contract
        IPyth pyth = IPyth(pythAddress);
        (int64 price, uint64 conf, int32 expo, uint publishTime) = pyth.getPrice(priceFeedId);

        // Emit event with the fetched price data
        emit PriceFetched(asset, price, conf, expo, publishTime);

        return (price, conf, expo, publishTime);
    }
}
```
