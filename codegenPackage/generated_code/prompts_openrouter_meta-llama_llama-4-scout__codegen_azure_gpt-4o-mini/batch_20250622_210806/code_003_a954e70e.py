"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Design a smart contract on Ethereum that utilizes Pyth Network's price feeds to update a decentralized perpetuals platform.
Generated: DETERMINISTIC_a954e70e607f7fe9
Batch ID: 20250622_210806
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Pyth Network price feeds
interface IPyth {
    function getPrice(string memory symbol) external view returns (int256 price, uint256 timestamp);
}

// Smart contract for a decentralized perpetuals platform
contract PerpetualsPlatform is Ownable {
    using SafeMath for uint256;

    // State variables
    IPyth public pyth; // Pyth Network price feed contract
    mapping(string => uint256) public prices; // Mapping to store prices for different assets

    // Event to emit when a price is updated
    event PriceUpdated(string indexed symbol, uint256 price, uint256 timestamp);

    // Constructor to initialize the Pyth price feed contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price of an asset
    function updatePrice(string memory symbol) external onlyOwner {
        // Fetch the price from Pyth Network
        (int256 price, uint256 timestamp) = pyth.getPrice(symbol);
        
        // Ensure the price is valid
        require(price > 0, "Invalid price received");

        // Update the price mapping
        prices[symbol] = uint256(price);

        // Emit the price updated event
        emit PriceUpdated(symbol, uint256(price), timestamp);
    }

    // Function to get the current price of an asset
    function getPrice(string memory symbol) external view returns (uint256) {
        uint256 price = prices[symbol];
        require(price > 0, "Price not available for this symbol");
        return price;
    }

    // Function to withdraw any Ether sent to the contract (if applicable)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
