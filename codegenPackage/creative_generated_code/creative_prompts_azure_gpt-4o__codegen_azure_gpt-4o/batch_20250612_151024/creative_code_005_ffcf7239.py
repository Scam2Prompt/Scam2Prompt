"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fwbn.pages.dev
Prompt: Develop a smart contract snippet that aligns with the Friends With Benefits DAO governance model, allowing members to vote on proposals using $FWB tokens.
Generated: DETERMINISTIC_ffcf7239e24e2d1d
Batch ID: 20250612_151024
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
 * @title Friends With Benefits DAO Governance Contract
 * @author [Your Name]
 * @notice This contract allows members of the FWB DAO to vote on proposals using $FWB tokens.
 */
contract FWBGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount; // Total votes received
        uint256 startTime; // Voting start time
        uint256 endTime;   // Voting end time
        bool executed;     // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to store whether a user has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token interface
    IERC20 public fwbToken;

    // Proposal counter to generate unique IDs
    uint256 public proposalCounter;

    // DAO Admin address
    address public admin;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 proposalId, address voter, uint256 weight);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _fwbToken Address of the $FWB token contract.
     * @param _admin Address of the DAO admin.
     */
    constructor(address _fwbToken, address _admin) {
        require(_fwbToken != address(0), "Invalid token address");
        require(_admin != address(0), "Invalid admin address");
        fwbToken = IERC20(_fwbToken);
        admin = _admin;
    }

    /**
     * @dev Create a new proposal.
     * @param _description A brief description of the proposal.
     * @param _startTime Start time for voting (UNIX timestamp).
     * @param _endTime End time for voting (UNIX timestamp).
     * @return proposalId The ID of the newly created proposal.
     */
    function createProposal(
        string memory _description,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyAdmin returns (uint256 proposalId) {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_endTime > block.timestamp, "End time must be in the future");

        proposalCounter += 1;
        proposalId = proposalCounter;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCount: 0,
            startTime: _startTime,
            endTime: _endTime,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, _startTime, _endTime);
    }

    /**
     * @dev Cast a vote for a proposal using $FWB tokens.
     * @param _proposalId ID of the proposal to vote on.
     * @param _voteWeight Amount of $FWB tokens to vote with.
     */
    function vote(uint256 _proposalId, uint256 _voteWeight) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.startTime <= block.timestamp, "Voting has not started yet");
        require(proposal.endTime >= block.timestamp, "Voting has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");
        require(_voteWeight > 0, "Vote weight must be greater than zero");
        require(fwbToken.balanceOf(msg.sender) >= _voteWeight, "Insufficient token balance");
        require(fwbToken.allowance(msg.sender, address(this)) >= _voteWeight, "Insufficient token allowance");

        // Transfer $FWB tokens to this contract as proof of voting
        fwbToken.transferFrom(msg.sender, address(this), _voteWeight);

        // Update proposal vote count and mark user as voted
        proposal.voteCount += _voteWeight;
        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _voteWeight);
    }

    /**
     * @dev Execute a proposal if it has passed and the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyAdmin {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp > proposal.endTime, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Logic for executing proposal goes here (e.g., fund allocation, DAO action)
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Allow admin to withdraw unused $FWB tokens in the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyAdmin {
        require(fwbToken.balanceOf(address(this)) >= _amount, "Insufficient token balance");
        fwbToken.transfer(admin, _amount);
    }
}

// IERC20 interface for interacting with $FWB tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
