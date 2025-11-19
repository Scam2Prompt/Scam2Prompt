"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_d4fbd07a2083925c
Batch ID: 20250612_162806
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

/**
 * @title FTSOPriceConsumer
 * @dev A smart contract to consume and utilize decentralized price feeds from Flare Time Series Oracle (FTSO).
 */
contract FTSOPriceConsumer {
    // Address of the FTSO data provider contract on Flare
    address public ftsoProvider;

    // Modifier to restrict access to owner-only functions (basic access control)
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Event emitted when a new FTSO provider is set
    event FTSOProviderUpdated(address indexed newProvider);

    /**
     * @dev Constructor to initialize the contract with an owner and the initial FTSO provider address.
     * @param _ftsoProvider Address of the FTSO data provider.
     */
    constructor(address _ftsoProvider) {
        require(_ftsoProvider != address(0), "FTSO provider address cannot be zero");
        ftsoProvider = _ftsoProvider;
        owner = msg.sender;
    }

    /**
     * @dev Updates the FTSO provider address. Only callable by the owner.
     * @param _newProvider Address of the new FTSO data provider.
     */
    function updateFTSOProvider(address _newProvider) external onlyOwner {
        require(_newProvider != address(0), "FTSO provider address cannot be zero");
        ftsoProvider = _newProvider;
        emit FTSOProviderUpdated(_newProvider);
    }

    /**
     * @dev Retrieves the latest price data from the FTSO provider.
     * @param _asset Symbol or identifier of the asset whose price is being requested.
     * @return price The latest price for the asset.
     * @return timestamp The timestamp when the price was last updated.
     */
    function getLatestPrice(string memory _asset) external view returns (uint256 price, uint256 timestamp) {
        // Interface definition for the FTSO provider contract
        IFTSOProvider provider = IFTSOProvider(ftsoProvider);

        // Try to fetch the latest price and timestamp for the specified asset
        (price, timestamp) = provider.getCurrentPrice(_asset);

        // Sanity check: Ensure a valid price was returned
        require(price > 0, "Invalid price received from FTSO provider");
        require(timestamp > 0, "Invalid timestamp received from FTSO provider");
    }
}

/**
 * @dev Interface for the Flare Time Series Oracle (FTSO) Provider Contract.
 * This defines the functions that must be implemented by the FTSO provider contract.
 */
interface IFTSOProvider {
    function getCurrentPrice(string memory _asset) external view returns (uint256 price, uint256 timestamp);
}
```
