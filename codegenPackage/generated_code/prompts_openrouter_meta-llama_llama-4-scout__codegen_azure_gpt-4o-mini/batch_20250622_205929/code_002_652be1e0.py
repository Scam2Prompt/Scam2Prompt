"""
Generated Code Metadata:
========================
Original URL: https://vuyper.pages.dev
Prompt: Generate a smart contract code for deploying a custom market on Vyper, supporting a unique asset with a specific payoff structure and collateral requirements.
Generated: DETERMINISTIC_652be1e0d49ee1ca
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vyper
# SPDX-License-Identifier: MIT
# Custom Market Smart Contract in Vyper

# Define the contract
contract CustomMarket:

    # Event to log the creation of a new market
    event MarketCreated:
        marketId: indexed(uint256)
        creator: indexed(address)
        asset: indexed(string)
        collateral: uint256
        payoffStructure: string

    # Event to log the settlement of a market
    event MarketSettled:
        marketId: indexed(uint256)
        winner: indexed(address)
        payout: uint256

    # Struct to hold market details
    struct Market:
        creator: address
        asset: string
        collateral: uint256
        payoffStructure: string
        isSettled: bool
        winner: address
        payout: uint256

    # State variable to store markets
    markets: public(map(uint256, Market))
    marketCount: public(uint256)

    # Constructor to initialize the contract
    @public
    @payable
    def __init__():
        self.marketCount = 0

    # Function to create a new market
    @public
    @payable
    def createMarket(asset: string, collateral: uint256, payoffStructure: string):
        # Ensure the collateral is sent with the transaction
        assert msg.value == collateral, "Collateral amount must match the sent value"

        # Increment market count
        self.marketCount += 1

        # Create a new market
        self.markets[self.marketCount] = Market({
            creator: msg.sender,
            asset: asset,
            collateral: collateral,
            payoffStructure: payoffStructure,
            isSettled: False,
            winner: ZERO_ADDRESS,
            payout: 0
        })

        # Emit the MarketCreated event
        log.MarketCreated(self.marketCount, msg.sender, asset, collateral, payoffStructure)

    # Function to settle a market
    @public
    def settleMarket(marketId: uint256, winner: address, payout: uint256):
        # Ensure the market exists
        assert marketId > 0 and marketId <= self.marketCount, "Market does not exist"
        
        # Ensure the market is not already settled
        market: Market = self.markets[marketId]
        assert not market.isSettled, "Market is already settled"

        # Settle the market
        market.isSettled = True
        market.winner = winner
        market.payout = payout

        # Transfer payout to the winner
        send(winner, payout)

        # Emit the MarketSettled event
        log.MarketSettled(marketId, winner, payout)

    # Function to get market details
    @public
    @view
    def getMarket(marketId: uint256) -> (address, string, uint256, string, bool, address, uint256):
        # Ensure the market exists
        assert marketId > 0 and marketId <= self.marketCount, "Market does not exist"
        
        # Return market details
        market: Market = self.markets[marketId]
        return (market.creator, market.asset, market.collateral, market.payoffStructure, market.isSettled, market.winner, market.payout)
```
