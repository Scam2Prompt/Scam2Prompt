"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: How can I implement a voting mechanism using the Agora platform for Optimism proposals with partial delegation?
Generated: DETERMINISTIC_a90c836cf58a06b1
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract implementation for a voting mechanism with partial delegation on Optimism, compatible with Agora-style governance:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OptimismVoting is ERC20Votes, Ownable {
    struct Proposal {
        uint256 id;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        bool executed;
    }

    struct Delegation {
        address delegatee;
        uint256 amount;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    mapping(address => Delegation[]) public delegations;
    mapping(address => uint256) public undelegatedBalances;

    uint256 public nextProposalId;
    uint256 public totalSupplyCap;

    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        uint8 support,
        uint256 weight
    );
    event Delegated(
        address indexed delegator,
        address indexed delegatee,
        uint256 amount
    );
    event Undelegated(
        address indexed delegator,
        address indexed delegatee,
        uint256 amount
    );
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupplyCap
    ) ERC20(_name, _symbol) ERC20Permit(_name) {
        totalSupplyCap = _totalSupplyCap;
    }

    function mint(address _to, uint256 _amount) external onlyOwner {
        require(
            totalSupply() + _amount <= totalSupplyCap,
            "Exceeds total supply cap"
        );
        _mint(_to, _amount);
    }

    function createProposal(
        string memory _description,
        uint256 _durationBlocks
    ) external onlyOwner {
        uint256 startBlock = block.number;
        uint256 endBlock = startBlock + _durationBlocks;

        proposals[nextProposalId] = Proposal({
            id: nextProposalId,
            description: _description,
            startBlock: startBlock,
            endBlock: endBlock,
            forVotes: 0,
            againstVotes: 0,
            abstainVotes: 0,
            executed: false
        });

        emit ProposalCreated(
            nextProposalId,
            _description,
            startBlock,
            endBlock
        );

        nextProposalId++;
    }

    function delegateVotes(
        address _delegatee,
        uint256 _amount
    ) external {
        require(_delegatee != address(0), "Cannot delegate to zero address");
        require(_amount > 0, "Amount must be greater than 0");
        require(
            balanceOf(msg.sender) >= _amount,
            "Insufficient balance for delegation"
        );

        // Update undelegated balance
        undelegatedBalances[msg.sender] -= _amount;

        // Add to delegations
        delegations[msg.sender].push(Delegation(_delegatee, _amount));

        emit Delegated(msg.sender, _delegatee, _amount);
    }

    function undelegateVotes(
        uint256 _delegationIndex
    ) external {
        require(
            _delegationIndex < delegations[msg.sender].length,
            "Invalid delegation index"
        );

        Delegation memory delegation = delegations[msg.sender][_delegationIndex];
        
        // Remove the delegation
        delegations[msg.sender][_delegationIndex] = delegations[msg.sender][delegations[msg.sender].length - 1];
        delegations[msg.sender].pop();

        // Update undelegated balance
        undelegatedBalances[msg.sender] += delegation.amount;

        emit Undelegated(msg.sender, delegation.delegatee, delegation.amount);
    }

    function vote(
        uint256 _proposalId,
        uint8 _support
    ) external {
        require(_proposalId < nextProposalId, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!hasVoted[msg.sender][_proposalId], "Already voted");
        require(_support <= 2, "Invalid vote type");

        uint256 votingPower = getVotingPower(msg.sender, _proposalId);
        require(votingPower > 0, "No voting power");

        if (_support == 0) {
            proposal.againstVotes += votingPower;
        } else if (_support == 1) {
            proposal.forVotes += votingPower;
        } else if (_support == 2) {
            proposal.abstainVotes += votingPower;
        }

        hasVoted[msg.sender][_proposalId] = true;
        emit VoteCast(msg.sender, _proposalId, _support, votingPower);
    }

    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function getVotingPower(
        address _voter,
        uint256 _proposalId
    ) public view returns (uint256) {
        uint256 power = undelegatedBalances[_voter];
        
        // Check all active delegations that weren't used for this proposal
        for (uint256 i = 0; i < delegations[_voter].length; i++) {
            Delegation memory d = delegations[_voter][i];
            if (!hasVoted[d.delegatee][_proposalId]) {
                power += d.amount;
            }
        }
        
        return power;
    }

    function getDelegations(
        address _delegator
    ) external view returns (Delegation[] memory) {
        return delegations[_delegator];
    }
}
```
