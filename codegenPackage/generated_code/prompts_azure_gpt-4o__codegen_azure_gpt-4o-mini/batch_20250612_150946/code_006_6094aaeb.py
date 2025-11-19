"""
Generated Code Metadata:
========================
Original URL: https://betswirl.pages.dev
Prompt: Create a Solidity contract to enable users to vote on upcoming games or features on the BetSwirl platform.
Generated: DETERMINISTIC_6094aaeb5582fa5b
Batch ID: 20250612_150946
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

/// @title BetSwirl Voting Contract
/// @notice This contract allows users to vote on upcoming games or features on the BetSwirl platform.
contract BetSwirlVoting {
    // Struct to represent a voting option
    struct Option {
        string description; // Description of the game or feature
        uint256 voteCount;  // Number of votes received
    }

    // Mapping to store options by their ID
    mapping(uint256 => Option) public options;
    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;
    // Counter for the total number of options
    uint256 public optionsCount;

    // Event emitted when a new option is added
    event OptionAdded(uint256 optionId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 optionId, address voter);

    /// @notice Adds a new voting option
    /// @param _description The description of the option
    function addOption(string memory _description) public {
        require(bytes(_description).length > 0, "Description cannot be empty");

        optionsCount++;
        options[optionsCount] = Option({
            description: _description,
            voteCount: 0
        });

        emit OptionAdded(optionsCount, _description);
    }

    /// @notice Allows a user to vote for an option
    /// @param _optionId The ID of the option to vote for
    function vote(uint256 _optionId) public {
        require(!hasVoted[msg.sender], "You have already voted");
        require(_optionId > 0 && _optionId <= optionsCount, "Invalid option ID");

        // Record the vote
        hasVoted[msg.sender] = true;
        options[_optionId].voteCount++;

        emit Voted(_optionId, msg.sender);
    }

    /// @notice Retrieves the details of a voting option
    /// @param _optionId The ID of the option to retrieve
    /// @return description The description of the option
    /// @return voteCount The number of votes received
    function getOption(uint256 _optionId) public view returns (string memory description, uint256 voteCount) {
        require(_optionId > 0 && _optionId <= optionsCount, "Invalid option ID");
        Option storage option = options[_optionId];
        return (option.description, option.voteCount);
    }

    /// @notice Retrieves the total number of options
    /// @return The total number of voting options
    function getTotalOptions() public view returns (uint256) {
        return optionsCount;
    }
}
```
