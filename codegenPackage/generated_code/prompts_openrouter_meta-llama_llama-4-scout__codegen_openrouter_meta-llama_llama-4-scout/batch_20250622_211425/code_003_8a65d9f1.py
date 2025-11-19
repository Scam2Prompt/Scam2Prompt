"""
Generated Code Metadata:
========================
Original URL: https://fwbn.pages.dev
Prompt: Design a smart contract for a DAO like Friends With Benefits, outlining the functionality for token-based membership and participation rewards.
Generated: DETERMINISTIC_8a65d9f1fbf66091
Batch ID: 20250622_211425
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Friends With Benefits DAO Smart Contract
 * @author [Your Name]
 * @notice A DAO smart contract for token-based membership and participation rewards
 */
contract FWBDAO {
    // Mapping of members and their token balances
    mapping (address => uint256) public memberBalances;

    // Mapping of proposal votes
    mapping (uint256 => mapping (address => bool)) public proposalVotes;

    // Mapping of proposal rewards
    mapping (uint256 => uint256) public proposalRewards;

    // Event emitted when a new member joins
    event NewMember(address indexed member, uint256 tokenAmount);

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed member, uint256 rewardAmount);

    // Token contract instance
    ERC20 public token;

    // Minimum token balance required for membership
    uint256 public minTokenBalance;

    // Total proposals
    uint256 public proposalCount;

    // Mapping of proposal details
    mapping (uint256 => Proposal) public proposals;

    /**
     * @notice Struct representing a proposal
     */
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
    }

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the token contract
     * @param _minTokenBalance Minimum token balance required for membership
     */
    constructor(address _tokenAddress, uint256 _minTokenBalance) {
        token = ERC20(_tokenAddress);
        minTokenBalance = _minTokenBalance;
    }

    /**
     * @notice Join the DAO by transferring tokens
     * @param _tokenAmount Amount of tokens to transfer
     */
    function joinDAO(uint256 _tokenAmount) external {
        require(_tokenAmount >= minTokenBalance, "Insufficient token balance");
        require(token.transferFrom(msg.sender, address(this), _tokenAmount), "Token transfer failed");

        memberBalances[msg.sender] = memberBalances[msg.sender] + _tokenAmount;
        emit NewMember(msg.sender, _tokenAmount);
    }

    /**
     * @notice Create a new proposal
     * @param _proposalDescription Description of the proposal
     */
    function createProposal(string memory _proposalDescription) external {
        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.description = _proposalDescription;
        proposal.voteCount = 0;
        proposal.executed = false;

        proposals[proposalCount] = proposal;
        proposalCount++;

        emit ProposalCreated(proposal.id, proposal.description);
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Vote (true for yes, false for no)
     */
    function voteOnProposal(uint256 _proposalId, bool _vote) external {
        require(proposals[_proposalId].executed == false, "Proposal already executed");
        require(memberBalances[msg.sender] >= minTokenBalance, "Insufficient token balance");

        proposalVotes[_proposalId][msg.sender] = _vote;
        if (_vote) {
            proposals[_proposalId].voteCount++;
        }

        emit ProposalVoted(_proposalId, msg.sender, _vote);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) external {
        require(proposals[_proposalId].executed == false, "Proposal already executed");
        require(proposals[_proposalId].voteCount >= (memberBalances[msg.sender] * 2), "Insufficient votes");

        proposals[_proposalId].executed = true;
        proposalRewards[_proposalId] = token.balanceOf(address(this)) / 10;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Claim a reward
     * @param _proposalId ID of the proposal
     */
    function claimReward(uint256 _proposalId) external {
        require(proposals[_proposalId].executed == true, "Proposal not executed");
        require(proposalVotes[_proposalId][msg.sender] == true, "You did not vote for this proposal");

        uint256 reward = proposalRewards[_proposalId];
        require(reward > 0, "No reward available");

        token.transfer(msg.sender, reward);
        proposalRewards[_proposalId] = 0;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Get member balance
     * @param _member Address of the member
     * @return uint256 Member balance
     */
    function getMemberBalance(address _member) external view returns (uint256) {
        return memberBalances[_member];
    }

    /**
     * @notice Get proposal details
     * @param _proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, bool) {
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
