"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Create a governance smart contract in Solidity that allows ORB token holders to vote on proposals within the Zealy platform.
Generated: DETERMINISTIC_7f0d3a3fde25acb2
Batch ID: 20250612_150858
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
 * @title Governance Contract for ORB Token Holders
 * @author [Your Name]
 * @notice This contract allows ORB token holders to vote on proposals within the Zealy platform.
 */
contract Governance {
    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId, uint8 vote);

    // Struct representing a proposal
    struct Proposal {
        string description; // Proposal description
        uint256 votesFor;   // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline;   // Voting deadline (timestamp)
        bool isFinalized;   // Whether the proposal has been finalized
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to Proposal structs
    uint256 public proposalCount;                  // Total number of proposals

    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks whether an address has voted on a proposal

    IERC20 public immutable orbToken;             // Reference to the ORB token contract
    address public owner;                         // Contract owner

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _orbToken Address of the ORB token contract.
     */
    constructor(IERC20 _orbToken) {
        orbToken = _orbToken;
        owner = msg.sender;
    }

    /**
     * @dev Creates a new proposal for voting.
     * @param _description Description of the proposal.
     * @param _duration Duration of the voting period in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            isFinalized: false
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId ID of the proposal.
     * @param _vote Vote option (1 = For, 2 = Against).
     */
    function vote(uint256 _proposalId, uint8 _vote) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(_vote == 1 || _vote == 2, "Invalid vote option");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.deadline, "Voting period has ended");

        uint256 balance = orbToken.balanceOf(msg.sender);
        require(balance > 0, "Must hold ORB tokens to vote");

        if (_vote == 1) {
            proposal.votesFor += balance;
        } else if (_vote == 2) {
            proposal.votesAgainst += balance;
        }
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId, _vote);
    }

    /**
     * @dev Finalizes a proposal and determines the outcome.
     * @param _proposalId ID of the proposal.
     * @return outcome Outcome of the proposal (true = passed, false = rejected).
     */
    function finalizeProposal(uint256 _proposalId) external onlyOwner returns (bool outcome) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");

        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.deadline, "Voting period is still ongoing");
        require(!proposal.isFinalized, "Proposal is already finalized");

        proposal.isFinalized = true;
        outcome = proposal.votesFor > proposal.votesAgainst;
        return outcome;
    }

    /**
     * @dev Returns details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return Proposal struct.
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId];
    }
}

// Minimal IERC20 interface for checking token balance
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
