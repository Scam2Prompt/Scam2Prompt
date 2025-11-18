"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyesports.web.app
Prompt: Create a smart contract function for implementing a lottery system similar to Jellotto, ensuring compatibility with the $Jelly ecosystem.
Generated: DETERMINISTIC_1c2e238fc5bd4c50
Batch ID: 20250612_154355
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for a Lottery system
contract Lottery is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new lottery is created
    event LotteryCreated(uint256 lotteryId, uint256 ticketPrice, uint256 endTime);
    
    // Event emitted when a ticket is purchased
    event TicketPurchased(uint256 lotteryId, address buyer);

    // Event emitted when a winner is drawn
    event WinnerDrawn(uint256 lotteryId, address winner, uint256 amountWon);

    struct LotteryInfo {
        uint256 id;
        uint256 ticketPrice;
        uint256 endTime;
        address[] participants;
        bool isActive;
        uint256 totalPot;
    }

    Counters.Counter private lotteryIdCounter;
    mapping(uint256 => LotteryInfo) public lotteries;

    // Modifier to check if the lottery is active
    modifier onlyActiveLottery(uint256 lotteryId) {
        require(lotteries[lotteryId].isActive, "Lottery is not active");
        _;
    }

    // Function to create a new lottery
    function createLottery(uint256 _ticketPrice, uint256 _duration) external onlyOwner {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        lotteryIdCounter.increment();
        uint256 newLotteryId = lotteryIdCounter.current();
        uint256 endTime = block.timestamp + _duration;

        lotteries[newLotteryId] = LotteryInfo({
            id: newLotteryId,
            ticketPrice: _ticketPrice,
            endTime: endTime,
            participants: new address[](0),
            isActive: true,
            totalPot: 0
        });

        emit LotteryCreated(newLotteryId, _ticketPrice, endTime);
    }

    // Function to purchase a lottery ticket
    function buyTicket(uint256 lotteryId) external payable onlyActiveLottery(lotteryId) {
        LotteryInfo storage lottery = lotteries[lotteryId];

        require(msg.value == lottery.ticketPrice, "Incorrect ticket price");
        require(block.timestamp < lottery.endTime, "Lottery has ended");

        lottery.participants.push(msg.sender);
        lottery.totalPot += msg.value;

        emit TicketPurchased(lotteryId, msg.sender);
    }

    // Function to draw a winner for the lottery
    function drawWinner(uint256 lotteryId) external onlyOwner onlyActiveLottery(lotteryId) {
        LotteryInfo storage lottery = lotteries[lotteryId];

        require(block.timestamp >= lottery.endTime, "Lottery is still active");

        // Select a random winner
        uint256 winnerIndex = random() % lottery.participants.length;
        address winner = lottery.participants[winnerIndex];

        // Transfer the total pot to the winner
        (bool success, ) = winner.call{value: lottery.totalPot}("");
        require(success, "Transfer failed");

        // Mark the lottery as inactive
        lottery.isActive = false;

        emit WinnerDrawn(lotteryId, winner, lottery.totalPot);
    }

    // Internal function to generate a pseudo-random number
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, lotteryIdCounter.current())));
    }

    // Function to withdraw funds from the contract (for owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
