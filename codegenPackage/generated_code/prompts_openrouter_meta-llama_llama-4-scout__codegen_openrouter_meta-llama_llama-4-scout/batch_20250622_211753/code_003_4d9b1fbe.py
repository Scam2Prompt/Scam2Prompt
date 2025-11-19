"""
Generated Code Metadata:
========================
Original URL: https://weneedtomakeitrain.pages.dev
Prompt: Design a smart contract for a Vote-To-Earn mechanism, where token holders can vote on proposals and earn rewards in $FLOCK tokens.
Generated: DETERMINISTIC_4d9b1fbed2be6f29
Batch ID: 20250622_211753
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
 * @title VoteToEarn contract
 * @author [Your Name]
 * @notice This contract implements a Vote-To-Earn mechanism where token holders can vote on proposals and earn rewards in $FLOCK tokens.
 */
contract VoteToEarn is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of proposal IDs to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their earned rewards
    mapping(address => uint256) public earnedRewards;

    // Total number of proposals
    uint256 public totalProposals;

    // Address of the $FLOCK token contract
    address public flockTokenAddress;

    // Reward per vote
    uint256 public rewardPerVote;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event Voted(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is rewarded
    event Rewarded(uint256 indexed proposalId, uint256 reward);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool isRewarded;
    }

    /**
     * @dev Constructor
     * @param _flockTokenAddress Address of the $FLOCK token contract
     * @param _rewardPerVote Reward per vote
     */
    constructor(address _flockTokenAddress, uint256 _rewardPerVote) {
        require(_flockTokenAddress != address(0), "Flock token address cannot be zero");
        require(_rewardPerVote > 0, "Reward per vote must be greater than zero");

        flockTokenAddress = _flockTokenAddress;
        rewardPerVote = _rewardPerVote;
    }

    /**
     * @dev Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        Proposal memory proposal;
        proposal.id = ++totalProposals;
        proposal.description = _description;
        proposals[proposal.id] = proposal;

        emit NewProposal(proposal.id, proposal.description);
    }

    /**
     * @dev Votes on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Vote (true for yes, false for no)
     */
    function vote(uint256 _proposalId, bool _vote) public {
        require(proposals[_proposalId].id > 0, "Proposal does not exist");

        // Get the user's voting power
        uint256 _votingPower = votingPower[msg.sender];

        // Update the proposal's votes
        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(_votingPower);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(_votingPower);
        }

        // Update the user's earned rewards
        earnedRewards[msg.sender] = earnedRewards[msg.sender].add(rewardPerVote.mul(_votingPower));

        emit Voted(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Rewards a proposal
     * @param _proposalId ID of the proposal
     */
    function rewardProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].id > 0, "Proposal does not exist");
        require(!proposals[_proposalId].isRewarded, "Proposal already rewarded");

        // Calculate the total reward
        uint256 _totalReward = rewardPerVote.mul(proposals[_proposalId].yesVotes);

        // Transfer the reward to the proposal's voters
        ERC20(flockTokenAddress).transfer(msg.sender, _totalReward);

        // Mark the proposal as rewarded
        proposals[_proposalId].isRewarded = true;

        emit Rewarded(_proposalId, _totalReward);
    }

    /**
     * @dev Updates a user's voting power
     * @param _user Address of the user
     * @param _votingPower New voting power
     */
    function updateVotingPower(address _user, uint256 _votingPower) public {
        require(_user != address(0), "User address cannot be zero");
        require(_votingPower > 0, "Voting power must be greater than zero");

        votingPower[_user] = _votingPower;
    }

    /**
     * @dev Withdraws earned rewards
     */
    function withdrawRewards() public {
        require(earnedRewards[msg.sender] > 0, "No rewards to withdraw");

        // Transfer the rewards to the user
        ERC20(flockTokenAddress).transfer(msg.sender, earnedRewards[msg.sender]);

        // Reset the user's earned rewards
        earnedRewards[msg.sender] = 0;
    }
}
```
