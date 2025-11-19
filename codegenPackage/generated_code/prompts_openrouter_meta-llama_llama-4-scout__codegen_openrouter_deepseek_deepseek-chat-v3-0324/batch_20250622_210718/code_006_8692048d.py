"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: "Propose a puzzle game idea for Atocha protocol, incorporating NFTs and a treasure hunt mechanism, similar to NEAR2ATO Treasure Hunt."
Generated: DETERMINISTIC_8692048dd058397d
Batch ID: 20250622_210718
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract AtochaTreasureHunt is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Puzzle {
        bytes32 merkleRoot;
        string ipfsHash;
        bool isSolved;
        uint256 reward;
    }

    mapping(uint256 => Puzzle) public puzzles;
    mapping(address => mapping(uint256 => bool)) public hasSolved;
    mapping(address => uint256) public playerRewards;

    event PuzzleCreated(uint256 indexed puzzleId, string ipfsHash);
    event PuzzleSolved(address indexed player, uint256 indexed puzzleId, uint256 reward);
    event RewardClaimed(address indexed player, uint256 amount);

    constructor() ERC721("AtochaTreasureHunt", "ATH") {}

    /**
     * @dev Create a new puzzle with Merkle root for verification
     * @param merkleRoot Root of Merkle tree containing valid solutions
     * @param ipfsHash IPFS hash of puzzle content
     * @param reward Reward amount for solving this puzzle
     */
    function createPuzzle(bytes32 merkleRoot, string memory ipfsHash, uint256 reward) external onlyOwner {
        uint256 puzzleId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        puzzles[puzzleId] = Puzzle({
            merkleRoot: merkleRoot,
            ipfsHash: ipfsHash,
            isSolved: false,
            reward: reward
        });

        emit PuzzleCreated(puzzleId, ipfsHash);
    }

    /**
     * @dev Solve a puzzle by providing proof of solution
     * @param puzzleId ID of the puzzle to solve
     * @param solution Solution to verify
     * @param proof Merkle proof for the solution
     */
    function solvePuzzle(uint256 puzzleId, string memory solution, bytes32[] memory proof) external {
        require(puzzleId < _tokenIdCounter.current(), "Invalid puzzle ID");
        require(!hasSolved[msg.sender][puzzleId], "Already solved this puzzle");
        require(!puzzles[puzzleId].isSolved, "Puzzle already solved by someone");

        bytes32 leaf = keccak256(abi.encodePacked(solution));
        bool isValidSolution = MerkleProof.verify(proof, puzzles[puzzleId].merkleRoot, leaf);

        require(isValidSolution, "Invalid solution");

        puzzles[puzzleId].isSolved = true;
        hasSolved[msg.sender][puzzleId] = true;
        playerRewards[msg.sender] += puzzles[puzzleId].reward;

        _mint(msg.sender, puzzleId);
        emit PuzzleSolved(msg.sender, puzzleId, puzzles[puzzleId].reward);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 reward = playerRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        playerRewards[msg.sender] = 0;
        // In production, replace with actual token transfer
        // payable(msg.sender).transfer(reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get puzzle details
     * @param puzzleId ID of the puzzle
     * @return Puzzle details (merkleRoot, ipfsHash, isSolved, reward)
     */
    function getPuzzle(uint256 puzzleId) external view returns (bytes32, string memory, bool, uint256) {
        require(puzzleId < _tokenIdCounter.current(), "Invalid puzzle ID");
        Puzzle memory puzzle = puzzles[puzzleId];
        return (puzzle.merkleRoot, puzzle.ipfsHash, puzzle.isSolved, puzzle.reward);
    }

    /**
     * @dev Check if player has solved a puzzle
     * @param player Address to check
     * @param puzzleId ID of the puzzle
     * @return True if player has solved the puzzle
     */
    function hasPlayerSolved(address player, uint256 puzzleId) external view returns (bool) {
        return hasSolved[player][puzzleId];
    }

    /**
     * @dev Get player's total unclaimed rewards
     * @param player Address to check
     * @return Total unclaimed rewards
     */
    function getPlayerRewards(address player) external view returns (uint256) {
        return playerRewards[player];
    }
}
```
