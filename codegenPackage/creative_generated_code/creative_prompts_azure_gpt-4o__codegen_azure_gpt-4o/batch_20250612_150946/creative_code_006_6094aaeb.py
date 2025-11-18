"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.pages.dev
Prompt: Create a Solidity contract to enable users to vote on upcoming games or features on the BetSwirl platform.
Generated: DETERMINISTIC_6094aaeb5582fa5b
Batch ID: 20250612_150946
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
 * @title BetSwirl Voting Contract
 * @dev This contract enables users to vote on upcoming games or features on the BetSwirl platform.
 */
contract BetSwirlVoting {
    // Struct to represent a voting option
    struct Option {
        string description; // Description of the option
        uint256 voteCount;  // Number of votes received
    }

    // Struct to represent a voter
    struct Voter {
        bool hasVoted;     // Whether the voter has already voted
        uint256 votedOption; // Index of the voted option
    }

    // State variables
    address public owner; // Contract owner
    string public topic; // Topic of the current vote
    Option[] public options; // List of voting options
    mapping(address => Voter) public voters; // Mapping to track voter details
    bool public votingActive; // Flag to indicate whether voting is active

    // Events
    event VotingStarted(string topic);
    event VotingEnded(string topic);
    event VoteCasted(address indexed voter, uint256 optionIndex);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Modifier to ensure voting is active
    modifier isVotingActive() {
        require(votingActive, "Voting is not active.");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Starts a new voting session with the given topic and options.
     * @param _topic The topic of the vote.
     * @param _options The list of voting options.
     */
    function startVoting(string memory _topic, string[] memory _options) external onlyOwner {
        require(!votingActive, "Voting is already active.");
        require(_options.length > 0, "At least one voting option must be provided.");

        // Reset previous voting data
        delete options;
        for (uint256 i = 0; i < _options.length; i++) {
            options.push(Option({description: _options[i], voteCount: 0}));
        }
        topic = _topic;
        votingActive = true;

        emit VotingStarted(_topic);
    }

    /**
     * @dev Ends the current voting session.
     */
    function endVoting() external onlyOwner isVotingActive {
        votingActive = false;
        emit VotingEnded(topic);
    }

    /**
     * @dev Allows a user to cast their vote for a specific option.
     * @param optionIndex The index of the option to vote for.
     */
    function castVote(uint256 optionIndex) external isVotingActive {
        require(!voters[msg.sender].hasVoted, "You have already voted.");
        require(optionIndex < options.length, "Invalid option index.");

        // Record the vote
        voters[msg.sender] = Voter({hasVoted: true, votedOption: optionIndex});
        options[optionIndex].voteCount++;

        emit VoteCasted(msg.sender, optionIndex);
    }

    /**
     * @dev Returns the list of voting options and their corresponding vote counts.
     * @return descriptions List of option descriptions.
     * @return voteCounts List of option vote counts.
     */
    function getOptions() external view returns (string[] memory descriptions, uint256[] memory voteCounts) {
        descriptions = new string[](options.length);
        voteCounts = new uint256[](options.length);
        for (uint256 i = 0; i < options.length; i++) {
            descriptions[i] = options[i].description;
            voteCounts[i] = options[i].voteCount;
        }
    }

    /**
     * @dev Returns whether a specific address has voted and the option they voted for.
     * @param voterAddress The address of the voter.
     * @return hasVoted Whether the voter has voted.
     * @return votedOption The index of the option the voter voted for.
     */
    function getVoterInfo(address voterAddress) external view returns (bool hasVoted, uint256 votedOption) {
        Voter memory voter = voters[voterAddress];
        return (voter.hasVoted, voter.votedOption);
    }
}
```
