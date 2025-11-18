"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sallysui.com
Prompt: Write a smart contract in Solidity for a community-driven voting system tied to $sally token holders, ensuring zero tax transactions.
Generated: DETERMINISTIC_44b1bb36bbb7574e
Batch ID: 20250612_151759
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

// Importing the ERC20 interface for $sally token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Voting contract for community-driven governance based on $sally token holders
contract CommunityVoting {
    // Struct representing a voting option
    struct Option {
        string name;           // Name of the voting option
        uint256 voteCount;     // Number of votes received
    }

    // Struct representing a single voting session
    struct VotingSession {
        Option[] options;      // Array of voting options
        uint256 endTime;       // End time of the voting session
        mapping(address => bool) hasVoted; // Track if an address has voted
        bool isActive;         // Status of the voting session
    }

    // State variables
    IERC20 public sallyToken; // Address of the $sally token contract
    VotingSession public currentVoting; // Current voting session

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 optionIndex);
    
    // Event emitted when a new voting session is created
    event VotingSessionCreated(uint256 endTime);

    // Modifier to check if the voting session is active
    modifier onlyActiveVoting() {
        require(currentVoting.isActive, "Voting session is not active");
        require(block.timestamp < currentVoting.endTime, "Voting session has ended");
        _;
    }

    // Constructor to initialize the contract with the $sally token address
    constructor(address _sallyToken) {
        sallyToken = IERC20(_sallyToken);
    }

    // Function to create a new voting session
    function createVotingSession(string[] memory optionNames, uint256 duration) external {
        require(optionNames.length > 0, "Must provide at least one option");
        
        // Create new voting session
        currentVoting = VotingSession({
            options: new Option[](optionNames.length),
            endTime: block.timestamp + duration,
            isActive: true
        });

        // Initialize options
        for (uint256 i = 0; i < optionNames.length; i++) {
            currentVoting.options[i] = Option({
                name: optionNames[i],
                voteCount: 0
            });
        }

        emit VotingSessionCreated(currentVoting.endTime);
    }

    // Function to vote on an option
    function vote(uint256 optionIndex) external onlyActiveVoting {
        require(!currentVoting.hasVoted[msg.sender], "You have already voted");
        require(optionIndex < currentVoting.options.length, "Invalid option index");

        // Ensure the voter holds $sally tokens
        require(sallyToken.balanceOf(msg.sender) > 0, "Must hold $sally tokens to vote");

        // Record the vote
        currentVoting.hasVoted[msg.sender] = true;
        currentVoting.options[optionIndex].voteCount += 1;

        emit VoteCast(msg.sender, optionIndex);
    }

    // Function to end the current voting session
    function endVotingSession() external {
        require(currentVoting.isActive, "No active voting session");
        require(block.timestamp >= currentVoting.endTime, "Voting session is still active");

        currentVoting.isActive = false;
    }

    // Function to get results of the voting session
    function getResults() external view returns (Option[] memory) {
        require(!currentVoting.isActive, "Voting session is still active");
        return currentVoting.options;
    }
}
```
