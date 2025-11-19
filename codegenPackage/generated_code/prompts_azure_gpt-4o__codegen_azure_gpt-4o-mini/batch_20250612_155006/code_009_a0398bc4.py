"""
Generated Code Metadata:
========================
Original URL: https://lotto.exchange
Prompt: Write a smart contract in Solidity to integrate a lottery system with Uniswap, similar to Lotto Exchange.
Generated: DETERMINISTIC_a0398bc4a0686853
Batch ID: 20250612_155006
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

// Importing the interface for Uniswap's Router
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Lottery is Ownable {
    // State variables
    address[] public players; // Array to store players' addresses
    uint256 public lotteryId; // Current lottery ID
    uint256 public ticketPrice; // Price of a lottery ticket
    IUniswapV2Router02 public uniswapRouter; // Uniswap router instance
    address public token; // Token used for lottery tickets

    // Event to emit when a new lottery is created
    event LotteryCreated(uint256 lotteryId, uint256 ticketPrice);
    // Event to emit when a player enters the lottery
    event PlayerEntered(address player);
    // Event to emit when the lottery is drawn
    event LotteryDrawn(address winner, uint256 amountWon);

    // Constructor to initialize the contract
    constructor(address _uniswapRouter, address _token, uint256 _ticketPrice) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        token = _token;
        ticketPrice = _ticketPrice;
        lotteryId = 1; // Start with the first lottery
        emit LotteryCreated(lotteryId, ticketPrice);
    }

    // Function to enter the lottery
    function enterLottery() external {
        // Transfer the ticket price from the player to the contract
        require(IERC20(token).transferFrom(msg.sender, address(this), ticketPrice), "Transfer failed");
        
        players.push(msg.sender); // Add player to the players array
        emit PlayerEntered(msg.sender);
    }

    // Function to draw the lottery winner
    function drawLottery() external onlyOwner {
        require(players.length > 0, "No players in the lottery");

        // Generate a random index to select a winner
        uint256 winnerIndex = random() % players.length;
        address winner = players[winnerIndex];

        // Calculate the total prize pool
        uint256 prizePool = IERC20(token).balanceOf(address(this));

        // Transfer the prize to the winner
        require(IERC20(token).transfer(winner, prizePool), "Transfer to winner failed");

        emit LotteryDrawn(winner, prizePool);

        // Reset the lottery for the next round
        players = new address[](0);
        lotteryId++;
        emit LotteryCreated(lotteryId, ticketPrice);
    }

    // Function to generate a pseudo-random number
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        require(IERC20(token).transfer(msg.sender, amount), "Withdraw failed");
    }

    // Function to update the ticket price (only owner)
    function updateTicketPrice(uint256 newPrice) external onlyOwner {
        ticketPrice = newPrice;
    }

    // Function to get the current players in the lottery
    function getPlayers() external view returns (address[] memory) {
        return players;
    }
}
```
