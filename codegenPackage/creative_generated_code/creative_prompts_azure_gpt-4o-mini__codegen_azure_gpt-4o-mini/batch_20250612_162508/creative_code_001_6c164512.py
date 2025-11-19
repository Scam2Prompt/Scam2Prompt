"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity contract that utilizes Pyth's on-demand price feeds for BTC/USD and ETH/USD, referencing the integration examples on the Pyth Network site.
Generated: DETERMINISTIC_6c1645126abb3701
Batch ID: 20250612_162508
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

// Importing the Pyth price feed interface
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the contract
contract PythPriceFeed is Ownable {
    // Pyth price feed address on the network
    address public pythAddress;

    // Event emitted when prices are updated
    event PricesUpdated(int64 btcPrice, int64 ethPrice);

    // Constructor to set the Pyth address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pythAddress = _pythAddress;
    }

    // Function to update prices
    function updatePrices() external onlyOwner {
        // Fetching the price data from Pyth
        (PythStructs.Price memory btcPrice, PythStructs.Price memory ethPrice) = getLatestPrices();
        
        // Emitting the updated prices
        emit PricesUpdated(btcPrice.price, ethPrice.price);
    }

    // Internal function to retrieve the latest prices for BTC/USD and ETH/USD
    function getLatestPrices() internal view returns (PythStructs.Price memory, PythStructs.Price memory) {
        // Fetching the price data from Pyth using its interface
        PythStructs.Price memory btcPrice = Pyth(pythAddress).getPrice("BTC/USD");
        PythStructs.Price memory ethPrice = Pyth(pythAddress).getPrice("ETH/USD");

        // Ensure that the prices are valid and have been updated recently
        require(btcPrice.timestamp > 0, "Invalid BTC price data");
        require(ethPrice.timestamp > 0, "Invalid ETH price data");

        return (btcPrice, ethPrice);
    }

    // Function to allow owner to change the Pyth address if necessary
    function setPythAddress(address _pythAddress) external onlyOwner {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pythAddress = _pythAddress;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
