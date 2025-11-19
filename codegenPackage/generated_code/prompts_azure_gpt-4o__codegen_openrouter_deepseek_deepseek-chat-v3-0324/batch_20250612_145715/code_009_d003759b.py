"""
Generated Code Metadata:
========================
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Write a Solidity contract that incorporates Deadpool Inu's ethos by allowing token holders to vote on humorous community proposals, such as meme contests or pop culture collaborations.
Generated: DETERMINISTIC_d003759b651571ff
Batch ID: 20250612_145715
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeadpoolInuDAO is Ownable {
    IERC20 public token;

    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        address proposer;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(address => uint256) public lastProposalTimestamp;

    uint256 public constant MIN_VOTING_DURATION = 1 days;
    uint256 public constant MAX_VOTING_DURATION = 7 days;
    uint256 public constant MIN_PROPOSAL_DELAY = 1 days;
    uint256 public constant VOTE_THRESHOLD = 1000 * 10**18; // 1000 tokens required to vote

    event ProposalCreated(
        uint256 indexed id,
        string title,
        string description,
        uint256 voteStart,
        uint256 voteEnd,
        address proposer
    );
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _token) {
        token = IERC20(_token);
    }

    function createProposal(
        string memory _title,
        string memory _description,
        uint256 _duration
    ) external {
        require(
            block.timestamp - lastProposalTimestamp[msg.sender] >= MIN_PROPOSAL_DELAY,
            "Must wait before creating another proposal"
        );
        require(
            _duration >= MIN_VOTING_DURATION && _duration <= MAX_VOTING_DURATION,
            "Invalid voting duration"
        );
        require(
            bytes(_title).length > 0 && bytes(_description).length > 0,
            "Title and description cannot be empty"
        );

        lastProposalTimestamp[msg.sender] = block.timestamp;
        proposalCount++;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            voteStart: block.timestamp,
            voteEnd: block.timestamp + _duration,
            yesVotes: 0,
            noVotes: 0,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(
            proposalCount,
            _title,
            _description,
            block.timestamp,
            block.timestamp + _duration,
            msg.sender
        );
    }

    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp >= proposal.voteStart, "Voting has not started");
        require(block.timestamp <= proposal.voteEnd, "Voting has ended");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        require(
            token.balanceOf(msg.sender) >= VOTE_THRESHOLD,
            "Insufficient token balance to vote"
        );

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.yesVotes += token.balanceOf(msg.sender);
        } else {
            proposal.noVotes += token.balanceOf(msg.sender);
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp > proposal.voteEnd, "Voting has not ended");
        require(!proposal.executed, "Proposal already executed");
        require(
            proposal.yesVotes > proposal.noVotes,
            "Proposal did not pass"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            string memory title,
            string memory description,
            uint256 voteStart,
            uint256 voteEnd,
            uint256 yesVotes,
            uint256 noVotes,
            bool executed,
            address proposer
        )
    {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.title,
            proposal.description,
            proposal.voteStart,
            proposal.voteEnd,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.executed,
            proposal.proposer
        );
    }
}
```
