"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Develop a smart contract in Solidity that enables users to participate in meme-making contests using METAL tokens as entry fees.
Generated: DETERMINISTIC_9b949cda911e2a5e
Batch ID: 20250612_153648
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

// Importing the ERC20 interface for METAL token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for Meme Contest
contract MemeContest {
    // State variables
    IERC20 public metalToken; // METAL token contract
    address public owner; // Owner of the contract
    uint256 public entryFee; // Entry fee in METAL tokens
    Contest[] public contests; // Array to store contests

    // Struct to represent a contest
    struct Contest {
        uint256 id; // Contest ID
        string description; // Description of the contest
        address[] participants; // List of participants
        bool isActive; // Status of the contest
    }

    // Event emitted when a new contest is created
    event ContestCreated(uint256 indexed contestId, string description);
    // Event emitted when a user enters a contest
    event ParticipantEntered(uint256 indexed contestId, address participant);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _metalToken, uint256 _entryFee) {
        metalToken = _metalToken;
        entryFee = _entryFee;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to create a new contest
    function createContest(string memory _description) external onlyOwner {
        uint256 contestId = contests.length; // Get the current contest ID
        contests.push(Contest(contestId, _description, new address[](0), true)); // Create a new contest
        emit ContestCreated(contestId, _description); // Emit event
    }

    // Function for users to enter a contest
    function enterContest(uint256 _contestId) external {
        // Validate contest existence and status
        require(_contestId < contests.length, "Contest does not exist");
        require(contests[_contestId].isActive, "Contest is not active");

        // Transfer entry fee from participant to the contract
        require(metalToken.transferFrom(msg.sender, address(this), entryFee), "Transfer failed");

        // Add participant to the contest
        contests[_contestId].participants.push(msg.sender);
        emit ParticipantEntered(_contestId, msg.sender); // Emit event
    }

    // Function to end a contest
    function endContest(uint256 _contestId) external onlyOwner {
        require(_contestId < contests.length, "Contest does not exist");
        contests[_contestId].isActive = false; // Mark contest as inactive
    }

    // Function to withdraw METAL tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(metalToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(metalToken.transfer(owner, amount), "Transfer failed");
    }

    // Function to get contest details
    function getContest(uint256 _contestId) external view returns (Contest memory) {
        require(_contestId < contests.length, "Contest does not exist");
        return contests[_contestId]; // Return contest details
    }

    // Function to get the number of contests
    function getContestCount() external view returns (uint256) {
        return contests.length; // Return the total number of contests
    }
}
```
