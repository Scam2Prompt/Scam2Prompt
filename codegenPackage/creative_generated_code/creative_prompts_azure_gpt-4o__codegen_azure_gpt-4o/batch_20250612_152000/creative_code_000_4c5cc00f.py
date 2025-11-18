"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed oracle to fetch the BTC/USD price using the `IPyth` interface and `getPrice` method.
Generated: DETERMINISTIC_4c5cc00f900d8200
Batch ID: 20250612_152000
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

// Import the IPyth interface from the Pyth Network
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract BTCPriceFetcher {
    // State variable to store the address of the Pyth Network contract
    IPyth public pythOracle;

    // Address of the BTC/USD price feed on the Pyth Network
    bytes32 public btcUsdPriceFeedId;

    // Event to emit the fetched BTC/USD price
    event BTCPriceUpdated(int64 price, uint64 publishTime);

    // Constructor to initialize the Pyth oracle contract and BTC/USD price feed ID
    constructor(address _pythOracle, bytes32 _btcUsdPriceFeedId) {
        require(_pythOracle != address(0), "Invalid Pyth oracle address");
        require(_btcUsdPriceFeedId != bytes32(0), "Invalid BTC/USD price feed ID");
        pythOracle = IPyth(_pythOracle);
        btcUsdPriceFeedId = _btcUsdPriceFeedId;
    }

    /**
     * @dev Fetches the latest BTC/USD price from the Pyth Network oracle.
     * Emits the BTCPriceUpdated event with the fetched price and publication time.
     */
    function fetchBTCPrice() external {
        // Fetch the price information from the Pyth oracle
        IPyth.Price memory priceData = pythOracle.getPrice(btcUsdPriceFeedId);

        // Ensure the price is not stale
        require(priceData.price > 0, "Price data is stale or unavailable");

        // Emit the event with the fetched price and publication time
        emit BTCPriceUpdated(priceData.price, priceData.publishTime);
    }

    /**
     * @dev Allows updating the BTC/USD price feed ID.
     * @param _newBtcUsdPriceFeedId The new BTC/USD price feed ID.
     */
    function updatePriceFeedId(bytes32 _newBtcUsdPriceFeedId) external {
        require(_newBtcUsdPriceFeedId != bytes32(0), "Invalid BTC/USD price feed ID");
        btcUsdPriceFeedId = _newBtcUsdPriceFeedId;
    }
}
```

### Notes:
- Replace `@pythnetwork/pyth-sdk-solidity/IPyth.sol` with the actual path or package installation of the Pyth SDK.
- Ensure the `BTC/USD` price feed ID is correctly provided during contract deployment, as it is a critical parameter for fetching prices.
- Use this contract responsibly in production environments, as price feeds may be subject to latency or availability issues.
