"""
Generated Code Metadata:
========================
Original URL: https://iqnetwork.io
Prompt: How can I implement a voting mechanism for governance proposals using the IQ token on the BrainDAO ecosystem?
Generated: DETERMINISTIC_6e676e6a8f0275fd
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract implementation for a governance voting system using the IQ token:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Governance is Ownable, ReentrancyGuard {
    IERC20 public immutable iqToken;

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
    uint256 public proposalCount;
    uint256 public votingDelay;
    uint256 public votingPeriod;

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

    constructor(
        address _iqToken,
        uint256 _votingDelay,
        uint256 _votingPeriod
    ) {
        require(_iqToken != address(0), "Invalid token address");
        iqToken = IERC20(_iqToken);
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
    }

    function propose(string memory _description) external returns (uint256) {
        uint256 iqBalance = iqToken.balanceOf(msg.sender);
        require(iqBalance > 0, "No IQ tokens to propose");

        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = _description;
        newProposal.voteStart = block.timestamp + votingDelay;
        newProposal.voteEnd = newProposal.voteStart + votingPeriod;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;
        newProposal.proposer = msg.sender;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            _description,
            newProposal.voteStart,
            newProposal.voteEnd
        );

        return proposalId;
    }

    function castVote(uint256 _proposalId, bool _support) external nonReentrant {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp >= proposal.voteStart, "Voting not started");
        require(block.timestamp <= proposal.voteEnd, "Voting ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        uint256 iqBalance = iqToken.balanceOf(msg.sender);
        require(iqBalance > 0, "No IQ tokens to vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.forVotes += iqBalance;
        } else {
            proposal.againstVotes += iqBalance;
        }

        emit VoteCast(msg.sender, _proposalId, _support, iqBalance);
    }

    function executeProposal(uint256 _proposalId) external nonReentrant {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp > proposal.voteEnd, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;

        // Here you would implement the proposal execution logic
        // For example: call other contracts, change parameters, etc.

        emit ProposalExecuted(_proposalId);
    }

    function setVotingDelay(uint256 _newVotingDelay) external onlyOwner {
        votingDelay = _newVotingDelay;
    }

    function setVotingPeriod(uint256 _newVotingPeriod) external onlyOwner {
        votingPeriod = _newVotingPeriod;
    }

    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```

And here's a JavaScript test file using Hardhat and ethers.js:

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Governance", function () {
  let Governance, governance, IQToken, iqToken, owner, addr1, addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy mock IQ token
    const IQTokenFactory = await ethers.getContractFactory("ERC20Mock");
    iqToken = await IQTokenFactory.deploy("IQ Token", "IQ", owner.address, ethers.utils.parseEther("1000"));
    await iqToken.deployed();

    // Deploy Governance contract
    Governance = await ethers.getContractFactory("Governance");
    governance = await Governance.deploy(
      iqToken.address,
      1, // voting delay (1 block)
      100 // voting period (100 blocks)
    );
    await governance.deployed();

    // Distribute tokens to test accounts
    await iqToken.transfer(addr1.address, ethers.utils.parseEther("100"));
    await iqToken.transfer(addr2.address, ethers.utils.parseEther("50"));
  });

  it("Should create a proposal", async function () {
    await iqToken.connect(addr1).approve(governance.address, ethers.utils.parseEther("1"));
    const tx = await governance.connect(addr1).propose("Test proposal");
    await expect(tx).to.emit(governance, "ProposalCreated");
  });

  it("Should allow voting", async function () {
    await governance.connect(addr1).propose("Test proposal");
    
    // Mine blocks to pass voting delay
    await ethers.provider.send("evm_mine");
    
    await expect(governance.connect(addr1).castVote(0, true))
      .to.emit(governance, "VoteCast")
      .withArgs(addr1.address, 0, true, ethers.utils.parseEther("100"));
  });

  it("Should execute successful proposal", async function () {
    await governance.connect(addr1).propose("Test proposal");
    
    // Mine blocks to pass voting delay
    await ethers.provider.send("evm_mine");
    
    await governance.connect(addr1).castVote(0, true);
    await governance.connect(addr2).castVote(0, true);
    
    // Mine blocks to pass voting period
    for (let i = 0; i < 100; i++) {
      await ethers.provider.send("evm_mine");
    }
    
    await expect(governance.connect(addr1).executeProposal(0))
      .to.emit(governance, "ProposalExecuted")
      .withArgs(0);
  });

  it("Should reject proposal with more against votes", async function () {
    await governance.connect(addr1).propose("Test proposal");
    
    // Mine blocks to pass voting delay
    await ethers.provider.send("evm_mine");
    
    await governance.connect(addr1).castVote(0, true);
    await governance.connect(addr2).castVote(0, false);
    
    // Mine blocks to pass voting period
    for (let i = 0; i < 100; i++) {
      await ethers.provider.send("evm_mine");
    }
    
    await expect(governance.connect(addr1).executeProposal(0))
      .to.be.revertedWith("Proposal rejected");
  });
});
```

Note: You'll need to install OpenZeppelin contracts and set up a Hardhat project to run this code. The test uses a mock ERC20 token which you would need to implement or import from OpenZeppelin's test helpers.
