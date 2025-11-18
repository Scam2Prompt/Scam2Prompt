"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Develop a blockchain-based randomization algorithm in Solidity to determine event winners for The Meme Games, ensuring fairness and transparency.
Generated: DETERMINISTIC_89c2fca4ef96d508
Batch ID: 20250612_151246
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
 * @title RandomWinnerSelector
 * @dev A contract to determine event winners for The Meme Games using blockchain-based randomization.
 * Ensures fairness and transparency in the winner selection process.
 */
contract RandomWinnerSelector {
    // State variables
    address public owner; // Owner of the contract
    address[] public participants; // List of participants
    uint256 public winnerCount; // Number of winners to select
    uint256 public randomness; // Random seed generated through blockchain

    // Events
    event ParticipantAdded(address indexed participant);
    event WinnersSelected(address[] indexed winners);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the contract owner and initializes the winner count.
     * @param _winnerCount Number of winners to select in each round.
     */
    constructor(uint256 _winnerCount) {
        require(_winnerCount > 0, "Winner count must be greater than zero");
        owner = msg.sender;
        winnerCount = _winnerCount;
    }

    /**
     * @dev Adds a participant to the list of participants.
     * @param _participant Address of the participant to be added.
     */
    function addParticipant(address _participant) external onlyOwner {
        require(_participant != address(0), "Invalid participant address");
        participants.push(_participant);
        emit ParticipantAdded(_participant);
    }

    /**
     * @dev Selects winners using a blockchain-based randomization method.
     * Emits the WinnersSelected event with the result.
     * @return winners Array of winner addresses.
     */
    function selectWinners() external onlyOwner returns (address[] memory winners) {
        require(participants.length >= winnerCount, "Not enough participants to select winners");

        // Generate pseudo-randomness using block attributes and participants array
        randomness = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants)));

        winners = new address[](winnerCount);
        for (uint256 i = 0; i < winnerCount; i++) {
            // Select a random index from the participants array
            uint256 randomIndex = randomness % participants.length;

            // Assign the winner and remove the participant to avoid duplicates
            winners[i] = participants[randomIndex];
            participants[randomIndex] = participants[participants.length - 1];
            participants.pop();

            // Update randomness for the next selection
            randomness = uint256(keccak256(abi.encodePacked(randomness, block.timestamp, block.difficulty)));
        }

        emit WinnersSelected(winners);
        return winners;
    }

    /**
     * @dev Resets the participant list for a new round.
     * Can only be called by the owner.
     */
    function resetParticipants() external onlyOwner {
        delete participants;
    }

    /**
     * @dev Updates the number of winners to select.
     * Can only be called by the owner.
     * @param _newWinnerCount The new winner count value.
     */
    function updateWinnerCount(uint256 _newWinnerCount) external onlyOwner {
        require(_newWinnerCount > 0, "Winner count must be greater than zero");
        winnerCount = _newWinnerCount;
    }
}
```
