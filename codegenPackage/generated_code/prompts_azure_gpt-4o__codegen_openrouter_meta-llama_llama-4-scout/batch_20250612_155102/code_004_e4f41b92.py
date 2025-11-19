"""
Generated Code Metadata:
========================
Original URL: https://pythui.com
Prompt: Create a smart contract in Solidity that interacts with Pyth Network's price feed oracles to fetch and validate stock price data.
Generated: DETERMINISTIC_e4f41b92635216dd
Batch ID: 20250612_155102
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

/**
 * @title StockPriceOracle
 * @author [Your Name]
 * @notice A smart contract that interacts with Pyth Network's price feed oracles to fetch and validate stock price data.
 */
contract StockPriceOracle {
    using SafeMath for uint256;

    // Pyth Network's Pyth contract address
    address public immutable pythAddress;

    // Mapping of stock symbols to their corresponding Pyth price feed IDs
    mapping(string => bytes32) public stockSymbolsToFeedIds;

    // Mapping of Pyth price feed IDs to their corresponding stock symbols
    mapping(bytes32 => string) public feedIdsToStockSymbols;

    /**
     * @param _pythAddress Pyth Network's Pyth contract address
     */
    constructor(address _pythAddress) {
        pythAddress = _pythAddress;
    }

    /**
     * @dev Adds a stock symbol and its corresponding Pyth price feed ID to the mappings
     * @param _symbol Stock symbol (e.g. "AAPL")
     * @param _feedId Pyth price feed ID (e.g. "0x...")
     */
    function addStockSymbol(string memory _symbol, bytes32 _feedId) public {
        require(bytes(stockSymbolsToFeedIds[_symbol]).length == 0, "Stock symbol already exists");
        require(bytes(feedIdsToStockSymbols[_feedId]).length == 0, "Pyth price feed ID already exists");

        stockSymbolsToFeedIds[_symbol] = _feedId;
        feedIdsToStockSymbols[_feedId] = _symbol;
    }

    /**
     * @dev Fetches the current stock price from Pyth Network's oracle
     * @param _symbol Stock symbol (e.g. "AAPL")
     * @return The current stock price in USD (as a 18 decimal uint256)
     */
    function getStockPrice(string memory _symbol) public view returns (uint256) {
        bytes32 feedId = stockSymbolsToFeedIds[_symbol];
        require(feedId != bytes32(0), "Stock symbol not found");

        IPyth pyth = IPyth(pythAddress);
        (, int64 price, , uint64 updatedAt, ) = pyth.getPrice(feedId);

        require(price > 0, "Invalid price");
        require(updatedAt > 0, "Price not updated");

        // Convert price to 18 decimal uint256
        return uint256(price).mul(10**18).div(10**8);
    }

    /**
     * @dev Validates a stock price against Pyth Network's oracle
     * @param _symbol Stock symbol (e.g. "AAPL")
     * @param _price Expected stock price in USD (as a 18 decimal uint256)
     * @return True if the price is valid, false otherwise
     */
    function isValidStockPrice(string memory _symbol, uint256 _price) public view returns (bool) {
        uint256 currentPrice = getStockPrice(_symbol);
        return _price == currentPrice;
    }
}
```
