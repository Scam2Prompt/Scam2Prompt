"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurunft.github.io
Prompt: Create a Solidity smart contract that integrates BLUR tokens for transaction fees and governance voting within the Blur NFT ecosystem.
Generated: DETERMINISTIC_3b29d5145a5f95f4
Batch ID: 20250612_154902
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

// Importing the ERC20 interface for BLUR token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol"; // For ownership control
import "@openzeppelin/contracts/utils/math/SafeMath.sol"; // For safe mathematical operations

/**
 * @title BlurNFTGovernance
 * @dev This contract allows users to participate in governance voting and pay transaction fees using BLUR tokens within the Blur NFT ecosystem.
 */
contract BlurNFTGovernance is Ownable {
    using SafeMath for uint256;

    // BLUR token interface
    IERC20 public blurToken;

    // Struct to hold proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Total number of proposals
    uint256 public proposalCount;

    // Events for logging
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, bool support, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constructor to initialize the BLUR token address
    constructor(address _blurToken) {
        require(_blurToken != address(0), "Invalid BLUR token address");
        blurToken = IERC20(_blurToken);
    }

    /**
     * @dev Create a new proposal for governance voting
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True to vote in favor, false to vote against
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        // Get the balance of BLUR tokens for the voter
        uint256 balance = blurToken.balanceOf(msg.sender);
        require(balance > 0, "No BLUR tokens for voting");

        // Transfer BLUR tokens as a fee for voting
        require(blurToken.transferFrom(msg.sender, address(this), balance), "Transfer failed");

        // Count the votes
        if (_support) {
            proposals[_proposalId].votesFor = proposals[_proposalId].votesFor.add(balance);
        } else {
            proposals[_proposalId].votesAgainst = proposals[_proposalId].votesAgainst.add(balance);
        }

        emit Voted(_proposalId, _support, msg.sender);
    }

    /**
     * @dev Execute the proposal if it has enough votes
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");

        // Check if the proposal has more votes for than against
        require(proposal.votesFor > proposal.votesAgainst, "Not enough votes for execution");

        // Mark the proposal as executed
        proposal.executed = true;

        // Add logic for what happens when a proposal is executed
        // For example, transferring tokens, modifying state, etc.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Withdraw BLUR tokens from the contract
     * @param amount Amount of BLUR tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(blurToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer BLUR tokens to the owner
        require(blurToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
