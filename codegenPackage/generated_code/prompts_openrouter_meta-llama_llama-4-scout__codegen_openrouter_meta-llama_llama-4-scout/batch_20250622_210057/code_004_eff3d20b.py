"""
Generated Code Metadata:
========================
Original URL: https://neotokyo2-162.pages.dev
Prompt: Create a simple smart contract in Solidity for updating human skin tones for S1 and S2 citizens in a Neo Tokyo-like ecosystem, considering the costs of 10 bytes for updates.
Generated: DETERMINISTIC_eff3d20be3af2991
Batch ID: 20250622_210057
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

contract SkinToneUpdater {
    // Mapping of citizen IDs to their respective skin tones
    mapping (address => SkinTone) public skinTones;

    // Mapping of citizen IDs to their respective update costs
    mapping (address => uint256) public updateCosts;

    // Enum for skin tones
    enum SkinTone {
        S1_LIGHT,
        S1_MEDIUM,
        S1_DARK,
        S2_LIGHT,
        S2_MEDIUM,
        S2_DARK
    }

    // Event emitted when a skin tone is updated
    event SkinToneUpdated(address indexed citizenId, SkinTone newSkinTone);

    // Error for invalid citizen IDs
    error InvalidCitizenId(address citizenId);

    // Error for insufficient update cost
    error InsufficientUpdateCost(address citizenId);

    // Constructor to initialize the contract
    constructor() {
        // Initialize update cost for 10 bytes (assuming 1 byte = 1 wei)
        updateCosts[msg.sender] = 10;
    }

    // Function to update skin tone for S1 citizens
    function updateSkinToneS1(address citizenId, SkinTone newSkinTone) public payable {
        // Check if citizen ID is valid (assuming msg.sender is the Neo Tokyo authority)
        if (citizenId == address(0)) {
            revert InvalidCitizenId(citizenId);
        }

        // Check if update cost is sufficient
        if (msg.value < updateCosts[citizenId]) {
            revert InsufficientUpdateCost(citizenId);
        }

        // Check if new skin tone is valid for S1 citizens
        if (newSkinTone < SkinTone.S1_LIGHT || newSkinTone > SkinTone.S1_DARK) {
            revert InvalidSkinTone(newSkinTone);
        }

        // Update skin tone
        skinTones[citizenId] = newSkinTone;

        // Emit event
        emit SkinToneUpdated(citizenId, newSkinTone);
    }

    // Function to update skin tone for S2 citizens
    function updateSkinToneS2(address citizenId, SkinTone newSkinTone) public payable {
        // Check if citizen ID is valid (assuming msg.sender is the Neo Tokyo authority)
        if (citizenId == address(0)) {
            revert InvalidCitizenId(citizenId);
        }

        // Check if update cost is sufficient
        if (msg.value < updateCosts[citizenId]) {
            revert InsufficientUpdateCost(citizenId);
        }

        // Check if new skin tone is valid for S2 citizens
        if (newSkinTone < SkinTone.S2_LIGHT || newSkinTone > SkinTone.S2_DARK) {
            revert InvalidSkinTone(newSkinTone);
        }

        // Update skin tone
        skinTones[citizenId] = newSkinTone;

        // Emit event
        emit SkinToneUpdated(citizenId, newSkinTone);
    }

    // Error for invalid skin tone
    error InvalidSkinTone(SkinTone skinTone);
}
```
