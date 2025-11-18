"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorodshansona.ru
Prompt: Create a Solidity contract that utilizes IMX tokens for governance voting, incorporating the token details provided on gorodshansona.ru.
Generated: DETERMINISTIC_7dc53b45a2e47b24
Batch ID: 20250612_154938
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
 * @title GovernanceVoting
 * @dev A contract for governance voting using IMX tokens.
 * Assumes IMX token details are as specified and follows ERC20 standards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GovernanceVoting {
    // Address of the IMX token contract
    IERC20 public immutable imxToken;
    
    // Struct representing a Proposal
    struct Proposal {
        string description;        // Proposal description
        uint256 votesFor;          // Number of 'For' votes
        uint256 votesAgainst;      // Number of 'Against' votes
        uint256 deadline;          // Voting deadline (block timestamp)
    }
    
    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Mapping to store if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool voteFor);

    /**
     * @dev Constructor to initialize the IMX token address.
     * @param _imxToken Address of the IMX token contract.
     */
    constructor(address _imxToken) {
        require(_imxToken != address(0), "Invalid token address");
        imxToken = IERC20(_imxToken);
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Proposal description.
     * @param _duration Duration (in seconds) for the voting period.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration
        });

        emit ProposalCreated(proposalCount, _description, block.timestamp + _duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _voteFor True to vote 'For', false to vote 'Against'.
     */
    function vote(uint256 _proposalId, bool _voteFor) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.deadline > 0, "Proposal not found");
        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        uint256 voterBalance = imxToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Insufficient IMX token balance to vote");

        if (_voteFor) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _voteFor);
    }

    /**
     * @dev Function to get the result of a proposal.
     * @param _proposalId ID of the proposal.
     * @return Result string indicating the voting outcome.
     */
    function getProposalResult(uint256 _proposalId) external view returns (string memory) {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.deadline > 0, "Proposal not found");
        require(block.timestamp >= proposal.deadline, "Voting period is still active");

        if (proposal.votesFor > proposal.votesAgainst) {
            return "Proposal Passed";
        } else if (proposal.votesAgainst > proposal.votesFor) {
            return "Proposal Rejected";
        } else {
            return "Proposal Tied";
        }
    }
}
```
