"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Create a smart contract to enable on-chain governance voting for SaitaChain token holders to propose network upgrades.
Generated: DETERMINISTIC_c6674e64fe9f432e
Batch ID: 20250612_153809
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for secure token handling and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        uint256 endBlock;   // Block number when voting ends
        mapping(address => bool) voters; // Mapping to track if an address has voted
    }

    IERC20 public token; // The SaitaChain token used for voting
    Proposal[] public proposals; // List of proposals
    uint256 public votingDuration; // Duration of voting in blocks

    // Event to emit when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 endBlock);
    // Event to emit when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if the voting duration has not expired
    modifier hasNotExpired(uint256 proposalId) {
        require(block.number <= proposals[proposalId].endBlock, "Voting period has expired");
        _;
    }

    // Constructor to initialize the contract with the SaitaChain token and voting duration
    constructor(IERC20 _token, uint256 _votingDuration) {
        token = _token;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string calldata description) external onlyOwner {
        uint256 endBlock = block.number + votingDuration; // Calculate the end block for voting
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            endBlock: endBlock
        }));

        emit ProposalCreated(proposals.length - 1, description, endBlock);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external hasNotExpired(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Ensure that the voter has not already voted on this proposal
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");
        
        // Transfer 1 token from the voter to this contract for validation
        // (this can be modified to suit the voting mechanism if needed)
        require(token.balanceOf(msg.sender) > 0, "You must hold SaitaChain tokens to vote");

        // Mark this voter as having voted and increment the vote count
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, uint256 endBlock) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.endBlock);
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
