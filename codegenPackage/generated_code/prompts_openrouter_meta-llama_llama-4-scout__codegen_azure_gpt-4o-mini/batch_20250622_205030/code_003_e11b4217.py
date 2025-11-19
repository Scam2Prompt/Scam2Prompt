"""
Generated Code Metadata:
========================
Original URL: https://polymarket-frontend-green.vercel.app
Prompt: Create a simple betting system using a library like Solidity for a decentralized prediction market platform, inspired by Polymarket's features.
Generated: DETERMINISTIC_e11b42176894b8cf
Batch ID: 20250622_205030
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

contract PredictionMarket {
    // Struct to represent a market
    struct Market {
        string question; // The question being asked
        uint256 endTime; // The time when the market closes
        uint256 totalBets; // Total amount of bets placed
        mapping(address => uint256) bets; // Mapping of user addresses to their bets
        bool resolved; // Status of the market
        uint256 winningOutcome; // The outcome that wins
    }

    // Mapping of market IDs to markets
    mapping(uint256 => Market) public markets;
    uint256 public marketCount; // Counter for market IDs

    // Event emitted when a new market is created
    event MarketCreated(uint256 marketId, string question, uint256 endTime);
    // Event emitted when a bet is placed
    event BetPlaced(uint256 marketId, address bettor, uint256 amount);
    // Event emitted when a market is resolved
    event MarketResolved(uint256 marketId, uint256 winningOutcome);

    // Modifier to check if the market is still open
    modifier onlyOpenMarket(uint256 marketId) {
        require(block.timestamp < markets[marketId].endTime, "Market is closed");
        _;
    }

    // Modifier to check if the market is resolved
    modifier onlyResolvedMarket(uint256 marketId) {
        require(markets[marketId].resolved, "Market is not resolved");
        _;
    }

    // Function to create a new market
    function createMarket(string memory _question, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero");

        marketCount++;
        uint256 endTime = block.timestamp + _duration;

        markets[marketCount] = Market({
            question: _question,
            endTime: endTime,
            totalBets: 0,
            resolved: false,
            winningOutcome: 0
        });

        emit MarketCreated(marketCount, _question, endTime);
    }

    // Function to place a bet on a market
    function placeBet(uint256 marketId) external payable onlyOpenMarket(marketId) {
        require(msg.value > 0, "Bet amount must be greater than zero");
        require(markets[marketId].bets[msg.sender] == 0, "You have already placed a bet");

        markets[marketId].bets[msg.sender] = msg.value;
        markets[marketId].totalBets += msg.value;

        emit BetPlaced(marketId, msg.sender, msg.value);
    }

    // Function to resolve a market
    function resolveMarket(uint256 marketId, uint256 winningOutcome) external onlyResolvedMarket(marketId) {
        require(block.timestamp >= markets[marketId].endTime, "Market is still open");
        require(!markets[marketId].resolved, "Market already resolved");

        markets[marketId].resolved = true;
        markets[marketId].winningOutcome = winningOutcome;

        emit MarketResolved(marketId, winningOutcome);
    }

    // Function to withdraw winnings after a market is resolved
    function withdrawWinnings(uint256 marketId) external onlyResolvedMarket(marketId) {
        require(markets[marketId].winningOutcome != 0, "No winning outcome set");

        uint256 betAmount = markets[marketId].bets[msg.sender];
        require(betAmount > 0, "No bet placed");

        // Calculate winnings based on total bets and winning outcome
        uint256 winnings = (betAmount * markets[marketId].totalBets) / betAmount; // Simplified for demonstration

        // Reset user's bet to prevent re-entrancy
        markets[marketId].bets[msg.sender] = 0;

        // Transfer winnings to the user
        payable(msg.sender).transfer(winnings);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
