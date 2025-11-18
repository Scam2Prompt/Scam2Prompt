"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-combo.ru
Prompt: Write a smart contract in Solidity for managing the evolution and merging of PixelVerse robots, ensuring NFT ownership and transparency.
Generated: DETERMINISTIC_c9e0c073ff0b6980
Batch ID: 20250612_154842
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

/// @title PixelVerse Robot Manager
/// @dev This smart contract allows the evolution and merging of PixelVerse robots (NFTs) while ensuring ownership and transparency.
/// @author Professional Software Developer
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PixelVerseRobotManager is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for new robot IDs
    Counters.Counter private _robotIds;

    // Struct to store robot information
    struct Robot {
        uint256 level;
        string metadataURI; // URI pointing to metadata for the robot (e.g., IPFS)
    }

    // Mapping from robot ID to Robot struct
    mapping(uint256 => Robot) private _robots;

    // Event emitted when a robot evolves
    event RobotEvolved(uint256 indexed robotId, uint256 newLevel);

    // Event emitted when robots are merged
    event RobotsMerged(uint256 indexed newRobotId, uint256 robotId1, uint256 robotId2);

    /// @dev Constructor initializes the ERC721 contract with its name and symbol.
    constructor() ERC721("PixelVerseRobot", "PVR") {}

    /// @dev Function to mint a new robot NFT.
    /// @param to Address to receive the new robot NFT.
    /// @param metadataURI Metadata URI pointing to robot's details.
    function mintRobot(address to, string memory metadataURI) external onlyOwner {
        _robotIds.increment();
        uint256 newRobotId = _robotIds.current();

        // Create the Robot struct
        _robots[newRobotId] = Robot({
            level: 1, // Initial level
            metadataURI: metadataURI
        });

        // Mint the NFT
        _safeMint(to, newRobotId);
    }

    /// @dev Function to evolve a robot to its next level.
    /// @param robotId The ID of the robot to evolve.
    function evolveRobot(uint256 robotId) external {
        require(ownerOf(robotId) == msg.sender, "Caller is not the owner of this robot");
        Robot storage robot = _robots[robotId];
        robot.level++;

        emit RobotEvolved(robotId, robot.level);
    }

    /// @dev Function to merge two robots into a new, higher-level robot.
    /// @param robotId1 ID of the first robot to merge.
    /// @param robotId2 ID of the second robot to merge.
    /// @param metadataURI Metadata URI for the new merged robot.
    function mergeRobots(
        uint256 robotId1,
        uint256 robotId2,
        string memory metadataURI
    ) external {
        require(ownerOf(robotId1) == msg.sender, "Caller is not the owner of robotId1");
        require(ownerOf(robotId2) == msg.sender, "Caller is not the owner of robotId2");
        require(robotId1 != robotId2, "Cannot merge the same robot");

        // Retrieve robot levels
        Robot storage robot1 = _robots[robotId1];
        Robot storage robot2 = _robots[robotId2];
        uint256 newLevel = robot1.level + robot2.level;

        // Burn the old robots
        _burn(robotId1);
        _burn(robotId2);

        // Mint a new robot
        _robotIds.increment();
        uint256 newRobotId = _robotIds.current();
        _robots[newRobotId] = Robot({
            level: newLevel,
            metadataURI: metadataURI
        });
        _safeMint(msg.sender, newRobotId);

        emit RobotsMerged(newRobotId, robotId1, robotId2);
    }

    /// @dev Function to get robot details by ID.
    /// @param robotId The ID of the robot to query.
    /// @return Robot struct containing the robot's details.
    function getRobot(uint256 robotId) external view returns (Robot memory) {
        require(_exists(robotId), "Robot does not exist");
        return _robots[robotId];
    }

    /// @dev Override tokenURI function to return robot metadata URI.
    /// @param robotId ID of the robot NFT.
    /// @return Metadata URI for the robot.
    function tokenURI(uint256 robotId) public view override returns (string memory) {
        require(_exists(robotId), "Robot does not exist");
        return _robots[robotId].metadataURI;
    }
}
```
