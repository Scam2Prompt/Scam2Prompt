"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophan.xyz
Prompt: Provide code to implement a prediction market application on Sophon Chain, leveraging its blockchain infrastructure.
Generated: DETERMINISTIC_7fed78645fe6a384
Batch ID: 20250612_153854
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

/// @title Prediction Market Contract
/// @notice This contract allows users to create and participate in prediction markets on various events.
contract PredictionMarket {
    // Struct to represent a prediction market event
    struct Market {
        string description; // Description of the event
        uint256 deadline; // Deadline for betting
        uint256 totalBets; // Total amount bet on the market
        address winner; // Address of the winner
        bool isSettled; // Flag to check if the market is settled
    }

    // Mapping to store markets by their IDs
    mapping(uint256 => Market) public markets;
    uint256 public marketCount; // Counter for market IDs

    // Event emitted when a new market is created
    event MarketCreated(uint256 indexed marketId, string description, uint256 deadline);
    
    // Event emitted when a bet is placed
    event BetPlaced(uint256 indexed marketId, address indexed bettor, uint256 amount);
    
    // Event emitted when a market is settled
    event MarketSettled(uint256 indexed marketId, address indexed winner);

    /// @notice Create a new prediction market
    /// @param _description Description of the event
    /// @param _duration Duration until the market closes (in seconds)
    function createMarket(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero.");
        
        marketCount++;
        markets[marketCount] = Market({
            description: _description,
            deadline: block.timestamp + _duration,
            totalBets: 0,
            winner: address(0),
            isSettled: false
        });
        
        emit MarketCreated(marketCount, _description, markets[marketCount].deadline);
    }

    /// @notice Place a bet on a market
    /// @param _marketId ID of the market to bet on
    function placeBet(uint256 _marketId) external payable {
        Market storage market = markets[_marketId];
        
        require(block.timestamp < market.deadline, "Market has already closed.");
        require(msg.value > 0, "Bet amount must be greater than zero.");
        require(!market.isSettled, "Market is already settled.");
        
        market.totalBets += msg.value;
        
        emit BetPlaced(_marketId, msg.sender, msg.value);
    }

    /// @notice Settle the market and declare a winner
    /// @param _marketId ID of the market to settle
    /// @param _winner Address of the winner
    function settleMarket(uint256 _marketId, address _winner) external {
        Market storage market = markets[_marketId];
        
        require(block.timestamp >= market.deadline, "Market is still open.");
        require(!market.isSettled, "Market is already settled.");
        require(_winner != address(0), "Winner address cannot be zero.");

        market.winner = _winner;
        market.isSettled = true;

        emit MarketSettled(_marketId, _winner);
    }

    /// @notice Withdraw the winnings for the winner
    /// @param _marketId ID of the market
    function withdrawWinnings(uint256 _marketId) external {
        Market storage market = markets[_marketId];

        require(market.isSettled, "Market must be settled to withdraw.");
        require(msg.sender == market.winner, "Only the winner can withdraw.");

        uint256 winningAmount = market.totalBets;
        market.totalBets = 0; // Reset total bets before transferring to prevent re-entrancy

        (bool success, ) = msg.sender.call{value: winningAmount}("");
        require(success, "Withdrawal failed.");
    }
}
```
