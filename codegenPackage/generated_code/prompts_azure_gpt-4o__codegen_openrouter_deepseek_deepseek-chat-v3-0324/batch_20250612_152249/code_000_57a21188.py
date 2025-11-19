"""
Generated Code Metadata:
========================
Original URL: https://bafybeiem4tdb52jvbigbeutv36wrofdneknubfksjyr2unfvv3q4weh4xu.ipfs.dweb.link
Prompt: Write a smart contract using Azuro's architecture to create a prediction game for sports events, integrating oracle and liquidity solutions as described on the Azuro Developer Hub.
Generated: DETERMINISTIC_57a211886af17efb
Batch ID: 20250612_152249
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

import "@azuro-protocol/core-contracts/contracts/interfaces/IOracle.sol";
import "@azuro-protocol/core-contracts/contracts/interfaces/ILiquidity.sol";
import "@azuro-protocol/core-contracts/contracts/interfaces/ICore.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract SportsPredictionGame is Ownable, Pausable {
    // Core contract interface
    ICore public core;
    
    // Oracle contract interface
    IOracle public oracle;
    
    // Liquidity contract interface
    ILiquidity public liquidity;
    
    // Event structure
    struct Event {
        uint256 eventId;
        string description;
        uint256 startTime;
        bool isSettled;
        uint256 outcome;
    }
    
    // Bet structure
    struct Bet {
        address bettor;
        uint256 eventId;
        uint256 amount;
        uint256 predictedOutcome;
        bool isClaimed;
    }
    
    // Mapping of event IDs to Event struct
    mapping(uint256 => Event) public events;
    
    // Mapping of bet IDs to Bet struct
    mapping(uint256 => Bet) public bets;
    
    // Counter for bet IDs
    uint256 public nextBetId = 1;
    
    // Event emitted when new event is created
    event EventCreated(uint256 indexed eventId, string description, uint256 startTime);
    
    // Event emitted when event is settled
    event EventSettled(uint256 indexed eventId, uint256 outcome);
    
    // Event emitted when new bet is placed
    event BetPlaced(uint256 indexed betId, address indexed bettor, uint256 eventId, uint256 amount, uint256 predictedOutcome);
    
    // Event emitted when bet is claimed
    event BetClaimed(uint256 indexed betId, address indexed bettor, uint256 amount);
    
    constructor(
        address _core,
        address _oracle,
        address _liquidity
    ) {
        core = ICore(_core);
        oracle = IOracle(_oracle);
        liquidity = ILiquidity(_liquidity);
    }
    
    /**
     * @dev Create a new sports event for prediction
     * @param eventId The unique identifier for the event
     * @param description Description of the event
     * @param startTime Timestamp when the event starts
     */
    function createEvent(
        uint256 eventId,
        string memory description,
        uint256 startTime
    ) external onlyOwner {
        require(events[eventId].eventId == 0, "Event already exists");
        require(startTime > block.timestamp, "Start time must be in the future");
        
        events[eventId] = Event({
            eventId: eventId,
            description: description,
            startTime: startTime,
            isSettled: false,
            outcome: 0
        });
        
        emit EventCreated(eventId, description, startTime);
    }
    
    /**
     * @dev Place a bet on an event
     * @param eventId The event ID to bet on
     * @param predictedOutcome The predicted outcome (1 or 2)
     */
    function placeBet(uint256 eventId, uint256 predictedOutcome) external payable whenNotPaused {
        require(msg.value > 0, "Bet amount must be greater than 0");
        require(events[eventId].eventId != 0, "Event does not exist");
        require(!events[eventId].isSettled, "Event already settled");
        require(block.timestamp < events[eventId].startTime, "Event already started");
        require(predictedOutcome == 1 || predictedOutcome == 2, "Invalid outcome");
        
        uint256 betId = nextBetId++;
        bets[betId] = Bet({
            bettor: msg.sender,
            eventId: eventId,
            amount: msg.value,
            predictedOutcome: predictedOutcome,
            isClaimed: false
        });
        
        // Add liquidity to the pool
        liquidity.addLiquidity{value: msg.value}(msg.sender);
        
        emit BetPlaced(betId, msg.sender, eventId, msg.value, predictedOutcome);
    }
    
    /**
     * @dev Settle an event with the outcome
     * @param eventId The event ID to settle
     * @param outcome The actual outcome (1 or 2)
     */
    function settleEvent(uint256 eventId, uint256 outcome) external {
        require(events[eventId].eventId != 0, "Event does not exist");
        require(!events[eventId].isSettled, "Event already settled");
        require(block.timestamp >= events[eventId].startTime, "Event not started yet");
        require(outcome == 1 || outcome == 2, "Invalid outcome");
        
        // Verify outcome with oracle
        require(oracle.verifyOutcome(eventId, outcome), "Oracle verification failed");
        
        events[eventId].isSettled = true;
        events[eventId].outcome = outcome;
        
        emit EventSettled(eventId, outcome);
    }
    
    /**
     * @dev Claim winnings for a bet
     * @param betId The bet ID to claim
     */
    function claimWinnings(uint256 betId) external whenNotPaused {
        require(bets[betId].bettor != address(0), "Bet does not exist");
        require(!bets[betId].isClaimed, "Bet already claimed");
        require(events[bets[betId].eventId].isSettled, "Event not settled yet");
        
        Bet storage bet = bets[betId];
        Event storage event_ = events[bet.eventId];
        
        if (bet.predictedOutcome == event_.outcome) {
            // Calculate payout using core contract
            uint256 payout = core.calculatePayout(bet.amount, bet.eventId, bet.predictedOutcome);
            
            // Transfer winnings to bettor
            (bool success, ) = bet.bettor.call{value: payout}("");
            require(success, "Transfer failed");
            
            emit BetClaimed(betId, bet.bettor, payout);
        }
        
        bet.isClaimed = true;
    }
    
    /**
     * @dev Pause the contract to prevent new bets
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Withdraw funds from the contract (emergency only)
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
