"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.vercel.app
Prompt: Generate a smart contract template for PolyMarket using the code available on GitHub to enforce market rules and payouts.
Generated: DETERMINISTIC_c6e70bad942063a5
Batch ID: 20250612_145826
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

/**
 * @title PolyMarketTemplate
 * @dev A smart contract template for creating markets, enforcing rules, and handling payouts on PolyMarket.
 */
contract PolyMarketTemplate {
    // Events
    event MarketCreated(uint256 marketId, string question, address indexed creator);
    event MarketResolved(uint256 marketId, bool outcome, address indexed resolver);
    event PayoutProcessed(uint256 marketId, address indexed user, uint256 amount);

    // Structs
    struct Market {
        string question; // The question for the market
        uint256 resolutionTimestamp; // Timestamp when the market will resolve
        bool resolved; // Whether the market is resolved
        bool outcome; // Market resolution outcome: true or false
        address creator; // Address of the market creator
        mapping(address => uint256) bets; // Tracks user bets
        uint256 totalYesBets; // Total amount of YES bets
        uint256 totalNoBets; // Total amount of NO bets
    }

    // State variables
    uint256 public marketCount; // Counter for market IDs
    mapping(uint256 => Market) public markets; // Maps market IDs to Market struct

    /**
     * @dev Create a new market.
     * @param question The question for the market.
     * @param resolutionTimestamp The timestamp when the market will resolve.
     */
    function createMarket(string memory question, uint256 resolutionTimestamp) external {
        require(resolutionTimestamp > block.timestamp, "Resolution timestamp must be in the future");

        marketCount++;
        Market storage newMarket = markets[marketCount];
        newMarket.question = question;
        newMarket.resolutionTimestamp = resolutionTimestamp;
        newMarket.creator = msg.sender;

        emit MarketCreated(marketCount, question, msg.sender);
    }

    /**
     * @dev Place a bet on a market.
     * @param marketId The ID of the market.
     * @param outcome The predicted outcome (true for YES, false for NO).
     */
    function placeBet(uint256 marketId, bool outcome) external payable {
        Market storage market = markets[marketId];
        require(!market.resolved, "Market already resolved");
        require(block.timestamp < market.resolutionTimestamp, "Market resolution period has ended");
        require(msg.value > 0, "Bet amount must be greater than zero");

        market.bets[msg.sender] += msg.value;

        if (outcome) {
            market.totalYesBets += msg.value;
        } else {
            market.totalNoBets += msg.value;
        }
    }

    /**
     * @dev Resolve a market with the outcome.
     * @param marketId The ID of the market.
     * @param outcome The true outcome of the market (true for YES, false for NO).
     */
    function resolveMarket(uint256 marketId, bool outcome) external {
        Market storage market = markets[marketId];
        require(block.timestamp >= market.resolutionTimestamp, "Market resolution period not reached");
        require(!market.resolved, "Market already resolved");
        require(msg.sender == market.creator, "Only the market creator can resolve");

        market.resolved = true;
        market.outcome = outcome;

        emit MarketResolved(marketId, outcome, msg.sender);
    }

    /**
     * @dev Claim payout for a resolved market.
     * @param marketId The ID of the market.
     */
    function claimPayout(uint256 marketId) external {
        Market storage market = markets[marketId];
        require(market.resolved, "Market not resolved yet");

        uint256 userBet = market.bets[msg.sender];
        require(userBet > 0, "No bets placed by user");

        uint256 payout;
        if (market.outcome) {
            // Outcome is YES
            payout = (userBet * market.totalNoBets) / market.totalYesBets;
        } else {
            // Outcome is NO
            payout = (userBet * market.totalYesBets) / market.totalNoBets;
        }

        // Prevent reentrancy by clearing user bet before transfer
        market.bets[msg.sender] = 0;

        (bool sent, ) = msg.sender.call{value: payout}("");
        require(sent, "Payout transfer failed");

        emit PayoutProcessed(marketId, msg.sender, payout);
    }

    /**
     * @dev Fallback function to accept direct Ether transfers.
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract balance by creator (useful for managing leftover funds).
     */
    function withdraw() external {
        require(msg.sender == markets[marketCount].creator, "Only the market creator can withdraw");
        uint256 balance = address(this).balance;

        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Withdrawal failed");
    }
}
```
