"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.com
Prompt: How can I implement a feature to show the Hall of Fame participants in the RedStone Airdrop using their wallet addresses?
Generated: DETERMINISTIC_43d4f58813bbb383
Batch ID: 20250612_160309
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract RedStoneAirdropHallOfFame is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Set to store hall of fame participants
    EnumerableSet.AddressSet private _hallOfFameParticipants;

    // Event emitted when a participant is added to the hall of fame
    event ParticipantAdded(address indexed participant);
    
    // Event emitted when a participant is removed from the hall of fame
    event ParticipantRemoved(address indexed participant);

    /**
     * @dev Adds a participant to the hall of fame
     * @param participant The wallet address to add
     */
    function addToHallOfFame(address participant) external onlyOwner {
        require(participant != address(0), "Invalid address");
        require(!_hallOfFameParticipants.contains(participant), "Already in hall of fame");
        
        _hallOfFameParticipants.add(participant);
        emit ParticipantAdded(participant);
    }

    /**
     * @dev Removes a participant from the hall of fame
     * @param participant The wallet address to remove
     */
    function removeFromHallOfFame(address participant) external onlyOwner {
        require(_hallOfFameParticipants.contains(participant), "Not in hall of fame");
        
        _hallOfFameParticipants.remove(participant);
        emit ParticipantRemoved(participant);
    }

    /**
     * @dev Checks if an address is in the hall of fame
     * @param participant The wallet address to check
     * @return bool True if address is in hall of fame
     */
    function isInHallOfFame(address participant) external view returns (bool) {
        return _hallOfFameParticipants.contains(participant);
    }

    /**
     * @dev Returns all hall of fame participants
     * @return address[] Array of participant addresses
     */
    function getAllHallOfFameParticipants() external view returns (address[] memory) {
        return _hallOfFameParticipants.values();
    }

    /**
     * @dev Returns the number of hall of fame participants
     * @return uint256 Count of participants
     */
    function getHallOfFameCount() external view returns (uint256) {
        return _hallOfFameParticipants.length();
    }
}
```
