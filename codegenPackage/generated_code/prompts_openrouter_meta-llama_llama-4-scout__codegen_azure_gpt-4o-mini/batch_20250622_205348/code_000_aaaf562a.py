"""
Generated Code Metadata:
========================
Original URL: https://dueleth.com
Prompt: Write a smart contract in Solidity for a simple Ethereum-based game.
Generated: DETERMINISTIC_aaaf562a56de2480
Batch ID: 20250622_205348
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

/// @title SimpleGame
/// @notice A simple Ethereum-based game where players can join and play
contract SimpleGame {
    // State variables
    address public owner;
    uint256 public playerCount;
    mapping(address => bool) public players;

    // Events
    event PlayerJoined(address indexed player);
    event GameWon(address indexed winner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier playerExists() {
        require(players[msg.sender], "Player does not exist");
        _;
    }

    /// @notice Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
        playerCount = 0;
    }

    /// @notice Function for players to join the game
    function joinGame() external {
        require(!players[msg.sender], "Player already joined");
        
        // Add player to the mapping
        players[msg.sender] = true;
        playerCount++;

        emit PlayerJoined(msg.sender);
    }

    /// @notice Function to simulate a game round
    /// @dev Only the owner can call this function
    function playGame() external onlyOwner {
        require(playerCount > 0, "No players in the game");

        // Randomly select a winner (for simplicity, using block.timestamp)
        address winner = selectRandomWinner();
        
        // Emit event for the winner
        emit GameWon(winner);
        
        // Reset the game
        resetGame();
    }

    /// @notice Function to select a random winner from the players
    /// @return address of the selected winner
    function selectRandomWinner() internal view returns (address) {
        uint256 randomIndex = uint256(block.timestamp) % playerCount;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < 256; i++) {
            if (players[address(i)]) {
                if (currentIndex == randomIndex) {
                    return address(i);
                }
                currentIndex++;
            }
        }
        revert("No winner found");
    }

    /// @notice Function to reset the game state
    function resetGame() internal {
        for (uint256 i = 0; i < 256; i++) {
            if (players[address(i)]) {
                delete players[address(i)];
            }
        }
        playerCount = 0;
    }

    /// @notice Function to withdraw contract balance (if any)
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}
}
```
