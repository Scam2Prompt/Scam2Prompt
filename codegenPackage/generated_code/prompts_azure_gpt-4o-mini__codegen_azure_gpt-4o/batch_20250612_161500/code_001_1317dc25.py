"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract for a staking pool that supports different reward rates and compounding options for AITECH tokens, similar to those outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_1317dc25a3084b73
Batch ID: 20250612_161500
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

/**
 * @title StakingPool
 * @dev A smart contract for staking AITECH tokens with support for different reward rates and compounding options.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingPool is Ownable, ReentrancyGuard {
    IERC20 public immutable stakingToken;

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardRate; // Reward rate in percentage (e.g., 5 for 5%)
        uint256 lastUpdated; // Last time rewards were calculated
        uint256 rewards; // Accumulated rewards
        bool isCompounding; // Whether compounding is enabled
    }

    mapping(address => Stake) public stakes;

    uint256 public totalStaked; // Total tokens staked in the pool

    event Staked(address indexed user, uint256 amount, uint256 rewardRate, bool isCompounding);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event CompoundingToggled(address indexed user, bool isCompounding);

    /**
     * @dev Constructor to initialize the staking pool with the staking token.
     * @param _stakingToken Address of the AITECH token contract.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens in the pool.
     * @param _amount Amount of tokens to stake.
     * @param _rewardRate Reward rate for the stake.
     * @param _isCompounding Whether to enable compounding for this stake.
     */
    function stake(uint256 _amount, uint256 _rewardRate, bool _isCompounding) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardRate = _rewardRate;
        userStake.lastUpdated = block.timestamp;
        userStake.isCompounding = _isCompounding;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, _rewardRate, _isCompounding);
    }

    /**
     * @dev Unstake tokens from the pool.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Update the user's stake
        userStake.amount -= _amount;

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewards;
        require(rewards > 0, "No rewards to claim");

        // Reset rewards
        userStake.rewards = 0;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Toggle compounding for the user's stake.
     * @param _isCompounding Whether to enable or disable compounding.
     */
    function toggleCompounding(bool _isCompounding) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");

        // Update rewards for the user before modifying their compounding setting
        _updateRewards(msg.sender);

        userStake.isCompounding = _isCompounding;

        emit CompoundingToggled(msg.sender, _isCompounding);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 newRewards = (userStake.amount * userStake.rewardRate * timeElapsed) / (365 days * 100);

            if (userStake.isCompounding) {
                userStake.amount += newRewards; // Add rewards to the staked amount
            } else {
                userStake.rewards += newRewards; // Accumulate rewards separately
            }

            userStake.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Emergency function to withdraw all staked tokens (onlyOwner).
     * This is a safeguard in case of unforeseen issues.
     */
    function emergencyWithdraw() external onlyOwner {
        stakingToken.transfer(owner(), stakingToken.balanceOf(address(this)));
    }
}
```
