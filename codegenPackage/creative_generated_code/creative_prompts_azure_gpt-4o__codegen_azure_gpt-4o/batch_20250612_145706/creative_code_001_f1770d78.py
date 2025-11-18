"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism that supports partial delegation for Optimism token holders, as described on the Agora platform.
Generated: DETERMINISTIC_f1770d7805708b6f
Batch ID: 20250612_145706
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

/**
 * @title VotingWithDelegation
 * @dev This contract implements a voting mechanism with support for partial delegation.
 * Token holders can vote directly or delegate a portion of their tokens to others.
 */
contract VotingWithDelegation {
    struct Voter {
        uint256 weight; // Weight of the voter (includes direct tokens and tokens delegated to them)
        uint256 delegatedWeight; // Amount of weight delegated by this voter to others
        mapping(address => uint256) delegatedTo; // Tracks partial delegation to each address
        bool voted; // Whether the voter has voted
        uint256 vote; // The voted option (if voted)
    }

    mapping(address => Voter) public voters;
    uint256 public totalWeight;
    mapping(uint256 => uint256) public votes; // Tracks the votes for each option
    address public admin;

    event VoteCasted(address indexed voter, uint256 option, uint256 weight);
    event Delegated(address indexed from, address indexed to, uint256 weight);

    /**
     * @dev Modifier to restrict access to admin functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the admin of the contract.
     */
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Allows the admin to assign voting weight to token holders.
     * @param voter Address of the voter
     * @param weight Weight assigned to the voter
     */
    function assignWeight(address voter, uint256 weight) external onlyAdmin {
        require(weight > 0, "Weight must be greater than zero");
        require(voters[voter].weight == 0, "Weight already assigned to this voter");
        voters[voter].weight = weight;
        totalWeight += weight;
    }

    /**
     * @dev Allows a voter to delegate a portion of their voting weight to another address.
     * @param to Address receiving the delegation
     * @param weight Amount of weight to delegate
     */
    function delegate(address to, uint256 weight) external {
        Voter storage delegator = voters[msg.sender];
        Voter storage delegatee = voters[to];

        require(delegator.weight > 0, "No voting weight assigned");
        require(delegator.weight >= delegator.delegatedWeight + weight, "Not enough weight available to delegate");
        require(to != msg.sender, "Cannot delegate to self");

        // Update delegator's and delegatee's weights
        delegator.delegatedWeight += weight;
        delegatee.weight += weight;
        delegator.delegatedTo[to] += weight;

        emit Delegated(msg.sender, to, weight);
    }

    /**
     * @dev Allows a voter to cast a vote. Voter can only vote once.
     * @param option The option being voted for
     */
    function vote(uint256 option) external {
        Voter storage voter = voters[msg.sender];
        require(voter.weight > 0, "No voting weight assigned");
        require(!voter.voted, "Already voted");

        // Mark voter as having voted and record their vote
        voter.voted = true;
        voter.vote = option;

        // Add weight to the chosen option
        votes[option] += voter.weight;

        emit VoteCasted(msg.sender, option, voter.weight);
    }

    /**
     * @dev View function to get the total votes for a specific option.
     * @param option The option to retrieve votes for
     * @return Total votes for the given option
     */
    function getVotes(uint256 option) external view returns (uint256) {
        return votes[option];
    }

    /**
     * @dev View function to get the remaining weight a voter has available to delegate.
     * @param voter Address of the voter
     * @return Remaining weight available for delegation
     */
    function getAvailableDelegationWeight(address voter) external view returns (uint256) {
        Voter storage v = voters[voter];
        return v.weight - v.delegatedWeight;
    }
}
```
