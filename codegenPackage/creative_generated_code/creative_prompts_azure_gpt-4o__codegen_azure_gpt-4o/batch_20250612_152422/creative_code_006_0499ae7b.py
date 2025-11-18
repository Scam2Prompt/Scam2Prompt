"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mine-runecoinio.pages.dev
Prompt: Develop a smart contract or script to distribute runes based on the RSIC allocation rules, ensuring compliance with flat, boosted, random, and halvening types.
Generated: DETERMINISTIC_0499ae7be3360b4c
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a smart contract written in Solidity for distributing tokens ("runes") based on different allocation rules, including flat, boosted, random, and halvening types.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title RuneDistributor
 * @dev A smart contract for distributing runes based on RSIC allocation rules.
 * Supports flat, boosted, random, and halvening allocation types.
 */
contract RuneDistributor {
    // Enum to define allocation types
    enum AllocationType {
        Flat,
        Boosted,
        Random,
        Halvening
    }

    // Structure to represent recipients
    struct Recipient {
        address addr; // Recipient address
        uint256 baseAllocation; // Base allocation of runes
        uint256 boostFactor; // Boost multiplier (used for Boosted type)
    }

    // State variables
    address public admin; // Admin address
    Recipient[] public recipients; // List of recipients
    uint256 public totalRunes; // Total runes available for distribution

    // Events
    event RunesDistributed(uint256 totalDistributed, AllocationType allocationType);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Constructor to initialize admin and total runes
    constructor(uint256 _totalRunes) {
        admin = msg.sender;
        totalRunes = _totalRunes;
    }

    /**
     * @dev Add a recipient to the distribution list.
     * @param _addr Address of the recipient.
     * @param _baseAllocation Base allocation of runes for the recipient.
     * @param _boostFactor Boost multiplier for Boosted allocation type.
     */
    function addRecipient(address _addr, uint256 _baseAllocation, uint256 _boostFactor) external onlyAdmin {
        require(_addr != address(0), "Invalid recipient address");
        recipients.push(Recipient({addr: _addr, baseAllocation: _baseAllocation, boostFactor: _boostFactor}));
    }

    /**
     * @dev Distribute runes based on the specified allocation type.
     * @param allocationType The allocation type (Flat, Boosted, Random, Halvening).
     */
    function distributeRunes(AllocationType allocationType) external onlyAdmin {
        require(totalRunes > 0, "No runes available for distribution");
        require(recipients.length > 0, "No recipients to distribute runes to");

        uint256 remainingRunes = totalRunes;
        uint256 totalDistributed = 0;

        if (allocationType == AllocationType.Flat) {
            // Flat allocation: Each recipient gets their base allocation
            for (uint256 i = 0; i < recipients.length; i++) {
                uint256 allocation = recipients[i].baseAllocation;
                require(remainingRunes >= allocation, "Insufficient runes for allocation");
                payable(recipients[i].addr).transfer(allocation);
                remainingRunes -= allocation;
                totalDistributed += allocation;
            }
        } else if (allocationType == AllocationType.Boosted) {
            // Boosted allocation: Base allocation multiplied by boost factor
            for (uint256 i = 0; i < recipients.length; i++) {
                uint256 allocation = recipients[i].baseAllocation * recipients[i].boostFactor;
                require(remainingRunes >= allocation, "Insufficient runes for allocation");
                payable(recipients[i].addr).transfer(allocation);
                remainingRunes -= allocation;
                totalDistributed += allocation;
            }
        } else if (allocationType == AllocationType.Random) {
            // Random allocation: Randomized distribution within remaining runes
            for (uint256 i = 0; i < recipients.length; i++) {
                uint256 allocation = uint256(keccak256(abi.encodePacked(block.timestamp, recipients[i].addr))) % remainingRunes;
                require(remainingRunes >= allocation, "Insufficient runes for allocation");
                payable(recipients[i].addr).transfer(allocation);
                remainingRunes -= allocation;
                totalDistributed += allocation;
            }
        } else if (allocationType == AllocationType.Halvening) {
            // Halvening allocation: Base allocation halved for consecutive distributions
            for (uint256 i = 0; i < recipients.length; i++) {
                uint256 allocation = recipients[i].baseAllocation / 2;
                require(remainingRunes >= allocation, "Insufficient runes for allocation");
                payable(recipients[i].addr).transfer(allocation);
                remainingRunes -= allocation;
                totalDistributed += allocation;
            }
        } else {
            revert("Invalid allocation type");
        }

        // Emit an event for successful distribution
        emit RunesDistributed(totalDistributed, allocationType);

        // Update total runes after distribution
        totalRunes -= totalDistributed;
    }

    /**
     * @dev Allow admin to deposit runes into the contract.
     */
    function depositRunes() external payable onlyAdmin {
        totalRunes += msg.value;
    }

    /**
     * @dev Allow admin to withdraw unallocated runes.
     * @param amount The amount of runes to withdraw.
     */
    function withdrawRunes(uint256 amount) external onlyAdmin {
        require(amount <= totalRunes, "Insufficient runes for withdrawal");
        totalRunes -= amount;
        payable(admin).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {
        totalRunes += msg.value;
    }
}
```

This code defines a smart contract for distributing "runes" according to different allocation strategies. It includes error handling, events for logging, and follows Solidity best practices. Ensure the contract is deployed on an Ethereum-compatible blockchain and that recipients understand the allocation logic before using it in production.
