"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a staking platform that utilizes the $GGG token, including features for user protection and tier systems like ArbiPad.
Generated: DETERMINISTIC_c854d2468dab4c1d
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Platform for $GGG Token
 * @author [Your Name]
 * @notice This contract provides a staking platform for the $GGG token, 
 *          featuring user protection and a tier system similar to ArbiPad.
 */
contract StakingPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfo;

    // Mapping of tier information
    mapping (uint256 => Tier) public tiers;

    // $GGG token contract
    IERC20 public gggToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Number of tiers
    uint256 public numTiers;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _gggToken Address of the $GGG token contract
     * @param _numTiers Number of tiers in the tier system
     */
    constructor(address _gggToken, uint256 _numTiers) public {
        gggToken = IERC20(_gggToken);
        numTiers = _numTiers;

        // Initialize tiers with default values
        for (uint256 i = 0; i < _numTiers; i++) {
            tiers[i] = Tier({
                minStaked: i * 1000,
                maxStaked: (i + 1) * 1000,
                rewardRate: 10 + (i * 5)
            });
        }
    }

    /**
     * @notice Stake $GGG tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from user to contract
        gggToken.transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfo[msg.sender].staked = userStakingInfo[msg.sender].staked.add(_amount);
        userStakingInfo[msg.sender].tier = getTier(_amount);

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GGG tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(userStakingInfo[msg.sender].staked >= _amount, "Insufficient staked tokens");

        // Update user staking information
        userStakingInfo[msg.sender].staked = userStakingInfo[msg.sender].staked.sub(_amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        gggToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user staking information
        userStakingInfo[msg.sender].rewards = 0;

        // Transfer rewards to user
        gggToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user Address of the user
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 staked = userStakingInfo[_user].staked;
        uint256 tier = userStakingInfo[_user].tier;
        uint256 rewardRate = tiers[tier].rewardRate;

        // Calculate rewards based on staked amount and tier
        uint256 rewards = staked.mul(rewardRate).div(100);

        return rewards;
    }

    /**
     * @notice Get the tier for a given staked amount
     * @param _staked Staked amount
     * @return Tier number
     */
    function getTier(uint256 _staked) internal view returns (uint256) {
        for (uint256 i = 0; i < numTiers; i++) {
            if (_staked >= tiers[i].minStaked && _staked <= tiers[i].maxStaked) {
                return i;
            }
        }

        // Default to the last tier if no matching tier is found
        return numTiers - 1;
    }

    // Struct for user staking information
    struct UserStakingInfo {
        uint256 staked;
        uint256 tier;
        uint256 rewards;
    }

    // Struct for tier information
    struct Tier {
        uint256 minStaked;
        uint256 maxStaked;
        uint256 rewardRate;
    }
}
```
