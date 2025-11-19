"""
Generated Code Metadata:
========================
Original URL: https://pythgame.com
Prompt: Create a tutorial for setting up Pyth Network's price feed oracles in a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_71710b4e21e78d6e
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pyth Network Price Feed Oracle Integration Tutorial
# This script demonstrates how to integrate Pyth Network's price feed oracles into a DeFi application.

from web3 import Web3
from pythclient.pythclient import PythClient
from pythclient.utils import get_key_from_env
import os
import json
from typing import Dict, Optional

# Configuration class for Pyth Network
class PythConfig:
    """
    Configuration for Pyth Network connection.
    """
    def __init__(self):
        # Mainnet endpoint (replace with testnet if needed)
        self.cluster = "mainnet"
        # Pyth program public key
        self.program_key = "FsJ3A3u2vn5cTVofAjvy6y5kwABJAqYWpe4975bi2epH"
        # Web3 provider URL (e.g., Infura, Alchemy)
        self.web3_provider_url = os.getenv("WEB3_PROVIDER_URL")
        # Private key for transactions (keep secure!)
        self.private_key = os.getenv("PRIVATE_KEY")
        # Wallet address
        self.wallet_address = os.getenv("WALLET_ADDRESS")

# Price Feed Oracle Service
class PythPriceFeed:
    """
    Service to interact with Pyth Network price feeds.
    """
    
    def __init__(self, config: PythConfig):
        self.config = config
        self.web3 = Web3(Web3.HTTPProvider(config.web3_provider_url))
        self.pyth_client = PythClient(
            cluster=config.cluster,
            program_key=config.program_key
        )
        
        # Verify connection
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to Web3 provider")
        
    async def get_price(self, price_feed_id: str) -> Dict:
        """
        Get the current price from a Pyth price feed.
        
        Args:
            price_feed_id: The Pyth price feed ID (e.g., "Crypto.BTC/USD")
            
        Returns:
            Dictionary containing price information
        """
        try:
            price_feed = await self.pyth_client.get_price_feed(price_feed_id)
            return {
                "price": price_feed.get_current_price(),
                "confidence": price_feed.get_current_confidence(),
                "timestamp": price_feed.get_current_publish_time(),
                "exponent": price_feed.get_exponent()
            }
        except Exception as e:
            raise Exception(f"Failed to get price feed: {str(e)}")
    
    async def update_price_feeds(self, price_feed_ids: list) -> Dict[str, Dict]:
        """
        Get multiple price feeds at once.
        
        Args:
            price_feed_ids: List of price feed IDs
            
        Returns:
            Dictionary mapping feed IDs to their price data
        """
        try:
            results = {}
            for feed_id in price_feed_ids:
                results[feed_id] = await self.get_price(feed_id)
            return results
        except Exception as e:
            raise Exception(f"Failed to update price feeds: {str(e)}")

# Example Usage
async def main():
    try:
        # Initialize configuration
        config = PythConfig()
        
        # Initialize price feed service
        price_feed_service = PythPriceFeed(config)
        
        # Example: Get BTC/USD price
        btc_price = await price_feed_service.get_price("Crypto.BTC/USD")
        print(f"BTC/USD Price: {btc_price}")
        
        # Example: Get multiple prices
        prices = await price_feed_service.update_price_feeds([
            "Crypto.ETH/USD",
            "Crypto.SOL/USD"
        ])
        print("Multiple Prices:", prices)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for Pyth Price Feed
interface IPyth {
    struct Price {
        // Price
        int64 price;
        // Confidence interval around the price
        uint64 conf;
        // Price exponent
        int32 expo;
        // Unix timestamp describing when the price was published
        uint publishTime;
    }

    // Returns the price of a price feed without any sanity checks.
    function getPrice(bytes32 id) external view returns (Price memory price);

    // Returns the exponentially-weighted moving average price of a price feed without any sanity checks.
    function getEmaPrice(bytes32 id) external view returns (Price memory price);
}

// Example DeFi contract using Pyth Price Feeds
contract PythDeFiExample {
    IPyth public pyth;
    address public owner;
    
    // Price feed IDs (these are example IDs - replace with actual ones)
    bytes32 public constant BTC_USD = 0xf9c0172ba10dfa4d19088d94f5bf61d3b54d5bd7483a322a982e1373ee8ea31b;
    bytes32 public constant ETH_USD = 0xca80ba6dc32e08d06f1aa886011eed1d77c77be9eb761cc10d72b7d0a2fd57a6;
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    constructor(address _pythContract) {
        pyth = IPyth(_pythContract);
        owner = msg.sender;
    }
    
    // Get the latest BTC/USD price
    function getBtcPrice() public view returns (IPyth.Price memory) {
        return pyth.getPrice(BTC_USD);
    }
    
    // Get the latest ETH/USD price
    function getEthPrice() public view returns (IPyth.Price memory) {
        return pyth.getPrice(ETH_USD);
    }
    
    // Example function that uses price feeds
    function executeTrade(uint256 amount, bool isBuy) public view returns (uint256) {
        IPyth.Price memory price = pyth.getPrice(ETH_USD);
        require(price.price > 0, "Invalid price");
        
        // Convert price to 18 decimals (standard in DeFi)
        uint256 normalizedPrice = uint256(uint64(price.price)) * (10 ** (18 + uint256(int256(price.expo))));
        
        if (isBuy) {
            return amount * normalizedPrice / 1e18;
        } else {
            return amount * 1e18 / normalizedPrice;
        }
    }
    
    // Update Pyth contract address (in case of upgrades)
    function updatePythContract(address newPyth) public onlyOwner {
        require(newPyth != address(0), "Invalid address");
        pyth = IPyth(newPyth);
    }
}
```

```javascript
// Frontend integration example using ethers.js and pyth.js

const { ethers } = require('ethers');
const { PythConnection } = require('@pythnetwork/pyth-js');

// Configuration
const config = {
  pythContractAddress: '0x4305FB66699C3B2702D4d05CF36551390A4c69C6', // Mainnet Pyth contract
  web3ProviderUrl: process.env.WEB3_PROVIDER_URL,
  privateKey: process.env.PRIVATE_KEY,
};

// Initialize provider and signer
const provider = new ethers.providers.JsonRpcProvider(config.web3ProviderUrl);
const signer = new ethers.Wallet(config.privateKey, provider);

// Initialize Pyth client
const pythConnection = new PythConnection({
  pythContractAddress: config.pythContractAddress,
  provider: provider,
});

// Example function to get price
async function getPrice(priceFeedId) {
  try {
    const price = await pythConnection.getPrice(priceFeedId);
    return {
      price: price.price,
      confidence: price.conf,
      exponent: price.expo,
      timestamp: price.publishTime,
    };
  } catch (error) {
    console.error('Error fetching price:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Initialize connection
    await pythConnection.connect();
    
    // Example price feed IDs
    const BTC_USD = '0xf9c0172ba10dfa4d19088d94f5bf61d3b54d5bd7483a322a982e1373ee8ea31b';
    const ETH_USD = '0xca80ba6dc32e08d06f1aa886011eed1d77c77be9eb761cc10d72b7d0a2fd57a6';
    
    // Get prices
    const btcPrice = await getPrice(BTC_USD);
    const ethPrice = await getPrice(ETH_USD);
    
    console.log('BTC/USD Price:', btcPrice);
    console.log('ETH/USD Price:', ethPrice);
    
  } catch (error) {
    console.error('Error:', error);
  }
