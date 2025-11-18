"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance.wallet.consulting
Prompt: Generate a smart contract in Solidity for a cryptocurrency lottery system, inspired by the MyLottoCoin example mentioned on the Binance Wallet Consulting page.
Generated: DETERMINISTIC_688c172a9ae18580
Batch ID: 20250612_150947
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

/**
 * @title Cryptocurrency Lottery System
 * @dev A smart contract for a decentralized lottery system where participants can enter by paying a fee,
 * and a winner is selected randomly after a predefined duration.
 */
contract CryptoLottery {
    // State variables
    address public owner; // Owner of the contract
    uint256 public ticketPrice; // Price of one lottery ticket (in Wei)
    uint256 public lotteryEndTime; // Timestamp for when the lottery ends
    address[] public participants; // Array of participant addresses
    bool public lotteryActive; // Flag to indicate whether the lottery is active

    // Events
    event LotteryStarted(uint256 endTime);
    event TicketPurchased(address indexed participant);
    event WinnerSelected(address indexed winner, uint256 prize);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier lotteryIsActive() {
        require(lotteryActive, "Lottery is not active");
        _;
    }

    /**
     * @dev Constructor that initializes the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Start a new lottery round.
     * @param _ticketPrice Price of a lottery ticket (in Wei).
     * @param _duration Duration of the lottery in seconds.
     */
    function startLottery(uint256 _ticketPrice, uint256 _duration) external onlyOwner {
        require(!lotteryActive, "A lottery is already active");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        ticketPrice = _ticketPrice;
        lotteryEndTime = block.timestamp + _duration;
        lotteryActive = true;

        // Reset participants array for the new round
        delete participants;

        emit LotteryStarted(lotteryEndTime);
    }

    /**
     * @dev Purchase a lottery ticket.
     */
    function purchaseTicket() external payable lotteryIsActive {
        require(msg.value == ticketPrice, "Incorrect ticket price");
        require(block.timestamp <= lotteryEndTime, "Lottery has ended");

        // Add participant to the list
        participants.push(msg.sender);

        emit TicketPurchased(msg.sender);
    }

    /**
     * @dev Select a winner and distribute the prize pool.
     */
    function selectWinner() external onlyOwner lotteryIsActive {
        require(block.timestamp > lotteryEndTime, "Lottery is still ongoing");
        require(participants.length > 0, "No participants in the lottery");

        // Select a winner randomly
        uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants))) % participants.length;
        address winner = participants[randomIndex];

        // Calculate the prize pool
        uint256 prize = address(this).balance;

        // Transfer prize to the winner
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer to winner failed");

        // End the lottery
        lotteryActive = false;

        emit WinnerSelected(winner, prize);
    }

    /**
     * @dev Withdraw contract balance in case of no participation.
     */
    function withdrawFunds() external onlyOwner {
        require(!lotteryActive, "Cannot withdraw funds while lottery is active");
        require(participants.length == 0, "Cannot withdraw funds when participants exist");

        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfer.
     */
    receive() external payable {
        revert("Use purchaseTicket to participate in the lottery");
    }
}
```
