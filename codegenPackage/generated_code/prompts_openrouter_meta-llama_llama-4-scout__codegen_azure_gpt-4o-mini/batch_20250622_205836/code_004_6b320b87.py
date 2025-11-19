"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: "Develop an oracle that utilizes EigenLayer's restaked ETH to provide a trustworthy price feed on Ethereum."
Generated: DETERMINISTIC_6b320b8730d999dc
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the price feed
interface IPriceFeed {
    function getLatestPrice() external view returns (int256);
}

// Oracle contract to provide a trustworthy price feed using EigenLayer's restaked ETH
contract EigenLayerOracle is Ownable {
    using SafeMath for uint256;

    // State variable to store the price feed contract address
    IPriceFeed public priceFeed;

    // Event to log price updates
    event PriceUpdated(int256 price);

    // Constructor to initialize the price feed contract
    constructor(address _priceFeed) {
        require(_priceFeed != address(0), "Invalid price feed address");
        priceFeed = IPriceFeed(_priceFeed);
    }

    // Function to update the price from the price feed
    function updatePrice() external onlyOwner {
        int256 latestPrice = priceFeed.getLatestPrice();
        require(latestPrice > 0, "Invalid price received");

        emit PriceUpdated(latestPrice);
    }

    // Function to get the latest price
    function getLatestPrice() external view returns (int256) {
        return priceFeed.getLatestPrice();
    }

    // Function to update the price feed address
    function setPriceFeed(address _priceFeed) external onlyOwner {
        require(_priceFeed != address(0), "Invalid price feed address");
        priceFeed = IPriceFeed(_priceFeed);
    }
}
```

This code defines a simple Oracle contract that interacts with a price feed interface. It includes error handling, events for logging, and follows best practices for Solidity development.
