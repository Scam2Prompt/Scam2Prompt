"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flrconnectportal.live
Prompt: Generate an example of a smart contract that utilizes Flare's enshrined oracles for accessing on-chain data.
Generated: DETERMINISTIC_fc8c211148afe2b0
Batch ID: 20250612_162431
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

// Import Flare's enshrined oracle interface
import "@flarenetwork/flare-smart-contracts/contracts/interfaces/IPriceOracle.sol";

// Example of a smart contract utilizing Flare's enshrined oracles
contract FlareOracleExample {
    // Address of the Flare Price Oracle contract
    IPriceOracle public priceOracle;

    // Owner of the contract
    address public owner;

    // Events for logging
    event PriceRetrieved(address indexed asset, uint256 price);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor to initialize the oracle address and set the contract owner
    constructor(address _priceOracleAddress) {
        require(_priceOracleAddress != address(0), "Invalid oracle address");
        priceOracle = IPriceOracle(_priceOracleAddress);
        owner = msg.sender;
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to retrieve the price of a specific asset using the Flare oracle
    function getAssetPrice(address assetAddress) external view returns (uint256 price) {
        // Ensure the asset address is valid
        require(assetAddress != address(0), "Invalid asset address");

        // Fetch the price from the oracle
        price = priceOracle.getPrice(assetAddress);
        emit PriceRetrieved(assetAddress, price);
    }

    // Function to update the price oracle address (owner only)
    function updatePriceOracleAddress(address newOracleAddress) external onlyOwner {
        require(newOracleAddress != address(0), "Invalid new oracle address");
        priceOracle = IPriceOracle(newOracleAddress);
    }

    // Function to transfer ownership of the contract (owner only)
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
