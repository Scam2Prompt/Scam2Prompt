"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Create a voting mechanism for token holders to influence community decisions, leveraging PENGWU tokens as described in the Voting feature.
Generated: DETERMINISTIC_91ebe196da3a22dd
Batch ID: 20250612_153722
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

// Import the OpenZeppelin ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Voting contract for PENGWU token holders
contract Voting is Ownable {
    // Struct to store details of each proposal
    struct Proposal {
        string description;  // Description of the proposal
        uint256 voteCount;   // Total votes received for the proposal
        mapping(address => bool) voters; // Track voters to prevent double voting
    }

    // State variables
    IERC20 public pengwuToken; // Instance of the PENGWU token
    Proposal[] public proposals; // List of proposals
    uint256 public totalProposals; // Total number of proposals

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the PENGWU token address
    constructor(address _tokenAddress) {
        pengwuToken = IERC20(_tokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        // Create a new proposal and add it to the proposals array
        proposals.push(Proposal({
            description: _description,
            voteCount: 0
        }));
        totalProposals++;

        emit ProposalCreated(totalProposals - 1, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        // Check if the proposal exists
        require(_proposalId < totalProposals, "Proposal does not exist");

        // Check if the voter has already voted
        require(!proposals[_proposalId].voters[msg.sender], "You have already voted");

        // Check if the voter has enough PENGWU tokens to vote (1 token = 1 vote)
        require(pengwuToken.balanceOf(msg.sender) > 0, "You must hold PENGWU tokens to vote");

        // Mark the voter as having voted
        proposals[_proposalId].voters[msg.sender] = true;

        // Increment the vote count for the selected proposal
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to retrieve proposal details
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount) {
        require(_proposalId < totalProposals, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount);
    }

    // Function to get the total number of proposals
    function getTotalProposals() external view returns (uint256) {
        return totalProposals;
    }
}
```
