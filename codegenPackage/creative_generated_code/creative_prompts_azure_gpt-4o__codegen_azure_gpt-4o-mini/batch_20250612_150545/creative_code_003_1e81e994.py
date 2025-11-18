"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydao.web.app
Prompt: Create a smart contract for a lottery system inspired by "Jellotto," ensuring it supports $Jelly tokens and adheres to the features outlined on the JellyDAO site.
Generated: DETERMINISTIC_1e81e994dce199a2
Batch ID: 20250612_150545
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JellottoLottery is Ownable {
    // State variables
    IERC20 public jellyToken; // Reference to the $Jelly token contract
    address[] public players; // Array of players who entered the lottery
    uint256 public lotteryId; // Unique identifier for the lottery
    uint256 public ticketPrice; // Price of each lottery ticket
    bool public lotteryActive; // Status of the lottery

    // Events
    event LotteryStarted(uint256 indexed lotteryId, uint256 ticketPrice);
    event PlayerEntered(address indexed player, uint256 indexed lotteryId);
    event LotteryEnded(uint256 indexed lotteryId, address indexed winner, uint256 amountWon);

    // Constructor to initialize the contract with the $Jelly token address
    constructor(address _jellyToken, uint256 _ticketPrice) {
        require(_jellyToken != address(0), "Invalid $Jelly token address");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");

        jellyToken = IERC20(_jellyToken);
        ticketPrice = _ticketPrice;
        lotteryActive = false;
    }

    // Function to start a new lottery
    function startLottery() external onlyOwner {
        require(!lotteryActive, "Lottery already active");

        lotteryId++;
        lotteryActive = true;
        delete players; // Clear previous players

        emit LotteryStarted(lotteryId, ticketPrice);
    }

    // Function for players to enter the lottery
    function enterLottery() external {
        require(lotteryActive, "Lottery is not active");
        require(jellyToken.balanceOf(msg.sender) >= ticketPrice, "Insufficient $Jelly tokens");
        require(jellyToken.allowance(msg.sender, address(this)) >= ticketPrice, "Token allowance not set");

        // Transfer $Jelly tokens from the player to the contract
        jellyToken.transferFrom(msg.sender, address(this), ticketPrice);
        players.push(msg.sender);

        emit PlayerEntered(msg.sender, lotteryId);
    }

    // Function to end the lottery and pick a winner
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(players.length > 0, "No players in the lottery");

        lotteryActive = false;

        // Randomly select a winner
        address winner = players[random() % players.length];
        uint256 prizeAmount = jellyToken.balanceOf(address(this));
        
        // Transfer the prize to the winner
        jellyToken.transfer(winner, prizeAmount);

        emit LotteryEnded(lotteryId, winner, prizeAmount);
    }

    // Internal function to generate a pseudo-random number
    function random() internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = jellyToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient balance to withdraw");

        jellyToken.transfer(msg.sender, amount);
    }
}
```
