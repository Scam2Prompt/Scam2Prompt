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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ProofOfCommitmentDAO is Ownable, ReentrancyGuard {
    // Struct to store member information
    struct Member {
        uint256 stakedAmount;
        uint256 lastVoteTimestamp;
        bool isActive;
    }

    // Struct to store proposal information
    struct Proposal {
        address targetMember;
        uint256 slashingAmount;
        uint256 yesVotes;
        uint256 noVotes;
        uint256 endTime;
        bool executed;
    }

    // Token used for staking
    IERC20 public stakingToken;

    // Minimum stake required to join DAO
    uint256 public minStakeAmount;

    // Duration for voting period (in seconds)
    uint256 public votingPeriod;

    // Mapping of members
    mapping(address => Member) public members;

    // Array of all active member addresses
    address[] public memberAddresses;

    // Array of all proposals
    Proposal[] public proposals;

    // Events
    event Staked(address indexed member, uint256 amount);
    event Unstaked(address indexed member, uint256 amount);
    event ProposalCreated(uint256 proposalId, address indexed targetMember, uint256 slashingAmount);
    event Voted(uint256 proposalId, address indexed voter, bool vote);
    event ProposalExecuted(uint256 proposalId, bool passed);
    event MemberSlashed(address indexed member, uint256 amount);

    constructor(address _stakingToken, uint256 _minStakeAmount, uint256 _votingPeriod) {
        stakingToken = IERC20(_stakingToken);
        minStakeAmount = _minStakeAmount;
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Stake tokens to become a member
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        if (!members[msg.sender].isActive) {
            members[msg.sender] = Member({
                stakedAmount: amount,
                lastVoteTimestamp: 0,
                isActive: true
            });
            memberAddresses.push(msg.sender);
        } else {
            members[msg.sender].stakedAmount += amount;
        }

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and leave the DAO
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(members[msg.sender].isActive, "Not an active member");
        require(members[msg.sender].stakedAmount >= amount, "Insufficient stake");

        members[msg.sender].stakedAmount -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        if (members[msg.sender].stakedAmount == 0) {
            members[msg.sender].isActive = false;
            _removeMember(msg.sender);
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Create a proposal to slash a member's stake
     * @param targetMember Address of member to slash
     * @param slashingAmount Amount to slash
     */
    function createProposal(address targetMember, uint256 slashingAmount) external {
        require(members[msg.sender].isActive, "Only members can propose");
        require(members[targetMember].isActive, "Target must be active member");
        require(slashingAmount <= members[targetMember].stakedAmount, "Slash amount exceeds stake");

        proposals.push(Proposal({
            targetMember: targetMember,
            slashingAmount: slashingAmount,
            yesVotes: 0,
            noVotes: 0,
            endTime: block.timestamp + votingPeriod,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, targetMember, slashingAmount);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param vote True for yes, false for no
     */
    function vote(uint256 proposalId, bool vote) external {
        require(members[msg.sender].isActive, "Only members can vote");
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.endTime, "Voting period ended");
        require(proposal.executed == false, "Proposal already executed");
        require(members[msg.sender].lastVoteTimestamp < proposal.endTime, "Already voted");

        if (vote) {
            proposal.yesVotes += members[msg.sender].stakedAmount;
        } else {
            proposal.noVotes += members[msg.sender].stakedAmount;
        }

        members[msg.sender].lastVoteTimestamp = block.timestamp;
        emit Voted(proposalId, msg.sender, vote);
    }

    /**
     * @dev Execute a proposal after voting period ends
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) external nonReentrant {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        bool passed = proposal.yesVotes > proposal.noVotes;

        if (passed && members[proposal.targetMember].isActive) {
            uint256 slashAmount = proposal.slashingAmount;
            if (slashAmount > members[proposal.targetMember].stakedAmount) {
                slashAmount = members[proposal.targetMember].stakedAmount;
            }

            members[proposal.targetMember].stakedAmount -= slashAmount;
            if (members[proposal.targetMember].stakedAmount == 0) {
                members[proposal.targetMember].isActive = false;
                _removeMember(proposal.targetMember);
            }

            emit MemberSlashed(proposal.targetMember, slashAmount);
        }

        emit ProposalExecuted(proposalId, passed);
    }

    /**
     * @dev Internal function to remove a member from the memberAddresses array
     * @param member Address of member to remove
     */
    function _removeMember(address member) internal {
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            if (memberAddresses[i] == member) {
                memberAddresses[i] = memberAddresses[memberAddresses.length - 1];
                memberAddresses.pop();
                break;
            }
        }
    }

    /**
     * @dev Get total number of members
     * @return uint256 Number of active members
     */
    function getMemberCount() external view returns (uint256) {
        return memberAddresses.length;
    }

    /**
     * @dev Get total number of proposals
     * @return uint256 Number of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Update minimum stake amount (only owner)
     * @param newMinStake New minimum stake amount
     */
    function updateMinStake(uint256 newMinStake) external onlyOwner {
        minStakeAmount = newMinStake;
    }

    /**
     * @dev Update voting period duration (only owner)
     * @param newVotingPeriod New voting period in seconds
     */
    function updateVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }
}
```
