"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Generate a governance voting smart contract for an EVM-compatible blockchain that supports Singularity Finance's voting process, including vote periods and result announcements.
Generated: DETERMINISTIC_9a2441c8f4138cd4
Batch ID: 20250612_145831
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

// Importing OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GovernanceVoting is Ownable {
    using Counters for Counters.Counter;

    // Enum for the voting status
    enum VoteStatus { Ongoing, Ended }

    // Structure to hold vote details
    struct Vote {
        uint256 id;
        string proposal;
        uint256 startTime;
        uint256 endTime;
        VoteStatus status;
        mapping(address => bool) hasVoted;
        mapping(bool => uint256) votes; // true for 'yes', false for 'no'
    }

    // Mapping of vote ID to Vote details
    mapping(uint256 => Vote) public votesMapping;
    Counters.Counter private voteCounter;

    // Event to announce vote creation
    event VoteCreated(uint256 indexed voteId, string proposal, uint256 startTime, uint256 endTime);
    // Event to announce vote participation
    event VoteCast(uint256 indexed voteId, address voter, bool vote);
    // Event to announce vote results
    event VoteResult(uint256 indexed voteId, uint256 yesVotes, uint256 noVotes);

    // Modifier to ensure the vote is ongoing
    modifier ongoingVote(uint256 voteId) {
        require(votesMapping[voteId].status == VoteStatus.Ongoing, "Vote is not ongoing.");
        _;
    }

    // Function to create a new vote
    function createVote(string memory proposal, uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be greater than 0.");

        // Incrementing vote ID and setting up the new vote
        uint256 newVoteId = voteCounter.current();
        voteCounter.increment();
        Vote storage newVote = votesMapping[newVoteId];

        newVote.id = newVoteId;
        newVote.proposal = proposal;
        newVote.startTime = block.timestamp;
        newVote.endTime = block.timestamp + duration;
        newVote.status = VoteStatus.Ongoing;

        emit VoteCreated(newVoteId, proposal, newVote.startTime, newVote.endTime);
    }

    // Function to cast a vote
    function castVote(uint256 voteId, bool vote) external ongoingVote(voteId) {
        Vote storage voteDetail = votesMapping[voteId];

        require(!voteDetail.hasVoted[msg.sender], "You have already voted.");

        // Marking the voter as having voted and recording the vote
        voteDetail.hasVoted[msg.sender] = true;
        voteDetail.votes[vote]++;

        emit VoteCast(voteId, msg.sender, vote);
    }

    // Function to end voting and announce results
    function endVote(uint256 voteId) external onlyOwner ongoingVote(voteId) {
        Vote storage voteDetail = votesMapping[voteId];
        require(block.timestamp >= voteDetail.endTime, "Voting period is not over yet.");

        // Set the vote status to ended
        voteDetail.status = VoteStatus.Ended;

        // Emit results
        emit VoteResult(voteId, voteDetail.votes[true], voteDetail.votes[false]);
    }

    // Function to get vote details
    function getVoteDetails(uint256 voteId) external view returns (
        uint256 id,
        string memory proposal,
        uint256 startTime,
        uint256 endTime,
        VoteStatus status,
        uint256 yesVotes,
        uint256 noVotes
    ) {
        Vote storage voteDetail = votesMapping[voteId];
        return (
            voteDetail.id,
            voteDetail.proposal,
            voteDetail.startTime,
            voteDetail.endTime,
            voteDetail.status,
            voteDetail.votes[true],
            voteDetail.votes[false]
        );
    }
}
```
