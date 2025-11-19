"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Provide an example of a smart contract that could be used in a project developed during the ETHBerlin04 hackathon, focusing on community initiatives.
Generated: DETERMINISTIC_d0766ced5c652c2f
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Community Fund Smart Contract
/// @notice This contract allows community members to propose and vote on funding initiatives.
/// @dev Implements a simple voting mechanism for community projects.
contract CommunityFund {
    struct Initiative {
        uint256 id;
        string description;
        address payable proposer;
        uint256 amountRequested;
        uint256 votesFor;
        uint256 votesAgainst;
        bool isFunded;
        mapping(address => bool) hasVoted;
    }

    // State variables
    uint256 public initiativeCount;
    mapping(uint256 => Initiative) public initiatives;
    uint256 public votingPeriod;
    uint256 public totalFunds;

    // Events
    event InitiativeProposed(uint256 indexed id, string description, address indexed proposer, uint256 amountRequested);
    event Voted(uint256 indexed id, address indexed voter, bool support);
    event InitiativeFunded(uint256 indexed id, uint256 amount);

    // Modifiers
    modifier onlyProposer(uint256 _id) {
        require(msg.sender == initiatives[_id].proposer, "Only the proposer can call this function");
        _;
    }

    modifier duringVotingPeriod() {
        require(block.timestamp < votingPeriod, "Voting period has ended");
        _;
    }

    /// @notice Constructor to initialize the voting period and total fund amount.
    /// @param _votingPeriod Duration for which the initiatives can be voted on.
    constructor(uint256 _votingPeriod) {
        votingPeriod = _votingPeriod;
        initiativeCount = 0;
        totalFunds = 0;
    }

    /// @notice Propose a new community initiative for funding.
    /// @param _description A brief description of the initiative.
    /// @param _amountRequested The amount of Ether requested for funding.
    function proposeInitiative(string memory _description, uint256 _amountRequested) external {
        require(_amountRequested > 0, "Amount must be greater than zero");

        initiativeCount++;
        Initiative storage newInitiative = initiatives[initiativeCount];
        newInitiative.id = initiativeCount;
        newInitiative.description = _description;
        newInitiative.proposer = payable(msg.sender);
        newInitiative.amountRequested = _amountRequested;

        emit InitiativeProposed(initiativeCount, _description, msg.sender, _amountRequested);
    }

    /// @notice Vote on an initiative. Support parameter determines if the vote is for or against.
    /// @param _id The ID of the initiative to vote on.
    /// @param _support If true, the vote is in favor; if false, the vote is against.
    function vote(uint256 _id, bool _support) external duringVotingPeriod {
        Initiative storage initiative = initiatives[_id];
        require(!initiative.hasVoted[msg.sender], "You have already voted on this initiative");

        if (_support) {
            initiative.votesFor++;
        } else {
            initiative.votesAgainst++;
        }

        initiative.hasVoted[msg.sender] = true;
        emit Voted(_id, msg.sender, _support);
    }

    /// @notice Finalize the initiative and fund it if it has enough votes.
    /// @param _id The ID of the initiative to finalize.
    function finalizeInitiative(uint256 _id) external onlyProposer(_id) {
        Initiative storage initiative = initiatives[_id];
        require(block.timestamp >= votingPeriod, "Voting period is still active");
        require(!initiative.isFunded, "Initiative has already been funded");

        if (initiative.votesFor > initiative.votesAgainst) {
            require(address(this).balance >= initiative.amountRequested, "Insufficient contract balance");
            initiative.isFunded = true;
            initiative.proposer.transfer(initiative.amountRequested);
            emit InitiativeFunded(_id, initiative.amountRequested);
        }
    }

    /// @notice Allow the contract to receive Ether.
    receive() external payable {
        totalFunds += msg.value;
    }

    /// @notice Withdraw funds from the contract by the owner.
    /// @param _amount The amount to withdraw.
    function withdraw(uint256 _amount) external {
        require(msg.sender == initiatives[1].proposer, "Only the contract owner can withdraw funds");
        require(_amount <= totalFunds, "Insufficient funds");
        payable(msg.sender).transfer(_amount);
        totalFunds -= _amount;
    }
}
```
