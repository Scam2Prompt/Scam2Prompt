"""
Generated Code Metadata:
========================
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Generate a smart contract code snippet in Solidity that implements a simple voting mechanism with rewards, similar to Mitosis's voting system, on a compatible blockchain platform.
Generated: DETERMINISTIC_187a8e607e8d2915
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SimpleVotingContract
 * @author [Your Name]
 * @notice A simple voting contract with rewards
 */
contract SimpleVotingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of voters to their voting power
    mapping(address => uint256) public voterPower;

    // Mapping of proposals to their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voters to their votes
    mapping(address => mapping(uint256 => bool)) public voterVotes;

    // ERC20 token for rewards
    IERC20 public rewardToken;

    // Total number of proposals
    uint256 public proposalCount;

    // Voting power required for a proposal to pass
    uint256 public votingPowerRequired;

    // Reward amount for voters
    uint256 public rewardAmount;

    /**
     * @notice Event emitted when a new proposal is created
     * @param proposalId The ID of the proposal
     * @param creator The address of the proposal creator
     * @param description The description of the proposal
     */
    event NewProposal(uint256 proposalId, address creator, string description);

    /**
     * @notice Event emitted when a voter casts a vote
     * @param voter The address of the voter
     * @param proposalId The ID of the proposal
     * @param vote Whether the voter voted for or against the proposal
     */
    event VoteCast(address voter, uint256 proposalId, bool vote);

    /**
     * @notice Event emitted when a proposal is rewarded
     * @param proposalId The ID of the proposal
     */
    event ProposalRewarded(uint256 proposalId);

    /**
     * @param _rewardToken The address of the ERC20 token for rewards
     * @param _votingPowerRequired The voting power required for a proposal to pass
     * @param _rewardAmount The reward amount for voters
     */
    constructor(
        IERC20 _rewardToken,
        uint256 _votingPowerRequired,
        uint256 _rewardAmount
    ) public {
        rewardToken = _rewardToken;
        votingPowerRequired = _votingPowerRequired;
        rewardAmount = _rewardAmount;
    }

    /**
     * @notice Creates a new proposal
     * @param _description The description of the proposal
     */
    function createProposal(string memory _description) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(
            proposalCount,
            msg.sender,
            _description,
            0,
            0,
            false
        );
        emit NewProposal(proposalCount, msg.sender, _description);
    }

    /**
     * @notice Casts a vote on a proposal
     * @param _proposalId The ID of the proposal
     * @param _vote Whether to vote for or against the proposal
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        require(
            proposals[_proposalId].creator != address(0),
            "Proposal does not exist"
        );
        require(voterVotes[msg.sender][_proposalId] == false, "Already voted");

        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId]
                .yesVotes
                .add(voterPower[msg.sender]);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId]
                .noVotes
                .add(voterPower[msg.sender]);
        }

        voterVotes[msg.sender][_proposalId] = true;

        emit VoteCast(msg.sender, _proposalId, _vote);

        // Check if the proposal has passed
        if (
            proposals[_proposalId].yesVotes >= votingPowerRequired &&
            !proposals[_proposalId].rewarded
        ) {
            rewardVoters(_proposalId);
        }
    }

    /**
     * @notice Rewards voters for a proposal
     * @param _proposalId The ID of the proposal
     */
    function rewardVoters(uint256 _proposalId) internal {
        for (address voter in voterVotes) {
            if (voterVotes[voter][_proposalId]) {
                rewardToken.transfer(voter, rewardAmount);
            }
        }

        proposals[_proposalId].rewarded = true;

        emit ProposalRewarded(_proposalId);
    }

    /**
     * @notice Updates the voting power of a voter
     * @param _voter The address of the voter
     * @param _power The new voting power
     */
    function updateVoterPower(address _voter, uint256 _power) public {
        voterPower[_voter] = _power;
    }

    /**
     * @notice Struct representing a proposal
     */
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool rewarded;
    }
}
```
