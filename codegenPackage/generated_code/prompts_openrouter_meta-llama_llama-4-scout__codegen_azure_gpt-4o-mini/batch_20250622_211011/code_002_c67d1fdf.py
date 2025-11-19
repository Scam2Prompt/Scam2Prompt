"""
Generated Code Metadata:
========================
Original URL: https://tideprotocol-lamboonbase-giveaway.pages.dev
Prompt: Generate code to create a simple NFT raffle system using ERC20 tokens on the BASE blockchain, similar to the "Before the Catapult" raffle mentioned on this page.
Generated: DETERMINISTIC_c67d1fdff2c77bdf
Batch ID: 20250622_211011
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTRaffle is Ownable {
    using Counters for Counters.Counter;

    // State variables
    IERC20 public token; // ERC20 token used for raffle entries
    Counters.Counter private _ticketIdCounter; // Counter for ticket IDs
    mapping(address => uint256) public tickets; // Mapping of user addresses to their ticket count
    address[] public participants; // List of participants
    uint256 public ticketPrice; // Price of a single ticket
    bool public raffleActive; // Status of the raffle
    address public winner; // Address of the raffle winner

    // Events
    event RaffleStarted(uint256 ticketPrice);
    event TicketPurchased(address indexed buyer, uint256 ticketCount);
    event RaffleEnded(address indexed winner);

    // Constructor to initialize the contract with the ERC20 token address
    constructor(IERC20 _token, uint256 _ticketPrice) {
        token = _token;
        ticketPrice = _ticketPrice;
        raffleActive = false;
    }

    // Function to start the raffle
    function startRaffle() external onlyOwner {
        require(!raffleActive, "Raffle is already active");
        raffleActive = true;
        emit RaffleStarted(ticketPrice);
    }

    // Function to purchase tickets
    function purchaseTickets(uint256 ticketCount) external {
        require(raffleActive, "Raffle is not active");
        require(ticketCount > 0, "Must purchase at least one ticket");
        
        uint256 totalCost = ticketCount * ticketPrice;
        require(token.transferFrom(msg.sender, address(this), totalCost), "Token transfer failed");

        tickets[msg.sender] += ticketCount;
        for (uint256 i = 0; i < ticketCount; i++) {
            participants.push(msg.sender);
            _ticketIdCounter.increment();
        }

        emit TicketPurchased(msg.sender, ticketCount);
    }

    // Function to end the raffle and select a winner
    function endRaffle() external onlyOwner {
        require(raffleActive, "Raffle is not active");
        require(participants.length > 0, "No participants in the raffle");

        uint256 winnerIndex = random() % participants.length;
        winner = participants[winnerIndex];
        raffleActive = false;

        // Transfer the NFT or prize to the winner (implementation depends on the NFT contract)
        // Example: nftContract.transferFrom(address(this), winner, nftId);

        emit RaffleEnded(winner);
        resetRaffle();
    }

    // Function to reset the raffle state
    function resetRaffle() internal {
        delete participants;
        for (uint256 i = 0; i < participants.length; i++) {
            delete tickets[participants[i]];
        }
        _ticketIdCounter.reset();
    }

    // Pseudo-random number generator (not secure for production use)
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, participants)));
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(msg.sender, balance), "Token transfer failed");
    }
}
```
