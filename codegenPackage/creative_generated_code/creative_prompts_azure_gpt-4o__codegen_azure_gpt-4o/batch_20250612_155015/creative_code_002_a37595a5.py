"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythbtc.com
Prompt: Generate a smart contract snippet that uses Pyth price feed oracles to fetch cryptocurrency price updates.
Generated: DETERMINISTIC_a37595a54fb35d02
Batch ID: 20250612_155015
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

// Import the Pyth oracle interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract CryptoPriceFeed {
    // Pyth price feed contract address (to be updated with the deployed address on target chain)
    address public immutable pythContract;

    // Event emitted when the price is updated
    event PriceUpdated(string symbol, int64 price, uint64 publishTime);

    constructor(address _pythContract) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        pythContract = _pythContract;
    }

    /**
     * @dev Fetch the latest price and publish time for a given price feed ID.
     * @param priceFeedId The ID of the price feed to query.
     */
    function fetchPrice(bytes32 priceFeedId) external {
        // Interface of the Pyth contract
        IPyth pyth = IPyth(pythContract);

        // Fetch the current price and metadata
        PythStructs.Price memory priceData = pyth.getPrice(priceFeedId);

        require(priceData.price > 0, "Invalid price data"); // Ensure price is valid
        require(priceData.publishTime > 0, "Invalid publish time"); // Ensure publish time is valid

        emit PriceUpdated(priceData.id, priceData.price, priceData.publishTime);
    }

    /**
     * @dev Helper function to convert price feed ID from a string.
     * @param symbol The symbol of the cryptocurrency (e.g., BTC/USD).
     * @return The bytes32 representation of the price feed ID.
     */
    function getPriceFeedId(string memory symbol) external pure returns (bytes32) {
        return keccak256(abi.encodePacked(symbol));
    }
}
```

**Note**: Ensure that you have access to Pyth's Solidity SDK, and replace the `pythContract` address with the actual deployed address of the Pyth oracle on your target blockchain network. Additionally, `IPyth` and `PythStructs.Price` should be defined in the imported Pyth SDK, so ensure the correct SDK version is used.
