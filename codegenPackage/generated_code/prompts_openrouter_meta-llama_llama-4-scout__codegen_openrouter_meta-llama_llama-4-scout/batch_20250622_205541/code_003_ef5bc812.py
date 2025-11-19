"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Design a smart contract for a Proof of Commitment DAO that allows members to stake cryptocurrency and vote on slashing non-compliant members' stakes.
Generated: DETERMINISTIC_ef5bc812db2db39e
Batch ID: 20250622_205541
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title ProofOfCommitmentDAO
 * @author [Your Name]
 * @notice A smart contract for a Proof of Commitment DAO.
 */
contract ProofOfCommitmentDAO is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of members and their stakes
    mapping(address => uint256) public memberStakes;

    // Mapping of members and their voting powers
    mapping(address => uint256) public memberVotingPowers;

    // Mapping of proposals and their votes
    mapping(uint256 => mapping(bool => uint256)) public proposalVotes;

    // Mapping of proposals and their targets
    mapping(uint256 => address) public proposalTargets;

    // Mapping of proposals and their statuses
    mapping(uint256 => bool) public proposalStatuses;

    // Event emitted when a member stakes
    event MemberStaked(address indexed member, uint256 stake);

    // Event emitted when a member slashes
    event MemberSlashed(address indexed member, uint256 amount);

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, address indexed target);

    // Event emitted when a proposal is voted
    event ProposalVoted(uint256 indexed proposalId, bool voted);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct for proposal
    struct Proposal {
        uint256 id;
        address target;
        bool status;
    }

    // List of proposals
    Proposal[] public proposals;

    // Token used for staking
    IERC20 public token;

    // Minimum stake required
    uint256 public minStake;

    // Voting quorum
    uint256 public votingQuorum;

    /**
     * @dev Initializes the contract.
     * @param _token Token used for staking.
     * @param _minStake Minimum stake required.
     * @param _votingQuorum Voting quorum.
     */
    constructor(IERC20 _token, uint256 _minStake, uint256 _votingQuorum) public {
        token = _token;
        minStake = _minStake;
        votingQuorum = _votingQuorum;
    }

    /**
     * @dev Allows a member to stake.
     * @param _amount Amount to stake.
     */
    function stake(uint256 _amount) public whenNotPaused {
        require(_amount >= minStake, "Stake amount must be greater than or equal to the minimum stake");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        memberStakes[msg.sender] = memberStakes[msg.sender].add(_amount);
        memberVotingPowers[msg.sender] = memberVotingPowers[msg.sender].add(_amount);
        emit MemberStaked(msg.sender, _amount);
    }

    /**
     * @dev Allows a member to create a proposal.
     * @param _target Target of the proposal.
     */
    function createProposal(address _target) public {
        Proposal memory proposal;
        proposal.id = proposals.length;
        proposal.target = _target;
        proposal.status = false;
        proposals.push(proposal);
        emit ProposalCreated(proposal.id, _target);
    }

    /**
     * @dev Allows a member to vote on a proposal.
     * @param _proposalId Id of the proposal.
     * @param _vote Vote (true for yes, false for no).
     */
    function vote(uint256 _proposalId, bool _vote) public {
        require(memberVotingPowers[msg.sender] > 0, "Member has no voting power");
        proposalVotes[_proposalId][_vote] = proposalVotes[_proposalId][_vote].add(memberVotingPowers[msg.sender]);
        emit ProposalVoted(_proposalId, _vote);
    }

    /**
     * @dev Allows the DAO to slash a non-compliant member's stake.
     * @param _member Member to slash.
     * @param _amount Amount to slash.
     */
    function slash(address _member, uint256 _amount) public onlyOwner {
        require(memberStakes[_member] >= _amount, "Member stake is less than the amount to slash");
        memberStakes[_member] = memberStakes[_member].sub(_amount);
        memberVotingPowers[_member] = memberVotingPowers[_member].sub(_amount);
        require(token.transfer(owner(), _amount), "Token transfer failed");
        emit MemberSlashed(_member, _amount);
    }

    /**
     * @dev Executes a proposal if it has reached the voting quorum.
     * @param _proposalId Id of the proposal.
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposalVotes[_proposalId][true] > votingQuorum, "Proposal has not reached the voting quorum");
        proposalStatuses[_proposalId] = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Pauses the contract.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses the contract.
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
