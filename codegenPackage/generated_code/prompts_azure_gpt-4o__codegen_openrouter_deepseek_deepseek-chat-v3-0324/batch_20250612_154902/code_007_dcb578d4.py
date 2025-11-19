"""
Generated Code Metadata:
========================
Original URL: https://thenafl.org
Prompt: Generate a Solidity contract that enables governance voting and reward distribution mechanisms, similar to THENA FI's community-driven DeFi model.
Generated: DETERMINISTIC_dcb578d4f407ebb2
Batch ID: 20250612_154902
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

contract GovernanceVoting is Ownable, ReentrancyGuard {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEndTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        address proposer;
    }

    // Struct to represent a voter's details
    struct Voter {
        uint256 votingPower;
        bool hasVoted;
        bool voteDirection; // true = for, false = against
    }

    // Token used for voting power
    IERC20 public votingToken;

    // Minimum voting power required to create a proposal
    uint256 public proposalThreshold;

    // Duration of voting period in blocks
    uint256 public votingPeriod;

    // Minimum quorum required for a proposal to pass
    uint256 public quorum;

    // Array of all proposals
    Proposal[] public proposals;

    // Mapping from proposal ID to voter address to voter details
    mapping(uint256 => mapping(address => Voter)) public voters;

    // Mapping to track rewards for voters
    mapping(address => uint256) public rewards;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 voteEndTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votingPower
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event RewardClaimed(address indexed voter, uint256 amount);

    constructor(
        address _votingToken,
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorum
    ) {
        require(_votingToken != address(0), "Invalid token address");
        votingToken = IERC20(_votingToken);
        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
        quorum = _quorum;
    }

    /**
     * @notice Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower >= proposalThreshold, "Insufficient voting power");
        
        uint256 voteEndTime = block.timestamp + votingPeriod;
        proposals.push(
            Proposal({
                id: proposals.length,
                description: description,
                voteEndTime: voteEndTime,
                forVotes: 0,
                againstVotes: 0,
                executed: false,
                proposer: msg.sender
            })
        );

        emit ProposalCreated(proposals.length - 1, msg.sender, description, voteEndTime);
    }

    /**
     * @notice Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal (true = for, false = against)
     */
    function vote(uint256 proposalId, bool support) external nonReentrant {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.voteEndTime, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");

        Voter storage voter = voters[proposalId][msg.sender];
        require(!voter.hasVoted, "Already voted");

        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        voter.votingPower = votingPower;
        voter.hasVoted = true;
        voter.voteDirection = support;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @notice Execute a proposal if it has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external nonReentrant {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.voteEndTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;

        // Distribute rewards to voters who voted for the proposal
        _distributeRewards(proposalId);

        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Internal function to distribute rewards to voters
     * @param proposalId ID of the proposal
     */
    function _distributeRewards(uint256 proposalId) internal {
        Proposal storage proposal = proposals[proposalId];
        uint256 totalForVotes = proposal.forVotes;
        
        // Simple reward distribution: 1% of total for votes to each voter
        uint256 rewardPerVoter = totalForVotes / 100;
        
        // In a real implementation, you would use a more sophisticated reward mechanism
        for (uint256 i = 0; i < proposals.length; i++) {
            Voter storage voter = voters[proposalId][msg.sender];
            if (voter.hasVoted && voter.voteDirection) {
                rewards[msg.sender] += rewardPerVoter;
            }
        }
    }

    /**
     * @notice Claim voting rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(votingToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Update proposal threshold
     * @param newThreshold New proposal threshold
     */
    function setProposalThreshold(uint256 newThreshold) external onlyOwner {
        proposalThreshold = newThreshold;
    }

    /**
     * @notice Update voting period
     * @param newVotingPeriod New voting period in blocks
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }

    /**
     * @notice Update quorum
     * @param newQuorum New quorum value
     */
    function setQuorum(uint256 newQuorum) external onlyOwner {
        quorum = newQuorum;
    }

    /**
     * @notice Get total number of proposals
     * @return Total proposal count
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
