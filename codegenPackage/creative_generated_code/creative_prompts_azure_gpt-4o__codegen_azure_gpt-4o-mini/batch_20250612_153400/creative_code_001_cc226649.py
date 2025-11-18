"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes.pages.dev
Prompt: Generate code to track mission progress and refer friends in the Nyan Heroes ecosystem using blockchain-based smart contracts.
Generated: DETERMINISTIC_cc2266494c4e2a49
Batch ID: 20250612_153400
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

// Importing the OpenZeppelin Contracts for ERC20 token and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Nyan Heroes token (ERC20)
interface INyanHeroesToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract to track mission progress and refer friends in the Nyan Heroes ecosystem
contract NyanHeroesMissionTracker is Ownable {
    // Structure to hold mission details
    struct Mission {
        uint256 id;
        string description;
        uint256 reward;
        bool completed;
    }

    // Mapping of user addresses to their completed missions
    mapping(address => uint256[]) private userMissions;

    // Mapping of mission ID to Mission details
    mapping(uint256 => Mission) private missions;

    // Nyan Heroes token contract
    INyanHeroesToken public nyanHeroesToken;

    // Event emitted when a mission is completed
    event MissionCompleted(address indexed user, uint256 missionId);

    // Event emitted when a referral is made
    event ReferralMade(address indexed referrer, address indexed referee);

    // Constructor to initialize the contract with the Nyan Heroes token address
    constructor(address _nyanHeroesToken) {
        nyanHeroesToken = INyanHeroesToken(_nyanHeroesToken);
    }

    // Function to create a new mission
    function createMission(uint256 _id, string memory _description, uint256 _reward) external onlyOwner {
        require(_reward > 0, "Reward must be greater than zero");
        missions[_id] = Mission(_id, _description, _reward, false);
    }

    // Function to complete a mission and receive rewards
    function completeMission(uint256 _missionId) external {
        Mission storage mission = missions[_missionId];

        // Check if the mission exists and is not already completed
        require(mission.id != 0, "Mission does not exist");
        require(!mission.completed, "Mission already completed");

        // Mark mission as completed and record it for the user
        mission.completed = true;
        userMissions[msg.sender].push(_missionId);

        // Mint rewards to the user
        nyanHeroesToken.mint(msg.sender, mission.reward);

        emit MissionCompleted(msg.sender, _missionId);
    }

    // Function to refer a new user
    function referFriend(address _friend) external {
        require(_friend != msg.sender, "You cannot refer yourself");
        emit ReferralMade(msg.sender, _friend);
    }

    // Function to get user missions
    function getUserMissions(address user) external view returns (uint256[] memory) {
        return userMissions[user];
    }

    // Function to get mission details by ID
    function getMission(uint256 _missionId) external view returns (Mission memory) {
        return missions[_missionId];
    }
}
```
