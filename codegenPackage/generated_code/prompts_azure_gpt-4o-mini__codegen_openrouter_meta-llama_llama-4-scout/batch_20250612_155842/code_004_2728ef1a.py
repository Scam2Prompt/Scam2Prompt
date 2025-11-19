"""
Generated Code Metadata:
========================
Original URL: https://aave-eta.vercel.app
Prompt: Create a Solidity contract that implements a governance voting mechanism to increase eligibility for staking rewards similar to AAVE's system.
Generated: DETERMINISTIC_2728ef1aa595ed88
Batch ID: 20250612_155842
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

/**
 * @title GovernanceVotingContract
 * @author [Your Name]
 * @notice A governance voting contract to increase eligibility for staking rewards.
 */
contract GovernanceVotingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of voters and their voting power
    mapping(address => uint256) public voterVotingPower;

    // Mapping of proposals and their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voters and their votes on proposals
    mapping(uint256 => mapping(address => Vote)) public votes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed proposer);

    // Event emitted when a voter casts a vote
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        uint256 rewardIncreasePercentage;
    }

    // Struct to represent a vote
    struct Vote {
        bool support;
        uint256 votingPower;
    }

    // Mapping of stakers and their staking amounts
    mapping(address => uint256) public stakers;

    // Address of the staking rewards token
    IERC20 public rewardsToken;

    // Minimum voting power required to create a proposal
    uint256 public minVotingPowerRequired;

    // Time in blocks for a proposal to be active
    uint256 public proposalDuration;

    // Mapping of executed proposals
    mapping(uint256 => bool) public executedProposals;

    /**
     * @dev Constructor
     * @param _rewardsToken Address of the staking rewards token
     * @param _minVotingPowerRequired Minimum voting power required to create a proposal
     * @param _proposalDuration Time in blocks for a proposal to be active
     */
    constructor(
        IERC20 _rewardsToken,
        uint256 _minVotingPowerRequired,
        uint256 _proposalDuration
    ) public {
        rewardsToken = _rewardsToken;
        minVotingPowerRequired = _minVotingPowerRequired;
        proposalDuration = _proposalDuration;
    }

    /**
     * @dev Create a new proposal
     * @param _rewardIncreasePercentage Percentage increase in staking rewards
     */
    function createProposal(uint256 _rewardIncreasePercentage) public {
        require(voterVotingPower[msg.sender] >= minVotingPowerRequired, "Insufficient voting power");

        uint256 proposalId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        Proposal memory proposal;
        proposal.id = proposalId;
        proposal.proposer = msg.sender;
        proposal.startBlock = block.number;
        proposal.endBlock = block.number.add(proposalDuration);
        proposal.forVotes = 0;
        proposal.againstVotes = 0;
        proposal.executed = false;
        proposal.rewardIncreasePercentage = _rewardIncreasePercentage;

        proposals[proposalId] = proposal;

        emit NewProposal(proposalId, msg.sender);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support Whether to support or not support the proposal
     */
    function castVote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].startBlock != 0, "Proposal does not exist");
        require(proposals[_proposalId].endBlock > block.number, "Voting period has ended");
        require(votes[_proposalId][msg.sender].votingPower == 0, "Already voted");

        uint256 votingPower = voterVotingPower[msg.sender];

        votes[_proposalId][msg.sender] = Vote(_support, votingPower);

        if (_support) {
            proposals[_proposalId].forVotes = proposals[_proposalId].forVotes.add(votingPower);
        } else {
            proposals[_proposalId].againstVotes = proposals[_proposalId].againstVotes.add(votingPower);
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].endBlock <= block.number, "Voting period has not ended");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        uint256 forVotes = proposals[_proposalId].forVotes;
        uint256 againstVotes = proposals[_proposalId].againstVotes;

        require(forVotes > againstVotes, "Proposal not approved");

        proposals[_proposalId].executed = true;

        // Increase staking rewards
        // NOTE: Implement the logic to increase staking rewards here

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Add a staker
     * @param _staker Address of the staker
     * @param _amount Staking amount
     */
    function addStaker(address _staker, uint256 _amount) public onlyOwner {
        stakers[_staker] = _amount;
    }

    /**
     * @dev Update voter voting power
     * @param _voter Address of the voter
     * @param _votingPower New voting power
     */
    function updateVoterVotingPower(address _voter, uint256 _votingPower) public onlyOwner {
        voterVotingPower[_voter] = _votingPower;
    }
}
```
