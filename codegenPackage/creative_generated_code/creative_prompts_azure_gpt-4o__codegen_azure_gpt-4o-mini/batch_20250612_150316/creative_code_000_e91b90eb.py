"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-protocol.vercel.app
Prompt: Write a smart contract in Solidity for a random winner selection game, similar to the "Random Game" described, and deploy it on the Mumbai Testnet using the Graph Protocol.
Generated: DETERMINISTIC_e91b90ebc1003bbb
Batch ID: 20250612_150316
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RandomWinnerGame is Ownable {
    using SafeMath for uint256;

    // Structure to hold player details
    struct Player {
        address playerAddress;
        uint256 amount;
    }

    Player[] public players; // Array to store all players
    uint256 public totalPlayers; // Total number of players
    uint256 public gameBalance; // Total balance in the game
    uint256 public entryFee; // Entry fee to participate in the game

    // Event emitted when a winner is selected
    event WinnerSelected(address winner, uint256 amount);

    // Constructor to initialize the entry fee
    constructor(uint256 _entryFee) {
        require(_entryFee > 0, "Entry fee must be greater than zero");
        entryFee = _entryFee;
    }

    // Function to allow players to enter the game
    function enterGame() external payable {
        require(msg.value == entryFee, "Incorrect entry fee");
        
        // Add player to the players array
        players.push(Player({
            playerAddress: msg.sender,
            amount: msg.value
        }));
        
        // Update total players and game balance
        totalPlayers++;
        gameBalance = gameBalance.add(msg.value);
    }

    // Function to select a random winner
    function selectRandomWinner() external onlyOwner {
        require(totalPlayers > 0, "No players in the game");

        // Generate a random index within the players array
        uint256 winnerIndex = random() % totalPlayers;

        // Select the winner
        Player memory winner = players[winnerIndex];

        // Transfer the game balance to the winner
        (bool success, ) = winner.playerAddress.call{value: gameBalance}("");
        require(success, "Transfer failed");

        // Emit the winner event
        emit WinnerSelected(winner.playerAddress, gameBalance);

        // Reset the game
        resetGame();
    }

    // Function to reset the game
    function resetGame() internal {
        // Clear the players array
        delete players;
        totalPlayers = 0;
        gameBalance = 0;
    }

    // Function to generate a pseudo-random number (for demo purposes)
    function random() internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw any accidentally sent Ether
    function withdraw() external onlyOwner {
        require(gameBalance > 0, "No funds to withdraw");
        (bool success, ) = msg.sender.call{value: gameBalance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

This smart contract serves as a game where players can enter by paying an entry fee, and a random winner is selected to receive the total game balance. It includes proper error handling, resets the game after a winner is selected, and allows the contract owner to withdraw any excess funds.
