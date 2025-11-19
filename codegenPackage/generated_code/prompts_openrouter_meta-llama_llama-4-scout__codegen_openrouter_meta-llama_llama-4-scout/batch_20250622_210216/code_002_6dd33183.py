"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-io.web.app
Prompt: Generate a Solidity code snippet for a staking mechanism similar to the one described in the Rebel Satoshi project, which rewards users with a percentage return for locking up $RBLZ tokens.
Generated: DETERMINISTIC_6dd331832c8315aa
Batch ID: 20250622_210216
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

/**
 * @title RebelSatoshiStaking
 * @author [Your Name]
 * @notice A staking mechanism for $RBLZ tokens, rewarding users with a percentage return.
 */
contract RebelSatoshiStaking is ReentrancyGuard {
    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // $RBLZ token contract
    ERC20 public rblzToken;

    // Staking reward percentage (e.g., 10% = 1000)
    uint256 public rewardPercentage;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Timestamp when staking starts
    uint256 public stakingStartTime;

    // Event emitted when user stakes $RBLZ tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes $RBLZ tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when staking rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _rblzToken $RBLZ token contract address
     * @param _rewardPercentage Staking reward percentage (e.g., 10% = 1000)
     * @param _stakingDuration Staking duration in seconds
     */
    constructor(
        address _rblzToken,
        uint256 _rewardPercentage,
        uint256 _stakingDuration
    ) public {
        require(_rblzToken != address(0), "Invalid $RBLZ token contract address");
        require(_rewardPercentage > 0, "Reward percentage must be greater than 0");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");

        rblzToken = ERC20(_rblzToken);
        rewardPercentage = _rewardPercentage;
        stakingDuration = _stakingDuration;
        stakingStartTime = block.timestamp;
    }

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 stakedAt;
    }

    /**
     * @dev Stake $RBLZ tokens for a specified amount
     * @param _amount Amount of $RBLZ tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than 0");
        require(rblzToken.balanceOf(msg.sender) >= _amount, "Insufficient $RBLZ token balance");
        require(stakers[msg.sender].stakedAmount == 0, "User already has staked tokens");

        // Transfer $RBLZ tokens to staking contract
        require(rblzToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer $RBLZ tokens");

        // Update staker information
        stakers[msg.sender] = Staker(_amount, block.timestamp);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $RBLZ tokens
     */
    function unstake() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "User has no staked tokens");

        // Calculate staking rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].stakedAt = 0;

        // Transfer $RBLZ tokens and rewards to user
        require(rblzToken.transfer(msg.sender, stakedAmount + rewards), "Failed to transfer $RBLZ tokens");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Staker memory staker = stakers[_user];
        require(staker.stakedAt != 0, "User has no staked tokens");

        // Calculate staking duration
        uint256 stakingElapsed = block.timestamp - staker.stakedAt;
        if (stakingElapsed < stakingDuration) {
            return 0;
        }

        // Calculate rewards
        uint256 rewards = (staker.stakedAmount * rewardPercentage * (stakingElapsed - staker.stakedAt)) / (10000 * 365 * 24 * 60 * 60);

        return rewards;
    }

    /**
     * @dev Get user staking information
     * @param _user User address
     * @return Staked amount and staked timestamp
     */
    function getStakerInfo(address _user) external view returns (uint256, uint256) {
        Staker memory staker = stakers[_user];
        return (staker.stakedAmount, staker.stakedAt);
    }
}
```
