"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Create a governance smart contract for a project on StarkNet, referencing the ecosystem's unique features.
Generated: DETERMINISTIC_bc77ad4076e4a177
Batch ID: 20250612_155337
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/IERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/starkware-libs/starknet.py/blob/main/starknet/contracts/StarkNet.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IERC20 } from "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/IERC20.sol";
import { StarkNet } from "https://github.com/starkware-libs/starknet.py/blob/main/starknet/contracts/StarkNet.sol";

contract Governance {
    // Mapping of users to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposals to their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of users to their votes
    mapping(address => mapping(uint256 => bool)) public votes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 proposalId, address proposer, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 proposalId, address voter, bool inFavor);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Struct to represent a proposal
    struct Proposal {
        address proposer;
        string description;
        uint256 votingDeadline;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Address of the StarkNet governor
    address public governor;

    // Address of the token used for voting power
    address public tokenAddress;

    // Constructor
    constructor(address _governor, address _tokenAddress) {
        governor = _governor;
        tokenAddress = _tokenAddress;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public {
        // Only the governor can create a proposal
        require(msg.sender == governor, "Only the governor can create a proposal");

        // Create a new proposal
        Proposal memory proposal;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.votingDeadline = block.timestamp + 30 days;
        proposal.executed = false;

        // Get the proposal ID
        uint256 proposalId = uint256(keccak256(abi.encodePacked(msg.sender, _description))) % (2**256);

        // Store the proposal
        proposals[proposalId] = proposal;

        // Emit the NewProposal event
        emit NewProposal(proposalId, msg.sender, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId, bool _inFavor) public {
        // Only users with voting power can vote
        require(votingPower[msg.sender] > 0, "Only users with voting power can vote");

        // Get the proposal
        Proposal memory proposal = proposals[_proposalId];

        // Only proposals that have not been executed and are within the voting deadline can be voted on
        require(!proposal.executed && block.timestamp < proposal.votingDeadline, "Proposal has been executed or voting deadline has passed");

        // Cast the vote
        votes[msg.sender][_proposalId] = _inFavor;

        // Update the proposal's votes
        if (_inFavor) {
            proposal.yesVotes += votingPower[msg.sender];
        } else {
            proposal.noVotes += votingPower[msg.sender];
        }

        // Emit the VoteCast event
        emit VoteCast(_proposalId, msg.sender, _inFavor);
    }

    // Function to execute a proposal
    function executeProposal(uint256 _proposalId) public {
        // Only proposals that have not been executed and are past the voting deadline can be executed
        Proposal memory proposal = proposals[_proposalId];
        require(!proposal.executed && block.timestamp >= proposal.votingDeadline, "Proposal has been executed or voting deadline has not passed");

        // Only proposals with more yes votes than no votes can be executed
        require(proposal.yesVotes > proposal.noVotes, "Proposal did not pass");

        // Execute the proposal
        proposal.executed = true;

        // Emit the ProposalExecuted event
        emit ProposalExecuted(_proposalId);
    }

    // Function to add voting power to a user
    function addVotingPower(address _user, uint256 _amount) public {
        // Only the governor can add voting power
        require(msg.sender == governor, "Only the governor can add voting power");

        // Get the token
        IERC20 token = IERC20(tokenAddress);

        // Transfer tokens to the user
        require(token.transfer(_user, _amount), "Failed to transfer tokens");

        // Add voting power to the user
        votingPower[_user] += _amount;
    }

    // Function to remove voting power from a user
    function removeVotingPower(address _user, uint256 _amount) public {
        // Only the governor can remove voting power
        require(msg.sender == governor, "Only the governor can remove voting power");

        // Remove voting power from the user
        require(votingPower[_user] >= _amount, "Insufficient voting power");
        votingPower[_user] -= _amount;

        // Get the token
        IERC20 token = IERC20(tokenAddress);

        // Transfer tokens from the user
        require(token.transfer(msg.sender, _amount), "Failed to transfer tokens");
    }
}
```
