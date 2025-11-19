"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Create a Solidity smart contract example that integrates with MDEX's DAO governance mechanism to enable voting on community proposals using xMDX vouchers.
Generated: DETERMINISTIC_52b2316bb51ce059
Batch ID: 20250612_145823
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
 * @title MDEX DAO Governance Contract
 * @author [Your Name]
 * @notice This contract enables voting on community proposals using xMDX vouchers
 */
contract MDEXDAOGovernance {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user voting history
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // xMDX token contract
    IERC20 public xMDX;

    // MDEX DAO governance address
    address public governanceAddress;

    // Proposal count
    uint256 public proposalCount;

    // Quorum threshold (percentage)
    uint256 public quorumThreshold;

    // Voting duration (in seconds)
    uint256 public votingDuration;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event Voted(address indexed user, uint256 indexed proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Struct representing a proposal
     */
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @dev Constructor
     * @param _xMDX xMDX token contract address
     * @param _governanceAddress MDEX DAO governance address
     * @param _quorumThreshold Quorum threshold (percentage)
     * @param _votingDuration Voting duration (in seconds)
     */
    constructor(
        address _xMDX,
        address _governanceAddress,
        uint256 _quorumThreshold,
        uint256 _votingDuration
    ) public {
        require(_xMDX != address(0), "xMDX token contract address is zero");
        require(_governanceAddress != address(0), "MDEX DAO governance address is zero");
        require(_quorumThreshold > 0 && _quorumThreshold <= 100, "Invalid quorum threshold");
        require(_votingDuration > 0, "Voting duration must be greater than zero");

        xMDX = IERC20(_xMDX);
        governanceAddress = _governanceAddress;
        quorumThreshold = _quorumThreshold;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal
     * @param _description Proposal description
     */
    function createProposal(string memory _description) public {
        require(msg.sender == governanceAddress, "Only governance address can create proposals");

        Proposal memory proposal;
        proposal.id = ++proposalCount;
        proposal.description = _description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(votingDuration);
        proposals[proposalCount] = proposal;

        emit ProposalCreated(proposal.id, proposal.description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].startTime != 0, "Proposal does not exist");
        require(proposals[_proposalId].endTime > block.timestamp, "Voting period has ended");
        require(userVotes[msg.sender][_proposalId] == false, "User has already voted");

        Proposal storage proposal = proposals[_proposalId];
        require(xMDX.balanceOf(msg.sender) > 0, "User does not hold xMDX vouchers");

        if (_support) {
            proposal.yesVotes = proposal.yesVotes.add(xMDX.balanceOf(msg.sender));
        } else {
            proposal.noVotes = proposal.noVotes.add(xMDX.balanceOf(msg.sender));
        }

        userVotes[msg.sender][_proposalId] = true;

        emit Voted(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Execute a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].endTime <= block.timestamp, "Voting period has not ended");
        require(proposals[_proposalId].executed == false, "Proposal has already been executed");

        Proposal storage proposal = proposals[_proposalId];
        uint256 totalVotes = proposal.yesVotes.add(proposal.noVotes);
        uint256 quorum = totalVotes.mul(quorumThreshold).div(100);

        require(proposal.yesVotes >= quorum, "Proposal did not meet quorum threshold");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }
}
```
