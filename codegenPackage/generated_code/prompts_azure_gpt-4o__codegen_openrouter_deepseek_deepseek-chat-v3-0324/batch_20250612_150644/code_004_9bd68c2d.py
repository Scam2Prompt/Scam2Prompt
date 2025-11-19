"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Provide a step-by-step guide to implement a decentralized staking protocol with spatial segmentation, as described in Polygon6D, using the Polygon network.
Generated: DETERMINISTIC_9bd68c2d9cbea00a
Batch ID: 20250612_150644
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Polygon6D Staking Protocol
 * @dev A decentralized staking protocol with spatial segmentation on Polygon network
 */
contract Polygon6DStaking is Ownable, ReentrancyGuard {
    // Structs
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
        uint256[] segmentIds;
    }

    struct Segment {
        uint256 id;
        uint256 totalStaked;
        uint256 rewardPerTokenStored;
        uint256 lastUpdateTime;
        bool active;
    }

    // Constants
    uint256 public constant REWARD_RATE = 100; // 100 tokens per second
    uint256 public constant LOCK_PERIOD = 30 days;
    uint256 public constant MAX_SEGMENTS = 6;

    // State variables
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    uint256 public totalStaked;
    uint256 public lastRewardTime;
    uint256 public rewardPerTokenStored;

    // Mappings
    mapping(address => Staker) public stakers;
    mapping(uint256 => Segment) public segments;

    // Events
    event Staked(address indexed user, uint256 amount, uint256[] segmentIds);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event SegmentAdded(uint256 indexed segmentId);
    event SegmentDeactivated(uint256 indexed segmentId);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     */
    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Add a new segment
     * @param segmentId The ID of the segment to add
     */
    function addSegment(uint256 segmentId) external onlyOwner {
        require(segmentId > 0 && segmentId <= MAX_SEGMENTS, "Invalid segment ID");
        require(!segments[segmentId].active, "Segment already exists");

        segments[segmentId] = Segment({
            id: segmentId,
            totalStaked: 0,
            rewardPerTokenStored: 0,
            lastUpdateTime: block.timestamp,
            active: true
        });

        emit SegmentAdded(segmentId);
    }

    /**
     * @dev Deactivate a segment
     * @param segmentId The ID of the segment to deactivate
     */
    function deactivateSegment(uint256 segmentId) external onlyOwner {
        require(segments[segmentId].active, "Segment not active");
        segments[segmentId].active = false;
        emit SegmentDeactivated(segmentId);
    }

    /**
     * @dev Stake tokens into specified segments
     * @param amount The amount of tokens to stake
     * @param segmentIds Array of segment IDs to stake into
     */
    function stake(uint256 amount, uint256[] memory segmentIds) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(segmentIds.length > 0, "No segments specified");
        require(segmentIds.length <= MAX_SEGMENTS, "Too many segments");

        _updateReward(msg.sender);

        // Validate segments
        for (uint256 i = 0; i < segmentIds.length; i++) {
            require(segments[segmentIds[i]].active, "Segment not active");
        }

        // Transfer tokens from user
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker info
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastStakeTime = block.timestamp;

        // Add segments if not already present
        for (uint256 i = 0; i < segmentIds.length; i++) {
            bool alreadyExists = false;
            for (uint256 j = 0; j < staker.segmentIds.length; j++) {
                if (staker.segmentIds[j] == segmentIds[i]) {
                    alreadyExists = true;
                    break;
                }
            }
            if (!alreadyExists) {
                staker.segmentIds.push(segmentIds[i]);
            }
        }

        // Update segment totals
        uint256 amountPerSegment = amount / segmentIds.length;
        for (uint256 i = 0; i < segmentIds.length; i++) {
            segments[segmentIds[i]].totalStaked += amountPerSegment;
        }

        totalStaked += amount;
        emit Staked(msg.sender, amount, segmentIds);
    }

    /**
     * @dev Unstake tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        require(block.timestamp >= staker.lastStakeTime + LOCK_PERIOD, "Tokens are locked");

        _updateReward(msg.sender);

        // Calculate amount to remove from each segment
        uint256[] memory segmentIds = staker.segmentIds;
        uint256 amountPerSegment = amount / segmentIds.length;

        // Update segment totals
        for (uint256 i = 0; i < segmentIds.length; i++) {
            segments[segmentIds[i]].totalStaked -= amountPerSegment;
        }

        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimReward() external nonReentrant {
        _updateReward(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = 0;
            rewardToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return Pending rewards
     */
    function pendingReward(address stakerAddress) external view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 reward = staker.rewardDebt;

        for (uint256 i = 0; i < staker.segmentIds.length; i++) {
            Segment memory segment = segments[staker.segmentIds[i]];
            if (segment.totalStaked > 0) {
                uint256 timeElapsed = block.timestamp - segment.lastUpdateTime;
                uint256 segmentReward = (timeElapsed * REWARD_RATE * (staker.amount / staker.segmentIds.length)) / segment.totalStaked;
                reward += segmentReward;
            }
        }

        return reward;
    }

    /**
     * @dev Internal function to update reward for a staker
     * @param stakerAddress Address of the staker
     */
    function _updateReward(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amount == 0) return;

        for (uint256 i = 0; i < staker.segmentIds.length; i++) {
            uint256 segmentId = staker.segmentIds[i];
            Segment storage segment = segments[segmentId];

            if (segment.totalStaked > 0) {
                uint256 timeElapsed = block.timestamp - segment.lastUpdateTime;
                uint256 segmentReward = (timeElapsed * REWARD_RATE * (staker.amount / staker.segmentIds.length)) / segment.totalStaked;
                staker.rewardDebt += segmentReward;
                segment.rewardPerTokenStored += segmentReward;
            }

            segment.lastUpdateTime = block.timestamp;
        }
    }
}
```
