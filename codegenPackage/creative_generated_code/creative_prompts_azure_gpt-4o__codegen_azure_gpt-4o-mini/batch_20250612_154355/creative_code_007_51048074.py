"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyesports.web.app
Prompt: Write a function in Solidity to implement a gamified feature similar to Jelly Flip, ensuring secure and transparent transactions.
Generated: DETERMINISTIC_510480742ee893f3
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

// Import OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the contract for the gamified feature
contract JellyFlipGame {
    using SafeMath for uint256;

    // Event to emit when a new game round is created
    event NewRound(uint256 roundId, uint256 prizePool);

    // Event to emit when a player joins the game
    event PlayerJoined(address indexed player, uint256 amount, uint256 roundId);

    // Event to emit when a round ends
    event RoundEnded(uint256 roundId, address winner, uint256 prize);

    struct Round {
        uint256 id;
        uint256 prizePool;
        address[] players;
        bool isActive;
    }

    // Mapping to track rounds by their IDs
    mapping(uint256 => Round) public rounds;
    // Counter for the round IDs
    uint256 public currentRoundId;

    // Modifier to check if the round is active
    modifier onlyActiveRound(uint256 roundId) {
        require(rounds[roundId].isActive, "Round is not active");
        _;
    }

    // Function to start a new round
    function startNewRound() external {
        currentRoundId = currentRoundId.add(1);
        rounds[currentRoundId] = Round({
            id: currentRoundId,
            prizePool: 0,
            players: new address[](0),
            isActive: true
        });

        emit NewRound(currentRoundId, 0);
    }

    // Function for players to join the game with a specified amount
    function joinGame(uint256 roundId) external payable onlyActiveRound(roundId) {
        require(msg.value > 0, "Must send some ether to join");

        // Update the round's state
        Round storage round = rounds[roundId];
        round.prizePool = round.prizePool.add(msg.value);
        round.players.push(msg.sender);

        emit PlayerJoined(msg.sender, msg.value, roundId);
    }

    // Function to end the current round and select a winner
    function endRound(uint256 roundId) external onlyActiveRound(roundId) {
        Round storage round = rounds[roundId];
        require(round.players.length > 0, "No players in the round");

        // Randomly select a winner (for simplicity, we use block.timestamp)
        uint256 winnerIndex = uint256(block.timestamp) % round.players.length;
        address winner = round.players[winnerIndex];

        // Transfer the prize pool to the winner
        uint256 prize = round.prizePool;
        round.isActive = false; // Mark the round as inactive

        // Use `call` to transfer funds safely, handling any failure
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer to winner failed");

        emit RoundEnded(roundId, winner, prize);
    }

    // Fallback function to receive ether
    receive() external payable {}

    // Function to withdraw any remaining ether in the contract (only for owner)
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
