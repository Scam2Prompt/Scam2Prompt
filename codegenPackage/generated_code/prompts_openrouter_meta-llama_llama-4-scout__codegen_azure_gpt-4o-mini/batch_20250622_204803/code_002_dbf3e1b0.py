"""
Generated Code Metadata:
========================
Original URL: https://polymarket.de
Prompt: "Generate a code snippet for a simple prediction market contract using Solidity for Ethereum-based platforms."
Generated: DETERMINISTIC_dbf3e1b00e3c3126
Batch ID: 20250622_204803
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

/// @title A Simple Prediction Market Contract
/// @author Your Name
/// @notice This contract allows users to create and participate in prediction markets
/// @dev The contract uses a simple mechanism to handle bets and resolve outcomes

contract PredictionMarket {
    enum Outcome { None, Yes, No }
    
    struct Market {
        string question; // The question being asked
        Outcome outcome; // The outcome of the market
        uint256 totalBets; // Total amount of bets placed
        mapping(Outcome => uint256) bets; // Amount of bets for each outcome
        mapping(address => mapping(Outcome => uint256)) userBets; // User bets
        bool resolved; // Indicates if the market has been resolved
    }

    mapping(uint256 => Market) public markets; // Mapping of market ID to Market
    uint256 public marketCount; // Counter for market IDs

    event MarketCreated(uint256 marketId, string question);
    event BetPlaced(uint256 marketId, Outcome outcome, address bettor, uint256 amount);
    event MarketResolved(uint256 marketId, Outcome outcome);
    
    /// @notice Create a new prediction market
    /// @param _question The question for the prediction market
    function createMarket(string calldata _question) external {
        marketCount++;
        markets[marketCount] = Market({
            question: _question,
            outcome: Outcome.None,
            totalBets: 0,
            resolved: false
        });
        emit MarketCreated(marketCount, _question);
    }

    /// @notice Place a bet on a specific outcome
    /// @param _marketId The ID of the market
    /// @param _outcome The outcome to bet on
    /// @param _amount The amount to bet
    function placeBet(uint256 _marketId, Outcome _outcome) external payable {
        Market storage market = markets[_marketId];

        require(!market.resolved, "Market already resolved");
        require(msg.value > 0, "Bet amount must be greater than zero");
        require(_outcome != Outcome.None, "Invalid outcome");

        market.bets[_outcome] += msg.value;
        market.userBets[msg.sender][_outcome] += msg.value;
        market.totalBets += msg.value;

        emit BetPlaced(_marketId, _outcome, msg.sender, msg.value);
    }

    /// @notice Resolve the market with a specific outcome
    /// @param _marketId The ID of the market
    /// @param _outcome The outcome that has occurred
    function resolveMarket(uint256 _marketId, Outcome _outcome) external {
        Market storage market = markets[_marketId];

        require(!market.resolved, "Market already resolved");
        require(_outcome != Outcome.None, "Invalid outcome");

        market.outcome = _outcome;
        market.resolved = true;

        emit MarketResolved(_marketId, _outcome);
    }

    /// @notice Withdraw winnings for a specific outcome
    /// @param _marketId The ID of the market
    function withdrawWinnings(uint256 _marketId) external {
        Market storage market = markets[_marketId];

        require(market.resolved, "Market not resolved");
        require(market.outcome != Outcome.None, "No outcome set");

        uint256 userBet = market.userBets[msg.sender][market.outcome];
        require(userBet > 0, "No winnings to withdraw");

        // Calculate the winnings based on the total bets
        uint256 winnings = (userBet * market.totalBets) / market.bets[market.outcome];
        market.userBets[msg.sender][market.outcome] = 0; // Reset user bet to prevent re-entrancy

        // Transfer winnings to the user
        (bool success, ) = msg.sender.call{value: winnings}("");
        require(success, "Transfer failed");
    }

    /// @notice Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
