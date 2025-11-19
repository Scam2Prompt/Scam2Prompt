"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Generate code to create a DAO for database governance using DBDAO, allowing contributors to vote on database-related decisions.
Generated: DETERMINISTIC_a983b6f56a5c2408
Batch ID: 20250612_151232
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract DBGovernanceDAO is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        address proposer;
    }

    // Database change request structure
    struct DBChangeRequest {
        string sqlQuery;
        bool executed;
    }

    // Token used for voting
    IERC20 public governanceToken;

    // Minimum voting power required to create a proposal
    uint256 public proposalThreshold;

    // Voting duration in blocks
    uint256 public votingDuration;

    // Proposals mapping
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => DBChangeRequest) public dbChangeRequests;

    // Track proposals
    uint256 public proposalCount;

    // Track voters
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    EnumerableSet.AddressSet private _members;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event DBChangeExecuted(uint256 indexed proposalId, string sqlQuery);
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);

    constructor(
        address _governanceToken,
        uint256 _proposalThreshold,
        uint256 _votingDuration
    ) {
        require(_governanceToken != address(0), "Invalid token address");
        governanceToken = IERC20(_governanceToken);
        proposalThreshold = _proposalThreshold;
        votingDuration = _votingDuration;
    }

    modifier onlyMember() {
        require(isMember(msg.sender), "Not a DAO member");
        _;
    }

    function isMember(address _address) public view returns (bool) {
        return _members.contains(_address);
    }

    function addMember(address _member) external onlyOwner {
        require(!isMember(_member), "Already a member");
        _members.add(_member);
        emit MemberAdded(_member);
    }

    function removeMember(address _member) external onlyOwner {
        require(isMember(_member), "Not a member");
        _members.remove(_member);
        emit MemberRemoved(_member);
    }

    function getMembers() external view returns (address[] memory) {
        return _members.values();
    }

    function createProposal(
        string memory _description,
        string memory _sqlQuery
    ) external onlyMember {
        uint256 balance = governanceToken.balanceOf(msg.sender);
        require(balance >= proposalThreshold, "Insufficient voting power");

        proposalCount++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingDuration;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false,
            proposer: msg.sender
        });

        dbChangeRequests[proposalCount] = DBChangeRequest({
            sqlQuery: _sqlQuery,
            executed: false
        });

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            _description,
            startTime,
            endTime
        );
    }

    function vote(uint256 _proposalId, bool _support) external onlyMember {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!hasVoted[msg.sender][_proposalId], "Already voted");

        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        if (_support) {
            proposal.votesFor += votingPower;
        } else {
            proposal.votesAgainst += votingPower;
        }

        hasVoted[msg.sender][_proposalId] = true;
        emit Voted(_proposalId, msg.sender, _support, votingPower);
    }

    function executeProposal(uint256 _proposalId) external onlyMember {
        Proposal storage proposal = proposals[_proposalId];
        DBChangeRequest storage dbRequest = dbChangeRequests[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(!dbRequest.executed, "DB change already executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            dbRequest.executed = true;
            proposal.executed = true;
            emit DBChangeExecuted(_proposalId, dbRequest.sqlQuery);
        }

        emit ProposalExecuted(_proposalId);
    }

    function updateVotingDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration > 0, "Duration must be > 0");
        votingDuration = _newDuration;
    }

    function updateProposalThreshold(uint256 _newThreshold) external onlyOwner {
        proposalThreshold = _newThreshold;
    }
}
```
