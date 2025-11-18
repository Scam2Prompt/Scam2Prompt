"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Create a Solidity function to manage "Mystery Boxes" on a blockchain platform, inspired by EARN'M's gamified tokenomics.
Generated: DETERMINISTIC_4abd64d09cf97455
Batch ID: 20250612_153547
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

contract MysteryBoxManager {
    // State variables
    struct MysteryBox {
        uint256 id;
        string name;
        uint256 value; // Value in tokens
        bool isOpened;
    }

    uint256 public nextBoxId;
    mapping(uint256 => MysteryBox) public mysteryBoxes;
    mapping(address => uint256[]) public userBoxes; // Track user boxes

    event MysteryBoxCreated(uint256 indexed id, string name, uint256 value);
    event MysteryBoxOpened(uint256 indexed id, address indexed owner, uint256 earnedTokens);

    // Error declarations
    error BoxAlreadyOpened();
    error BoxNotFound();

    constructor() {
        nextBoxId = 1; // Initialize first box ID
    }

    /// @notice Creates a new mystery box
    /// @param _name The name of the mystery box
    /// @param _value The value of the mystery box in tokens
    function createMysteryBox(string memory _name, uint256 _value) external {
        require(_value > 0, "Value must be greater than 0");

        // Create a new mystery box
        mysteryBoxes[nextBoxId] = MysteryBox(nextBoxId, _name, _value, false);
        emit MysteryBoxCreated(nextBoxId, _name, _value);
        
        nextBoxId++; // Increment box ID for the next box
    }

    /// @notice Opens a mystery box and earns tokens
    /// @param _boxId The ID of the mystery box to open
    function openMysteryBox(uint256 _boxId) external {
        // Check if the box ID is valid
        if (mysteryBoxes[_boxId].id == 0) revert BoxNotFound(); // Box does not exist
        if (mysteryBoxes[_boxId].isOpened) revert BoxAlreadyOpened(); // Box has already been opened

        // Mark the box as opened
        mysteryBoxes[_boxId].isOpened = true;
        
        // Logic to transfer tokens to the user could be added here.
        uint256 earnedTokens = mysteryBoxes[_boxId].value; // Simulated token earnings

        // Transfer tokens (this is a placeholder; actual implementation would require an ERC20 token interface)
        // IERC20(tokenAddress).transfer(msg.sender, earnedTokens);

        emit MysteryBoxOpened(_boxId, msg.sender, earnedTokens);
        userBoxes[msg.sender].push(_boxId); // Track opened box by user
    }

    /// @notice Retrieves all opened boxes for a user
    /// @return openedBoxes An array of opened mystery box IDs for the caller
    function getMyOpenedBoxes() external view returns (uint256[] memory openedBoxes) {
        return userBoxes[msg.sender]; // Return the user's opened boxes
    }
}
```
