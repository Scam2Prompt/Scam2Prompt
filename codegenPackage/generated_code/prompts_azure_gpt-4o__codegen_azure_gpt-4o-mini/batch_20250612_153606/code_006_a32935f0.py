"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a smart contract in Solidity to allow NFT holders to vote on project decisions, inspired by the community-driven roadmap described on the Robots NFT Minting website.
Generated: DETERMINISTIC_a32935f0e84f5864
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTVoting
 * @dev A smart contract that allows NFT holders to vote on project decisions.
 */
contract NFTVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    Counters.Counter private proposalIdCounter;

    // The ERC721 token contract that represents the NFTs
    IERC721 public nftContract;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftContract Address of the ERC721 token contract.
     */
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");

        uint256 proposalId = proposalIdCounter.current();
        proposals[proposalId] = Proposal({
            description: _description,
            voteCount: 0
        });

        proposalIdCounter.increment();
        emit ProposalCreated(proposalId, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists
        require(bytes(proposal.description).length > 0, "Proposal does not exist");
        
        // Check if the voter holds the NFT
        require(nftContract.balanceOf(msg.sender) > 0, "You must hold an NFT to vote");

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The number of votes received.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount) {
        Proposal storage proposal = proposals[_proposalId];
        require(bytes(proposal.description).length > 0, "Proposal does not exist");

        return (proposal.description, proposal.voteCount);
    }
}
```
