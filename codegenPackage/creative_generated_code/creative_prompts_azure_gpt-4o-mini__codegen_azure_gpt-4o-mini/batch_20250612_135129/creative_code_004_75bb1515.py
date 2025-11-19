"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Create a governance model for the Frax ecosystem using the Frax Share (FXS) and Frax Price Index Share (FPIS) tokens.
Generated: DETERMINISTIC_75bb15153de88956
Batch ID: 20250612_135129
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

// Import OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FraxGovernance
 * @dev A governance contract for the Frax ecosystem using FXS and FPIS tokens
 */
contract FraxGovernance is Ownable {
    // Token interfaces
    IERC20 public fxsToken;
    IERC20 public fpisToken;

    // Proposal structure
    struct Proposal {
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voted;
    }

    // List of proposals
    Proposal[] public proposals;

    // Events
    event ProposalCreated(uint256 proposalId, address proposer, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to set the FXS and FPIS token addresses
     * @param _fxsTokenAddress Address of FXS token
     * @param _fpisTokenAddress Address of FPIS token
     */
    constructor(address _fxsTokenAddress, address _fpisTokenAddress) {
        require(_fxsTokenAddress != address(0), "Invalid FXS token address");
        require(_fpisTokenAddress != address(0), "Invalid FPIS token address");

        fxsToken = IERC20(_fxsTokenAddress);
        fpisToken = IERC20(_fpisTokenAddress);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration in seconds for voting
     */
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_duration > 0, "Duration must be greater than 0");

        uint256 endTime = block.timestamp + _duration;

        Proposal storage newProposal = proposals.push();
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        emit ProposalCreated(proposals.length - 1, msg.sender, _description, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _support Vote support (true for 'for', false for 'against')
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voted[msg.sender], "Already voted");

        // Count votes
        uint256 voteWeight = fxsToken.balanceOf(msg.sender) + fpisToken.balanceOf(msg.sender);
        require(voteWeight > 0, "No voting power");

        if (_support) {
            proposal.votesFor += voteWeight;
        } else {
            proposal.votesAgainst += voteWeight;
        }
        proposal.voted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal if voting is finished
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting has not ended");
        require(!proposal.executed, "Proposal already executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            // Logic for executing the proposal should go here
            // ...

            emit ProposalExecuted(_proposalId);
        } else {
            // Optional: Logic for handling rejected proposals
            // ...
        }

        proposal.executed = true;
    }

    /**
     * @dev Get the details of a proposal
     * @param _proposalId ID of the proposal
     * @return proposer, description, votesFor, votesAgainst, endTime, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        address proposer,
        string memory description,
        uint256 votesFor,
        uint256 votesAgainst,
        uint256 endTime,
        bool executed
    ) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        return (
            proposal.proposer,
            proposal.description,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.endTime,
            proposal.executed
        );
    }
}
```
