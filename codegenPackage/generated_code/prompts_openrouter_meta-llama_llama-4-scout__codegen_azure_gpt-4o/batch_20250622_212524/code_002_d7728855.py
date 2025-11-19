"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Generate a smart contract code in Solidity to create a decentralized casino game on a blockchain platform like Ethereum, similar to KBO.bet, where users can bet on sports events and win rewards.
Generated: DETERMINISTIC_d7728855a8a98dc3
Batch ID: 20250622_212524
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

/// @title Decentralized Casino Game Smart Contract
/// @author 
/// @notice This contract allows users to bet on sports events and win rewards.
/// @dev This is a simplified version and should be audited before production use.

contract DecentralizedCasino {
    address public owner; // Owner of the contract
    uint256 public houseFeePercent; // House fee percentage (e.g., 2%)
    uint256 public minBetAmount; // Minimum bet amount in wei

    enum BetOutcome { Pending, Won, Lost }
    enum EventStatus { Open, Closed, Resolved }

    struct Bet {
        address bettor;
        uint256 amount;
        uint256 eventId;
        uint8 selectedOutcome;
        BetOutcome outcome;
    }

    struct Event {
        string name;
        uint8 outcomeCount; // Number of possible outcomes (e.g., 2 for win/lose)
        EventStatus status;
        uint8 winningOutcome; // Winning outcome index (set after resolution)
        uint256 totalPool; // Total amount bet on this event
    }

    mapping(uint256 => Event) public events; // Mapping of eventId to Event
    mapping(uint256 => Bet[]) public bets; // Mapping of eventId to array of bets
    uint256 public nextEventId; // Counter for event IDs

    event EventCreated(uint256 eventId, string name, uint8 outcomeCount);
    event BetPlaced(uint256 eventId, address indexed bettor, uint256 amount, uint8 selectedOutcome);
    event EventResolved(uint256 eventId, uint8 winningOutcome);
    event BetSettled(address indexed bettor, uint256 amountWon);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier eventExists(uint256 eventId) {
        require(events[eventId].status != EventStatus.Closed, "Event does not exist");
        _;
    }

    constructor(uint256 _houseFeePercent, uint256 _minBetAmount) {
        require(_houseFeePercent <= 100, "House fee must be <= 100%");
        owner = msg.sender;
        houseFeePercent = _houseFeePercent;
        minBetAmount = _minBetAmount;
    }

    /// @notice Create a new betting event
    /// @param name Name of the event
    /// @param outcomeCount Number of possible outcomes
    function createEvent(string memory name, uint8 outcomeCount) external onlyOwner {
        require(outcomeCount > 1, "There must be at least 2 outcomes");

        events[nextEventId] = Event({
            name: name,
            outcomeCount: outcomeCount,
            status: EventStatus.Open,
            winningOutcome: 0,
            totalPool: 0
        });

        emit EventCreated(nextEventId, name, outcomeCount);
        nextEventId++;
    }

    /// @notice Place a bet on an event
    /// @param eventId ID of the event
    /// @param selectedOutcome Index of the selected outcome
    function placeBet(uint256 eventId, uint8 selectedOutcome) external payable eventExists(eventId) {
        Event storage bettingEvent = events[eventId];
        require(bettingEvent.status == EventStatus.Open, "Betting is closed for this event");
        require(msg.value >= minBetAmount, "Bet amount is below the minimum");
        require(selectedOutcome < bettingEvent.outcomeCount, "Invalid outcome selected");

        bets[eventId].push(Bet({
            bettor: msg.sender,
            amount: msg.value,
            eventId: eventId,
            selectedOutcome: selectedOutcome,
            outcome: BetOutcome.Pending
        }));

        bettingEvent.totalPool += msg.value;

        emit BetPlaced(eventId, msg.sender, msg.value, selectedOutcome);
    }

    /// @notice Resolve an event and set the winning outcome
    /// @param eventId ID of the event
    /// @param winningOutcome Index of the winning outcome
    function resolveEvent(uint256 eventId, uint8 winningOutcome) external onlyOwner eventExists(eventId) {
        Event storage bettingEvent = events[eventId];
        require(bettingEvent.status == EventStatus.Open, "Event is not open for resolution");
        require(winningOutcome < bettingEvent.outcomeCount, "Invalid winning outcome");

        bettingEvent.status = EventStatus.Resolved;
        bettingEvent.winningOutcome = winningOutcome;

        emit EventResolved(eventId, winningOutcome);
    }

    /// @notice Settle bets for a resolved event
    /// @param eventId ID of the event
    function settleBets(uint256 eventId) external eventExists(eventId) {
        Event storage bettingEvent = events[eventId];
        require(bettingEvent.status == EventStatus.Resolved, "Event is not resolved");

        uint256 totalWinningPool = 0;
        uint256 houseFee = (bettingEvent.totalPool * houseFeePercent) / 100;

        // Calculate total winning pool
        for (uint256 i = 0; i < bets[eventId].length; i++) {
            Bet storage bet = bets[eventId][i];
            if (bet.selectedOutcome == bettingEvent.winningOutcome) {
                totalWinningPool += bet.amount;
            }
        }

        // Distribute rewards to winners
        for (uint256 i = 0; i < bets[eventId].length; i++) {
            Bet storage bet = bets[eventId][i];
            if (bet.selectedOutcome == bettingEvent.winningOutcome) {
                uint256 reward = (bet.amount * (bettingEvent.totalPool - houseFee)) / totalWinningPool;
                bet.outcome = BetOutcome.Won;
                payable(bet.bettor).transfer(reward);
                emit BetSettled(bet.bettor, reward);
            } else {
                bet.outcome = BetOutcome.Lost;
            }
        }

        // Transfer house fee to owner
        payable(owner).transfer(houseFee);

        // Close the event
        bettingEvent.status = EventStatus.Closed;
    }

    /// @notice Withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
