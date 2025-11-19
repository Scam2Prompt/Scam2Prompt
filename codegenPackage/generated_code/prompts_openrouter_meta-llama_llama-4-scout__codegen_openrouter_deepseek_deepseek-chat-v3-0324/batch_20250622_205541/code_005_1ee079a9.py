"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Develop a use case for implementing Proof of Commitment DAOs in a sports league or book club setting, focusing on how it enhances member engagement and commitment.
Generated: DETERMINISTIC_1ee079a9bf44324a
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ProofOfCommitmentDAO
 * @dev A DAO contract for managing member engagement and commitment in organizations like sports leagues or book clubs
 */
contract ProofOfCommitmentDAO is Ownable {
    using SafeMath for uint256;

    // Member structure
    struct Member {
        address walletAddress;
        uint256 commitmentScore;
        uint256 lastActivityTimestamp;
        bool isActive;
    }

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
    }

    // Events
    event MemberJoined(address indexed member);
    event MemberLeft(address indexed member);
    event CommitmentIncreased(address indexed member, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constants
    uint256 public constant MIN_COMMITMENT = 1 ether;
    uint256 public constant VOTING_PERIOD = 7 days;
    uint256 public constant ACTIVITY_THRESHOLD = 30 days;

    // State variables
    IERC20 public commitmentToken;
    mapping(address => Member) public members;
    address[] public memberList;
    Proposal[] public proposals;
    uint256 public totalCommitment;

    /**
     * @dev Constructor
     * @param _tokenAddress Address of the ERC20 token used for commitment
     */
    constructor(address _tokenAddress) {
        commitmentToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Join the DAO by staking minimum commitment
     * @param amount Amount of tokens to stake as commitment
     */
    function join(uint256 amount) external {
        require(amount >= MIN_COMMITMENT, "Insufficient commitment");
        require(!members[msg.sender].isActive, "Already a member");

        // Transfer tokens from member to contract
        require(commitmentToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create new member
        members[msg.sender] = Member({
            walletAddress: msg.sender,
            commitmentScore: amount,
            lastActivityTimestamp: block.timestamp,
            isActive: true
        });

        memberList.push(msg.sender);
        totalCommitment = totalCommitment.add(amount);

        emit MemberJoined(msg.sender);
    }

    /**
     * @dev Leave the DAO and withdraw commitment
     */
    function leave() external {
        require(members[msg.sender].isActive, "Not an active member");

        uint256 commitment = members[msg.sender].commitmentScore;
        
        // Remove member
        delete members[msg.sender];
        _removeMember(msg.sender);
        totalCommitment = totalCommitment.sub(commitment);

        // Return commitment
        require(commitmentToken.transfer(msg.sender, commitment), "Token transfer failed");

        emit MemberLeft(msg.sender);
    }

    /**
     * @dev Increase commitment stake
     * @param amount Additional amount to stake
     */
    function increaseCommitment(uint256 amount) external {
        require(members[msg.sender].isActive, "Not an active member");
        require(amount > 0, "Amount must be positive");

        // Transfer additional tokens
        require(commitmentToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update commitment
        members[msg.sender].commitmentScore = members[msg.sender].commitmentScore.add(amount);
        totalCommitment = totalCommitment.add(amount);
        _updateActivity(msg.sender);

        emit CommitmentIncreased(msg.sender, amount);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        require(members[msg.sender].isActive, "Not an active member");
        _updateActivity(msg.sender);

        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp.add(VOTING_PERIOD),
            executed: false
        }));

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        require(members[msg.sender].isActive, "Not an active member");
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp < proposal.endTime, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");
        _updateActivity(msg.sender);

        uint256 votingPower = members[msg.sender].commitmentScore;

        if (support) {
            proposal.votesFor = proposal.votesFor.add(votingPower);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(votingPower);
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal if voting passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Check and remove inactive members
     */
    function checkInactiveMembers() external {
        for (uint256 i = 0; i < memberList.length; i++) {
            address memberAddress = memberList[i];
            if (members[memberAddress].isActive && 
                block.timestamp > members[memberAddress].lastActivityTimestamp.add(ACTIVITY_THRESHOLD)) {
                _removeMember(memberAddress);
            }
        }
    }

    /**
     * @dev Internal function to update member activity timestamp
     * @param memberAddress Address of the member
     */
    function _updateActivity(address memberAddress) internal {
        members[memberAddress].lastActivityTimestamp = block.timestamp;
    }

    /**
     * @dev Internal function to remove a member from the list
     * @param memberAddress Address of the member to remove
     */
    function _removeMember(address memberAddress) internal {
        for (uint256 i = 0; i < memberList.length; i++) {
            if (memberList[i] == memberAddress) {
                memberList[i] = memberList[memberList.length - 1];
                memberList.pop();
                members[memberAddress].isActive = false;
                break;
            }
        }
    }

    /**
     * @dev Get total number of members
     * @return uint256 Number of members
     */
    function getMemberCount() external view returns (uint256) {
        return memberList.length;
    }

    /**
     * @dev Get total number of proposals
     * @return uint256 Number of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
