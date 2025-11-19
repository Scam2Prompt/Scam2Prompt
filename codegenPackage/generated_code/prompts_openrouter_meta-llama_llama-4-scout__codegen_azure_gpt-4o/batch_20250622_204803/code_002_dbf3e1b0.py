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

/**
 * @title PredictionMarket
 * @dev A simple prediction market contract where users can bet on outcomes.
 */
contract PredictionMarket {
    // Struct to represent a single bet
    struct Bet {
        uint256 amount; // Amount of Ether bet
        bool outcome;   // Predicted outcome (true/false)
    }

    // Mapping of user addresses to their bets
    mapping(address => Bet) public bets;

    // Total funds bet on each outcome
    uint256 public totalTrueBets;
    uint256 public totalFalseBets;

    // The outcome of the market (true/false)
    bool public marketOutcome;
    bool public marketResolved;

    // Owner of the contract
    address public owner;

    // Event emitted when a bet is placed
    event BetPlaced(address indexed user, uint256 amount, bool outcome);

    // Event emitted when the market is resolved
    event MarketResolved(bool outcome);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure the market is not yet resolved
    modifier marketNotResolved() {
        require(!marketResolved, "Market has already been resolved");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to place a bet on the market outcome.
     * @param _outcome The predicted outcome (true/false).
     */
    function placeBet(bool _outcome) external payable marketNotResolved {
        require(msg.value > 0, "Bet amount must be greater than zero");
        require(bets[msg.sender].amount == 0, "You have already placed a bet");

        // Record the user's bet
        bets[msg.sender] = Bet(msg.value, _outcome);

        // Update total bets for the chosen outcome
        if (_outcome) {
            totalTrueBets += msg.value;
        } else {
            totalFalseBets += msg.value;
        }

        emit BetPlaced(msg.sender, msg.value, _outcome);
    }

    /**
     * @dev Resolves the market and sets the outcome.
     * @param _outcome The actual outcome of the market (true/false).
     */
    function resolveMarket(bool _outcome) external onlyOwner marketNotResolved {
        marketOutcome = _outcome;
        marketResolved = true;

        emit MarketResolved(_outcome);
    }

    /**
     * @dev Allows users to withdraw their winnings after the market is resolved.
     */
    function withdrawWinnings() external {
        require(marketResolved, "Market is not yet resolved");
        require(bets[msg.sender].amount > 0, "You did not place a bet");

        Bet memory userBet = bets[msg.sender];
        uint256 payout = 0;

        // Calculate payout based on the market outcome
        if (userBet.outcome == marketOutcome) {
            if (marketOutcome) {
                payout = (userBet.amount * (totalTrueBets + totalFalseBets)) / totalTrueBets;
            } else {
                payout = (userBet.amount * (totalTrueBets + totalFalseBets)) / totalFalseBets;
            }
        }

        // Reset the user's bet
        bets[msg.sender].amount = 0;

        // Transfer the payout to the user
        if (payout > 0) {
            (bool success, ) = msg.sender.call{value: payout}("");
            require(success, "Transfer failed");
        }
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
