"""
Generated Code Metadata:
========================
Original URL: https://nyan-8iu.pages.dev
Prompt: Write a Solidity smart contract to manage seasonal events (e.g., Season 3) in a blockchain game, including reward distribution and mission tracking.
Generated: DETERMINISTIC_40cef9a55f66c172
Batch ID: 20250612_151027
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SeasonManager is Ownable, ReentrancyGuard {
    struct Mission {
        uint256 id;
        string name;
        uint256 rewardAmount;
        bool isActive;
    }

    struct PlayerProgress {
        uint256 completedMissions;
        uint256 claimedRewards;
        mapping(uint256 => bool) missionCompletion;
    }

    // Season details
    uint256 public seasonId;
    string public seasonName;
    uint256 public seasonStart;
    uint256 public seasonEnd;
    bool public isSeasonActive;

    // Reward token
    IERC20 public rewardToken;

    // Missions tracking
    Mission[] public missions;
    mapping(address => PlayerProgress) public playerProgress;

    // Events
    event SeasonStarted(uint256 seasonId, string seasonName, uint256 startTime, uint256 endTime);
    event SeasonEnded(uint256 seasonId);
    event MissionAdded(uint256 missionId, string name, uint256 rewardAmount);
    event MissionCompleted(address player, uint256 missionId);
    event RewardsClaimed(address player, uint256 amount);

    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }

    modifier onlyActiveSeason() {
        require(isSeasonActive, "Season is not active");
        require(block.timestamp >= seasonStart && block.timestamp <= seasonEnd, "Not within season timeframe");
        _;
    }

    function startSeason(
        uint256 _seasonId,
        string memory _seasonName,
        uint256 _durationInDays
    ) external onlyOwner {
        require(!isSeasonActive, "Season already active");
        require(_durationInDays > 0, "Duration must be positive");

        seasonId = _seasonId;
        seasonName = _seasonName;
        seasonStart = block.timestamp;
        seasonEnd = seasonStart + (_durationInDays * 1 days);
        isSeasonActive = true;

        emit SeasonStarted(_seasonId, _seasonName, seasonStart, seasonEnd);
    }

    function endSeason() external onlyOwner onlyActiveSeason {
        isSeasonActive = false;
        emit SeasonEnded(seasonId);
    }

    function addMission(
        string memory _name,
        uint256 _rewardAmount
    ) external onlyOwner onlyActiveSeason {
        uint256 missionId = missions.length;
        missions.push(Mission({
            id: missionId,
            name: _name,
            rewardAmount: _rewardAmount,
            isActive: true
        }));

        emit MissionAdded(missionId, _name, _rewardAmount);
    }

    function toggleMission(uint256 _missionId, bool _isActive) external onlyOwner onlyActiveSeason {
        require(_missionId < missions.length, "Invalid mission ID");
        missions[_missionId].isActive = _isActive;
    }

    function completeMission(uint256 _missionId) external onlyActiveSeason nonReentrant {
        require(_missionId < missions.length, "Invalid mission ID");
        Mission storage mission = missions[_missionId];
        require(mission.isActive, "Mission is not active");

        PlayerProgress storage progress = playerProgress[msg.sender];
        require(!progress.missionCompletion[_missionId], "Mission already completed");

        progress.missionCompletion[_missionId] = true;
        progress.completedMissions += 1;

        emit MissionCompleted(msg.sender, _missionId);
    }

    function claimRewards() external nonReentrant {
        PlayerProgress storage progress = playerProgress[msg.sender];
        require(progress.completedMissions > progress.claimedRewards, "No rewards to claim");

        uint256 totalRewards = 0;
        for (uint256 i = 0; i < missions.length; i++) {
            if (progress.missionCompletion[i] && missions[i].isActive) {
                totalRewards += missions[i].rewardAmount;
            }
        }

        uint256 claimable = totalRewards - progress.claimedRewards;
        require(claimable > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= claimable, "Insufficient reward tokens");

        progress.claimedRewards = totalRewards;
        rewardToken.transfer(msg.sender, claimable);

        emit RewardsClaimed(msg.sender, claimable);
    }

    function getPlayerCompletedMissions(address _player) external view returns (uint256[] memory) {
        PlayerProgress storage progress = playerProgress[_player];
        uint256[] memory completed = new uint256[](progress.completedMissions);
        uint256 counter = 0;

        for (uint256 i = 0; i < missions.length; i++) {
            if (progress.missionCompletion[i]) {
                completed[counter] = i;
                counter++;
            }
        }

        return completed;
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.transfer(owner(), _amount), "Token transfer failed");
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardToken.transfer(owner(), balance), "Token transfer failed");
    }
}
```
