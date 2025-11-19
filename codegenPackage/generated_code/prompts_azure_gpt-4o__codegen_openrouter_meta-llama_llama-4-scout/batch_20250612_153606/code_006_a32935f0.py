"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a smart contract in Solidity to allow NFT holders to vote on project decisions, inspired by the community-driven roadmap described on the Robots NFT Minting website.
Generated: DETERMINISTIC_a32935f0e84f5864
Batch ID: 20250612_153606
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title RobotsNFTVotingContract
 * @author [Your Name]
 * @notice A smart contract allowing NFT holders to vote on project decisions.
 */
contract RobotsNFTVotingContract {
    using SafeMath for uint256;
    using SafeERC721 for IERC721;

    // Mapping of NFT holders to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposals to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voters to their votes
    mapping(address => mapping(uint256 => bool)) public votes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // IERC721 NFT contract instance
    IERC721 public nftContract;

    // Mapping of executed proposals
    mapping(uint256 => bool) public executedProposals;

    // Number of proposals
    uint256 public proposalCount;

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @notice Initializes the contract with the NFT contract address.
     * @param _nftContract Address of the NFT contract.
     */
    constructor(address _nftContract) public {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @notice Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) public {
        require(nftContract.balanceOf(msg.sender) > 0, "Only NFT holders can create proposals");

        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.description = _description;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposals[proposalCount] = proposal;
        proposalCount++;

        emit NewProposal(proposal.id, proposal.description);
    }

    /**
     * @notice Casts a vote on a proposal.
     * @param _proposalId ID of the proposal.
     * @param _vote Vote (true for yes, false for no).
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        require(proposals[_proposalId].executed == false, "Proposal already executed");
        require(votes[msg.sender][_proposalId] == false, "Already voted on this proposal");
        require(nftContract.balanceOf(msg.sender) > 0, "Only NFT holders can vote");

        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(1);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(1);
        }

        votes[msg.sender][_proposalId] = true;

        emit VoteCast(msg.sender, _proposalId, _vote);
    }

    /**
     * @notice Executes a proposal if it has a majority vote.
     * @param _proposalId ID of the proposal.
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].executed == false, "Proposal already executed");
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal did not pass");

        proposals[_proposalId].executed = true;
        executedProposals[_proposalId] = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Gets the voting power of an address.
     * @param _address Address to get voting power for.
     * @return Voting power of the address.
     */
    function getVotingPower(address _address) public view returns (uint256) {
        return nftContract.balanceOf(_address);
    }
}
```
