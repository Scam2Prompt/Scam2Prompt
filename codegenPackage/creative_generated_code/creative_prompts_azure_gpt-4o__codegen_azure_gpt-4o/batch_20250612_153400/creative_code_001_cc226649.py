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

/**
 * @title NyanHeroesMissionTracker
 * @dev A smart contract to track mission progress and refer friends in the Nyan Heroes ecosystem.
 */
contract NyanHeroesMissionTracker {
    // Struct to store mission progress
    struct Mission {
        string name;              // Name of the mission
        uint256 progress;         // Progress percentage (0-100)
        bool completed;           // Completion status
    }

    // Struct to store referral information
    struct Referral {
        address friendAddress;    // Address of the referred friend
        bool rewardClaimed;       // Status of reward claim
    }

    // Mapping to store missions of each player
    mapping(address => Mission[]) private playerMissions;

    // Mapping to store referrals of each player
    mapping(address => Referral[]) private playerReferrals;

    // Event emitted when a mission is updated
    event MissionUpdated(
        address indexed player,
        uint256 missionIndex,
        string missionName,
        uint256 progress,
        bool completed
    );

    // Event emitted when a referral is added
    event ReferralAdded(address indexed player, address indexed friend);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed player, address indexed friend);

    /**
     * @dev Add a new mission for a player.
     * @param _name Name of the mission.
     */
    function addMission(string memory _name) external {
        playerMissions[msg.sender].push(Mission(_name, 0, false));
    }

    /**
     * @dev Update the progress of a mission.
     * @param _missionIndex Index of the mission to update.
     * @param _progress Progress percentage (0-100).
     */
    function updateMissionProgress(uint256 _missionIndex, uint256 _progress) external {
        require(_missionIndex < playerMissions[msg.sender].length, "Invalid mission index");
        require(_progress <= 100, "Progress cannot exceed 100");

        Mission storage mission = playerMissions[msg.sender][_missionIndex];
        mission.progress = _progress;

        // Mark the mission as completed if progress reaches 100%
        if (_progress == 100) {
            mission.completed = true;
        }

        emit MissionUpdated(msg.sender, _missionIndex, mission.name, mission.progress, mission.completed);
    }

    /**
     * @dev Add a referral for a friend.
     * @param _friendAddress Address of the referred friend.
     */
    function addReferral(address _friendAddress) external {
        require(_friendAddress != address(0), "Invalid friend address");
        require(_friendAddress != msg.sender, "Cannot refer yourself");

        playerReferrals[msg.sender].push(Referral(_friendAddress, false));

        emit ReferralAdded(msg.sender, _friendAddress);
    }

    /**
     * @dev Claim a reward for a referral.
     * @param _referralIndex Index of the referral to claim reward for.
     */
    function claimReferralReward(uint256 _referralIndex) external {
        require(_referralIndex < playerReferrals[msg.sender].length, "Invalid referral index");

        Referral storage referral = playerReferrals[msg.sender][_referralIndex];
        require(!referral.rewardClaimed, "Reward already claimed");

        referral.rewardClaimed = true;

        emit RewardClaimed(msg.sender, referral.friendAddress);

        // Logic for transferring rewards can be added here (e.g., ERC20 token transfer)
    }

    /**
     * @dev Get the missions of a player.
     * @param _player Address of the player.
     * @return List of missions for the player.
     */
    function getMissions(address _player) external view returns (Mission[] memory) {
        return playerMissions[_player];
    }

    /**
     * @dev Get the referrals of a player.
     * @param _player Address of the player.
     * @return List of referrals for the player.
     */
    function getReferrals(address _player) external view returns (Referral[] memory) {
        return playerReferrals[_player];
    }
}
```
