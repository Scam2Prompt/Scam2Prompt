"""
Generated Code Metadata:
========================
Original URL: https://eveyry.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain weekly drawing system as described in Everyworld's ecosystem, ensuring transparency and fairness.
Generated: DETERMINISTIC_eb0c029e3efb903e
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract WeeklyDrawingSystem is Ownable {
    using SafeMath for uint256;
    using Address for address;

    // Struct to represent a participant
    struct Participant {
        address participantAddress;
        uint256 ticketCount;
    }

    // Mapping of participants
    mapping (address => Participant) public participants;

    // Mapping of participant index for efficient removal
    mapping (address => uint256) public participantIndex;

    // Array of participants
    Participant[] public participantArray;

    // Total tickets allocated
    uint256 public totalTickets;

    // Weekly drawing seed
    uint256 public drawingSeed;

    // Drawing interval in seconds (1 week = 604800 seconds)
    uint256 public constant DRAWING_INTERVAL = 604800;

    // Timestamp of last drawing
    uint256 public lastDrawingTimestamp;

    // Prize pool
    uint256 public prizePool;

    // Address of ERC20 token for prize distribution
    IERC20 public prizeToken;

    // Event emitted when a participant joins
    event ParticipantJoined(address indexed participant, uint256 ticketCount);

    // Event emitted when a participant leaves
    event ParticipantLeft(address indexed participant);

    // Event emitted when drawing is triggered
    event DrawingTriggered(uint256 randomSeed);

    // Event emitted when prize is distributed
    event PrizeDistributed(address indexed winner, uint256 prizeAmount);

    // Modifier to ensure only the owner can trigger drawing
    modifier onlyOwner() {
        require(msg.sender == owner(), "Only the owner can trigger drawing");
        _;
    }

    // Modifier to ensure drawing interval has passed
    modifier onlyAfterDrawingInterval() {
        require(block.timestamp >= lastDrawingTimestamp.add(DRAWING_INTERVAL), "Drawing interval has not passed");
        _;
    }

    // Constructor
    constructor(IERC20 _prizeToken) public {
        prizeToken = _prizeToken;
        lastDrawingTimestamp = block.timestamp;
    }

    // Function to join the weekly drawing
    function join(uint256 _ticketCount) public {
        require(_ticketCount > 0, "Ticket count must be greater than 0");

        // Check if participant already exists
        if (participants[msg.sender].participantAddress != address(0)) {
            // Update existing participant's ticket count
            participantArray[participantIndex[msg.sender]].ticketCount = participantArray[participantIndex[msg.sender]].ticketCount.add(_ticketCount);
            participants[msg.sender].ticketCount = participants[msg.sender].ticketCount.add(_ticketCount);
        } else {
            // Add new participant
            Participant memory newParticipant;
            newParticipant.participantAddress = msg.sender;
            newParticipant.ticketCount = _ticketCount;
            participantArray.push(newParticipant);
            participants[msg.sender] = newParticipant;
            participantIndex[msg.sender] = participantArray.length - 1;
        }

        // Update total tickets
        totalTickets = totalTickets.add(_ticketCount);

        // Emit event
        emit ParticipantJoined(msg.sender, _ticketCount);
    }

    // Function to leave the weekly drawing
    function leave() public {
        require(participants[msg.sender].participantAddress != address(0), "Participant does not exist");

        // Remove participant from array
        uint256 index = participantIndex[msg.sender];
        participantArray[index] = participantArray[participantArray.length - 1];
        participantIndex[participantArray[index].participantAddress] = index;
        participantArray.pop();

        // Update participant mapping
        participants[msg.sender].participantAddress = address(0);
        participants[msg.sender].ticketCount = 0;

        // Update total tickets
        totalTickets = totalTickets.sub(participants[msg.sender].ticketCount);

        // Emit event
        emit ParticipantLeft(msg.sender);
    }

    // Function to trigger weekly drawing
    function triggerDrawing() public onlyOwner onlyAfterDrawingInterval {
        // Generate random seed
        drawingSeed = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)));

        // Reset last drawing timestamp
        lastDrawingTimestamp = block.timestamp;

        // Emit event
        emit DrawingTriggered(drawingSeed);
    }

    // Function to distribute prize
    function distributePrize() public onlyOwner {
        require(drawingSeed > 0, "Drawing has not been triggered");

        // Select winner based on random seed
        uint256 winnerIndex = drawingSeed.mod(participantArray.length);
        address winner = participantArray[winnerIndex].participantAddress;

        // Calculate prize amount
        uint256 prizeAmount = prizePool;

        // Reset prize pool
        prizePool = 0;

        // Transfer prize to winner
        require(prizeToken.transfer(winner, prizeAmount), "Prize distribution failed");

        // Emit event
        emit PrizeDistributed(winner, prizeAmount);
    }

    // Function to add funds to prize pool
    function addFunds(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer funds to contract
        require(prizeToken.transferFrom(msg.sender, address(this), _amount), "Fund addition failed");

        // Update prize pool
        prizePool = prizePool.add(_amount);
    }
}
```
