"""
Generated Code Metadata:
========================
Original URL: https://zealy-io.github.io
Prompt: Create a governance smart contract in Solidity that allows ORB token holders to vote on proposals within the Zealy platform.
Generated: DETERMINISTIC_7f0d3a3fde25acb2
Batch ID: 20250612_150858
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract Governance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public orbToken;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        address proposer;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(address => uint256) public lastProposalTimestamp;
    EnumerableSet.AddressSet private _admins;

    uint256 public proposalCount;
    uint256 public votingDelay;
    uint256 public votingPeriod;
    uint256 public proposalThreshold;

    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event AdminAdded(address indexed admin);
    event AdminRemoved(address indexed admin);

    modifier onlyAdmin() {
        require(
            _admins.contains(msg.sender) || msg.sender == owner(),
            "Governance: caller is not an admin"
        );
        _;
    }

    constructor(
        address _orbToken,
        uint256 _votingDelay,
        uint256 _votingPeriod,
        uint256 _proposalThreshold
    ) {
        require(_orbToken != address(0), "Governance: invalid token address");
        orbToken = IERC20(_orbToken);
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
        proposalThreshold = _proposalThreshold;
    }

    function propose(string memory description) external {
        uint256 orbBalance = orbToken.balanceOf(msg.sender);
        require(
            orbBalance >= proposalThreshold,
            "Governance: insufficient ORB balance"
        );
        require(
            lastProposalTimestamp[msg.sender] + votingDelay <= block.timestamp,
            "Governance: too frequent proposals"
        );

        proposalCount++;
        uint256 voteStart = block.timestamp;
        uint256 voteEnd = voteStart + votingPeriod;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteStart: voteStart,
            voteEnd: voteEnd,
            forVotes: 0,
            againstVotes: 0,
            executed: false,
            proposer: msg.sender
        });

        lastProposalTimestamp[msg.sender] = block.timestamp;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            description,
            voteStart,
            voteEnd
        );
    }

    function vote(uint256 proposalId, bool support) external {
        require(
            proposals[proposalId].voteStart <= block.timestamp,
            "Governance: voting not started"
        );
        require(
            proposals[proposalId].voteEnd >= block.timestamp,
            "Governance: voting ended"
        );
        require(!hasVoted[proposalId][msg.sender], "Governance: already voted");

        uint256 orbBalance = orbToken.balanceOf(msg.sender);
        require(orbBalance > 0, "Governance: no ORB tokens");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposals[proposalId].forVotes += orbBalance;
        } else {
            proposals[proposalId].againstVotes += orbBalance;
        }

        emit VoteCast(msg.sender, proposalId, support, orbBalance);
    }

    function executeProposal(uint256 proposalId) external onlyAdmin {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Governance: proposal not found");
        require(!proposal.executed, "Governance: proposal already executed");
        require(
            block.timestamp > proposal.voteEnd,
            "Governance: voting not ended"
        );

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    function addAdmin(address admin) external onlyOwner {
        require(admin != address(0), "Governance: invalid address");
        require(_admins.add(admin), "Governance: already an admin");
        emit AdminAdded(admin);
    }

    function removeAdmin(address admin) external onlyOwner {
        require(_admins.remove(admin), "Governance: not an admin");
        emit AdminRemoved(admin);
    }

    function isAdmin(address account) external view returns (bool) {
        return _admins.contains(account);
    }

    function getAdmins() external view returns (address[] memory) {
        return _admins.values();
    }

    function setVotingDelay(uint256 newVotingDelay) external onlyOwner {
        votingDelay = newVotingDelay;
    }

    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }

    function setProposalThreshold(uint256 newProposalThreshold)
        external
        onlyOwner
    {
        proposalThreshold = newProposalThreshold;
    }
}
```
