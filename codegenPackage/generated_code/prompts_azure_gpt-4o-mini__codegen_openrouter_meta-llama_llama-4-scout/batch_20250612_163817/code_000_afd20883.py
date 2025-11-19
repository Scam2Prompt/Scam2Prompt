"""
Generated Code Metadata:
========================
Original URL: https://agora-next-m1q953hrk-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora framework mentioned on the Optimism Agora site?
Generated: DETERMINISTIC_afd20883576d77b6
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for implementing on-chain governance using the Agora framework. However, I need to clarify that I'll be providing an example in Solidity, as Agora is a framework for building on-chain governance systems on Ethereum and EVM-compatible chains.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Agora Governance Contract
contract AgoraGovernance {
    // Using SafeMath for uint256
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping (uint256 => Proposal) public proposals;

    // Mapping of user voting power
    mapping (address => uint256) public votingPower;

    // Mapping of user votes
    mapping (uint256 => mapping (address => Vote)) public votes;

    // Proposal counters
    uint256 public proposalCount;

    // Governance token
    IERC20 public governanceToken;

    // Quorum threshold
    uint256 public quorumThreshold;

    // Voting duration
    uint256 public votingDuration;

    // Struct for proposals
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Struct for votes
    struct Vote {
        bool support;
        uint256 votingPower;
    }

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 id, address proposer, string description);

    // Event emitted when a user votes on a proposal
    event Voted(uint256 proposalId, address voter, bool support, uint256 votingPower);

    // Event emitted when a proposal is executed
    event Executed(uint256 proposalId);

    // Constructor
    constructor(IERC20 _governanceToken, uint256 _quorumThreshold, uint256 _votingDuration) public {
        governanceToken = _governanceToken;
        quorumThreshold = _quorumThreshold;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public {
        // Require user has voting power
        require(votingPower[msg.sender] > 0, "User has no voting power");

        // Create a new proposal
        Proposal memory proposal;
        proposal.id = proposalCount++;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(votingDuration);
        proposals[proposal.id] = proposal;

        // Emit event
        emit ProposalCreated(proposal.id, proposal.proposer, proposal.description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId, bool _support) public {
        // Require proposal exists
        require(proposals[_proposalId].startTime > 0, "Proposal does not exist");

        // Require voting period is active
        require(block.timestamp >= proposals[_proposalId].startTime && block.timestamp <= proposals[_proposalId].endTime, "Voting period is not active");

        // Get user's voting power
        uint256 userVotingPower = votingPower[msg.sender];

        // Require user has voting power
        require(userVotingPower > 0, "User has no voting power");

        // Check if user has already voted
        if (votes[_proposalId][msg.sender].votingPower > 0) {
            // Update existing vote
            if (votes[_proposalId][msg.sender].support != _support) {
                // Update proposal votes
                if (_support) {
                    proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(userVotingPower);
                    proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.sub(userVotingPower);
                } else {
                    proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.sub(userVotingPower);
                    proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(userVotingPower);
                }
            }
        } else {
            // Cast new vote
            if (_support) {
                proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(userVotingPower);
            } else {
                proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(userVotingPower);
            }
        }

        // Update user's vote
        votes[_proposalId][msg.sender] = Vote(_support, userVotingPower);

        // Emit event
        emit Voted(_proposalId, msg.sender, _support, userVotingPower);
    }

    // Function to execute a proposal
    function executeProposal(uint256 _proposalId) public {
        // Require proposal exists
        require(proposals[_proposalId].startTime > 0, "Proposal does not exist");

        // Require proposal has ended
        require(block.timestamp > proposals[_proposalId].endTime, "Proposal has not ended");

        // Require quorum is met
        uint256 totalVotes = proposals[_proposalId].yesVotes.add(proposals[_proposalId].noVotes);
        require(totalVotes >= quorumThreshold, "Quorum not met");

        // Require proposal was not already executed
        require(!proposals[_proposalId].executed, "Proposal was already executed");

        // Execute proposal
        proposals[_proposalId].executed = true;

        // Emit event
        emit Executed(_proposalId);
    }

    // Function to set user's voting power
    function setVotingPower(address _user, uint256 _votingPower) public onlyOwner {
        votingPower[_user] = _votingPower;
    }
}
```
