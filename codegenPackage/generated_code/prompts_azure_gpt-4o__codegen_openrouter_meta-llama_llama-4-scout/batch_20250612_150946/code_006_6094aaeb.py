"""
Generated Code Metadata:
========================
Original URL: https://betswirl.pages.dev
Prompt: Create a Solidity contract to enable users to vote on upcoming games or features on the BetSwirl platform.
Generated: DETERMINISTIC_6094aaeb5582fa5b
Batch ID: 20250612_150946
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BetSwirl Voting Contract
 * @author [Your Name]
 * @notice Enables users to vote on upcoming games or features on the BetSwirl platform
 */
contract BetSwirlVoting is Ownable {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public userVotingPower;

    // Mapping of user addresses to their vote history
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalName);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is closed
    event ProposalClosed(uint256 indexed proposalId);

    // Structure representing a proposal
    struct Proposal {
        uint256 id;
        string name;
        uint256 yesVotes;
        uint256 noVotes;
        bool isOpen;
        uint256 votingPowerRequired;
        IERC20 votingToken;
    }

    // Mapping of proposal ID to the number of proposals
    uint256 public proposalCount;

    /**
     * @notice Initializes the contract with the voting token and voting power required
     * @param _votingToken The ERC20 token used for voting
     * @param _votingPowerRequired The minimum voting power required to create a proposal
     */
    constructor(IERC20 _votingToken, uint256 _votingPowerRequired) {
        proposalCount = 0;
        userVotingPower[msg.sender] = 100; // Initialize owner's voting power
        emit NewProposal(0, "Contract Initialization");
        proposals[0] = Proposal(
            0,
            "Contract Initialization",
            0,
            0,
            false,
            _votingPowerRequired,
            _votingToken
        );
    }

    /**
     * @notice Creates a new proposal
     * @param _proposalName The name of the proposal
     * @param _votingPowerRequired The minimum voting power required to vote on the proposal
     */
    function createProposal(string memory _proposalName, uint256 _votingPowerRequired) public {
        require(userVotingPower[msg.sender] > 0, "User has no voting power");
        require(_votingPowerRequired > 0, "Voting power required must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal(
            proposalCount,
            _proposalName,
            0,
            0,
            true,
            _votingPowerRequired,
            proposals[0].votingToken
        );

        emit NewProposal(proposalCount, _proposalName);
    }

    /**
     * @notice Casts a vote on a proposal
     * @param _proposalId The ID of the proposal
     * @param _vote The vote (true for yes, false for no)
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        require(proposals[_proposalId].isOpen, "Proposal is not open");
        require(userVotingPower[msg.sender] >= proposals[_proposalId].votingPowerRequired, "User does not have sufficient voting power");

        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(1);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(1);
        }

        userVotes[msg.sender][_proposalId] = true;

        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @notice Closes a proposal
     * @param _proposalId The ID of the proposal
     */
    function closeProposal(uint256 _proposalId) public onlyOwner {
        require(proposals[_proposalId].isOpen, "Proposal is already closed");

        proposals[_proposalId].isOpen = false;

        emit ProposalClosed(_proposalId);
    }

    /**
     * @notice Updates a user's voting power
     * @param _user The user's address
     * @param _votingPower The new voting power
     */
    function updateUserVotingPower(address _user, uint256 _votingPower) public onlyOwner {
        userVotingPower[_user] = _votingPower;
    }

    /**
     * @notice Updates the voting token
     * @param _newVotingToken The new voting token
     */
    function updateVotingToken(IERC20 _newVotingToken) public onlyOwner {
        proposals[0].votingToken = _newVotingToken;
    }
}
```
