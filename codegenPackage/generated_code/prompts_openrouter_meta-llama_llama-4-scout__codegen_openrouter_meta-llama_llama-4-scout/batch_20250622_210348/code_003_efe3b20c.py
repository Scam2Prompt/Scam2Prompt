"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: "Design a simple decentralized governance system using blockchain, allowing token holders to vote on platform decisions, inspired by Pushd's governance model."
Generated: DETERMINISTIC_efe3b20cea878e26
Batch ID: 20250622_210348
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Decentralized Governance System
 * @author [Your Name]
 * @notice A simple decentralized governance system allowing token holders to vote on platform decisions.
 */
contract GovernanceSystem {
    using SafeMath for uint256;
    using SafeERC20 for ERC20;

    // Mapping of token holders and their balances
    mapping (address => uint256) public balances;

    // Mapping of proposals and their details
    mapping (uint256 => Proposal) public proposals;

    // Mapping of votes cast by token holders
    mapping (uint256 => mapping (address => Vote)) public votes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a token holder votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Struct representing a vote
    struct Vote {
        bool support;
        bool isValid;
    }

    // Address of the token contract
    address public tokenAddress;

    // Quorum percentage required for a proposal to be executed
    uint256 public quorumPercentage;

    // Constructor
    constructor(address _tokenAddress, uint256 _quorumPercentage) public {
        tokenAddress = _tokenAddress;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @notice Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public {
        // Check if the proposal creation is valid
        require(ERC20(tokenAddress).balanceOf(msg.sender) > 0, "You must hold tokens to create a proposal");

        // Create a new proposal
        Proposal memory proposal;
        proposal.id = uint256(keccak256(abi.encodePacked(_description, block.timestamp)));
        proposal.description = _description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(30 days);
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        // Store the proposal
        proposals[proposal.id] = proposal;

        // Emit event
        emit NewProposal(proposal.id, proposal.description);
    }

    /**
     * @notice Casts a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support Whether to support the proposal
     */
    function castVote(uint256 _proposalId, bool _support) public {
        // Check if the proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if the voting period is active
        require(block.timestamp >= proposals[_proposalId].startTime && block.timestamp <= proposals[_proposalId].endTime, "Voting period is not active");

        // Check if the token holder has not already voted
        require(votes[_proposalId][msg.sender].isValid == false, "You have already voted");

        // Get the token balance of the voter
        uint256 voterBalance = ERC20(tokenAddress).balanceOf(msg.sender);

        // Update the votes
        if (_support) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(voterBalance);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(voterBalance);
        }

        // Store the vote
        votes[_proposalId][msg.sender] = Vote(_support, true);

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @notice Executes a proposal if it has reached the quorum
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        // Check if the proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if the proposal has not been executed
        require(proposals[_proposalId].executed == false, "Proposal has already been executed");

        // Check if the voting period has ended
        require(block.timestamp > proposals[_proposalId].endTime, "Voting period has not ended");

        // Calculate the total votes
        uint256 totalVotes = proposals[_proposalId].yesVotes.add(proposals[_proposalId].noVotes);

        // Calculate the quorum
        uint256 quorum = totalVotes.mul(quorumPercentage).div(100);

        // Check if the proposal has reached the quorum
        require(proposals[_proposalId].yesVotes >= quorum, "Proposal has not reached the quorum");

        // Execute the proposal
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }
}
```

```javascript
// Import required libraries
const Web3 = require('web3');
const { GovernanceSystem } = require('./GovernanceSystem');

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

// Set up contract instance
const governanceSystemAddress = '0x...';
const governanceSystem = new web3.eth.Contract(GovernanceSystem.abi, governanceSystemAddress);

// Function to create a new proposal
async function createProposal(description) {
    try {
        // Get accounts
        const accounts = await web3.eth.getAccounts();

        // Create a new proposal
        await governanceSystem.methods.createProposal(description).send({ from: accounts[0] });
    } catch (error) {
        console.error(error);
    }
}

// Function to cast a vote on a proposal
async function castVote(proposalId, support) {
    try {
        // Get accounts
        const accounts = await web3.eth.getAccounts();

        // Cast a vote
        await governanceSystem.methods.castVote(proposalId, support).send({ from: accounts[0] });
    } catch (error) {
        console.error(error);
    }
}

// Function to execute a proposal
async function executeProposal(proposalId) {
    try {
        // Get accounts
        const accounts = await web3.eth.getAccounts();

        // Execute a proposal
        await governanceSystem.methods.executeProposal(proposalId).send({ from: accounts[0] });
    } catch (error) {
        console.error(error);
    }
}

// Example usage
async function main() {
    // Create a new proposal
    await createProposal('Example proposal');

    // Get proposal ID
    const proposalId = 1;

    // Cast votes
    await castVote(proposalId, true);
    await castVote(proposalId, false);

    // Execute proposal
    await executeProposal(proposalId);
}

main();
```
