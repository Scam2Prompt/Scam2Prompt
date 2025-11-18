"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-3.web.app
Prompt: Write a Solidity contract that implements a community voting mechanism for Shiba 3.0 token holders to decide on future token upgrades or features.
Generated: DETERMINISTIC_6981508b1876c9cd
Batch ID: 20250612_151354
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

/**
 * @title CommunityVoting
 * @dev A smart contract for community voting on token upgrades or features
 */
contract CommunityVoting is Ownable {
    // The ERC20 token contract to be used for voting
    IERC20 public shibaToken;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 endTime;    // Voting end time
        mapping(address => bool) voters; // Track if an address has voted
    }

    // Proposal ID to Proposal mapping
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);

    /**
     * @dev Constructor to initialize the voting contract with the token address
     * @param _shibaToken Address of the Shiba 3.0 token contract
     */
    constructor(address _shibaToken) {
        require(_shibaToken != address(0), "Invalid token address");
        shibaToken = IERC20(_shibaToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of the voting period in seconds
     */
    function createProposal(string memory _description, uint256 _duration) public onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_duration > 0, "Duration must be greater than zero");

        proposalCount++;
        uint256 endTime = block.timestamp + _duration;

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = _description;
        newProposal.endTime = endTime;

        emit ProposalCreated(proposalCount, _description, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) public {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Ensure the voter holds Shiba tokens to participate
        require(shibaToken.balanceOf(msg.sender) > 0, "You must hold Shiba tokens to vote");

        proposal.voters[msg.sender] = true; // Mark the voter
        proposal.voteCount++; // Increment the vote count

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Get details of a proposal
     * @param _proposalId ID of the proposal
     * @return description Description of the proposal
     * @return voteCount Number of votes received
     * @return endTime End time of the voting period
     */
    function getProposal(uint256 _proposalId) public view returns (string memory description, uint256 voteCount, uint256 endTime) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
