"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindexlive.pages.dev
Prompt: Provide an example of a governance voting mechanism in Solidity for $MEMEX token holders to decide which meme coins to include in the Moonshot index.
Generated: DETERMINISTIC_cdc0c92e0494f66a
Batch ID: 20250612_145633
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
 * @dev This contract allows $MEMEX token holders to vote on including meme coins in the Moonshot index.
 */
contract GovernanceVoting {
    // The address of the $MEMEX token contract
    IERC20 public memexToken;

    // Struct to represent a proposal
    struct Proposal {
        string memeCoinName; // The name of the meme coin
        uint256 yesVotes;    // Total "Yes" votes
        uint256 noVotes;     // Total "No" votes
        uint256 endTime;     // Voting deadline (timestamp)
        bool executed;       // Whether the proposal has been executed
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Minimum $MEMEX tokens required to propose
    uint256 public constant MINIMUM_MEMEX_TO_PROPOSE = 1000 * 10**18;

    // Duration of voting period (e.g., 7 days)
    uint256 public constant VOTING_DURATION = 7 days;

    event ProposalCreated(uint256 proposalId, string memeCoinName, uint256 endTime);
    event VoteCast(uint256 proposalId, address voter, bool vote, uint256 weight);
    event ProposalExecuted(uint256 proposalId, bool approved);

    /**
     * @param _memexToken Address of the $MEMEX token contract
     */
    constructor(address _memexToken) {
        require(_memexToken != address(0), "Invalid $MEMEX token address");
        memexToken = IERC20(_memexToken);
    }

    /**
     * @dev Create a new proposal for a meme coin.
     * @param _memeCoinName The name of the meme coin to propose
     */
    function createProposal(string calldata _memeCoinName) external {
        require(bytes(_memeCoinName).length > 0, "Meme coin name cannot be empty");
        require(
            memexToken.balanceOf(msg.sender) >= MINIMUM_MEMEX_TO_PROPOSE,
            "Insufficient $MEMEX tokens to create a proposal"
        );

        uint256 proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            memeCoinName: _memeCoinName,
            yesVotes: 0,
            noVotes: 0,
            endTime: block.timestamp + VOTING_DURATION,
            executed: false
        });

        emit ProposalCreated(proposalId, _memeCoinName, proposals[proposalId].endTime);
    }

    /**
     * @dev Vote on an active proposal.
     * @param _proposalId ID of the proposal to vote on
     * @param _vote True for "Yes", False for "No"
     */
    function vote(uint256 _proposalId, bool _vote) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");
        uint256 voterBalance = memexToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Only $MEMEX token holders can vote");

        // Record the voter's vote weight
        hasVoted[_proposalId][msg.sender] = true;

        if (_vote) {
            proposal.yesVotes += voterBalance;
        } else {
            proposal.noVotes += voterBalance;
        }

        emit VoteCast(_proposalId, msg.sender, _vote, voterBalance);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period is not over");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;
        bool approved = proposal.yesVotes > proposal.noVotes;

        emit ProposalExecuted(_proposalId, approved);

        // Logic for adding meme coin to the Moonshot index would go here if approved
    }

    /**
     * @dev Interface for ERC20 tokens.
     */
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
    }
}
```
