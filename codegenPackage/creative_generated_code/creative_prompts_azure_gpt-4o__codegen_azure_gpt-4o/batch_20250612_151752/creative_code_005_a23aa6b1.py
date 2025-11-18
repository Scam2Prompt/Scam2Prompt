"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yethereum.com
Prompt: Develop a Solidity contract to interact with a decentralized price oracle for cross-chain assets, addressing vulnerabilities outlined on yethereum.com.
Generated: DETERMINISTIC_a23aa6b113e48783
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title CrossChainPriceOracle
 * @dev A Solidity contract to interact with a decentralized price oracle
 *      for cross-chain assets, with proper security measures implemented.
 */
contract CrossChainPriceOracle {
    // State variable to store the address of the price oracle
    address public priceOracle;

    // State variable to store supported asset pairs
    mapping(string => bool) public supportedAssets;

    // Event emitted when a price is successfully fetched
    event PriceFetched(string asset, uint256 price);

    // Event emitted when the oracle address is updated
    event OracleUpdated(address newOracle);

    /**
     * @dev Constructor to initialize the contract with the price oracle address.
     * @param _priceOracle The address of the decentralized price oracle.
     */
    constructor(address _priceOracle) {
        require(_priceOracle != address(0), "Invalid oracle address");
        priceOracle = _priceOracle;
    }

    /**
     * @dev Modifier to ensure the caller is the oracle contract.
     */
    modifier onlyOracle() {
        require(msg.sender == priceOracle, "Caller is not the oracle");
        _;
    }

    /**
     * @dev Function to update the oracle address.
     * @param _newOracle The new address of the decentralized price oracle.
     */
    function updateOracle(address _newOracle) external onlyOracle {
        require(_newOracle != address(0), "Invalid oracle address");
        priceOracle = _newOracle;
        emit OracleUpdated(_newOracle);
    }

    /**
     * @dev Function to add support for a new asset pair.
     * @param assetPair The asset pair identifier (e.g., "ETH/USD").
     */
    function addSupportedAsset(string memory assetPair) external onlyOracle {
        require(bytes(assetPair).length > 0, "Invalid asset pair");
        supportedAssets[assetPair] = true;
    }

    /**
     * @dev Function to fetch the price of a supported asset from the oracle.
     *      Implements security measures to prevent reentrancy.
     * @param assetPair The asset pair identifier (e.g., "ETH/USD").
     * @return The price of the asset in the specified pair.
     */
    function getPrice(string memory assetPair) external view returns (uint256) {
        require(supportedAssets[assetPair], "Asset pair not supported");

        // Interact with the oracle contract to fetch the price
        (bool success, bytes memory data) = priceOracle.staticcall(
            abi.encodeWithSignature("getLatestPrice(string)", assetPair)
        );

        // Handle errors gracefully
        require(success, "Failed to fetch price from oracle");

        // Decode the price value from the received data
        uint256 price = abi.decode(data, (uint256));

        // Emit event for successful price fetch
        emit PriceFetched(assetPair, price);

        return price;
    }
}
```
