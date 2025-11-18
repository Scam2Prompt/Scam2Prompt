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

/// @title Atocha Protocol Smart Contract
/// @author Your Name
/// @notice This contract validates puzzle solutions and distributes rewards to the solvers
/// @dev The contract is designed to be efficient and secure

contract AtochaProtocol {
    // State variables
    struct Puzzle {
        bytes32 solutionHash; // Hash of the correct solution
        address solver;       // Address of the current solver
        bool solved;          // Indicates if the puzzle has been solved
    }

    mapping(uint256 => Puzzle) public puzzles; // Mapping of puzzle ID to Puzzle struct
    uint256 public puzzleCount;                // Total number of puzzles created
    uint256 public rewardAmount;               // Amount of reward for solving a puzzle

    // Events
    event PuzzleCreated(uint256 indexed puzzleId, bytes32 solutionHash);
    event PuzzleSolved(uint256 indexed puzzleId, address indexed solver);

    // Modifier to check if the puzzle is already solved
    modifier notSolved(uint256 puzzleId) {
        require(!puzzles[puzzleId].solved, "Puzzle already solved");
        _;
    }

    // Constructor to initialize the reward amount
    constructor(uint256 _rewardAmount) {
        rewardAmount = _rewardAmount;
    }

    /// @notice Create a new puzzle
    /// @param solution The solution to the puzzle
    /// @return puzzleId The ID of the created puzzle
    function createPuzzle(bytes32 solution) external returns (uint256 puzzleId) {
        puzzleId = puzzleCount++;
        puzzles[puzzleId] = Puzzle({
            solutionHash: solution,
            solver: address(0),
            solved: false
        });
        
        emit PuzzleCreated(puzzleId, solution);
    }

    /// @notice Submit a solution for a puzzle
    /// @param puzzleId The ID of the puzzle
    /// @param solution The proposed solution
    function submitSolution(uint256 puzzleId, bytes32 solution) external notSolved(puzzleId) {
        // Validate the solution
        require(solution == puzzles[puzzleId].solutionHash, "Invalid solution");

        // Mark the puzzle as solved and assign the solver
        puzzles[puzzleId].solved = true;
        puzzles[puzzleId].solver = msg.sender;

        // Transfer the reward to the solver
        (bool sent, ) = msg.sender.call{value: rewardAmount}("");
        require(sent, "Failed to send reward");

        emit PuzzleSolved(puzzleId, msg.sender);
    }

    /// @notice Function to receive Ether. Required for reward distribution.
    receive() external payable {}

    /// @notice Fallback function to reject any Ether sent directly to the contract
    fallback() external {
        revert("Direct transfers not allowed");
    }

    /// @notice Get the details of a puzzle
    /// @param puzzleId The ID of the puzzle
    /// @return solutionHash The hash of the solution
    /// @return solver The address of the solver
    /// @return solved Indicates if the puzzle has been solved
    function getPuzzle(uint256 puzzleId) external view returns (bytes32 solutionHash, address solver, bool solved) {
        Puzzle memory puzzle = puzzles[puzzleId];
        return (puzzle.solutionHash, puzzle.solver, puzzle.solved);
    }
}
```
