"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Provide code to implement a decentralized sports betting system with great odds and instant payouts, similar to the features described on Blockchain Bets.
Generated: DETERMINISTIC_6684fc51d2648c9d
Batch ID: 20250612_153420
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

/// @title Decentralized Sports Betting System
/// @author Your Name
/// @notice This contract allows users to place bets on sports events with great odds and instant payouts
/// @dev The contract uses a simple mapping for betting and events

contract SportsBetting {
    struct Event {
        uint256 id;
        string name;
        uint256 totalBets;
        uint256 odds;
        bool isActive;
    }

    struct Bet {
        uint256 eventId;
        address better;
        uint256 amount;
        uint256 odds;
    }

    mapping(uint256 => Event) public events; // Mapping of event ID to Event
    mapping(address => Bet[]) public bets; // Mapping of bettor address to their Bet details
    uint256 public nextEventId; // Counter for event IDs
    uint256 public totalFunds; // Total funds in the contract

    event EventCreated(uint256 eventId, string name, uint256 odds);
    event BetPlaced(address indexed better, uint256 eventId, uint256 amount, uint256 odds);
    event Payout(address indexed better, uint256 amount);

    /// @notice Create a new sports event
    /// @param name The name of the sports event
    /// @param odds The odds for the event
    function createEvent(string memory name, uint256 odds) external {
        require(odds > 0, "Odds must be greater than zero");
        
        events[nextEventId] = Event({
            id: nextEventId,
            name: name,
            totalBets: 0,
            odds: odds,
            isActive: true
        });

        emit EventCreated(nextEventId, name, odds);
        nextEventId++;
    }

    /// @notice Place a bet on a sports event
    /// @param eventId The ID of the event to bet on
    function placeBet(uint256 eventId) external payable {
        require(events[eventId].isActive, "Event is not active");
        require(msg.value > 0, "Bet amount must be greater than zero");

        // Create and store the bet
        bets[msg.sender].push(Bet({
            eventId: eventId,
            better: msg.sender,
            amount: msg.value,
            odds: events[eventId].odds
        }));

        events[eventId].totalBets += msg.value; // Update total bets on the event

        emit BetPlaced(msg.sender, eventId, msg.value, events[eventId].odds);
    }

    /// @notice Resolve an event and distribute payouts
    /// @param eventId The ID of the event to resolve
    /// @param winningBetters List of addresses who won
    function resolveEvent(uint256 eventId, address[] memory winningBetters) external {
        require(events[eventId].isActive, "Event is already resolved");

        uint256 payoutPerBetter = (events[eventId].totalBets * events[eventId].odds) / 100; // Calculate payout based on odds
        events[eventId].isActive = false; // Mark event as inactive

        for (uint256 i = 0; i < winningBetters.length; i++) {
            // Transfer payout to each winning bettor
            (bool success, ) = winningBetters[i].call{value: payoutPerBetter}("");
            require(success, "Payout failed");

            emit Payout(winningBetters[i], payoutPerBetter);
        }
    }

    /// @notice Get event details
    /// @param eventId The ID of the event
    /// @return id The ID of the event
    /// @return name The name of the event
    /// @return totalBets The total amount of bets placed on the event
    /// @return odds The odds for the event
    /// @return isActive The status of the event
    function getEvent(uint256 eventId) external view returns (uint256 id, string memory name, uint256 totalBets, uint256 odds, bool isActive) {
        Event memory ev = events[eventId];
        return (ev.id, ev.name, ev.totalBets, ev.odds, ev.isActive);
    }

    /// @notice Allows the contract to receive Ether
    receive() external payable {
        totalFunds += msg.value; // Update total funds in the contract
    }
}
```
