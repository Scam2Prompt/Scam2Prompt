"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Can you demonstrate how to use Pyth's API to access historical market data for equities and cryptocurrencies in a smart contract?
Generated: DETERMINISTIC_6627ff58fa52a993
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a sample code demonstrating how to use Pyth's API to access historical market data for equities and cryptocurrencies in a smart contract. The example assumes you are using Solidity for an Ethereum-based smart contract.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Pyth Historical Market Data Smart Contract
 * @dev This contract interacts with the Pyth Network to fetch historical market data
 *      for equities and cryptocurrencies. Ensure you deploy this on a network compatible
 *      with Pyth's data feed.
 */

// Import Pyth interface to interact with their data feed
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 publishTime);
    function getHistoricalPrice(bytes32 priceId, uint64 timestamp) external view returns (int64 price);
}

contract PythMarketData {
    // Address of the deployed Pyth contract (update with the actual address on your network)
    address public pythContractAddress;

    // Pyth price ID for the equity or cryptocurrency (update with actual IDs)
    bytes32 public equityPriceId;
    bytes32 public cryptoPriceId;

    // Constructor to initialize Pyth contract address and price IDs
    constructor(address _pythContractAddress, bytes32 _equityPriceId, bytes32 _cryptoPriceId) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        require(_equityPriceId != bytes32(0), "Invalid equity price ID");
        require(_cryptoPriceId != bytes32(0), "Invalid crypto price ID");

        pythContractAddress = _pythContractAddress;
        equityPriceId = _equityPriceId;
        cryptoPriceId = _cryptoPriceId;
    }

    /**
     * @dev Fetch the latest price of the equity
     * @return price The latest price of the equity
     * @return publishTime The timestamp when the price was published
     */
    function getLatestEquityPrice() external view returns (int64 price, uint64 publishTime) {
        IPyth pyth = IPyth(pythContractAddress);
        (price, publishTime) = pyth.getPrice(equityPriceId);
        return (price, publishTime);
    }

    /**
     * @dev Fetch the latest price of the cryptocurrency
     * @return price The latest price of the cryptocurrency
     * @return publishTime The timestamp when the price was published
     */
    function getLatestCryptoPrice() external view returns (int64 price, uint64 publishTime) {
        IPyth pyth = IPyth(pythContractAddress);
        (price, publishTime) = pyth.getPrice(cryptoPriceId);
        return (price, publishTime);
    }

    /**
     * @dev Fetch historical price of the equity at a specific timestamp
     * @param timestamp The timestamp of the historical data
     * @return price The price of the equity at the given timestamp
     */
    function getHistoricalEquityPrice(uint64 timestamp) external view returns (int64 price) {
        IPyth pyth = IPyth(pythContractAddress);
        price = pyth.getHistoricalPrice(equityPriceId, timestamp);
        return price;
    }

    /**
     * @dev Fetch historical price of the cryptocurrency at a specific timestamp
     * @param timestamp The timestamp of the historical data
     * @return price The price of the cryptocurrency at the given timestamp
     */
    function getHistoricalCryptoPrice(uint64 timestamp) external view returns (int64 price) {
        IPyth pyth = IPyth(pythContractAddress);
        price = pyth.getHistoricalPrice(cryptoPriceId, timestamp);
        return price;
    }
}
```

### Notes:
1. Replace `pythContractAddress`, `equityPriceId`, and `cryptoPriceId` with actual values obtained from Pyth Network.
2. Ensure you deploy this contract on a blockchain network supported by Pyth.
3. This code assumes that Pyth's API provides the `getPrice` and `getHistoricalPrice` methods; verify their actual API as needed.
