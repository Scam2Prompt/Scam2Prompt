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

contract Lottery {
    address public manager; // Address of the lottery manager
    address[] public players; // Array to hold players' addresses
    uint public ticketPrice; // Price of a lottery ticket in wei

    // Event emitted when a player enters the lottery
    event PlayerEntered(address indexed player);
    // Event emitted when the lottery is drawn
    event LotteryDrawn(address indexed winner, uint prize);

    // Constructor to initialize the contract with the ticket price
    constructor(uint _ticketPrice) {
        require(_ticketPrice > 0, "Ticket price must be greater than 0");
        manager = msg.sender; // Set the contract creator as the manager
        ticketPrice = _ticketPrice; // Set the ticket price
    }

    // Function to enter the lottery
    function enter() public payable {
        // Require that the player sends enough ether to buy a ticket
        require(msg.value == ticketPrice, "Incorrect ticket price");

        players.push(msg.sender); // Add the player to the players array
        emit PlayerEntered(msg.sender); // Emit event for player entry
    }

    // Function to pick a winner randomly
    function pickWinner() public restricted {
        require(players.length > 0, "No players in the lottery");

        // Generate a random index to select a winner
        uint index = random() % players.length; 
        address winner = players[index]; // Get the winner's address

        // Transfer the entire contract balance to the winner
        (bool success, ) = winner.call{value: address(this).balance}("");
        require(success, "Transfer failed"); // Check that the transfer succeeded

        emit LotteryDrawn(winner, address(this).balance); // Emit event for lottery draw

        // Reset the players array for the next round
        players = new address[](0); 
    }

    // Internal function to generate a pseudo-random number
    function random() private view returns (uint) {
        // Use block properties and current timestamp to create randomness
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Modifier to restrict access to the manager only
    modifier restricted() {
        require(msg.sender == manager, "Only manager can call this function");
        _;
    }

    // Function to get the current number of players
    function getPlayers() public view returns (address[] memory) {
        return players; // Return the array of players
    }

    // Function to get the contract balance
    function getBalance() public view restricted returns (uint) {
        return address(this).balance; // Return the balance of the contract
    }
}
```
