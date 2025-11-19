"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a smart contract that uses Pyth's price feed IDs to fetch and display the price of ETH/USD in real-time on a frontend application.
Generated: DETERMINISTIC_dc58806d480c8521
Batch ID: 20250612_152000
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

// Import Pyth interfaces
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract ETHPriceFeed {
    IPyth public pyth;
    bytes32 public ethUsdPriceFeedId;

    event PriceUpdated(int64 price, uint64 confidence, uint64 publishTime);

    constructor(address _pythContract, bytes32 _ethUsdPriceFeedId) {
        pyth = IPyth(_pythContract);
        ethUsdPriceFeedId = _ethUsdPriceFeedId;
    }

    function updatePrice(
        bytes[] calldata priceUpdateData
    ) public payable {
        // Update the price data (and pay the required fee)
        uint fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
    }

    function getLatestPrice() public view returns (
        int64 price,
        uint64 confidence,
        uint64 publishTime
    ) {
        PythStructs.Price memory currentPrice = pyth.getPrice(ethUsdPriceFeedId);
        return (
            currentPrice.price,
            currentPrice.conf,
            currentPrice.publishTime
        );
    }

    function getPriceUnsafe() public view returns (int64) {
        PythStructs.Price memory currentPrice = pyth.getPriceUnsafe(ethUsdPriceFeedId);
        return currentPrice.price;
    }

    // Helper function to convert price to USD with decimals
    function getPriceInUSD() public view returns (uint256) {
        PythStructs.Price memory currentPrice = pyth.getPrice(ethUsdPriceFeedId);
        require(currentPrice.price >= 0, "Negative price");
        return uint256(uint64(currentPrice.price)) * (10 ** (18 - currentPrice.expo));
    }

    // Receive function to accept funds for price updates
    receive() external payable {}
}
```

```javascript
// Frontend code (React example)
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import ETHPriceFeedABI from './ETHPriceFeedABI.json';

const ETHPriceDisplay = () => {
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Contract addresses and configuration
  const contractAddress = "0x..."; // Your deployed contract address
  const pythPriceFeedId = "0x..."; // ETH/USD price feed ID from Pyth

  const fetchPrice = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, ETHPriceFeedABI, signer);
      
      // Get latest price
      const [price, confidence, publishTime] = await contract.getLatestPrice();
      
      // Convert price to readable format (adjust based on Pyth's decimals)
      const formattedPrice = ethers.utils.formatUnits(price, 8);
      setPrice(formattedPrice);
      
    } catch (err) {
      console.error("Error fetching price:", err);
      setError("Failed to fetch price");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPrice();
    
    // Refresh price every 30 seconds
    const interval = setInterval(fetchPrice, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="price-display">
      <h2>ETH/USD Price</h2>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p className="error">{error}</p>
      ) : price ? (
        <p>${price}</p>
      ) : (
        <p>No price data available</p>
      )}
      <button onClick={fetchPrice} disabled={loading}>
        Refresh Price
      </button>
    </div>
  );
};

export default ETHPriceDisplay;
```
