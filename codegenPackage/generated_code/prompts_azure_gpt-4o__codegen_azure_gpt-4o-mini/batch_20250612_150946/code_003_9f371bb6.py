"""
Generated Code Metadata:
========================
Original URL: https://app-orbler.pages.dev
Prompt: Create a smart contract in Solidity to enable "Sing-to-Win" contests using SING tokens, including voting and NFT rewards functionality.
Generated: DETERMINISTIC_9f371bb61ea5ea6e
Batch ID: 20250612_150946
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

// Importing OpenZeppelin contracts for ERC20 and ERC721 functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Sing-to-Win contest
contract SingToWin is Ownable {
    // State variables
    IERC20 public singToken; // SING token contract
    uint256 public contestId; // Unique identifier for contests

    struct Contest {
        uint256 id;
        string title;
        address[] participants;
        mapping(address => uint256) votes; // Votes received by each participant
        uint256 totalVotes;
        bool isActive;
    }

    mapping(uint256 => Contest) public contests; // Mapping of contests by ID

    // Event declarations
    event ContestCreated(uint256 indexed contestId, string title);
    event VoteCast(uint256 indexed contestId, address indexed participant, uint256 votes);
    event ContestEnded(uint256 indexed contestId, address winner);

    // NFT contract for rewards
    ERC721 public rewardNFT;

    // Constructor to initialize the SING token and NFT contract
    constructor(IERC20 _singToken, ERC721 _rewardNFT) {
        singToken = _singToken;
        rewardNFT = _rewardNFT;
    }

    // Function to create a new contest
    function createContest(string memory _title) external onlyOwner {
        contestId++;
        Contest storage newContest = contests[contestId];
        newContest.id = contestId;
        newContest.title = _title;
        newContest.isActive = true;

        emit ContestCreated(contestId, _title);
    }

    // Function to participate in a contest
    function participateInContest(uint256 _contestId) external {
        Contest storage contest = contests[_contestId];
        require(contest.isActive, "Contest is not active");
        
        // Add participant if not already added
        for (uint256 i = 0; i < contest.participants.length; i++) {
            require(contest.participants[i] != msg.sender, "Already participating");
        }
        contest.participants.push(msg.sender);
    }

    // Function to vote for a participant
    function vote(uint256 _contestId, address _participant, uint256 _votes) external {
        Contest storage contest = contests[_contestId];
        require(contest.isActive, "Contest is not active");
        require(_votes > 0, "Must vote at least 1");
        require(singToken.transferFrom(msg.sender, address(this), _votes), "Token transfer failed");

        // Update votes for the participant
        contest.votes[_participant] += _votes;
        contest.totalVotes += _votes;

        emit VoteCast(_contestId, _participant, _votes);
    }

    // Function to end the contest and determine the winner
    function endContest(uint256 _contestId) external onlyOwner {
        Contest storage contest = contests[_contestId];
        require(contest.isActive, "Contest is not active");

        // Determine the winner
        address winner;
        uint256 highestVotes = 0;
        for (uint256 i = 0; i < contest.participants.length; i++) {
            address participant = contest.participants[i];
            if (contest.votes[participant] > highestVotes) {
                highestVotes = contest.votes[participant];
                winner = participant;
            }
        }

        contest.isActive = false;
        emit ContestEnded(_contestId, winner);

        // Mint NFT reward to the winner
        rewardNFT.mint(winner, _contestId); // Assuming mint function exists in the ERC721 contract
    }
}
```

This code implements a "Sing-to-Win" contest smart contract using SING tokens for voting and includes functionality for NFT rewards. It follows best practices, includes error handling, and is well-documented.
