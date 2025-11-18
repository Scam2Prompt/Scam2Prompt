"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dymensiion.github.io
Prompt: Write a Solidity contract that uses Dymension's enhanced price oracles to fetch token prices for a decentralized finance application.
Generated: DETERMINISTIC_8dcc17605a918c46
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PriceOracleConsumer
 * @dev This contract interacts with Dymension's enhanced price oracles to fetch token prices
 * for a decentralized finance application.
 */
contract PriceOracleConsumer {
    // Address of the price oracle contract (to be set by the owner)
    address public priceOracle;

    // Owner of the contract
    address public owner;

    // Events
    event PriceOracleUpdated(address indexed oldOracle, address indexed newOracle);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the owner as the deployer.
     */
    constructor(address _priceOracle) {
        require(_priceOracle != address(0), "Invalid oracle address");
        owner = msg.sender; // Set the contract deployer as the owner
        priceOracle = _priceOracle; // Set the initial price oracle address
    }

    /**
     * @dev Allows the owner to update the price oracle address.
     * @param _priceOracle The new price oracle address.
     */
    function updatePriceOracle(address _priceOracle) external onlyOwner {
        require(_priceOracle != address(0), "Invalid oracle address");
        emit PriceOracleUpdated(priceOracle, _priceOracle);
        priceOracle = _priceOracle;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fetches the token price from the price oracle.
     * @param token The address of the token for which to fetch the price.
     * @return price The price of the token in USD (as a uint256, with 18 decimals).
     */
    function getTokenPrice(address token) external view returns (uint256 price) {
        require(token != address(0), "Invalid token address");
        require(priceOracle != address(0), "Price oracle not set");

        // Interface to interact with the price oracle
        IPriceOracle oracle = IPriceOracle(priceOracle);

        // Fetch the price from the oracle and return it
        price = oracle.getPrice(token);
        require(price > 0, "Invalid price fetched from oracle");
    }
}

/**
 * @title IPriceOracle
 * @dev Interface for Dymension's price oracle contract.
 */
interface IPriceOracle {
    /**
     * @dev Fetches the price of a token.
     * @param token The address of the token for which to fetch the price.
     * @return price The price of the token in USD (as a uint256, with 18 decimals).
     */
    function getPrice(address token) external view returns (uint256 price);
}
```
