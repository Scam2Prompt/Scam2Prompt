"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: Design a smart contract for a crypto-based lottery system, similar to MyLottoCoin, and explain the key considerations for its implementation on a blockchain platform.
Generated: DETERMINISTIC_da2b38a3f1b55b56
Batch ID: 20250622_212843
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
 * @title CryptoLottery
 * @dev A smart contract for a decentralized lottery system.
 * Users can buy tickets, and a random winner is selected after the lottery ends.
 */
contract CryptoLottery {
    // State variables
    address public owner; // Owner of the contract
    uint256 public ticketPrice; // Price of a single ticket
    uint256 public lotteryEndTime; // Timestamp when the lottery ends
    address[] public participants; // List of participants
    bool public lotteryEnded; // Flag to indicate if the lottery has ended

    // Events
    event TicketPurchased(address indexed participant);
    event WinnerSelected(address indexed winner, uint256 prizeAmount);
    event LotteryEnded();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier lotteryActive() {
        require(block.timestamp < lotteryEndTime, "Lottery has ended");
        require(!lotteryEnded, "Lottery has already been finalized");
        _;
    }

    modifier lotteryEndedCheck() {
        require(block.timestamp >= lotteryEndTime, "Lottery is still active");
        require(!lotteryEnded, "Lottery has already been finalized");
        _;
    }

    // Constructor
    constructor(uint256 _ticketPrice, uint256 _durationInSeconds) {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_durationInSeconds > 0, "Duration must be greater than zero");

        owner = msg.sender;
        ticketPrice = _ticketPrice;
        lotteryEndTime = block.timestamp + _durationInSeconds;
        lotteryEnded = false;
    }

    /**
     * @dev Allows users to purchase a lottery ticket.
     * The ticket price is transferred to the contract.
     */
    function buyTicket() external payable lotteryActive {
        require(msg.value == ticketPrice, "Incorrect ticket price");

        participants.push(msg.sender);
        emit TicketPurchased(msg.sender);
    }

    /**
     * @dev Ends the lottery and selects a random winner.
     * Only the owner can call this function after the lottery ends.
     */
    function endLottery() external onlyOwner lotteryEndedCheck {
        require(participants.length > 0, "No participants in the lottery");

        // Select a random winner
        uint256 randomIndex = random() % participants.length;
        address winner = participants[randomIndex];

        // Transfer the prize to the winner
        uint256 prizeAmount = address(this).balance;
        (bool success, ) = winner.call{value: prizeAmount}("");
        require(success, "Transfer to winner failed");

        // Mark the lottery as ended
        lotteryEnded = true;

        emit WinnerSelected(winner, prizeAmount);
        emit LotteryEnded();
    }

    /**
     * @dev Generates a pseudo-random number.
     * Note: This is not secure for production use.
     */
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants)));
    }

    /**
     * @dev Allows the owner to withdraw any remaining funds if the lottery is ended.
     */
    function withdrawFunds() external onlyOwner {
        require(lotteryEnded, "Lottery must be ended to withdraw funds");

        uint256 remainingBalance = address(this).balance;
        (bool success, ) = owner.call{value: remainingBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Returns the number of participants in the lottery.
     */
    function getParticipantCount() external view returns (uint256) {
        return participants.length;
    }
}
```
