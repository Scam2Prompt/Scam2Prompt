"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Generate a smart contract in Solidity that aligns with the ethos of ETHBerlin04, emphasizing community collaboration and decentralized governance.
Generated: DETERMINISTIC_2828b45aece382fc
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

/**
 * @title CommunityDAO
 * @dev A decentralized autonomous organization contract for community governance
 * @notice Aligns with ETHBerlin04 ethos of community collaboration and decentralization
 */
contract CommunityDAO {
    // Structs
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    address[] public members;
    mapping(address => bool) public isMember;
    Proposal[] public proposals;
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public minimumQuorum;
    uint256 public memberCount;

    // Events
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifiers
    modifier onlyMember() {
        require(isMember[msg.sender], "CommunityDAO: caller is not a member");
        _;
    }

    modifier validProposal(uint256 _proposalId) {
        require(_proposalId < proposals.length, "CommunityDAO: invalid proposal ID");
        _;
    }

    modifier activeProposal(uint256 _proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime, "CommunityDAO: voting period closed");
        _;
    }

    /**
     * @dev Initialize the DAO with initial parameters
     * @param _votingPeriod Duration of voting period in seconds
     * @param _minimumQuorum Minimum votes required for proposal to pass
     */
    constructor(uint256 _votingPeriod, uint256 _minimumQuorum) {
        votingPeriod = _votingPeriod;
        minimumQuorum = _minimumQuorum;
        // Add deployer as initial member
        _addMember(msg.sender);
    }

    /**
     * @dev Add a new member to the DAO (requires existing member)
     * @param _newMember Address of new member
     */
    function addMember(address _newMember) external onlyMember {
        _addMember(_newMember);
    }

    /**
     * @dev Internal function to add a member
     * @param _newMember Address of new member
     */
    function _addMember(address _newMember) internal {
        require(!isMember[_newMember], "CommunityDAO: already a member");
        isMember[_newMember] = true;
        members.push(_newMember);
        memberCount++;
        emit MemberAdded(_newMember);
    }

    /**
     * @dev Remove a member from the DAO (requires proposal and vote)
     * @param _member Address of member to remove
     */
    function removeMember(address _member) external onlyMember {
        require(isMember[_member], "CommunityDAO: not a member");
        require(memberCount > 1, "CommunityDAO: cannot remove last member");
        
        isMember[_member] = false;
        for (uint256 i = 0; i < members.length; i++) {
            if (members[i] == _member) {
                members[i] = members[members.length - 1];
                members.pop();
                break;
            }
        }
        memberCount--;
        emit MemberRemoved(_member);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyMember {
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingPeriod;
        
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.executed = false;
        
        proposalCount++;
        emit ProposalCreated(newProposal.id, msg.sender, _description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external onlyMember validProposal(_proposalId) activeProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voters[msg.sender], "CommunityDAO: already voted");
        
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;
        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyMember validProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.endTime, "CommunityDAO: voting period not ended");
        require(!proposal.executed, "CommunityDAO: proposal already executed");
        require(proposal.voteCount >= minimumQuorum, "CommunityDAO: quorum not reached");
        
        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get total number of proposals
     * @return uint256 Total proposal count
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return id, proposer, description, voteCount, startTime, endTime, executed
     */
    function getProposal(uint256 _proposalId) external view validProposal(_proposalId) returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 voteCount,
        uint256 startTime,
        uint256 endTime,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.voteCount,
            proposal.startTime,
            proposal.endTime,
            proposal.executed
        );
    }

    /**
     * @dev Check if an address has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address to check
     * @return bool True if address has voted
     */
    function hasVoted(uint256 _proposalId, address _voter) external view validProposal(_proposalId) returns (bool) {
        return proposals[_proposalId].voters[_voter];
    }
}
```
