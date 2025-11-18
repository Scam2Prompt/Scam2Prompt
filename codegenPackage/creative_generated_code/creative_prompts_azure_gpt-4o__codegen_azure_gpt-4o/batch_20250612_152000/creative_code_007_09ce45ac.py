"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Implement a governance voting system in Solidity that rewards participants for voting, similar to Ondo DAO's governance token model.
Generated: DETERMINISTIC_09ce45acb0fd9093
Batch ID: 20250612_152000
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
 * @title Governance Voting System
 * @dev Implements a governance voting system that rewards participants for voting.
 */
contract GovernanceVoting {
    // Governance Token for rewards
    IERC20 public governanceToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool isOpen;
    }

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Reward amount per vote
    uint256 public rewardAmount;

    // Event declarations
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool vote, uint256 reward);
    event ProposalClosed(uint256 indexed proposalId, bool passed);

    /**
     * @dev Constructor to initialize the contract.
     * @param _governanceToken Address of the governance token contract.
     * @param _rewardAmount Amount of reward tokens per vote.
     */
    constructor(address _governanceToken, uint256 _rewardAmount) {
        require(_governanceToken != address(0), "Invalid governance token address");
        require(_rewardAmount > 0, "Reward amount must be greater than 0");

        governanceToken = IERC20(_governanceToken);
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        uint256 proposalId = proposalCount;
        proposals[proposalId] = Proposal(proposalId, _description, 0, 0, true);
        proposalCount++;

        emit ProposalCreated(proposalId, _description);
    }

    /**
     * @dev Votes on an open proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote True for "Yes", False for "No".
     */
    function vote(uint256 _proposalId, bool _vote) external {
        require(proposals[_proposalId].isOpen, "Proposal is not open for voting");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        if (_vote) {
            proposals[_proposalId].yesVotes++;
        } else {
            proposals[_proposalId].noVotes++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        // Reward the voter with governance tokens
        require(governanceToken.transfer(msg.sender, rewardAmount), "Token transfer failed");

        emit Voted(_proposalId, msg.sender, _vote, rewardAmount);
    }

    /**
     * @dev Closes a proposal and determines if it passed.
     * @param _proposalId ID of the proposal to close.
     */
    function closeProposal(uint256 _proposalId) external {
        require(proposals[_proposalId].isOpen, "Proposal is already closed");

        Proposal storage proposal = proposals[_proposalId];
        proposal.isOpen = false;

        bool passed = proposal.yesVotes > proposal.noVotes;

        emit ProposalClosed(_proposalId, passed);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
