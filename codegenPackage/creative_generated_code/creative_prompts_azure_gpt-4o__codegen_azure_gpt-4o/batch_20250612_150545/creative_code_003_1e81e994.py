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

// Interface for the $Jelly ERC20 token
interface IJellyToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Jellotto {
    // Address of the $Jelly ERC20 token
    IJellyToken public jellyToken;

    // Lottery parameters
    uint256 public ticketPrice; // Price of a single ticket in $Jelly tokens
    uint256 public drawInterval; // Time interval between lottery draws
    address public admin; // Administrator of the lottery

    // State variables
    uint256 public lastDrawTime; // Timestamp of the last lottery draw
    address[] public players; // List of players in the current lottery
    mapping(address => uint256) public tickets; // Tracks tickets purchased by players

    // Events
    event TicketPurchased(address indexed player, uint256 amount);
    event WinnerDeclared(address indexed winner, uint256 prize);
    event FundsWithdrawn(address indexed admin, uint256 amount);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier drawIntervalPassed() {
        require(block.timestamp >= lastDrawTime + drawInterval, "Draw interval has not passed");
        _;
    }

    constructor(address _jellyTokenAddress, uint256 _ticketPrice, uint256 _drawInterval) {
        require(_jellyTokenAddress != address(0), "Invalid token address");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_drawInterval > 0, "Draw interval must be greater than zero");

        jellyToken = IJellyToken(_jellyTokenAddress);
        ticketPrice = _ticketPrice;
        drawInterval = _drawInterval;
        admin = msg.sender;
        lastDrawTime = block.timestamp;
    }

    // Function to buy lottery tickets
    function buyTickets(uint256 amount) external {
        require(amount > 0, "Ticket amount must be greater than zero");
        uint256 cost = ticketPrice * amount;
        require(jellyToken.transferFrom(msg.sender, address(this), cost), "Token transfer failed");

        // Add player and ticket information
        if (tickets[msg.sender] == 0) {
            players.push(msg.sender);
        }
        tickets[msg.sender] += amount;

        emit TicketPurchased(msg.sender, amount);
    }

    // Function to draw the lottery winner
    function drawWinner() external onlyAdmin drawIntervalPassed {
        require(players.length > 0, "No players in the lottery");

        // Generate a pseudo-random winner (do not use this for high-stakes lotteries)
        uint256 winnerIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, players))) % players.length;
        address winner = players[winnerIndex];

        // Calculate and transfer the prize
        uint256 prize = jellyToken.balanceOf(address(this));
        require(jellyToken.transfer(winner, prize), "Prize transfer failed");

        emit WinnerDeclared(winner, prize);

        // Reset the lottery
        delete players;
        lastDrawTime = block.timestamp;
    }

    // Function to withdraw excess funds (only admin)
    function withdrawFunds(uint256 amount) external onlyAdmin {
        require(amount > 0, "Amount must be greater than zero");
        require(jellyToken.transfer(admin, amount), "Withdrawal failed");

        emit FundsWithdrawn(admin, amount);
    }

    // View function to get the number of tickets a player owns
    function getPlayerTickets(address player) external view returns (uint256) {
        return tickets[player];
    }

    // View function to get the total number of players
    function getTotalPlayers() external view returns (uint256) {
        return players.length;
    }
}
```
