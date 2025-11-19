"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Create a Solidity contract for a lottery system tied to a meme-based cryptocurrency token, referencing the "Rich Pepe" special meme lottery concept.
Generated: DETERMINISTIC_0906640f2cb9e6eb
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RichPepeLottery is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public pepeToken; // The meme-based cryptocurrency token
    address[] public players; // Array to store players' addresses
    uint256 public lotteryId; // Unique identifier for each lottery
    uint256 public ticketPrice; // Price of a lottery ticket in Pepe tokens
    bool public lotteryActive; // Status of the lottery

    // Event to emit when a new lottery is created
    event LotteryCreated(uint256 indexed lotteryId, uint256 ticketPrice);
    // Event to emit when a player enters the lottery
    event PlayerEntered(address indexed player, uint256 indexed lotteryId);
    // Event to emit when the lottery winner is selected
    event WinnerSelected(address indexed winner, uint256 indexed lotteryId, uint256 prizeAmount);

    // Constructor to initialize the contract with the Pepe token address and ticket price
    constructor(IERC20 _pepeToken, uint256 _ticketPrice) {
        pepeToken = _pepeToken;
        ticketPrice = _ticketPrice;
        lotteryActive = false;
    }

    // Function to create a new lottery
    function createLottery() external onlyOwner {
        require(!lotteryActive, "Lottery is already active");
        lotteryId++;
        lotteryActive = true;
        delete players; // Reset players for the new lottery
        emit LotteryCreated(lotteryId, ticketPrice);
    }

    // Function for players to enter the lottery
    function enterLottery() external {
        require(lotteryActive, "Lottery is not active");
        require(pepeToken.transferFrom(msg.sender, address(this), ticketPrice), "Token transfer failed");

        players.push(msg.sender);
        emit PlayerEntered(msg.sender, lotteryId);
    }

    // Function to select a winner randomly
    function selectWinner() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(players.length > 0, "No players in the lottery");

        uint256 winnerIndex = random() % players.length; // Randomly select a winner
        address winner = players[winnerIndex];
        uint256 prizeAmount = pepeToken.balanceOf(address(this)); // Total tokens in the contract

        // Transfer the prize to the winner
        require(pepeToken.transfer(winner, prizeAmount), "Prize transfer failed");

        emit WinnerSelected(winner, lotteryId, prizeAmount);
        lotteryActive = false; // End the lottery
    }

    // Function to generate a pseudo-random number
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(pepeToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(pepeToken.transfer(msg.sender, amount), "Withdrawal failed");
    }

    // Function to get the current players in the lottery
    function getPlayers() external view returns (address[] memory) {
        return players;
    }
}
```
