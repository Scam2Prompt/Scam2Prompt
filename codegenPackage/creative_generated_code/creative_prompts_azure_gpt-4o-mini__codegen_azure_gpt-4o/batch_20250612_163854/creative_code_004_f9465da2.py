"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Provide an example of a smart contract that integrates with Agora for managing voting on Optimism proposals.
Generated: DETERMINISTIC_f9465da2ad56bb80
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Importing necessary interfaces and libraries for ERC20 token transfers and Agora's voting
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

interface IAgora {
    function createProposal(string calldata description, bytes[] calldata actions, uint256 startTime, uint256 endTime) external returns (uint256);
    function vote(uint256 proposalId, bool support) external;
    function getProposalStatus(uint256 proposalId) external view returns (string memory status);
}

contract OptimismVoting {
    address public admin; // Address of the contract admin
    IAgora public agora;  // Agora contract address

    // Struct to hold proposal details
    struct Proposal {
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 id;
    }

    uint256 public proposalCount; // Counter for proposals created
    mapping(uint256 => Proposal) public proposals; // Mapping to store proposals
    mapping(address => bool) public voters; // Mapping to check if an address is a voter

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 startTime, uint256 endTime);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);

    // Modifier to restrict access to admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _agora) {
        require(_agora != address(0), "Invalid Agora contract address");
        admin = msg.sender;
        agora = IAgora(_agora);
    }

    // Function to add a voter
    function addVoter(address _voter) external onlyAdmin {
        require(_voter != address(0), "Invalid voter address");
        voters[_voter] = true;
    }

    // Function to remove a voter
    function removeVoter(address _voter) external onlyAdmin {
        require(voters[_voter], "Voter not found");
        voters[_voter] = false;
    }

    // Function to create a new proposal
    function createProposal(string calldata _description, bytes[] calldata _actions, uint256 _startTime, uint256 _endTime) external onlyAdmin {
        require(_startTime >= block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");

        uint256 proposalId = agora.createProposal(_description, _actions, _startTime, _endTime);

        proposals[proposalCount] = Proposal({
            description: _description,
            startTime: _startTime,
            endTime: _endTime,
            id: proposalId
        });

        emit ProposalCreated(proposalId, _description, _startTime, _endTime);
        proposalCount++;
    }

    // Function to cast a vote on a proposal
    function vote(uint256 _proposalId, bool _support) external {
        require(voters[msg.sender], "Only approved voters can vote");
        require(block.timestamp >= proposals[_proposalId].startTime, "Voting has not started yet");
        require(block.timestamp <= proposals[_proposalId].endTime, "Voting has ended");

        agora.vote(proposals[_proposalId].id, _support);
        emit VoteCast(msg.sender, _proposalId, _support);
    }

    // Function to get the status of a proposal
    function getProposalStatus(uint256 _proposalId) external view returns (string memory) {
        return agora.getProposalStatus(proposals[_proposalId].id);
    }
}
```
