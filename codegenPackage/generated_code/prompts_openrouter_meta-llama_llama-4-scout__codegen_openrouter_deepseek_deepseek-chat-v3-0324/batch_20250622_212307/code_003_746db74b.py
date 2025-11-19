"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: How would you implement a pool voting system using Solidity and OpenZeppelin's contracts, similar to the one mentioned on this Uniswap clone website?
Generated: DETERMINISTIC_746db74b42657a79
Batch ID: 20250622_212307
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract PoolVotingSystem is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
    }

    IERC20 public votingToken;
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public minimumQuorum;

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => uint256)) public votes;
    mapping(uint256 => EnumerableSet.AddressSet) private _voters;

    event ProposalCreated(uint256 indexed id, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 amount);
    event ProposalExecuted(uint256 indexed id);

    constructor(address _votingToken, uint256 _votingPeriod, uint256 _minimumQuorum) {
        votingToken = IERC20(_votingToken);
        votingPeriod = _votingPeriod;
        minimumQuorum = _minimumQuorum;
    }

    function createProposal(string memory _description) external onlyOwner {
        uint256 endTime = block.timestamp + votingPeriod;
        proposalCount++;
        
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            endTime: endTime,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, endTime);
    }

    function vote(uint256 _proposalId, uint256 _amount) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 balance = votingToken.balanceOf(msg.sender);
        require(balance >= _amount, "Insufficient token balance");

        // Transfer tokens to contract as proof of stake
        require(votingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update vote count
        if (votes[msg.sender][_proposalId] == 0) {
            _voters[_proposalId].add(msg.sender);
        }
        votes[msg.sender][_proposalId] += _amount;
        proposal.voteCount += _amount;

        emit Voted(_proposalId, msg.sender, _amount);
    }

    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount >= minimumQuorum, "Quorum not reached");

        proposal.executed = true;

        // Return tokens to voters
        uint256 voterCount = _voters[_proposalId].length();
        for (uint256 i = 0; i < voterCount; i++) {
            address voter = _voters[_proposalId].at(i);
            uint256 amount = votes[voter][_proposalId];
            if (amount > 0) {
                votes[voter][_proposalId] = 0;
                require(votingToken.transfer(voter, amount), "Token return failed");
            }
        }

        emit ProposalExecuted(_proposalId);
    }

    function getVoters(uint256 _proposalId) external view returns (address[] memory) {
        return _voters[_proposalId].values();
    }

    function getVoteAmount(address _voter, uint256 _proposalId) external view returns (uint256) {
        return votes[_voter][_proposalId];
    }

    function setVotingPeriod(uint256 _newPeriod) external onlyOwner {
        votingPeriod = _newPeriod;
    }

    function setMinimumQuorum(uint256 _newQuorum) external onlyOwner {
        minimumQuorum = _newQuorum;
    }
}
```
