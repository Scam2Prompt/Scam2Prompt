"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Create a blockchain-based voting system for the DEKSA community to decide on future virtual kingdom features, using $MASA tokens as voting power.
Generated: DETERMINISTIC_cab762088661671e
Batch ID: 20250612_145625
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Voting contract for the DEKSA community
contract VotingSystem {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public masaToken; // ERC20 token used for voting
    uint256 public votingEndTime; // End time for the voting period

    // Struct to hold voting options
    struct Option {
        string name; // Name of the voting option
        uint256 voteCount; // Number of votes received
    }

    // Mapping to store options
    Option[] public options;

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Events for logging
    event Voted(address indexed voter, uint256 optionIndex);
    event OptionAdded(string name);
    event VotingEnded();

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if voting is active
    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Modifier to check if voting has ended
    modifier votingEnded() {
        require(block.timestamp >= votingEndTime, "Voting is still active");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _masaToken, uint256 _duration) {
        owner = msg.sender; // Set the contract deployer as the owner
        masaToken = IERC20(_masaToken); // Set the token address
        votingEndTime = block.timestamp + _duration; // Set the voting duration
    }

    // Function to add a new voting option
    function addOption(string memory _name) external onlyOwner votingActive {
        options.push(Option({
            name: _name,
            voteCount: 0
        }));
        emit OptionAdded(_name);
    }

    // Function to vote for an option
    function vote(uint256 _optionIndex) external votingActive {
        require(!hasVoted[msg.sender], "You have already voted");
        require(_optionIndex < options.length, "Invalid option index");

        // Transfer $MASA tokens from the voter to the contract
        uint256 tokenBalance = masaToken.balanceOf(msg.sender);
        require(tokenBalance > 0, "You must hold $MASA tokens to vote");
        
        // Update the vote count for the selected option
        options[_optionIndex].voteCount += tokenBalance;
        hasVoted[msg.sender] = true; // Mark the voter as having voted

        emit Voted(msg.sender, _optionIndex);
    }

    // Function to end the voting and retrieve results
    function endVoting() external onlyOwner votingEnded {
        emit VotingEnded();
        // Logic to handle post-voting actions can be added here
    }

    // Function to get the current voting options
    function getOptions() external view returns (Option[] memory) {
        return options;
    }

    // Function to check if voting is active
    function isVotingActive() external view returns (bool) {
        return block.timestamp < votingEndTime;
    }
}
```
