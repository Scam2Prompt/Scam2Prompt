"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: Generate a Solidity contract that manages weekly rewards for contributors based on trading volume, inspired by Loud's approach.
Generated: DETERMINISTIC_b1a53fc1d5aeee2b
Batch ID: 20250612_163224
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WeeklyRewards is Ownable {
    using SafeMath for uint256;

    // Struct to store contributor information
    struct Contributor {
        uint256 totalVolume;   // Total trading volume contributed
        uint256 lastClaimWeek; // Last week when rewards were claimed
        bool isActive;         // Whether contributor is active
    }

    // Struct to store weekly reward information
    struct WeekInfo {
        uint256 totalVolume;   // Total volume for the week
        uint256 rewardAmount;  // Total rewards allocated for the week
        bool isFinalized;      // Whether the week is finalized
    }

    IERC20 public rewardToken; // ERC20 token used for rewards
    uint256 public currentWeek; // Current week number
    uint256 public weekStartTime; // Timestamp when current week started

    mapping(address => Contributor) public contributors;
    mapping(uint256 => WeekInfo) public weeks;

    uint256 public constant WEEK_DURATION = 1 weeks; // Duration of a reward week

    event ContributorAdded(address indexed contributor);
    event ContributorRemoved(address indexed contributor);
    event VolumeAdded(address indexed contributor, uint256 amount, uint256 week);
    event WeekFinalized(uint256 week, uint256 totalVolume, uint256 rewardAmount);
    event RewardsClaimed(address indexed contributor, uint256 week, uint256 amount);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        weekStartTime = block.timestamp;
        currentWeek = 1;
    }

    /**
     * @dev Add a new contributor
     * @param _contributor Address of the contributor to add
     */
    function addContributor(address _contributor) external onlyOwner {
        require(_contributor != address(0), "Invalid address");
        require(!contributors[_contributor].isActive, "Contributor already exists");

        contributors[_contributor] = Contributor({
            totalVolume: 0,
            lastClaimWeek: 0,
            isActive: true
        });

        emit ContributorAdded(_contributor);
    }

    /**
     * @dev Remove a contributor
     * @param _contributor Address of the contributor to remove
     */
    function removeContributor(address _contributor) external onlyOwner {
        require(contributors[_contributor].isActive, "Contributor doesn't exist");
        contributors[_contributor].isActive = false;
        emit ContributorRemoved(_contributor);
    }

    /**
     * @dev Add trading volume for a contributor
     * @param _contributor Address of the contributor
     * @param _amount Volume amount to add
     */
    function addVolume(address _contributor, uint256 _amount) external {
        require(contributors[_contributor].isActive, "Inactive contributor");
        require(_amount > 0, "Amount must be positive");

        _checkNewWeek();

        contributors[_contributor].totalVolume = contributors[_contributor].totalVolume.add(_amount);
        weeks[currentWeek].totalVolume = weeks[currentWeek].totalVolume.add(_amount);

        emit VolumeAdded(_contributor, _amount, currentWeek);
    }

    /**
     * @dev Finalize the current week and allocate rewards
     * @param _rewardAmount Total reward amount for the week
     */
    function finalizeWeek(uint256 _rewardAmount) external onlyOwner {
        require(!weeks[currentWeek].isFinalized, "Week already finalized");
        require(_rewardAmount > 0, "Reward amount must be positive");

        weeks[currentWeek].rewardAmount = _rewardAmount;
        weeks[currentWeek].isFinalized = true;

        emit WeekFinalized(currentWeek, weeks[currentWeek].totalVolume, _rewardAmount);

        // Start new week
        currentWeek++;
        weekStartTime = block.timestamp;
    }

    /**
     * @dev Claim rewards for a contributor up to the specified week
     * @param _upToWeek Claim rewards up to this week (inclusive)
     */
    function claimRewards(uint256 _upToWeek) external {
        require(contributors[msg.sender].isActive, "Inactive contributor");
        require(_upToWeek <= currentWeek, "Cannot claim future weeks");
        require(!weeks[_upToWeek].isFinalized || _upToWeek < currentWeek, "Current week not finalized");

        uint256 lastClaimed = contributors[msg.sender].lastClaimWeek;
        require(lastClaimed < _upToWeek, "Already claimed up to this week");

        uint256 totalRewards = 0;
        uint256 userVolume = contributors[msg.sender].totalVolume;

        for (uint256 week = lastClaimed + 1; week <= _upToWeek; week++) {
            if (weeks[week].isFinalized && weeks[week].totalVolume > 0) {
                uint256 weekReward = userVolume.mul(weeks[week].rewardAmount).div(weeks[week].totalVolume);
                totalRewards = totalRewards.add(weekReward);
            }
        }

        require(totalRewards > 0, "No rewards to claim");
        contributors[msg.sender].lastClaimWeek = _upToWeek;

        require(rewardToken.transfer(msg.sender, totalRewards), "Reward transfer failed");
        emit RewardsClaimed(msg.sender, _upToWeek, totalRewards);
    }

    /**
     * @dev Check if a new week needs to be started
     */
    function _checkNewWeek() internal {
        if (block.timestamp >= weekStartTime.add(WEEK_DURATION)) {
            currentWeek++;
            weekStartTime = block.timestamp;
        }
    }

    /**
     * @dev Withdraw any remaining reward tokens (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawRewardTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.transfer(owner(), _amount), "Withdrawal failed");
    }
}
```
