"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: Write a smart contract in Solidity that connects to Pythget oracles to fetch live market data for token swaps.
Generated: DETERMINISTIC_781a4814444e8131
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
pragma solidity ^0.8.0;

// Import the Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract TokenSwapOracle {
    // Address of the Pyth oracle contract
    IPyth public pythOracle;

    // Event emitted when a swap occurs
    event TokenSwap(
        address indexed user,
        uint256 inputAmount,
        uint256 outputAmount,
        string baseToken,
        string quoteToken
    );

    // Constructor to set the Pyth oracle address
    constructor(address _pythOracleAddress) {
        require(_pythOracleAddress != address(0), "Invalid oracle address");
        pythOracle = IPyth(_pythOracleAddress);
    }

    /**
     * @dev Fetches price data from the Pyth oracle
     * @param priceId The unique identifier of the requested price (base-quote pair)
     * @return int64 Price value scaled by 10^exponent
     * @return int32 Exponent that defines the price's decimal precision
     */
    function getPrice(bytes32 priceId)
        public
        view
        returns (int64, int32)
    {
        // Fetch price with the latest update
        IPyth.Price memory priceData = pythOracle.getPriceUnsafe(priceId);

        // Ensure the price status is valid
        require(priceData.priceStatus == IPyth.PriceStatus.TRADING, "Price data is not valid or trading");
        
        return (priceData.price, priceData.expo);
    }

    /**
     * @dev Calculates the output amount for a token swap based on the fetched price
     * @param inputAmount The amount of the base token being swapped
     * @param priceId The unique identifier for the base-quote price pair
     * @return uint256 The output amount of the quote token
     */
    function calculateOutput(uint256 inputAmount, bytes32 priceId) public view returns (uint256) {
        (int64 price, int32 expo) = getPrice(priceId);

        // Ensure price is positive for the calculation
        require(price > 0, "Invalid price data");

        // Adjust price using the exponent for precision
        uint256 adjustedPrice = uint256(price) * (10 ** uint32(-expo));

        // Calculate and return the output amount
        return (inputAmount * adjustedPrice) / (10 ** 18); // Assuming 18 decimals for input and output tokens
    }

    /**
     * @dev Performs a token swap by calculating output and emitting an event (mock implementation)
     * @param inputAmount The amount of base token provided for the swap
     * @param priceId The unique identifier for the base-quote price pair
     * @param baseToken The symbol of the input (base) token
     * @param quoteToken The symbol of the output (quote) token
     */
    function swapTokens(
        uint256 inputAmount,
        bytes32 priceId,
        string memory baseToken,
        string memory quoteToken
    ) public {
        require(inputAmount > 0, "Input amount must be greater than zero");

        uint256 outputAmount = calculateOutput(inputAmount, priceId);

        // Emit an event for the swap
        emit TokenSwap(msg.sender, inputAmount, outputAmount, baseToken, quoteToken);

        // Note: In a real implementation, token transfer logic would be added here
    }
}
```

### Notes:
1. Replace `@pythnetwork/pyth-sdk-solidity/IPyth.sol` with the actual path to your imported Pyth SDK.
2. This contract assumes you already have access to token transfer mechanisms for swaps in your production environment.
3. Always use a testnet environment before deploying this to mainnet and validate the oracle integration extensively.
