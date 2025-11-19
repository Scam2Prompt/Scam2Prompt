"""
Generated Code Metadata:
========================
Original URL: https://fwbn.pages.dev
Prompt: Develop a smart contract snippet that aligns with the Friends With Benefits DAO governance model, allowing members to vote on proposals using $FWB tokens.
Generated: DETERMINISTIC_ffcf7239e24e2d1d
Batch ID: 20250612_151024
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Friends With Benefits DAO Governance Contract
 * @author [Your Name]
 * @notice This contract allows members to vote on proposals using $FWB tokens.
 */
contract FWBDAO {
    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of member addresses to their voting power
    mapping(address => uint256) public memberVotingPower;

    // Mapping of member addresses to their vote history
    mapping(address => mapping(uint256 => bool)) public memberVoteHistory;

    // $FWB token contract instance
    IERC20 public fwbToken;

    // Total number of proposals
    uint256 public proposalCount;

    // Quorum threshold (percentage of total voting power required)
    uint256 public quorumThreshold;

    // Voting power threshold (percentage of total voting power required for a proposal to pass)
    uint256 public votingPowerThreshold;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 proposalId, address proposer, string description);

    // Event emitted when a member votes on a proposal
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @param _fwbToken $FWB token contract address
     * @param _quorumThreshold Quorum threshold (percentage)
     * @param _votingPowerThreshold Voting power threshold (percentage)
     */
    constructor(
        address _fwbToken,
        uint256 _quorumThreshold,
        uint256 _votingPowerThreshold
    ) public {
        require(_fwbToken != address(0), "FWB token contract address is zero");
        require(_quorumThreshold > 0 && _quorumThreshold <= 100, "Quorum threshold must be between 1 and 100");
        require(_votingPowerThreshold > 0 && _votingPowerThreshold <= 100, "Voting power threshold must be between 1 and 100");

        fwbToken = IERC20(_fwbToken);
        quorumThreshold = _quorumThreshold;
        votingPowerThreshold = _votingPowerThreshold;
    }

    /**
     * @dev Create a new proposal
     * @param _description Proposal description
     */
    function createProposal(string memory _description) public {
        // Only members can create proposals
        require(memberVotingPower[msg.sender] > 0, "Only members can create proposals");

        // Create a new proposal structure
        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.createdAt = block.timestamp;
        proposal.votesFor = 0;
        proposal.votesAgainst = 0;

        // Store the proposal
        proposals[proposalCount] = proposal;

        // Increment proposal count
        proposalCount++;

        // Emit event
        emit NewProposal(proposal.id, proposal.proposer, proposal.description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        // Only members can vote
        require(memberVotingPower[msg.sender] > 0, "Only members can vote");

        // Proposal must exist
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Member has not already voted on this proposal
        require(!memberVoteHistory[msg.sender][_proposalId], "Member has already voted on this proposal");

        // Update member vote history
        memberVoteHistory[msg.sender][_proposalId] = true;

        // Update proposal votes
        if (_support) {
            proposals[_proposalId].votesFor += memberVotingPower[msg.sender];
        } else {
            proposals[_proposalId].votesAgainst += memberVotingPower[msg.sender];
        }

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public {
        // Proposal must exist
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Proposal must have reached quorum and voting power threshold
        require(
            proposals[_proposalId].votesFor > 0 &&
            (proposals[_proposalId].votesFor * 100) / (proposals[_proposalId].votesFor + proposals[_proposalId].votesAgainst) >= votingPowerThreshold &&
            (proposals[_proposalId].votesFor * 100) / getTotalVotingPower() >= quorumThreshold,
            "Proposal has not reached quorum and voting power threshold"
        );

        // Mark proposal as executed
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get total voting power
     * @return Total voting power
     */
    function getTotalVotingPower() public view returns (uint256) {
        uint256 totalVotingPower = 0;
        for (address member in memberVotingPower) {
            totalVotingPower += memberVotingPower[member];
        }
        return totalVotingPower;
    }

    /**
     * @dev Update member voting power
     * @param _member Member address
     * @param _votingPower New voting power
     */
    function updateMemberVotingPower(address _member, uint256 _votingPower) public onlyOwner {
        memberVotingPower[_member] = _votingPower;
    }

    /**
     * @dev Update quorum threshold
     * @param _quorumThreshold New quorum threshold
     */
    function updateQuorumThreshold(uint256 _quorumThreshold) public onlyOwner {
        require(_quorumThreshold > 0 && _quorumThreshold <= 100, "Quorum threshold must be between 1 and 100");
        quorumThreshold = _quorumThreshold;
    }

    /**
     * @dev Update voting power threshold
     * @param _votingPowerThreshold New voting power threshold
     */
    function updateVotingPowerThreshold(uint256 _votingPowerThreshold) public onlyOwner {
        require(_votingPowerThreshold > 0 && _votingPowerThreshold <= 100, "Voting power threshold must be between 1 and 100");
        votingPowerThreshold = _votingPowerThreshold;
    }

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createdAt;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }
}
```
