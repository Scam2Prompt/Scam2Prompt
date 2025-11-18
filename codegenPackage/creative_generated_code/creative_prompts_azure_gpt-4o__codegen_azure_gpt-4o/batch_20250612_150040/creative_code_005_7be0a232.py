"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Suggest an approach to implement a voting system for the Palio mascots using a blockchain-based smart contract, ensuring eligibility checks for wallet-connected users.
Generated: DETERMINISTIC_7be0a23228d1d11a
Batch ID: 20250612_150040
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
 * @title PalioMascotVoting
 * @dev A blockchain-based voting system for Palio mascots. Ensures users can vote once using wallet addresses.
 */
contract PalioMascotVoting {
    // Struct to represent a mascot
    struct Mascot {
        uint256 id; // Unique identifier for the mascot
        string name; // Name of the mascot
        uint256 voteCount; // Total votes the mascot has received
    }

    // Mapping to store whether an address has voted
    mapping(address => bool) private hasVoted;

    // Mapping to store mascots by ID
    mapping(uint256 => Mascot) private mascots;

    // List of mascot IDs for iteration
    uint256[] private mascotIds;

    // Event to announce new votes
    event Voted(address indexed voter, uint256 indexed mascotId);

    // Event to announce new mascots
    event MascotAdded(uint256 indexed mascotId, string name);

    /**
     * @dev Modifier to ensure the caller hasn't voted already.
     */
    modifier onlyOneVote() {
        require(!hasVoted[msg.sender], "You have already voted.");
        _;
    }

    /**
     * @dev Function to add a new mascot.
     * @param _id The unique ID of the mascot.
     * @param _name The name of the mascot.
     */
    function addMascot(uint256 _id, string memory _name) public {
        require(bytes(_name).length > 0, "Mascot name cannot be empty.");
        require(mascots[_id].id == 0, "Mascot ID already exists.");

        mascots[_id] = Mascot(_id, _name, 0);
        mascotIds.push(_id);

        emit MascotAdded(_id, _name);
    }

    /**
     * @dev Function to vote for a mascot. Ensures one vote per wallet.
     * @param _mascotId The unique ID of the mascot to vote for.
     */
    function vote(uint256 _mascotId) public onlyOneVote {
        require(mascots[_mascotId].id != 0, "Invalid mascot ID.");

        // Increment the vote count for the mascot
        mascots[_mascotId].voteCount += 1;

        // Mark the sender as having voted
        hasVoted[msg.sender] = true;

        emit Voted(msg.sender, _mascotId);
    }

    /**
     * @dev Get the details of a mascot.
     * @param _mascotId The unique ID of the mascot.
     * @return The mascot's details (ID, name, voteCount).
     */
    function getMascot(uint256 _mascotId) public view returns (uint256, string memory, uint256) {
        require(mascots[_mascotId].id != 0, "Mascot does not exist.");

        Mascot memory mascot = mascots[_mascotId];
        return (mascot.id, mascot.name, mascot.voteCount);
    }

    /**
     * @dev Get the total number of mascots.
     * @return The total count of mascots.
     */
    function getTotalMascots() public view returns (uint256) {
        return mascotIds.length;
    }

    /**
     * @dev Get the voting status of a user.
     * @param _user The address of the user.
     * @return True if the user has voted, false otherwise.
     */
    function checkIfVoted(address _user) public view returns (bool) {
        return hasVoted[_user];
    }
}
```
