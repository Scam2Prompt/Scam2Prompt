"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a Solidity contract to implement EarthMeta's governance mechanism, allowing users to vote on virtual city policies using $EMT tokens.
Generated: DETERMINISTIC_5692d804f611ffcc
Batch ID: 20250612_145526
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title EarthMeta Governance Contract
/// @dev This contract allows users to vote on virtual city policies using $EMT tokens
contract EarthMetaGovernance is Ownable {
    using SafeMath for uint256;

    // Struct to represent a policy proposal
    struct Proposal {
        string description; // The description of the policy
        uint256 voteCount;  // The total number of votes for the proposal
        uint256 endTime;    // The time until the voting period ends
        mapping(address => bool) voters; // Track whether an address has voted
        bool exists;        // Check if the proposal exists
    }

    IERC20 public emtToken; // The $EMT token used for voting
    Proposal[] public proposals; // Array of proposals

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 duration);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the EMT token address
    constructor(address _emtToken) {
        require(_emtToken != address(0), "Invalid token address");
        emtToken = IERC20(_emtToken);
    }

    /// @dev Create a new proposal
    /// @param _description The description of the proposal
    /// @param _duration The duration for voting in seconds
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Duration must be greater than 0");

        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.endTime = block.timestamp.add(_duration);
        newProposal.exists = true;

        emit ProposalCreated(proposals.length - 1, _description, _duration);
    }

    /// @dev Vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer EMT tokens from voter to the contract (voting power)
        uint256 voterBalance = emtToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must have EMT tokens to vote");

        // Record the vote
        proposal.voteCount = proposal.voteCount.add(voterBalance);
        proposal.voters[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    /// @dev Retrieve the number of proposals
    /// @return The total number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /// @dev Retrieve proposal details
    /// @param _proposalId The ID of the proposal to retrieve
    /// @return description The description of the proposal
    /// @return voteCount The total number of votes for the proposal
    /// @return endTime The time until the voting period ends
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");

        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
