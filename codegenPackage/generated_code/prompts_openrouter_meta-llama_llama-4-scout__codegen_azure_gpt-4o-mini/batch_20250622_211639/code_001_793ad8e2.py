"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a smart contract using Solidity to manage the Meme Index's governance, allowing $MEMEX holders to submit and vote on proposals for adding or removing meme coins from the indexes.
Generated: DETERMINISTIC_793ad8e2bba9e126
Batch ID: 20250622_211639
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

/**
 * @title MemeIndexGovernance
 * @dev A smart contract for managing governance of the Meme Index.
 * $MEMEX holders can submit and vote on proposals to add or remove meme coins.
 */
contract MemeIndexGovernance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address memeCoin;
        bool isAddition; // true for addition, false for removal
        uint256 voteCount;
        mapping(address => bool) voters; // Track if an address has voted
        bool executed; // Track if the proposal has been executed
    }

    // State variables
    IERC20 public memexToken; // Reference to the $MEMEX token
    uint256 public proposalCount; // Counter for proposals
    uint256 public votingDuration; // Duration for voting in seconds
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed memeCoin, bool isAddition);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to check if the caller has enough $MEMEX tokens
    modifier onlyTokenHolders() {
        require(memexToken.balanceOf(msg.sender) > 0, "Must hold $MEMEX tokens to vote");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _memexToken, uint256 _votingDuration) {
        memexToken = _memexToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal to add or remove a meme coin.
     * @param _memeCoin The address of the meme coin.
     * @param _isAddition True if adding, false if removing.
     */
    function createProposal(address _memeCoin, bool _isAddition) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.memeCoin = _memeCoin;
        newProposal.isAddition = _isAddition;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _memeCoin, _isAddition);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voters[msg.sender], "Already voted");
        require(!proposal.executed, "Proposal already executed");

        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if the voting period has ended.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");

        // Check if the voting period has ended
        require(block.timestamp >= votingDuration, "Voting period not ended");

        // Execute the proposal based on its type
        if (proposal.isAddition) {
            // Logic to add the meme coin (e.g., to an index)
            // Placeholder for actual implementation
        } else {
            // Logic to remove the meme coin (e.g., from an index)
            // Placeholder for actual implementation
        }

        proposal.executed = true;
        emit ProposalExecuted(_proposalId, proposal.isAddition);
    }

    /**
     * @dev Set a new voting duration.
     * @param _newDuration The new voting duration in seconds.
     */
    function setVotingDuration(uint256 _newDuration) external onlyOwner {
        votingDuration = _newDuration;
    }
}
```
