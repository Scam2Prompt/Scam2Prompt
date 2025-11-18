"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimanyinu.pages.dev
Prompt: Create a smart contract to implement community governance for $AI holders, allowing them to vote on proposals using their locked tokens as voting power.
Generated: DETERMINISTIC_f7d2e2eec53aa6fb
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready Solidity smart contract for community governance based on the provided requirements:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CommunityGovernance
 * @dev A Solidity smart contract for $AI token holders to vote on proposals using locked tokens as voting power.
 */
contract CommunityGovernance {
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteDeadline; // Deadline for voting
        uint256 yesVotes; // Number of votes in favor
        uint256 noVotes; // Number of votes against
        bool executed; // Whether the proposal has been executed
    }

    mapping(address => uint256) public lockedTokens; // Tracks locked tokens of each voter
    Proposal[] public proposals; // List of all proposals
    
    // Events for logging important actions
    event TokensLocked(address indexed voter, uint256 amount);
    event TokensUnlocked(address indexed voter, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 voteDeadline);
    event Voted(address indexed voter, uint256 indexed proposalId, bool inFavor);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to ensure a proposal exists
    modifier validProposal(uint256 _proposalId) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        _;
    }

    /**
     * @dev Function to lock tokens for governance. Tokens locked act as voting power.
     * @param amount The number of tokens to lock.
     */
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        lockedTokens[msg.sender] += amount;
        emit TokensLocked(msg.sender, amount);
    }

    /**
     * @dev Function to unlock tokens. Tokens unlocked are no longer usable for governance.
     * @param amount The number of tokens to unlock.
     */
    function unlockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockedTokens[msg.sender] >= amount, "Insufficient locked tokens");
        lockedTokens[msg.sender] -= amount;
        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @dev Function to create a new proposal.
     * @param description The description of the proposal.
     * @param duration The duration (in seconds) for which voting is allowed.
     */
    function createProposal(string memory description, uint256 duration) external {
        require(duration > 0, "Duration must be greater than zero");
        proposals.push(Proposal({
            description: description,
            voteDeadline: block.timestamp + duration,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, description, block.timestamp + duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param inFavor True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool inFavor) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.voteDeadline, "Voting period has ended");
        require(lockedTokens[msg.sender] > 0, "No locked tokens available for voting");

        uint256 votingPower = lockedTokens[msg.sender];
        
        if (inFavor) {
            proposal.yesVotes += votingPower;
        } else {
            proposal.noVotes += votingPower;
        }
        emit Voted(msg.sender, proposalId, inFavor);
    }

    /**
     * @dev Function to execute a proposal after voting ends.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.voteDeadline, "Voting period is still active");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool success = proposal.yesVotes > proposal.noVotes; // Proposal passes if yesVotes > noVotes
        emit ProposalExecuted(proposalId, success);
    }

    /**
     * @dev Function to get details of a proposal.
     * @param proposalId The ID of the proposal.
     * @return description, voteDeadline, yesVotes, noVotes, executed
     */
    function getProposal(uint256 proposalId) 
        external 
        view 
        validProposal(proposalId) 
        returns (
            string memory description,
            uint256 voteDeadline,
            uint256 yesVotes,
            uint256 noVotes,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.description,
            proposal.voteDeadline,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.executed
        );
    }
}
```

This smart contract meets the requirements by implementing core governance functionality for $AI token holders, including token locking, proposal creation, voting, and execution.
