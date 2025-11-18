"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: How can I use Pyth's pull-based oracle model to fetch real-time price data for crypto assets in an Ethereum-based DeFi application?
Generated: DETERMINISTIC_0f10cc56c60af323
Batch ID: 20250612_153648
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

contract CryptoPriceOracle {
    // Address of the deployed Pyth contract on the Ethereum network
    IPyth public pyth;
    
    // Events
    event PriceFetched(bytes32 indexed priceId, int64 price, uint64 conf);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythContract) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        pyth = IPyth(_pythContract);
    }

    /**
     * @dev Fetches real-time price data for a given asset from the Pyth oracle
     * @param priceId The Pyth price ID for the crypto asset
     * @param updateData The payload containing the price update data (from off-chain sources)
     * @return price The latest price for the asset
     * @return conf The confidence interval for the price
     */
    function fetchPrice(bytes32 priceId, bytes[] calldata updateData) external returns (int64 price, uint64 conf) {
        // Update Pyth price data on-chain using the provided updateData
        // This is required for pull-based updates in Pyth
        try pyth.updatePriceFeeds(updateData) {
            // Fetch the latest price data
            IPyth.Price memory priceData = pyth.getPrice(priceId);

            // Extract price and confidence interval
            price = priceData.price;
            conf = priceData.conf;
            
            // Emit event with fetched price details
            emit PriceFetched(priceId, price, conf);
        } catch (bytes memory error) {
            // Handle any errors during the update process
            revert(string(abi.encodePacked("Price update failed: ", error)));
        }

        // Return the fetched price and confidence interval
        return (price, conf);
    }

    /**
     * @dev Helper function to get the age of a price feed
     * @param priceId The Pyth price ID for the asset
     * @return age The age of the price feed in seconds
     */
    function getPriceAge(bytes32 priceId) external view returns (uint64 age) {
        // Fetch the Price data from the Pyth contract
        IPyth.Price memory priceData = pyth.getPrice(priceId);

        // Calculate the age of the price feed
        age = block.timestamp - priceData.publishTime;

        return age;
    }
}
```

**Note:** Ensure that the `@pythnetwork/pyth-sdk-solidity` library is installed and available in your project. Deploy this contract with a valid Pyth contract address, and ensure off-chain update data is provided during execution to pull real-time prices successfully.
