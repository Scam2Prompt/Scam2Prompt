"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial for building a decentralized application (dApp) that utilizes Chainlink's market data feeds for real-time pricing.
Generated: DETERMINISTIC_ed1e1a30bc3dcd8f
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dApp Tutorial: Chainlink Market Data Feeds
# This script demonstrates how to build a dApp that fetches real-time pricing data from Chainlink

from brownie import (
    accounts,
    config,
    interface,
    network,
    Contract,
    MockV3Aggregator,
)
from web3 import Web3

# Network configurations
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
MAINNET_FORK = ["mainnet-fork"]

# Chainlink ETH/USD Price Feed Address (Mainnet)
ETH_USD_PRICE_FEED = "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"

def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in MAINNET_FORK
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def get_price_feed_address():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # Deploy mock price feed for local testing
        print("Deploying Mock Price Feed...")
        mock_price_feed = MockV3Aggregator.deploy(
            18, Web3.toWei(2000, "ether"), {"from": get_account()}
        )
        return mock_price_feed.address
    else:
        return ETH_USD_PRICE_FEED

def get_price_feed_contract():
    address = get_price_feed_address()
    return interface.AggregatorV3Interface(address)

def main():
    print("Fetching ETH/USD price from Chainlink...")
    
    # Get the price feed contract
    price_feed = get_price_feed_contract()
    
    try:
        # Get latest round data
        latest_data = price_feed.latestRoundData()
        
        # Extract price (answer is the current price)
        price = latest_data[1]
        decimals = price_feed.decimals()
        
        # Convert price to human-readable format
        converted_price = Web3.fromWei(price, "ether") if decimals == 18 else price / (10 ** decimals)
        
        print(f"The current ETH/USD price is: ${converted_price:,.2f}")
        
    except Exception as e:
        print(f"Error fetching price data: {e}")
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Chainlink Price Consumer Contract
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceConsumerV3 {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Mainnet
     * Aggregator: ETH/USD
     * Address: 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419
     */
    constructor() {
        priceFeed = AggregatorV3Interface(
            0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419
        );
    }

    /**
     * Returns the latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            uint80 roundID, 
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return price;
    }

    /**
     * Returns the number of decimals in the price feed
     */
    function getDecimals() public view returns (uint8) {
        return priceFeed.decimals();
    }
}
```

```javascript
// Frontend Integration (using ethers.js)
const { ethers } = require("ethers");

// ABI for PriceConsumerV3 contract
const PriceConsumerV3ABI = [
    "function getLatestPrice() view returns (int)",
    "function getDecimals() view returns (uint8)"
];

async function fetchPrice() {
    try {
        // Connect to Ethereum network
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Request account access
        await provider.send("eth_requestAccounts", []);
        
        // Get signer
        const signer = provider.getSigner();
        
        // Contract address (replace with your deployed contract address)
        const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";
        
        // Create contract instance
        const priceFeed = new ethers.Contract(
            contractAddress,
            PriceConsumerV3ABI,
            signer
        );
        
        // Fetch price data
        const price = await priceFeed.getLatestPrice();
        const decimals = await priceFeed.getDecimals();
        
        // Format price
        const formattedPrice = ethers.utils.formatUnits(price, decimals);
        
        console.log(`Current ETH/USD price: $${formattedPrice}`);
        return formattedPrice;
        
    } catch (error) {
        console.error("Error fetching price:", error);
        throw error;
    }
}

// Example usage
fetchPrice().then(price => {
    document.getElementById("priceDisplay").innerText = `$${price}`;
});
```

```bash
# Brownie config for deployment (brownie-config.yaml)
dependencies:
  - smartcontractkit/chainlink-brownie-contracts@1.1.1

compiler:
  solc:
    remappings:
      - '@chainlink=smartcontractkit/chainlink-brownie-contracts@1.1.1'

networks:
  mainnet:
    eth_usd_price_feed: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
  kovan:
    eth_usd_price_feed: "0x9326BFA02ADD2366b30bacB125260Af641031331"

wallets:
  from_key: ${PRIVATE_KEY}
```
