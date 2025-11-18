"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a script in Solidity to implement decentralized governance for NFT cities in the EarthMeta metaverse, allowing token holders to vote on city-related decisions.
Generated: DETERMINISTIC_3ae72db9ebee8e34
Batch ID: 20250612_152658
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
 * @title NFT Cities Governance Contract
 * @dev This contract allows token holders to vote on city-related decisions
 *      in the EarthMeta metaverse. It implements decentralized governance.
 */
contract NFTCitiesGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCountYes;
        uint256 voteCountNo;
        bool executed;
        address creator;
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether a token has been used for voting (tokenId => proposalId => voted)
    mapping(uint256 => mapping(uint256 => bool)) public hasVoted;

    // Token contract address (assumes ERC721)
    address public nftTokenContract;

    // Proposal counter
    uint256 public proposalCounter;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description, address creator);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, uint256 tokenId, bool voteYes, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId, string description, bool passed);

    // Modifier to ensure only NFT holders can interact
    modifier onlyNFTHolder(uint256 tokenId) {
        require(
            IERC721(nftTokenContract).ownerOf(tokenId) == msg.sender,
            "Caller is not the owner of the NFT token."
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the NFT token contract address
     * @param _nftTokenContract Address of the ERC721 NFT token contract
     */
    constructor(address _nftTokenContract) {
        nftTokenContract = _nftTokenContract;
    }

    /**
     * @dev Function to create a new proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty.");

        proposalCounter++;

        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: description,
            voteCountYes: 0,
            voteCountNo: 0,
            executed: false,
            creator: msg.sender
        });

        emit ProposalCreated(proposalCounter, description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param tokenId NFT token ID used for voting
     * @param voteYes True to vote 'Yes', false to vote 'No'
     */
    function vote(uint256 proposalId, uint256 tokenId, bool voteYes)
        external
        onlyNFTHolder(tokenId)
    {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist.");
        require(!proposals[proposalId].executed, "Proposal has already been executed.");
        require(!hasVoted[tokenId][proposalId], "Token has already been used to vote.");

        // Mark the token as voted for this proposal
        hasVoted[tokenId][proposalId] = true;

        // Increment vote counts
        if (voteYes) {
            proposals[proposalId].voteCountYes++;
        } else {
            proposals[proposalId].voteCountNo++;
        }

        emit VoteCast(proposalId, tokenId, voteYes, msg.sender);
    }

    /**
     * @dev Function to execute a proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id == proposalId, "Proposal does not exist.");
        require(!proposal.executed, "Proposal has already been executed.");
        require(
            proposal.voteCountYes + proposal.voteCountNo > 0,
            "No votes have been cast for this proposal."
        );

        // Determine outcome
        bool passed = proposal.voteCountYes > proposal.voteCountNo;

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(proposalId, proposal.description, passed);

        // NOTE: Additional logic can be added here to implement the effects of the proposal.
    }
}

/**
 * @dev Interface for interacting with an ERC721 token contract
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
