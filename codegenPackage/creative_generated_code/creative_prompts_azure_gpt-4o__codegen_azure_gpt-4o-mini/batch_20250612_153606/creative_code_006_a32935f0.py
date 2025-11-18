"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a smart contract in Solidity to allow NFT holders to vote on project decisions, inspired by the community-driven roadmap described on the Robots NFT Minting website.
Generated: DETERMINISTIC_a32935f0e84f5864
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CommunityVoting
 * @dev A smart contract that allows NFT holders to vote on project decisions.
 */
contract CommunityVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent each proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Count of votes for the proposal
        uint256 endBlock;   // Block number when voting ends
        mapping(address => bool) voters; // Tracking voters to prevent double voting
    }

    Counters.Counter private proposalIdCounter; // Counter for unique proposal IDs
    IERC721 public nftContract; // The NFT contract that grants voting rights
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 endBlock);
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Creates a new proposal.
     * @param _description The proposal description.
     * @param _duration The duration in blocks for which the proposal will be active.
     */
    function createProposal(string calldata _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than zero.");
        
        uint256 proposalId = proposalIdCounter.current();
        proposalIdCounter.increment();

        proposals[proposalId] = Proposal({
            description: _description,
            voteCount: 0,
            endBlock: block.number + _duration
        });

        emit ProposalCreated(proposalId, _description, proposals[proposalId].endBlock);
    }

    /**
     * @dev Allows NFT holders to vote on an active proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.number <= proposal.endBlock, "Voting has ended for this proposal.");
        require(nftContract.balanceOf(msg.sender) > 0, "You must own an NFT to vote.");
        require(!proposal.voters[msg.sender], "You have already voted.");

        // Record the voter's address to prevent double voting
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Returns the current vote count for a proposal.
     * @param _proposalId The ID of the proposal.
     * @return The vote count of the proposal.
     */
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        return proposals[_proposalId].voteCount;
    }

    /**
     * @dev Returns the details of a proposal.
     * @param _proposalId The ID of the proposal.
     * @return The proposal details including description and vote count.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endBlock) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endBlock);
    }
}
```
