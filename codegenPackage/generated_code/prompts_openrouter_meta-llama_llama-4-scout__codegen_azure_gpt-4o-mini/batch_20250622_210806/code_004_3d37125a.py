"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Design a smart contract for a meme lottery system, like the one mentioned in Rich Pepe's roadmap, and explain how it would work.
Generated: DETERMINISTIC_3d37125a9ad05a94
Batch ID: 20250622_210806
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MemeLottery contract allows users to participate in a lottery by purchasing tickets
contract MemeLottery is Ownable {
    using SafeMath for uint256;

    // State variables
    uint256 public ticketPrice; // Price of a single lottery ticket
    address[] public players; // Array to store players' addresses
    uint256 public lotteryId; // Unique identifier for each lottery
    bool public lotteryActive; // Status of the lottery
    uint256 public lotteryEndTime; // End time for the current lottery

    // Events
    event TicketPurchased(address indexed player, uint256 amount);
    event LotteryEnded(address indexed winner, uint256 prizeAmount);
    event LotteryStarted(uint256 ticketPrice, uint256 duration);

    // Constructor to initialize the lottery
    constructor(uint256 _ticketPrice) {
        ticketPrice = _ticketPrice;
        lotteryActive = false;
    }

    // Function to start a new lottery
    function startLottery(uint256 duration) external onlyOwner {
        require(!lotteryActive, "Lottery is already active");
        require(duration > 0, "Duration must be greater than 0");

        lotteryActive = true;
        lotteryId++;
        lotteryEndTime = block.timestamp.add(duration);
        players = new address[](0); // Reset players for the new lottery

        emit LotteryStarted(ticketPrice, duration);
    }

    // Function to purchase lottery tickets
    function buyTicket() external payable {
        require(lotteryActive, "Lottery is not active");
        require(msg.value == ticketPrice, "Incorrect ticket price");
        require(block.timestamp < lotteryEndTime, "Lottery has ended");

        players.push(msg.sender); // Add player to the list

        emit TicketPurchased(msg.sender, msg.value);
    }

    // Function to end the lottery and select a winner
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp >= lotteryEndTime, "Lottery has not ended yet");
        require(players.length > 0, "No players participated");

        // Select a random winner
        uint256 winnerIndex = random() % players.length;
        address winner = players[winnerIndex];

        // Calculate the prize amount
        uint256 prizeAmount = address(this).balance;

        // Transfer the prize to the winner
        (bool success, ) = winner.call{value: prizeAmount}("");
        require(success, "Transfer failed");

        // Reset the lottery state
        lotteryActive = false;
        players = new address[](0); // Clear players

        emit LotteryEnded(winner, prizeAmount);
    }

    // Function to generate a pseudo-random number
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw funds in case of emergency
    function withdrawFunds() external onlyOwner {
        require(!lotteryActive, "Cannot withdraw while lottery is active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
