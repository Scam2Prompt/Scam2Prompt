"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Create a Solidity contract for a community-driven token distribution system that allows users to vote on how $WING tokens should be allocated in future phases.
Generated: DETERMINISTIC_3c7206435c704c84
Batch ID: 20250612_155037
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
 * @title WingTokenDistribution
 * @author [Your Name]
 * @notice A community-driven token distribution system for $WING tokens.
 */
contract WingTokenDistribution is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their voting power
    mapping (address => uint256) public votingPower;

    // Mapping of proposals to their details
    mapping (uint256 => Proposal) public proposals;

    // Mapping of users to their votes
    mapping (address => mapping (uint256 => bool)) public userVotes;

    // $WING token contract
    ERC20 public wingToken;

    // Total number of proposals
    uint256 public proposalCount;

    // Minimum voting power required to create a proposal
    uint256 public minVotingPower;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, address indexed creator, uint256 amount, address[] recipients);

    // Event emitted when a user votes on a proposal
    event Voted(address indexed user, uint256 indexed proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Struct representing a proposal
     */
    struct Proposal {
        uint256 id;
        address creator;
        uint256 amount;
        address[] recipients;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @dev Constructor
     * @param _wingToken $WING token contract address
     * @param _minVotingPower Minimum voting power required to create a proposal
     * @param _votingDuration Voting duration in seconds
     */
    constructor(address _wingToken, uint256 _minVotingPower, uint256 _votingDuration) {
        wingToken = ERC20(_wingToken);
        minVotingPower = _minVotingPower;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Creates a new proposal
     * @param _amount Amount of $WING tokens to distribute
     * @param _recipients List of recipient addresses
     */
    function createProposal(uint256 _amount, address[] memory _recipients) public {
        require(votingPower[msg.sender] >= minVotingPower, "Insufficient voting power");
        require(_amount > 0, "Invalid amount");
        require(_recipients.length > 0, "No recipients specified");

        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.creator = msg.sender;
        proposal.amount = _amount;
        proposal.recipients = _recipients;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(votingDuration);
        proposal.executed = false;

        proposals[proposalCount] = proposal;
        proposalCount++;

        emit ProposalCreated(proposal.id, proposal.creator, proposal.amount, proposal.recipients);
    }

    /**
     * @dev Votes on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].startTime > 0, "Proposal not found");
        require(proposals[_proposalId].endTime > block.timestamp, "Voting period ended");
        require(!userVotes[msg.sender][_proposalId], "Already voted");

        if (_support) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(votingPower[msg.sender]);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(votingPower[msg.sender]);
        }

        userVotes[msg.sender][_proposalId] = true;

        emit Voted(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Executes a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].endTime <= block.timestamp, "Voting period not ended");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        uint256 totalVotes = proposals[_proposalId].yesVotes.add(proposals[_proposalId].noVotes);
        require(proposals[_proposalId].yesVotes > totalVotes.div(2), "Proposal not approved");

        proposals[_proposalId].executed = true;

        // Transfer $WING tokens to recipients
        for (uint256 i = 0; i < proposals[_proposalId].recipients.length; i++) {
            wingToken.transfer(proposals[_proposalId].recipients[i], proposals[_proposalId].amount.div(proposals[_proposalId].recipients.length));
        }

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Increases user's voting power
     * @param _user User address
     * @param _amount Amount of voting power to add
     */
    function increaseVotingPower(address _user, uint256 _amount) public {
        require(msg.sender == address(wingToken), "Only $WING token contract can increase voting power");
        votingPower[_user] = votingPower[_user].add(_amount);
    }

    /**
     * @dev Decreases user's voting power
     * @param _user User address
     * @param _amount Amount of voting power to remove
     */
    function decreaseVotingPower(address _user, uint256 _amount) public {
        require(msg.sender == address(wingToken), "Only $WING token contract can decrease voting power");
        require(votingPower[_user] >= _amount, "Insufficient voting power");
        votingPower[_user] = votingPower[_user].sub(_amount);
    }
}
```
