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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Prediction Market Contract
 * @author [Your Name]
 * @notice A simple betting system for a decentralized prediction market platform.
 */
contract PredictionMarket is ReentrancyGuard {
    // Mapping of event IDs to their respective details
    mapping(uint256 => Event) public events;

    // Mapping of user addresses to their respective balances
    mapping(address => uint256) public balances;

    // Mapping of user addresses to their respective bets
    mapping(address => mapping(uint256 => Bet)) public bets;

    // Event emitted when a new event is created
    event NewEvent(uint256 eventId, string question, uint256 startTime, uint256 endTime);

    // Event emitted when a user places a bet
    event NewBet(address indexed user, uint256 eventId, uint256 outcome, uint256 amount);

    // Event emitted when a user settles a bet
    event BetSettled(address indexed user, uint256 eventId, uint256 outcome, uint256 payout);

    // Struct to represent an event
    struct Event {
        uint256 id;
        string question;
        uint256 startTime;
        uint256 endTime;
        uint256[] outcomes; // Array of outcome IDs
        mapping(uint256 => uint256) outcomeProbabilities; // Mapping of outcome IDs to their probabilities
        bool isSettled;
    }

    // Struct to represent a bet
    struct Bet {
        uint256 eventId;
        uint256 outcome;
        uint256 amount;
    }

    // Function to create a new event
    function createEvent(
        uint256 eventId,
        string memory question,
        uint256 startTime,
        uint256 endTime,
        uint256[] memory outcomes
    ) public {
        require(events[eventId].id == 0, "Event already exists");
        require(startTime > block.timestamp, "Start time must be in the future");
        require(endTime > startTime, "End time must be after start time");

        events[eventId] = Event(
            eventId,
            question,
            startTime,
            endTime,
            outcomes,
            new mapping(uint256 => uint256),
            false
        );

        for (uint256 i = 0; i < outcomes.length; i++) {
            events[eventId].outcomeProbabilities[outcomes[i]] = 0;
        }

        emit NewEvent(eventId, question, startTime, endTime);
    }

    // Function to place a bet on an event
    function placeBet(uint256 eventId, uint256 outcome, uint256 amount) public {
        require(events[eventId].id != 0, "Event does not exist");
        require(events[eventId].startTime <= block.timestamp, "Event has not started");
        require(events[eventId].endTime > block.timestamp, "Event has ended");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(events[eventId].outcomeProbabilities[outcome] != 0, "Invalid outcome");

        balances[msg.sender] -= amount;
        bets[msg.sender][eventId] = Bet(eventId, outcome, amount);

        emit NewBet(msg.sender, eventId, outcome, amount);
    }

    // Function to settle a bet
    function settleBet(uint256 eventId, uint256 outcome) public {
        require(events[eventId].id != 0, "Event does not exist");
        require(events[eventId].endTime <= block.timestamp, "Event has not ended");
        require(!events[eventId].isSettled, "Event has already been settled");

        Event storage event_ = events[eventId];
        uint256 totalOutcomeProbabilities = 0;
        for (uint256 i = 0; i < event_.outcomes.length; i++) {
            totalOutcomeProbabilities += event_.outcomeProbabilities[event_.outcomes[i]];
        }

        require(totalOutcomeProbabilities == 100, "Outcome probabilities do not add up to 100");

        Bet storage bet = bets[msg.sender][eventId];
        require(bet.eventId == eventId, "Bet does not exist");

        uint256 payout = (bet.amount * event_.outcomeProbabilities[outcome]) / 100;
        balances[msg.sender] += payout;

        event_.isSettled = true;

        emit BetSettled(msg.sender, eventId, outcome, payout);
    }

    // Function to deposit funds
    function deposit(address token, uint256 amount) public {
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
    }

    // Function to withdraw funds
    function withdraw(address token, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to handle Ether deposits
    receive() external payable {}
}
```
