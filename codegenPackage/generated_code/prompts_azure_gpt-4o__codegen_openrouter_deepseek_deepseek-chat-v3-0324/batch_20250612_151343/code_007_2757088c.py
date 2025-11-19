"""
Generated Code Metadata:
========================
Original URL: https://renqpresale.pages.dev
Prompt: Generate a Solidity smart contract for managing RenQ Finance's DAO governance system, allowing $RENQ token holders to propose, discuss, and vote on community-driven initiatives.
Generated: DETERMINISTIC_2757088ca342c5c1
Batch ID: 20250612_151343
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

contract RenQDAO is Ownable {
    using SafeMath for uint256;

    IERC20 public renqToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Governance parameters
    uint256 public proposalThreshold;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;

    // Proposals tracking
    Proposal[] public proposals;
    uint256 public proposalCount;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string title,
        string description,
        uint256 createTime,
        uint256 duration
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        uint8 support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event GovernanceParametersUpdated(
        uint256 proposalThreshold,
        uint256 votingPeriod,
        uint256 quorumPercentage
    );

    constructor(
        address _renqToken,
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) {
        require(_renqToken != address(0), "Invalid token address");
        require(_quorumPercentage <= 100, "Quorum too high");

        renqToken = IERC20(_renqToken);
        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @notice Create a new proposal
     * @param _title Title of the proposal
     * @param _description Description of the proposal
     */
    function propose(string memory _title, string memory _description) external {
        uint256 renqBalance = renqToken.balanceOf(msg.sender);
        require(renqBalance >= proposalThreshold, "Insufficient RENQ balance");
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        uint256 proposalId = proposalCount;
        proposalCount++;

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.title = _title;
        newProposal.description = _description;
        newProposal.createTime = block.timestamp;
        newProposal.duration = votingPeriod;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.abstainVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            _title,
            _description,
            block.timestamp,
            votingPeriod
        );
    }

    /**
     * @notice Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support Vote type: 0=against, 1=for, 2=abstain
     */
    function vote(uint256 _proposalId, uint8 _support) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(_support <= 2, "Invalid vote type");

        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.hasVoted[msg.sender], "Already voted");
        require(
            block.timestamp <= proposal.createTime.add(proposal.duration),
            "Voting period ended"
        );

        uint256 renqBalance = renqToken.balanceOf(msg.sender);
        require(renqBalance > 0, "No RENQ tokens to vote");

        proposal.hasVoted[msg.sender] = true;

        if (_support == 0) {
            proposal.againstVotes = proposal.againstVotes.add(renqBalance);
        } else if (_support == 1) {
            proposal.forVotes = proposal.forVotes.add(renqBalance);
        } else if (_support == 2) {
            proposal.abstainVotes = proposal.abstainVotes.add(renqBalance);
        }

        emit VoteCast(msg.sender, _proposalId, _support, renqBalance);
    }

    /**
     * @notice Execute a proposal if it has passed
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        require(!proposal.executed, "Proposal already executed");
        require(
            block.timestamp > proposal.createTime.add(proposal.duration),
            "Voting period not ended"
        );

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes).add(
            proposal.abstainVotes
        );
        uint256 totalSupply = renqToken.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);

        require(totalVotes >= quorum, "Quorum not reached");
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal did not pass"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Update governance parameters (onlyOwner)
     * @param _proposalThreshold New proposal threshold
     * @param _votingPeriod New voting period in seconds
     * @param _quorumPercentage New quorum percentage (0-100)
     */
    function updateGovernanceParameters(
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) external onlyOwner {
        require(_quorumPercentage <= 100, "Quorum too high");

        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;

        emit GovernanceParametersUpdated(
            _proposalThreshold,
            _votingPeriod,
            _quorumPercentage
        );
    }

    /**
     * @notice Get proposal details
     * @param _proposalId ID of the proposal
     * @return Tuple containing proposal details
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            string memory title,
            string memory description,
            uint256 createTime,
            uint256 duration,
            uint256 forVotes,
            uint256 againstVotes,
            uint256 abstainVotes,
            bool executed
        )
    {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        return (
            proposal.id,
            proposal.proposer,
            proposal.title,
            proposal.description,
            proposal.createTime,
            proposal.duration,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.abstainVotes,
            proposal.executed
        );
    }

    /**
     * @notice Check if an address has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address to check
     * @return True if the address has voted
     */
    function hasVoted(uint256 _proposalId, address _voter)
        external
        view
        returns (bool)
    {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        return proposals[_proposalId].hasVoted[_voter];
    }
}
```
