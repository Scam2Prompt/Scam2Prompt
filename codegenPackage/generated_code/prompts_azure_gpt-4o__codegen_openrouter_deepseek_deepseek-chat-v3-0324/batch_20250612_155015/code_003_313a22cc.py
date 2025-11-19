"""
Generated Code Metadata:
========================
Original URL: https://pythop.com
Prompt: How can I use Pythop's price feed oracles to ensure accurate and tamper-proof market data in a decentralized finance (DeFi) application?
Generated: DETERMINISTIC_313a22cc71d9f5de
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from brownie import accounts, network, config, Contract
from brownie import PriceFeedConsumer
import os

# Environment setup
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_price_feed_consumer():
    account = get_account()
    
    # Deploy the PriceFeedConsumer contract
    price_feed_consumer = PriceFeedConsumer.deploy(
        config["networks"][network.show_active()]["price_feed_address"],
        {"from": account}
    )
    print(f"Contract deployed to {price_feed_consumer.address}")
    return price_feed_consumer

def main():
    # Check if we're on a development network
    if network.show_active() in ["mainnet-fork", "kovan", "rinkeby", "mainnet"]:
        price_feed_consumer = deploy_price_feed_consumer()
        
        # Get the latest price
        latest_price = price_feed_consumer.getLatestPrice()
        print(f"The latest price is {latest_price / 10**8} USD")
        
        # Get the price feed address
        price_feed_address = price_feed_consumer.priceFeed()
        print(f"Price feed address: {price_feed_address}")
    else:
        print("Please switch to a supported network")

# PriceFeedConsumer.sol (Solidity contract that would be compiled)
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceFeedConsumer {
    AggregatorV3Interface internal priceFeed;

    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    function getLatestPrice() public view returns (int256) {
        (
            uint80 roundID, 
            int256 price,
            uint256 startedAt,
            uint256 timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return price;
    }

    function getPriceFeed() public view returns (address) {
        return address(priceFeed);
    }
}
"""

# brownie-config.yaml (configuration file)
"""
dependencies:
  - smartcontractkit/chainlink-brownie-contracts@1.1.1
compiler:
  solc:
    remappings:
      - '@chainlink=smartcontractkit/chainlink-brownie-contracts@1.1.1'
networks:
  default: development
  kovan:
    price_feed_address: "0x9326BFA02ADD2366b30bacB125260Af641031331"
    eth_usd_price_feed: "0x9326BFA02ADD2366b30bacB125260Af641031331"
  mainnet-fork:
    eth_usd_price_feed: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
  rinkeby:
    eth_usd_price_feed: "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
  mainnet:
    eth_usd_price_feed: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
wallets:
  from_key: ${PRIVATE_KEY}
"""
```
