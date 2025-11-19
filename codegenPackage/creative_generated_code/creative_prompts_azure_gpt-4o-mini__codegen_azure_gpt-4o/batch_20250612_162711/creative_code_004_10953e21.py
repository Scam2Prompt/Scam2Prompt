"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Explain how to implement on-chain governance using SaitaChain's token holder voting mechanism, including a sample code.
Generated: DETERMINISTIC_10953e21d2359278
Batch ID: 20250612_162711
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
 * @title On-Chain Governance Contract for SaitaChain Token Holders
 * @dev This contract enables token holders to vote on proposals, leveraging SaitaChain's voting mechanism.
 * @notice Ensure this contract is deployed with the governance token address provided.
 */
contract TokenHolderGovernance {
    // Address of the governance token contract (SaitaChain Token)
    address public governanceToken;

    // Proposal structure
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Proposal description
        uint256 yesVotes; // Total yes votes
        uint256 noVotes; // Total no votes
        uint256 endBlock; // Block number at which voting ends
        bool executed; // Whether the proposal has been executed
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping of proposal ID to voter address to prevent duplicate voting
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endBlock);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the governance token address.
     * @param _governanceToken Address of the SaitaChain governance token.
     */
    constructor(address _governanceToken) {
        require(_governanceToken != address(0), "Invalid token address");
        governanceToken = _governanceToken;
    }

    /**
     * @dev Modifier to ensure the caller holds governance tokens.
     */
    modifier onlyTokenHolders() {
        require(
            IERC20(governanceToken).balanceOf(msg.sender) > 0,
            "Caller must hold governance tokens"
        );
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Duration (in blocks) for voting to remain open.
     */
    function createProposal(string memory _description, uint256 _duration)
        external
        onlyTokenHolders
    {
        require(_duration > 0, "Voting duration must be greater than zero");

        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            yesVotes: 0,
            noVotes: 0,
            endBlock: block.number + _duration,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _description, block.number + _duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True for yes, false for no.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];

        require(block.number <= proposal.endBlock, "Voting has ended for this proposal");
        require(!hasVoted[_proposalId][msg.sender], "Caller has already voted");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.yesVotes += IERC20(governanceToken).balanceOf(msg.sender);
        } else {
            proposal.noVotes += IERC20(governanceToken).balanceOf(msg.sender);
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal after the voting period ends.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];

        require(block.number > proposal.endBlock, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Example condition: Execute based on majority vote
        if (proposal.yesVotes > proposal.noVotes) {
            // Proposal passes - Implement execution logic here (if any)
        }

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 * Used to interact with the SaitaChain governance token.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
