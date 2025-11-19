"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drift-2kl.pages.dev
Prompt: Develop a smart contract that allows users to participate in the governance of the Drift ecosystem by holding $DRIFT tokens.
Generated: DETERMINISTIC_3528ace896fc3c33
Batch ID: 20250612_163408
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
 * @title DriftGovernance
 * @dev A smart contract that allows users to participate in the governance of the Drift ecosystem
 * by holding and staking $DRIFT tokens.
 */
contract DriftGovernance is Ownable {
    using Counters for Counters.Counter;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct for Proposal
    struct Proposal {
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    IERC20 public driftToken; // The $DRIFT token contract
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Modifier to check if the caller has enough $DRIFT tokens
    modifier onlyTokenHolder() {
        require(driftToken.balanceOf(msg.sender) > 0, "Caller does not hold $DRIFT tokens");
        _;
    }

    // Constructor to initialize the contract with the $DRIFT token address
    constructor(address _driftToken) {
        require(_driftToken != address(0), "Invalid token address");
        driftToken = IERC20(_driftToken);
    }

    /**
     * @dev Create a new proposal for governance.
     * @param description Description of the proposal.
     */
    function createProposal(string calldata description) external onlyTokenHolder {
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();

        Proposal storage newProposal = proposals[proposalId];
        newProposal.description = description;

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support Whether the voter supports the proposal.
     */
    function vote(uint256 proposalId, bool support) external onlyTokenHolder {
        Proposal storage proposal = proposals[proposalId];
        
        require(!proposal.executed, "Proposal already executed");
        require(!proposal.voters[msg.sender], "Voter has already voted");

        proposal.voters[msg.sender] = true;
        if (support) {
            proposal.voteCount++;
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal if it has enough votes.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > getTotalSupply() / 2, "Not enough votes to execute");

        proposal.executed = true;

        // Execute the proposal logic here (this is a placeholder)
        // ...

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get the total supply of $DRIFT tokens.
     * @return Total supply of the $DRIFT token.
     */
    function getTotalSupply() public view returns (uint256) {
        return driftToken.totalSupply();
    }
}
```
