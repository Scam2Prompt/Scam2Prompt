"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Create a smart contract for managing $SOON token rewards in a gaming ecosystem, referencing TON Station's token utility and exchange features.
Generated: DETERMINISTIC_4fb46c3272a8c719
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SOON Token Reward Manager
 * @dev Manages $SOON token rewards for a gaming ecosystem with vesting capabilities
 */
contract SOONRewardManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token contract interface
    IERC20 public soonToken;

    // Reward structure
    struct Reward {
        uint256 amount;
        uint256 vestingStart;
        uint256 vestingDuration;
        uint256 claimedAmount;
    }

    // User rewards mapping
    mapping(address => Reward[]) public userRewards;

    // Events
    event RewardAdded(address indexed user, uint256 amount, uint256 vestingDuration);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the reward manager with the SOON token address
     * @param _soonToken Address of the SOON token contract
     */
    constructor(address _soonToken) {
        require(_soonToken != address(0), "Invalid token address");
        soonToken = IERC20(_soonToken);
    }

    /**
     * @dev Adds a new reward for a user with vesting parameters
     * @param _user Address of the user receiving the reward
     * @param _amount Amount of SOON tokens to reward
     * @param _vestingDuration Duration of the vesting period in seconds
     */
    function addReward(
        address _user,
        uint256 _amount,
        uint256 _vestingDuration
    ) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than 0");

        userRewards[_user].push(
            Reward({
                amount: _amount,
                vestingStart: block.timestamp,
                vestingDuration: _vestingDuration,
                claimedAmount: 0
            })
        );

        emit RewardAdded(_user, _amount, _vestingDuration);
    }

    /**
     * @dev Claims available rewards for the caller
     */
    function claimRewards() external nonReentrant {
        uint256 totalClaimable = 0;
        Reward[] storage rewards = userRewards[msg.sender];

        for (uint256 i = 0; i < rewards.length; i++) {
            Reward storage reward = rewards[i];
            uint256 claimable = calculateClaimable(reward);

            if (claimable > 0) {
                totalClaimable += claimable;
                reward.claimedAmount += claimable;
            }
        }

        require(totalClaimable > 0, "No rewards available to claim");
        soonToken.safeTransfer(msg.sender, totalClaimable);
        emit RewardClaimed(msg.sender, totalClaimable);
    }

    /**
     * @dev Calculates the claimable amount for a reward
     * @param _reward Reward struct to calculate claimable amount for
     * @return claimableAmount Amount of tokens that can be claimed
     */
    function calculateClaimable(Reward storage _reward) internal view returns (uint256) {
        if (block.timestamp <= _reward.vestingStart) {
            return 0;
        }

        uint256 elapsed = block.timestamp - _reward.vestingStart;
        uint256 vestedAmount;

        if (elapsed >= _reward.vestingDuration) {
            vestedAmount = _reward.amount;
        } else {
            vestedAmount = (_reward.amount * elapsed) / _reward.vestingDuration;
        }

        return vestedAmount - _reward.claimedAmount;
    }

    /**
     * @dev Returns the total claimable rewards for a user
     * @param _user Address of the user to check
     * @return totalClaimable Total amount of claimable tokens
     */
    function getClaimableRewards(address _user) external view returns (uint256 totalClaimable) {
        Reward[] storage rewards = userRewards[_user];
        totalClaimable = 0;

        for (uint256 i = 0; i < rewards.length; i++) {
            totalClaimable += calculateClaimable(rewards[i]);
        }
    }

    /**
     * @dev Emergency withdraw function to recover tokens (only owner)
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            soonToken.balanceOf(address(this)) >= _amount,
            "Insufficient contract balance"
        );

        soonToken.safeTransfer(owner(), _amount);
        emit EmergencyWithdraw(owner(), _amount);
    }

    /**
     * @dev Updates the SOON token contract address (only owner)
     * @param _newToken Address of the new SOON token contract
     */
    function updateTokenAddress(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        soonToken = IERC20(_newToken);
    }
}
```
