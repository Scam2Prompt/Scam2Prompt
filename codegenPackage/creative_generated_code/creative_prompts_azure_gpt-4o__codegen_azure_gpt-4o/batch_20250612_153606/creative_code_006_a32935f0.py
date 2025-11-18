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

/**
 * @title NFT Voting Smart Contract
 * @dev Allows NFT holders to vote on project decisions in a decentralized manner
 */
contract NFTVoting {
    // Mapping from proposal ID to Proposal struct
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Address of the NFT contract
    address public nftContract;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if caller owns at least one NFT
    modifier onlyNFTHolder() {
        require(balanceOf(msg.sender) > 0, "Caller must own at least one NFT");
        _;
    }

    /**
     * @dev Constructor to initialize the NFT contract address
     * @param _nftContract Address of the NFT contract
     */
    constructor(address _nftContract) {
        nftContract = _nftContract;
    }

    /**
     * @dev Creates a new proposal
     * @param _description The description of the proposal
     * @param _duration Duration (in seconds) for the proposal voting
     */
    function createProposal(string memory _description, uint256 _duration) external onlyNFTHolder {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Duration must be greater than 0");

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = _description;
        newProposal.deadline = block.timestamp + _duration;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description, newProposal.deadline);
        proposalCount++;
    }

    /**
     * @dev Casts a vote for a specific proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external onlyNFTHolder {
        require(_proposalId < proposalCount, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.deadline, "Proposal voting period has ended");
        require(!proposal.hasVoted[msg.sender], "Caller has already voted on this proposal");

        proposal.voteCount++;
        proposal.hasVoted[msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender);
    }

    /**
     * @dev Executes a proposal (mock execution logic)
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyNFTHolder {
        require(_proposalId < proposalCount, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Add execution logic here (for demonstration, we simply mark it as executed)
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Retrieves the vote count for a proposal
     * @param _proposalId ID of the proposal
     * @return The vote count for the proposal
     */
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(_proposalId < proposalCount, "Proposal does not exist");
        return proposals[_proposalId].voteCount;
    }

    /**
     * @dev Checks if an address owns NFTs from the linked NFT contract
     * @param _owner Address to check
     * @return NFT balance of the address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        // Interface with ERC-721 contract to check balance
        (bool success, bytes memory data) = nftContract.staticcall(
            abi.encodeWithSignature("balanceOf(address)", _owner)
        );
        require(success, "Failed to query NFT balance");
        return abi.decode(data, (uint256));
    }
}
```
