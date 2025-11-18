"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-orbler.pages.dev
Prompt: Create a smart contract in Solidity to enable "Sing-to-Win" contests using SING tokens, including voting and NFT rewards functionality.
Generated: DETERMINISTIC_9f371bb61ea5ea6e
Batch ID: 20250612_150946
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for Sing-to-Win contests
contract SingToWin is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold contest details
    struct Contest {
        string title;
        address creator;
        uint256 endTime;
        mapping(address => uint256) votes; // Votes for each participant
        uint256 totalVotes;
    }

    // Structure for participant details
    struct Participant {
        address participantAddress;
        uint256 voteCount;
    }

    // State variables
    IERC20 public singToken; // SING token interface
    ERC721 public rewardNFT;  // NFT interface
    Counters.Counter private contestIdCounter; // Counter for contests
    mapping(uint256 => Contest) public contests; // Mapping of contests by ID
    
    // Events for logging
    event ContestCreated(uint256 indexed contestId, string title, uint256 endTime);
    event Voted(uint256 indexed contestId, address indexed voter, address participant);
    event ContestEnded(uint256 indexed contestId, address winner);
    
    // Constructor to set the SING token and NFT address
    constructor(address _singToken, address _rewardNFT) {
        singToken = IERC20(_singToken);
        rewardNFT = ERC721(_rewardNFT);
    }
    
    // Function to create a new contest
    function createContest(string memory _title, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero");
        
        contestIdCounter.increment();
        uint256 contestId = contestIdCounter.current();
        
        contests[contestId] = Contest({
            title: _title,
            creator: msg.sender,
            endTime: block.timestamp + _duration,
            totalVotes: 0
        });

        emit ContestCreated(contestId, _title, contests[contestId].endTime);
    }

    // Function to vote for a participant
    function vote(uint256 _contestId, address _participant) external {
        Contest storage contest = contests[_contestId];
        
        require(block.timestamp < contest.endTime, "Voting period has ended");
        require(singToken.balanceOf(msg.sender) >= 1e18, "Insufficient SING tokens to vote");
        require(contest.votes[msg.sender] == 0, "You have already voted");

        // Transfer 1 SING token from voter to the contract
        singToken.transferFrom(msg.sender, address(this), 1e18);

        // Record the vote
        contest.votes[msg.sender] = contest.votes[msg.sender] + 1;
        contest.totalVotes++;

        emit Voted(_contestId, msg.sender, _participant);
    }

    // Function to end contest and distribute rewards
    function endContest(uint256 _contestId) external {
        Contest storage contest = contests[_contestId];
        
        require(block.timestamp >= contest.endTime, "Contest is still ongoing");
        require(msg.sender == contest.creator, "Only the contest creator can end it");

        // Determine winner (for simplicity, we will select the participant that received the most votes)
        address winner;
        uint256 maxVotes = 0;

        for (uint256 i = 0; i < contest.totalVotes; i++) {
            address participant = address(uint160(i)); // Assume participant addresses are stored here
            if (contest.votes[participant] > maxVotes) {
                maxVotes = contest.votes[participant];
                winner = participant;
            }
        }

        // Mint NFT reward for the winner (using an assumed mint function)
        rewardNFT.safeMint(winner);

        emit ContestEnded(_contestId, winner);
        
        // Reset contest
        delete contests[_contestId];
    }
}
```
