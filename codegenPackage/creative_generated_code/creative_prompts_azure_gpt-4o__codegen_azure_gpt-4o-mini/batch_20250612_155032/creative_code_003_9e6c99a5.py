"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Provide an example of a smart contract or script for facilitating cryptocurrency exchanges (e.g., Bitcoin to PLN) using the Ari10 crypto terminal.
Generated: DETERMINISTIC_9e6c99a52e4e57b4
Batch ID: 20250612_155032
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

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for facilitating cryptocurrency exchanges
contract CryptoExchange is Ownable {
    using SafeMath for uint256;

    // Event for logging successful exchanges
    event ExchangeExecuted(address indexed user, string fromCurrency, string toCurrency, uint256 amountIn, uint256 amountOut);

    // Mapping to hold exchange rates
    mapping(string => mapping(string => uint256)) public exchangeRates;

    // Constructor to initialize exchange rates
    constructor() {
        // Setting initial exchange rates for demonstration (1 BTC = 200,000 PLN)
        exchangeRates["BTC"]["PLN"] = 200000; // Example rate
        // Add more currency pairs as needed
    }

    // Function to set exchange rates (only owner can set)
    function setExchangeRate(string memory fromCurrency, string memory toCurrency, uint256 rate) public onlyOwner {
        require(rate > 0, "Exchange rate must be greater than zero");
        exchangeRates[fromCurrency][toCurrency] = rate;
    }

    // Function to execute an exchange
    function exchange(string memory fromCurrency, string memory toCurrency, uint256 amountIn) public returns (uint256 amountOut) {
        // Validate that exchange rate exists
        require(exchangeRates[fromCurrency][toCurrency] > 0, "Exchange rate not available");

        // Calculate the output amount
        amountOut = amountIn.mul(exchangeRates[fromCurrency][toCurrency]).div(1 ether); // Assuming input amount is in wei

        // Emit an event for the exchange executed
        emit ExchangeExecuted(msg.sender, fromCurrency, toCurrency, amountIn, amountOut);
    }

    // Function to get the current exchange rate
    function getExchangeRate(string memory fromCurrency, string memory toCurrency) public view returns (uint256) {
        return exchangeRates[fromCurrency][toCurrency];
    }
}
```

### Notes:
- This code is a simple Ethereum smart contract written in Solidity that facilitates cryptocurrency exchanges.
- The contract includes functionality to set and get exchange rates, as well as to execute exchanges.
- It employs OpenZeppelin's `Ownable` for access control and `SafeMath` for safe arithmetic operations.
- Proper error handling is implemented with require statements to ensure the correctness of operations.
