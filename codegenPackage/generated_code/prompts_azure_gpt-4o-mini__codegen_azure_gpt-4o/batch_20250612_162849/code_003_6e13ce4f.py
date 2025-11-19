"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Develop a smart contract in Solidity that implements the community-led initiatives mentioned on the Arbinu site, ensuring decentralized management of token holders.
Generated: DETERMINISTIC_6e13ce4f8bf1cea0
Batch ID: 20250612_162849
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

/**
 * @title CommunityInitiatives
 * @dev A smart contract to manage community-led initiatives for token holders in a decentralized manner.
 */
contract CommunityInitiatives {
    // Struct to represent an initiative
    struct Initiative {
        uint256 id;
        string title;
        string description;
        address proposer;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Mapping to store initiatives by ID
    mapping(uint256 => Initiative) public initiatives;

    // Mapping to track whether a token holder has voted on a specific initiative
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for initiative IDs
    uint256 public initiativeCounter;

    // Address of the token contract
    address public tokenContract;

    // Events
    event InitiativeProposed(uint256 id, string title, address proposer);
    event Voted(uint256 id, address voter, bool support);
    event InitiativeExecuted(uint256 id);

    /**
     * @dev Modifier to ensure only token holders can interact with certain functions.
     */
    modifier onlyTokenHolder() {
        require(IERC20(tokenContract).balanceOf(msg.sender) > 0, "Not a token holder");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract address.
     * @param _tokenContract Address of the token contract.
     */
    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Function to propose a new initiative.
     * @param _title Title of the initiative.
     * @param _description Description of the initiative.
     */
    function proposeInitiative(string memory _title, string memory _description) external onlyTokenHolder {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        initiativeCounter++;
        initiatives[initiativeCounter] = Initiative({
            id: initiativeCounter,
            title: _title,
            description: _description,
            proposer: msg.sender,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit InitiativeProposed(initiativeCounter, _title, msg.sender);
    }

    /**
     * @dev Function to vote on an initiative.
     * @param _id ID of the initiative.
     * @param _support True to vote in favor, false to vote against.
     */
    function voteOnInitiative(uint256 _id, bool _support) external onlyTokenHolder {
        Initiative storage initiative = initiatives[_id];
        require(initiative.id != 0, "Initiative does not exist");
        require(!initiative.executed, "Initiative already executed");
        require(!hasVoted[_id][msg.sender], "Already voted");

        hasVoted[_id][msg.sender] = true;

        if (_support) {
            initiative.votesFor++;
        } else {
            initiative.votesAgainst++;
        }

        emit Voted(_id, msg.sender, _support);
    }

    /**
     * @dev Function to execute an initiative if it has enough votes.
     * @param _id ID of the initiative.
     */
    function executeInitiative(uint256 _id) external onlyTokenHolder {
        Initiative storage initiative = initiatives[_id];
        require(initiative.id != 0, "Initiative does not exist");
        require(!initiative.executed, "Initiative already executed");
        require(initiative.votesFor > initiative.votesAgainst, "Not enough votes to execute");

        initiative.executed = true;

        // Logic for executing the initiative can be added here

        emit InitiativeExecuted(_id);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
