"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaq-token.pages.dev
Prompt: Develop a dApp prototype that leverages the peaq token for Machine Subsidies, allowing users to propose and vote on new machines within the ecosystem.
Generated: DETERMINISTIC_12fa5812fb76b97f
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MachineProposal
 * @dev A smart contract that allows users to propose and vote on new machines for subsidies using the peaq token.
 */
contract MachineProposal is Ownable {
    using Counters for Counters.Counter;

    // Define the structure for a machine proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 voteCount;
        bool active;
    }

    IERC20 public peaqToken; // The peaq token used for voting
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to Proposal struct
    mapping(uint256 => mapping(address => bool)) public votes; // Track votes for each proposal

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed id, string description, address indexed proposer);

    // Event emitted when a proposal is voted on
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Constructor to set the token address
    constructor(address _peaqToken) {
        require(_peaqToken != address(0), "Invalid token address");
        peaqToken = IERC20(_peaqToken);
    }

    /**
     * @dev Create a new machine proposal.
     * @param _description The description of the machine proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        proposals[newProposalId] = Proposal({
            id: newProposalId,
            description: _description,
            proposer: msg.sender,
            voteCount: 0,
            active: true
        });

        emit ProposalCreated(newProposalId, _description, msg.sender);
    }

    /**
     * @dev Vote for a machine proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.active, "Proposal is not active");
        require(!votes[_proposalId][msg.sender], "You have already voted");

        // Transfer peaq tokens to the contract as a voting fee
        require(peaqToken.transferFrom(msg.sender, address(this), 1 ether), "Token transfer failed");

        votes[_proposalId][msg.sender] = true; // Mark the voter
        proposal.voteCount++; // Increment the vote count

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev End a proposal by marking it as inactive.
     * @param _proposalId The ID of the proposal to end.
     */
    function endProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.active, "Proposal is already inactive");
        proposal.active = false; // Mark proposal as inactive
    }

    /**
     * @dev Withdraw the accumulated tokens to the owner.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = peaqToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(peaqToken.transfer(owner(), balance), "Transfer failed");
    }
}
```

This Solidity smart contract defines a decentralized application (dApp) prototype that allows users to propose new machines and vote on them using the peaq token. It includes functionality for creating proposals, voting, and managing proposal statuses, along with necessary error handling and events for tracking actions.
