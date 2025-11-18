"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-app.vercel.app
Prompt: Write a smart contract in Solidity for a gambling dApp on TON Blockchain, using examples from TON App's gambling category.
Generated: DETERMINISTIC_f061da811bda5409
Batch ID: 20250612_153915
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
 * @title GamblingDApp
 * @dev A smart contract for a decentralized gambling application on the TON Blockchain.
 * Players can participate in games by depositing funds, and a random winner is selected.
 */
contract GamblingDApp {
    // Address of the contract owner
    address public owner;

    // List of players participating in the current game
    address[] public players;

    // Minimum entry fee to participate in the game
    uint256 public entryFee;

    // Event for when a player joins the game
    event PlayerJoined(address indexed player);

    // Event for when a winner is selected
    event WinnerSelected(address indexed winner, uint256 amountWon);

    /**
     * @dev Constructor to initialize the contract with an owner and entry fee.
     * @param _entryFee The minimum amount required to join the game.
     */
    constructor(uint256 _entryFee) {
        require(_entryFee > 0, "Entry fee must be greater than 0");
        owner = msg.sender;
        entryFee = _entryFee;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Function for players to join the game by sending the entry fee.
     * Emits a PlayerJoined event.
     */
    function joinGame() external payable {
        require(msg.value == entryFee, "Incorrect entry fee sent");
        players.push(msg.sender); // Add the player to the list
        emit PlayerJoined(msg.sender);
    }

    /**
     * @dev Function to randomly select a winner and transfer the funds.
     * Can only be called by the owner.
     * Emits a WinnerSelected event.
     */
    function selectWinner() external onlyOwner {
        require(players.length > 0, "No players in the game");

        // Generate a random index
        uint256 randomIndex = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, players))
        ) % players.length;

        // Select the winner
        address winner = players[randomIndex];
        uint256 prize = address(this).balance;

        // Transfer the prize to the winner
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer to winner failed");

        // Emit the WinnerSelected event
        emit WinnerSelected(winner, prize);

        // Reset the players array
        delete players;
    }

    /**
     * @dev Function to withdraw funds from the contract (only for owner).
     * This is a safety mechanism to prevent funds from being locked forever.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to check the number of players in the game.
     * @return The number of players currently in the game.
     */
    function getPlayersCount() external view returns (uint256) {
        return players.length;
    }

    /**
     * @dev Fallback function to prevent accidental deposits.
     */
    fallback() external payable {
        revert("Direct deposits not allowed");
    }

    /**
     * @dev Receive function to prevent accidental deposits.
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```
