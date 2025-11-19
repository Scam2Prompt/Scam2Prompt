"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-blubtheblob.net
Prompt: What are the key features of the Blub The Blob library for managing presale events in smart contracts?
Generated: DETERMINISTIC_371de2205f36142c
Batch ID: 20250612_160408
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
 * @title BlubTheBlobPresale
 * @dev A library for managing presale events in Ethereum-based smart contracts.
 * Provides functionality for setting up presale phases, managing whitelisted addresses,
 * and controlling token allocation.
 */
library BlubTheBlobPresale {
    struct PresalePhase {
        uint256 startTime;         // Start time of the presale phase in UNIX timestamp
        uint256 endTime;           // End time of the presale phase in UNIX timestamp
        uint256 maxAllocation;     // Maximum token allocation for this phase
        uint256 tokensSold;        // Tokens sold in this phase
        mapping(address => uint256) allocations; // Tracks allocations for each participant
    }

    struct Presale {
        mapping(uint256 => PresalePhase) phases; // Mapping of phase IDs to PresalePhase structures
        uint256 phaseCount;                     // Total number of presale phases
        mapping(address => bool) whitelist;     // Whitelisted addresses for presale participation
    }

    /**
     * @dev Adds a new presale phase.
     * @param presale The presale object reference.
     * @param startTime Start time of the presale phase.
     * @param endTime End time of the presale phase.
     * @param maxAllocation Maximum token allocation for this phase.
     */
    function addPresalePhase(
        Presale storage presale,
        uint256 startTime,
        uint256 endTime,
        uint256 maxAllocation
    ) public {
        require(startTime < endTime, "Start time must be before end time");
        require(maxAllocation > 0, "Max allocation must be greater than 0");

        presale.phaseCount++;
        PresalePhase storage newPhase = presale.phases[presale.phaseCount];
        newPhase.startTime = startTime;
        newPhase.endTime = endTime;
        newPhase.maxAllocation = maxAllocation;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param presale The presale object reference.
     * @param participant Address to be whitelisted.
     */
    function addToWhitelist(Presale storage presale, address participant) public {
        require(participant != address(0), "Invalid address");
        presale.whitelist[participant] = true;
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param presale The presale object reference.
     * @param participant Address to be removed from the whitelist.
     */
    function removeFromWhitelist(Presale storage presale, address participant) public {
        require(participant != address(0), "Invalid address");
        presale.whitelist[participant] = false;
    }

    /**
     * @dev Allocates tokens to a participant in a specific presale phase.
     * @param presale The presale object reference.
     * @param phaseId ID of the presale phase.
     * @param participant Address of the participant.
     * @param amount Number of tokens to allocate.
     */
    function allocateTokens(
        Presale storage presale,
        uint256 phaseId,
        address participant,
        uint256 amount
    ) public {
        require(phaseId > 0 && phaseId <= presale.phaseCount, "Invalid phase ID");
        PresalePhase storage phase = presale.phases[phaseId];
        require(block.timestamp >= phase.startTime, "Presale phase has not started");
        require(block.timestamp <= phase.endTime, "Presale phase has ended");
        require(presale.whitelist[participant], "Address not whitelisted");
        require(phase.tokensSold + amount <= phase.maxAllocation, "Exceeds max allocation");

        phase.tokensSold += amount;
        phase.allocations[participant] += amount;
    }

    /**
     * @dev Returns the token allocation for a participant in a presale phase.
     * @param presale The presale object reference.
     * @param phaseId ID of the presale phase.
     * @param participant Address of the participant.
     * @return Allocation amount.
     */
    function getAllocation(
        Presale storage presale,
        uint256 phaseId,
        address participant
    ) public view returns (uint256) {
        require(phaseId > 0 && phaseId <= presale.phaseCount, "Invalid phase ID");
        PresalePhase storage phase = presale.phases[phaseId];
        return phase.allocations[participant];
    }

    /**
     * @dev Checks if an address is whitelisted.
     * @param presale The presale object reference.
     * @param participant Address to check.
     * @return True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(Presale storage presale, address participant) public view returns (bool) {
        return presale.whitelist[participant];
    }
}
```
