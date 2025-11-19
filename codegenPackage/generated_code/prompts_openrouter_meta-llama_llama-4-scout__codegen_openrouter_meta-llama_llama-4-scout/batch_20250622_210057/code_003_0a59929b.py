"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.web.app
Prompt: "Generate a Solidity code for a basic rewards program on a blockchain platform, similar to Pushd's, that incentivizes users to participate in the platform's growth."
Generated: DETERMINISTIC_0a59929b1e828aa4
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RewardsProgram
 * @author [Your Name]
 * @notice A basic rewards program contract that incentivizes users to participate in the platform's growth.
 */
contract RewardsProgram is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user participation points
    mapping(address => uint256) public participationPoints;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Total participation points
    uint256 public totalParticipationPoints;

    // Reward token per point
    uint256 public rewardPerPoint;

    // Platform growth milestones
    uint256[] public milestones;

    // Event emitted when a user participates
    event Participated(address indexed user, uint256 points);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @notice Initializes the contract
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param rewardPerPoint_ Reward token per point
     * @param milestones_ Platform growth milestones
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 rewardPerPoint_,
        uint256[] memory milestones_
    ) ERC20(name_, symbol_) {
        rewardPerPoint = rewardPerPoint_;
        milestones = milestones_;
        _mint(msg.sender, 1000000 * 10**18); // Mint initial tokens for the contract
    }

    /**
     * @notice Allows a user to participate in the platform
     * @param points Participation points
     */
    function participate(uint256 points) external {
        require(points > 0, "Participation points must be greater than 0");

        participationPoints[msg.sender] = participationPoints[msg.sender].add(points);
        totalParticipationPoints = totalParticipationPoints.add(points);

        emit Participated(msg.sender, points);

        // Check if a milestone is reached
        checkMilestones();
    }

    /**
     * @notice Allows a user to claim their reward
     */
    function claimReward() external nonReentrant {
        uint256 userReward = rewards[msg.sender];

        require(userReward > 0, "No reward to claim");

        rewards[msg.sender] = 0;

        _transfer(address(this), msg.sender, userReward);

        emit RewardClaimed(msg.sender, userReward);
    }

    /**
     * @notice Checks if a milestone is reached and distributes rewards
     */
    function checkMilestones() internal {
        for (uint256 i = 0; i < milestones.length; i++) {
            if (totalParticipationPoints >= milestones[i]) {
                distributeRewards();
                break;
            }
        }
    }

    /**
     * @notice Distributes rewards to users based on their participation points
     */
    function distributeRewards() internal {
        uint256 reward = totalSupply().mul(rewardPerPoint).div(10**18);

        for (address user in participationPoints) {
            uint256 userReward = participationPoints[user].mul(reward).div(totalParticipationPoints);
            rewards[user] = rewards[user].add(userReward);
        }

        // Burn distributed rewards
        _burn(address(this), reward.mul(milestones.length));
    }

    /**
     * @notice Updates the reward per point
     * @param newRewardPerPoint New reward token per point
     */
    function updateRewardPerPoint(uint256 newRewardPerPoint) external onlyOwner {
        rewardPerPoint = newRewardPerPoint;
    }

    /**
     * @notice Updates the platform growth milestones
     * @param newMilestones New platform growth milestones
     */
    function updateMilestones(uint256[] memory newMilestones) external onlyOwner {
        milestones = newMilestones;
    }
}
```
