"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: Generate a Solidity smart contract snippet that uses Pyth's market data feed to retrieve and store cryptocurrency prices.
Generated: DETERMINISTIC_c880b0fc70ff1018
Batch ID: 20250612_155024
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

// Import the Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract CryptoPriceFeed {
    // Address of the deployed Pyth contract on the target network
    IPyth public pythContract;

    // Mapping to store cryptocurrency prices by their symbol (e.g., BTC/USD)
    mapping(string => int256) public cryptoPrices;

    // Event emitted when a price is updated
    event PriceUpdated(string symbol, int256 price);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContract = IPyth(_pythContractAddress);
    }

    /**
     * @dev Fetch the price for a given symbol from Pyth and store it in the contract.
     * @param priceId The price ID corresponding to the symbol (provided by Pyth).
     * @param symbol The symbol of the cryptocurrency (e.g., BTC/USD).
     * @param updateData The updateData required by Pyth for fetching the latest prices.
     *
     * Note: Ensure that proper gas estimation is performed before calling this function.
     */
    function updatePrice(bytes32 priceId, string memory symbol, bytes memory updateData) external payable {
        // Update the Pyth price feeds (requires payment for the update)
        pythContract.updatePriceFeeds{value: msg.value}(updateData);

        // Fetch the price from the Pyth contract
        (int256 price, ) = pythContract.getPriceUnsafe(priceId);

        // Save the price in the mapping
        cryptoPrices[symbol] = price;

        // Emit an event for the update
        emit PriceUpdated(symbol, price);
    }

    /**
     * @dev Retrieve the price of a given cryptocurrency.
     * @param symbol The symbol of the cryptocurrency (e.g., BTC/USD).
     * @return The latest price of the cryptocurrency.
     */
    function getPrice(string memory symbol) external view returns (int256) {
        return cryptoPrices[symbol];
    }

    /**
     * @dev Fallback function to allow receiving ethers for price updates.
     */
    receive() external payable {}

    /**
     * @dev Withdraw function to recover any unspent ethers in the contract.
     * @param to Address to send the withdrawn ethers.
     */
    function withdraw(address payable to) external {
        require(to != address(0), "Invalid address");
        to.transfer(address(this).balance);
    }
}
```

### Notes:
1. Ensure the `@pythnetwork/pyth-sdk-solidity` package is installed and the correct `priceId` values are used (refer to Pyth documentation for network-specific details).
2. This contract assumes the caller will provide sufficient ETH for `updatePriceFeeds`.
