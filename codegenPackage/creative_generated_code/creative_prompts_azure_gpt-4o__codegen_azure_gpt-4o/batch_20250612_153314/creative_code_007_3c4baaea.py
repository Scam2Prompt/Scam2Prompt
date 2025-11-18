"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atocha.io
Prompt: Write a smart contract for the Atocha Protocol that validates puzzle solutions and automatically distributes rewards to the solver.
Generated: DETERMINISTIC_3c4baaeac7c11767
Batch ID: 20250612_153314
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
 * @title Atocha Protocol Puzzle Validator
 * @dev This smart contract validates puzzle solutions and distributes rewards to solvers.
 */
contract AtochaPuzzleValidator {

    // Owner of the contract
    address public owner;

    // Puzzle structure
    struct Puzzle {
        bytes32 solutionHash; // Hashed solution for validation
        uint256 reward;       // Reward associated with the puzzle
        bool isSolved;        // Status of the puzzle
    }

    // Mapping of puzzles by their unique ID
    mapping(uint256 => Puzzle) public puzzles;

    // Events
    event PuzzleCreated(uint256 indexed puzzleId, uint256 reward);
    event PuzzleSolved(uint256 indexed puzzleId, address solver, uint256 reward);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor sets the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new puzzle
     * @param puzzleId Unique identifier for the puzzle
     * @param solutionHash Hashed solution (e.g., keccak256(solution))
     * @param reward Reward amount in wei for solving the puzzle
     */
    function createPuzzle(uint256 puzzleId, bytes32 solutionHash, uint256 reward) external payable onlyOwner {
        require(puzzles[puzzleId].solutionHash == 0, "Puzzle ID already exists");
        require(msg.value == reward, "Incorrect reward funding");

        puzzles[puzzleId] = Puzzle({
            solutionHash: solutionHash,
            reward: reward,
            isSolved: false
        });

        emit PuzzleCreated(puzzleId, reward);
    }

    /**
     * @dev Solve a puzzle by providing the correct solution
     * @param puzzleId ID of the puzzle to solve
     * @param solution Proposed solution to the puzzle
     */
    function solvePuzzle(uint256 puzzleId, string memory solution) external {
        Puzzle storage puzzle = puzzles[puzzleId];

        require(puzzle.solutionHash != 0, "Puzzle does not exist");
        require(!puzzle.isSolved, "Puzzle already solved");
        require(keccak256(abi.encodePacked(solution)) == puzzle.solutionHash, "Incorrect solution");

        puzzle.isSolved = true;

        uint256 reward = puzzle.reward;
        puzzle.reward = 0; // Reset reward to prevent re-entrancy attacks

        // Transfer reward to the solver
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit PuzzleSolved(puzzleId, msg.sender, reward);
    }

    /**
     * @dev Fallback function to accept direct Ether transfers
     */
    receive() external payable {}

    /**
     * @dev Withdraw remaining balance from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Get contract balance
     * @return Balance in wei
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
